from django.shortcuts import render
# from .forms import
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