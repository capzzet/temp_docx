"""inforesume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.views.static import serve

from resume.views import custom_page_not_found_view,custom_error_view,custom_bad_request_view,custom_permission_denied_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('resume.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
handler404 = custom_page_not_found_view
handler500 = custom_error_view
handler403 = custom_permission_denied_view
handler400 = custom_bad_request_view
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)