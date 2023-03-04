from django.db import models

# Create your models here.
class masturbation(models.Model):
    class Meta:
        verbose_name = '首充记录'
        verbose_name_plural = '首充记录'
    def __str__(self):
        return str(self.createDate)
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=20, verbose_name='用户', default="Rocky")
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='时间')