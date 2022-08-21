from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Lessons, catgory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from students.models import student
# Create your views here.

@login_required
def HomeV(request):
    context={
        "cats":catgory.objects.all(),
    }
    return render(request, "index.html", context)


@login_required
def lessonv(request, id):
    if not request.user.is_staff:
        cuser = student.objects.get(sinit=request.user)
        cat = catgory.objects.get(id=id)
        lessons = Lessons.objects.filter(catname=cat)
    if request.user.is_staff:
        cat = catgory.objects.get(id=id)
        lessons = Lessons.objects.filter(catname = cat)
    
    context={
        "les":lessons,
        "cat":cat
    }
    return render(request, "lessons.html", context)

@login_required
def lessondetail(request, id):
    
    if not request.user.is_staff:
        cuser = student.objects.get(sinit=request.user)
        if Lessons.objects.filter(id = id).exists:
            lesvisit = Lessons.objects.get(id = id)
        if cuser.points < 10 :
            if lesvisit in cuser.watchedlecs.all():
                lesvisit = lesvisit
            else:
                lesvisit = []
        if cuser.points >= 10 and lesvisit not in cuser.watchedlecs.all():
            lesvisit = Lessons.objects.get(id = id)
            cuser.watchedlecs.add(lesvisit)
            cuser.points = cuser.points - 10
            cuser.save()
    else:
        lesvisit = Lessons.objects.get(id = id)
    

    context={
        "lesson": lesvisit,
    }
    return render(request, "lesson.html", context)


@login_required
def lecsv(request):
    if not request.user.is_staff:
        cuser = student.objects.get(sinit=request.user)
        lessons = Lessons.objects.all()
    if request.user.is_staff:
        lessons = Lessons.objects.all()
    context={
        "all" : lessons
    }
    return render(request, "lecs.html", context)



def handel400(request, exception):
    return render(request, "400.html", status=400)

def handel403(request, exception):
    return render(request, "403.html", status=403)

def handel404(request, exception):
    return render(request, "404.html", status=404)

def handel500(request, exception):
    return render(request, "500.html", status=500)