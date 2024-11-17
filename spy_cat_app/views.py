from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import SpyCat


class SpyCatCreate(CreateView):
    model = SpyCat
    fields = '__all__'

class SpyCatUpdate(UpdateView):
    model = SpyCat
    fields = ['salary',]

class SpyCatDelete(DeleteView):
    model = SpyCat
    success_url = '/'

class SpyCatDetail(DetailView):
    model = SpyCat
    context_object_name = 'spy_cat'

class SpyCatListView(ListView):
    model = SpyCat
    context_object_name = 'spy_cat_list'

class SpyCatDetailView(DetailView):
    model = SpyCat
