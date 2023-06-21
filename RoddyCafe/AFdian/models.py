from django.db import models
from django.contrib.auth import settings

class AFD_info(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    token = models.CharField(max_length=100, verbose_name='爱发电auth_token')
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'