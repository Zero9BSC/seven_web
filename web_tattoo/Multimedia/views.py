from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required # DECORATORS para vistas basadas en Funciones
from django.contrib.auth.mixins import LoginRequiredMixin # MIXINS para vistas basadas en Clases

from .models import *
#from .forms import *



# VISTAS BASADAS EN FUNCIONES
def multimedia(request):

    return render (request, "multimedia.html")