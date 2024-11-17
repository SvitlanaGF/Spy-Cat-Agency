from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Target, Mission


class CreateTarget(CreateView):
    model = Target
    fields = '__all__'

class CreateMission(CreateView):
    model = Mission
    fields = ['name']

class DeleteMission(DeleteView):
    model = Mission

class UpdateTarget(UpdateView):
    model = Mission
    fields = ['isComplete', 'notes']

class MissionDetail(DetailView):
    model = Mission
    context_object_name = 'mission'

class MissionList(ListView):
    model = Mission
    context_object_name = 'missions'

class TargetDetail(DetailView):
    model = Target
    context_object_name = 'target'

class TargetList(ListView):
    model = Target
    context_object_name = 'targets'
