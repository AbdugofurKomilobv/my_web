from django.urls import path

from main.views import home,message

urlpatterns = [
    path('',home,name='home'),
    path('message/', message, name='message'),

]