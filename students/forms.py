from django.forms import ModelForm
from .models import student

class fstudent(ModelForm):
    
    class Meta:
        model = student
        fields = '__all__'
        exclude = ['sinit', 'Sstatus', 'finishedHomework', 'finishExam', 'Spercent', 'Spercenthomeworks', 'Spercentexams', 'shomeworks', 'sexams', 'watchedlecs', 'points']
