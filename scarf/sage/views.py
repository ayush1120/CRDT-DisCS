from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout


import os
import shutil
import json
import datetime
import signal
import random
import uuid


from scarf.settings import BASE_DIR
from sage.models import  *




def home(request):
    # Hello this is a function which returns home
    return render(request, 'base.html')
    # return HttpResponse("Hello")
    