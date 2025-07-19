from django.urls import path,include
from .views import *


urlpatterns = [
    path('', index, name= 'index'),
    path('scan/',scan,name='scan'),
    path('profiles/', profiles, name= 'profiles'),
    path('details/', details, name= 'details'),
    path('back/',back,name='back'),
    path('add_profile/',add_profile,name='add_profile'),
    path('edit_profile/<int:id>/',edit_profile,name='edit_profile'),
    path('delete_profile/<int:id>/',delete_profile,name='delete_profile'),
    path('clear_history/',clear_history,name='clear_history'),
    path('reset/',reset,name='reset'),
    path('sendmailsfinal/',sendmailsfinal,name="sendmailsfinal")

]
