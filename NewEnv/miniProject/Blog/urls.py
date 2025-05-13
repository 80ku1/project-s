from django.urls import path
from . import views

urlpatterns=[
    path ('home/', views.home, name='home'),
    path ('post/', views.post, name='post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
