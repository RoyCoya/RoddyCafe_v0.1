from django.db import models

class movie(models.Model):
    def __str__(self):
        return str(self.name)
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=20, verbose_name='电影名')
    poster = models.ImageField(blank=True, null=True, upload_to='ToolBox/MovieRank/%Y/%m/%d/', verbose_name='海报图')
    remarks = models.TextField(blank=True, null=True, verbose_name='影评')
    pre = models.ForeignKey('self', related_name='movie_pre', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='前结点')
    next = models.ForeignKey('self', related_name='movie_next', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='后结点')