from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import homeworkV, examlistV, examquestV
app_name="tasks"

urlpatterns = [
    path("<int:id>", homeworkV, name="homework"),
    path("exams", login_required(examlistV.as_view()), name="exams"),
    path("exam/<int:id>", examquestV, name="exam")
]
