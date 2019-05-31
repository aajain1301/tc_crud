from django.shortcuts import render
from .forms import EventForm
from .models import Event
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render (request,'index.html')
    
class EventCreate(LoginRequiredMixin,CreateView):
    model = Event
    fields = '__all__'

class EventList(LoginRequiredMixin,ListView):
    model = Event
    context_object_name = 'event_list'

class EventDetail(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = 'event_detail'

class EventUpdate(LoginRequiredMixin,UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(LoginRequiredMixin,DeleteView):
    model = Event
    success_url = reverse_lazy('events:list')
