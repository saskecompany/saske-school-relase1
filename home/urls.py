from django.urls import path
from .views import HomeV, lessondetail, lessonv, lecsv

app_name = "home"
urlpatterns = [
    path('', HomeV, name="home"),
    path('<int:id>', lessonv, name='lessons'),
    path('lesson/<int:id>', lessondetail, name='lesson'),
    path("lectures", lecsv, name="all")
    
]


