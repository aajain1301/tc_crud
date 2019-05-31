from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import views as auth_views
from events.views import index
# Create your views here.

def signup(request):
    form = UserForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')

    return render (request,'registration/signup.html',context)
