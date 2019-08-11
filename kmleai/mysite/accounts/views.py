from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth.views import login as auth_login

def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
	})

def login(request):
    provider_list = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        provider_list.append(provider)

    return auth_login(request, extra_context={
                'provider_list': provider_list,
            })

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
