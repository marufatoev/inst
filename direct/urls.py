from django.urls import path
from . import views

urlpatterns = [
  path('', views.direct,  name='direct'),
  path('directs/<username>', views.directs, name='directs'),
  path('send/', views.send_direct, name='send_direct'),
  path('new/', views.search_user, name='search_user'),
  path('new/<username>', views.newconversation, name='newconversation')
]