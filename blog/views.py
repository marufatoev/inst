from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . import forms

@login_required(login_url='/users/sign_in')
def articles_list(request):
    # search = request.GET.get('search')
    articles = Article.objects.all().order_by('date')
    # articles = articles.filter(Q(title__icontains=search) | Q(text__icontains=search)) if search else articles
    return render(request, 'articles_list.html', {'articles': articles})

def home(request):
    articles = Article.objects.filter(Q(author__profile__followers=request.user))
    return render(request, 'home.html', {'articles': articles,})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.article = article
            instance.save()
            return redirect('blog:article_detail', pk=pk)

    form = forms.CommentForm()  
    return render(request, 'article_detail.html', {'article': article, 'form':form})


@login_required(login_url='/users/sign_in')
def article_create(request):
    form = forms.ArticleFrom(request.POST or None, request.FILES)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('blog:articles_list')
    form = forms.ArticleFrom()
    return render(request, 'article_create.html', {'form': form})


def edit_article(request, pk):
    article = Article.objects.get(pk=pk)
    form = forms.ArticleFrom(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('blog:article_detail', article.pk)
    return render(request, 'edit_article.html', {'form': form, 'article': article})


def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('blog:articles_list')
    return render(request, 'delete_article.html', {'article': article})


def like_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user not in article.likes.all():
        article.likes.add(request.user)
        article.dislikes.remove(request.user)
    elif request.user in article.likes.all():
        article.likes.remove(request.user)
    return redirect('blog:article_detail', pk=pk)  


def dislike_article(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user not in article.dislikes.all():
        article.dislikes.add(request.user)
        article.likes.remove(request.user)
    elif request.user in article.dislikes.all():
        article.dislikes.remove(request.user)
    return redirect('blog:article_detail', pk=pk)

def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.user != comment.user:
       return render(request, 'error.html', {'comment': comment})
    if request.method == 'POST':
        comment.delete()

        return redirect('blog:article_detail', pk=comment.article.pk)
    return render(request, 'delete_comment.html', {'article': comment.article})


def edit_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    form = forms.CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect('blog:article_detail', pk=comment.article.pk)
    return render(request, 'comment_edit.html', {"form": form, 'article':comment.article})

def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    articles = Article.objects.filter(author=request.user)
    post_num = articles.count()
    return render(request, 'my_profile.html', {'profile': profile, 'articles': articles, 'post_num': post_num})

def profile(request,id=None,):
    if id is not None:
        profile_id = Profile.objects.get(id=id)
        posts = Article.objects.filter(author=request.user)
        posts_num = posts.count()
        profile = Profile.objects.get(user=request.user)
        profileimage = profile.profile_picture.url
    return render(request,'profile.html',{'profile':profile_id,'profileimage':profileimage,'profile_of_user':True,'posts':posts,'posts_num':posts_num})

def search(request):
    if not request.user.is_authenticated:
        return redirect("blog:sign_in")
    search = request.GET['username']
    profiles = Profile.objects.filter(Q(user__username__icontains=search))
    context = {'profiles':profiles,'username':search,}
    return render(request,'search.html',context)

def follow(request, id, username):
    profile = Profile.objects.get(id=id)
    login_profile = Profile.objects.get(user=request.user)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
        login_profile.followings.remove(profile.user)
    else:   
        profile.followers.add(request.user)
        login_profile.followings.add(profile.user)
    return redirect('blog:my_profile')


def direct(request):
    return render(request, 'direct.html')

