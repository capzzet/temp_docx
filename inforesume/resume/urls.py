from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='home'),
    path('resume/', resume,name='resume'),
    path('about/', about,name='about'),
    path('blog/', blog,name='blog'),
    path('download/', download,name='download'),
]
