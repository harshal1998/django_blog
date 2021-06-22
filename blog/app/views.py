from django.shortcuts import render, redirect
from django.template import Template
from django.http import HttpResponse
from .forms import *

# Create your views here.
from django.template.context_processors import request
from django.views.generic import TemplateView, ListView

from .models import *


class a(ListView):
    model = blog
    template_name = 'home.html'


def add(request):
    form = blogform()
    return render(request, "add.html", {"form": form})


