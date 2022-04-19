from django.shortcuts import render, redirect, get_list_or_404
from .forms import SignupForm, NeighborhoodForm, UpdateResidentForm, BusinessForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Neighborhood, Resident, Business
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
# Default page load N.B: From the user stories, one has to sign in to use
@login_required(login_url='login')
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

# Create a new Neighborhood in the app
def create_hood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighborhoodForm()
    return render(request, 'newhood.html', {'form': form})

# View to enable user to 