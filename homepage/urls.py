from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/details/<int:id>', views.details, name='details'),
    path('members/details/<int:id>', views.details, name='details'),
    # path('images/', views.images, name='images'),
    # path('chat/', views.chat, name='chat'),
    # path('videos/', views.videos, name='videos'),
    # path('maps/', views.maps, name='maps'),
]