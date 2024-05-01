from django.urls import path
from .views import home_page, blog_single_page, blog_page, about_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blogs/', blog_page, name='blogs'),
    path('detail/<int:pk>/', blog_single_page, name='detail'),
]