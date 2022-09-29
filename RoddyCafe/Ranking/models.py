from django.db import models

class RankItem(models.Model):
    def __str__(self):
        return str(self.name)
    id = models.AutoField(primary_key=True, verbose_name='id')
    type_choice = (
        ('movie','电影'),
        ('anime','番剧'),
        ('book','图书'),
    )
    type = models.CharField(choices=type_choice,default='movie' , max_length=10, verbose_name='类型')
    name = models.CharField(max_length=50, verbose_name='对象名')
    poster = models.ImageField(blank=True, null=True, upload_to='ToolBox/Ranking/%Y/%m/%d/', verbose_name='封面图')
    remarks = models.TextField(blank=True, null=True, verbose_name='评论')
    pre = models.ForeignKey('self', related_name='rank_pre', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='前结点')
    next = models.ForeignKey('self', related_name='rank_next', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='后结点')