from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles_list, name='articles_list'),
    path('article_detail/<int:pk>', views.article_detail, name='article_detail'),
    path('article_create', views.article_create, name='article_create'),
    path('edit/<int:pk>', views.edit_article, name='article_edit'),
    path('delete/<int:pk>', views.delete_article, name='article_delete'),
    path('like/<int:pk>', views.like_article, name='article_like'),
    path('dislike/<int:pk>', views.dislike_article, name='article_dislike'),
    path('delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:pk>', views.edit_comment , name='edit_comment'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('search/',views.search,name="search"),
    path('follow/<int:id>/<str:username>', views.follow, name='follow'),
    path('home', views.home, name='home'),
    path('favorite/<int:pk>', views.favorite, name='favorite'),
]