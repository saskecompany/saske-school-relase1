from django.http import request
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .forms import fstudent
from .models import student
from django.contrib.auth.models import User

# Create your views here.as_view
def joinV(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        stu = fstudent(request.POST)
        if form.is_valid and stu.is_valid:
            form.save()
            stu.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            cuser = User.objects.get(username = username)
            nstu = student.objects.get(Sidnumber=stu.cleaned_data.get('Sidnumber'))
            nstu.sinit = cuser
            nstu.Sstatus = True
            nstu.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form=UserCreationForm
        stu=fstudent


    context={
        "form":form,
        "stuf":stu
    }
    return render(request, "join.html", context)