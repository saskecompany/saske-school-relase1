from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class task(models.Model):
    def askimgupload(self, filename):
        file , ext = filename.split(".")
        return f"ask{self.lesson}/{file}.{ext}"
    answers = [
        ("1","الاجابه الاولي"),
        ("2","الاجابه الثانيه"),
        ("3","الاجابه الثالثه"),
        ("4","الاجابه الرابعه"),
        ]
    quest = models.TextField(_("السؤال"),null=True, blank=True)
    questimg = models.ImageField(_("صورة السؤال"), upload_to=askimgupload, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    lesson = models.ForeignKey("home.Lessons", verbose_name=_("الدرس المتعلق"), on_delete=models.CASCADE, null=True, blank=True)
    exam = models.ForeignKey("tasks.exam", verbose_name=_('امتحان'), on_delete=models.CASCADE, null=True, blank=True)
    answer1 = models.CharField(_("الاجابه الاولي"), max_length=50, null=True, blank=True)
    answer2 = models.CharField(_("الاجابه الثانيه"), max_length=50, null=True, blank=True)
    answer3 = models.CharField(_("الاجابه الثالثه"), max_length=50, null=True, blank=True)
    answer4 = models.CharField(_("الاجابه الرابعه"), max_length=50, null=True, blank=True)
    answer = models.CharField(_("الاجابه الصحيحه"), max_length=50, choices=answers, null=True, blank=True)
    class Meta:
        verbose_name = "الأسئله"
        verbose_name_plural = "الأسئله"
class exam(models.Model):
    title = models.CharField(_("عنوان الامتحان"), max_length=256)
    publishAt = models.DateTimeField(_("التاريخ"), auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "امتحان"
        verbose_name_plural = "الإمتحانات"