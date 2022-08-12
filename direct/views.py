from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator



def direct(request):
	messages = Message.get_messages(user=request.user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]
		active_direct = message['user']
		directs = Message.objects.filter(user=request.user, recipient=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'] == active_direct:
				message['unread'] = 0

	return render(request, 'direct.html', {'directs': directs, 'messages': messages,'active_direct': active_direct,})


def search_user(request):
	query = request.GET.get("q")
	context = {}
	
	if query:
		users = User.objects.filter(Q(username__icontains=query))

		#Pagination
		paginator = Paginator(users, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.get_page(page_number)

		context = {
				'users': users_paginator,
			}
	return render(request, 'search_user.html', context)


def directs(request, username):
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, recipient=username)
    directs.update(is_read=True)

    for message in messages:
            if message['user'].username == username:
                message['unread'] = 0   
                
    return render(request, 'direct.html', {'directs': directs, 'messages': messages,'active_direct': active_direct,})

def newconversation(request, username):
	from_user = request.user
	body = ''
	try:
		to_user = User.objects.get(username=username)
	except Exception as e:
		return redirect('usersearch')
	if from_user != to_user:
		Message.send_message(from_user, to_user, body)
	return redirect('direct:direct')

def send_direct(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	body = request.POST.get('body')
	
	if request.method == 'POST':
		to_user = User.objects.get(username=to_user_username)
		Message.send_message(from_user, to_user, body)
		return redirect('direct:direct')




	