from django.shortcuts import render
from django.contrib.auth.models import User,auth
from . import urls
from .models import Destination
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
     
