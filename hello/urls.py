from django.urls import path
from .models import LogMessage
from . import views

urlpatterns = [
    path('',
        views.HomeListView.as_view(
            queryset=LogMessage.objects.order_by('-log_date')[:5],  # :5 limits the results to the five most recent
            context_object_name='message_list',
            template_name='hello/home.html',),
        name="home"),
    path('hello/<name>', views.hello_there, name="hello_there"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('log/', views.log_message, name="log"),
]