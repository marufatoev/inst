
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'monday2'), namespace='blog')),
    path('users/', include(('users.urls', 'monday2'), namespace='users')),
     path('direct/', include(('direct.urls', 'monday2'), namespace='direct'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
