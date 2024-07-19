from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.views import generic
from django.utils.timezone import now 
from django.core.mail import send_mail
from django.conf import settings
from users.models import Invitation
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    CustomUserChangeForm,
    InvitationAcceptanceForm,
    InvitationForm,
)


# Homepage view
def homepage_view(request):
    return render(request, "homepage.html")


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "auth/signup.html"


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("users:profile")
    else:
        form = CustomAuthenticationForm()
    return render(request, "auth/login.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, "account/profile.html", {"form": form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "account/change_password.html", {"form": form})



def send_invitation(request):
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.sent_by = request.user  # Set the user who sent the invitation
            invitation.save()
            send_invitation_email(invitation)
            return redirect('users:homepage')
    else:
        form = InvitationForm()
    return render(request, 'invitation/send_invitation.html', {'form': form})

def accept_invitation(request, code):
    invitation = get_object_or_404(Invitation, code=code, accepted=False)
    if request.method == 'POST':
        form = InvitationAcceptanceForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            invitation.accepted = True
            invitation.accepted_at = now()
            invitation.save()
            return redirect('users:login')
    else:
        form = InvitationAcceptanceForm(initial={'email': invitation.email})
    return render(request, 'invitation/accept_invitation.html', {'form': form})

def send_invitation_email(invitation):
    subject = 'You are invited to join our platform'
    message = f'Please use the following link to accept the invitation and register: {settings.SITE_URL}/accept-invitation/{invitation.code}/'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [invitation.email])