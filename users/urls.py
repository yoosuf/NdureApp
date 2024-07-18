from django.urls import path
from .views import SignUpView, profile_view, change_password

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/change-password/', change_password, name='change_password'),
]
