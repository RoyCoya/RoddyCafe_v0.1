from django.db import models

# Create your models here.
class masturbation(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=20, verbose_name='用户', default="Rocky")
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='时间')