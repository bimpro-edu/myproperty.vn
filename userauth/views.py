from django.shortcuts import render

def profile_view(request):
    return render(request, 'account/profile.html')