from django.contrib import admin
from .models import student
# Register your models here.




class adminstudents(admin.ModelAdmin):
    list_display=['Sfname','Smname','Slname','Sidgroup','Spercent']
    exclude=["shomeworks", "sexams"]
admin.site.register(student, adminstudents)