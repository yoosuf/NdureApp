from django.urls import path

from .views import SignUpView, accept_invitation, homepage_view, profile_view, change_password, login_view, send_invitation
from django.contrib.auth.views import LogoutView

app_name = "users"  # Define the app namespace


urlpatterns = [
    path("", homepage_view, name="homepage"),
    path("login/", login_view, name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page="users:login"), name="logout"),
    path("profile/", profile_view, name="profile"),
    path("change-password/", change_password, name="change_password"),
    path('send-invitation/', send_invitation, name='send_invitation'),
    path('accept-invitation/<uuid:code>/', accept_invitation, name='accept_invitation'),

]
