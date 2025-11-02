from django.db import models
from django.conf import settings


class Run(models.Model):

    athlete = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Комментарий", max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Забег"
        verbose_name_plural = "Забеги"
