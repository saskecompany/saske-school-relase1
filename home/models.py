from django.db import models
from django.utils.translation import ugettext_lazy as _



class Lessons(models.Model):
    def upleson(self, filename):
        name = filename.split(".")
        return "lessons/%s.%s" %(self.name, name[-1])
    name = models.CharField(_("اسم الحصه"),max_length=256)
    catname = models.ForeignKey("home.catgory", verbose_name=_("يتبع"), on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField(_("تاريخ الحصه"), auto_now_add=True)
    video = models.FileField(_("الحصه"), upload_to=upleson, max_length=100)

    def __str__(self):
        return f'{self.id}- {self.name}, من فرع {self.catname}'
    class Meta:
        verbose_name = "الدرس"
        verbose_name_plural = "الدروس"


class catgory(models.Model):
    name = models.CharField(_("اسم التصنيف"), max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "الفرع"
        verbose_name_plural = "الفروع"
        