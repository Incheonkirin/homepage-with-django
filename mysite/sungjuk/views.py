# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sungjuk


class SungjukList(ListView):
    model = Sungjuk

class SungjukCreate(CreateView):
    model = Sungjuk
    success_url = reverse_lazy('sungjuk:sungjuk_list')
    fields = ['name', 'kor', 'mat', 'eng']

class SungjukUpdate(UpdateView):
    model = Sungjuk
    success_url = reverse_lazy('sungjuk:sungjuk_list')
    fields = ['name', 'kor', 'mat', 'eng']

class SungjukDelete(DeleteView):
    model = Sungjuk
    success_url = reverse_lazy('sungjuk:sungjuk_list')
