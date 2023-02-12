from django.urls import re_path
from main.views import HomeView, AllNotifications


urlpatterns = [
    re_path('^home/$', HomeView.as_view(), name='home'),
    re_path('^$', AllNotifications.as_view(), name='all-notification'),
]