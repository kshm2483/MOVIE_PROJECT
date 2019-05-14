from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.
def list(request):
    return render(request,'movies/list.html')