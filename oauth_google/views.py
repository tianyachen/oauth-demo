from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if 'picture' not in request.session:
        request.session['picture'] = request.user.social_auth.get(provider='google-oauth2').extra_data['picture']
    return render(request, 'oauth_google/index.html', {})