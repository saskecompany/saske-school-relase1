from students.models import student
from django.contrib.auth.models import User


def cuser(request):
    if request.user.is_authenticated:
        if not request.user.is_staff and not request.user.is_staff:
            currentuser = User.objects.get(username=request.user)
            cstudent = student.objects.get(sinit=currentuser.id)
        if request.user.is_staff:
            currentuser = User.objects.get(username=request.user)
            cstudent=""
    else:
        currentuser=""
        cstudent =""

    context={
        "user":currentuser,
        'cuser':cstudent
    }
    return (context)