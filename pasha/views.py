from django.shortcuts import render, redirect, get_list_or_404
from .forms import SignupForm, NeighborhoodForm, UpdateResidentForm, BusinessForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Neighborhood, Resident, Business
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
# Default page load
# @login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

# The Registration of a user
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# Display all the neighborhoods available in the system
def hoods(request):
    all_hoods = Neighborhood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all_hoods.html', params)