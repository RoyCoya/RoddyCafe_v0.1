from django.db import models
from django.contrib.auth import settings

#目录
#注意：本表采用森林转二叉树的数据结构存储，以便使目录能够手动排序而不用按标题字母等自动排序，且排序顺序存至数据库而非本地
class directory(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='目录id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='所属用户')
    name = models.CharField(max_length=20,verbose_name='目录名')
    discription = models.CharField(blank=True,null=True,max_length=200,verbose_name='目录描述')
    first_child = models.ForeignKey('self',related_name='directory_first_child',on_delete=models.SET_NULL,blank=True,null=True,verbose_name='第一个子目录（左子树）')
    next_brother = models.ForeignKey('self',related_name='directory_next_brother',on_delete=models.SET_NULL,blank=True,null=True,verbose_name='下一个同级目录（右子树）')
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = '目录'
        verbose_name_plural = '目录'

#笔记
class note(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='笔记id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='所属用户')
    directory = models.ForeignKey(directory,blank=True,null=True,on_delete=models.CASCADE,verbose_name='所属目录')
    #注：交互页面中，标题是直接根据笔记中的标题块、副标题块、第一句正文前20字等的优先级自动进行设置。在编辑笔记页面中可再次手动修改
    title = models.CharField(blank=True,null=True,max_length=50,verbose_name='笔记标题')
    content = models.TextField(blank=True,null=True,verbose_name='笔记内容')
    isPinTop = models.BooleanField(default=False,verbose_name='置顶')
    isPending = models.BooleanField(default=False,verbose_name='待编辑')
    createDate = models.DateTimeField(auto_now_add=True,verbose_name='笔记创建时间')
    editDate = models.DateTimeField(auto_now=True,verbose_name='笔记修改时间')
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = '笔记'
        verbose_name_plural = '笔记'

#笔记提醒
class alert(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='提醒id')
    note = models.ForeignKey(note,on_delete=models.CASCADE,verbose_name='所属笔记')
    datetime = models.DateTimeField(verbose_name='提醒时间')
    #TODO:重复提醒功能
    class Meta:
        verbose_name = '提醒'
        verbose_name_plural = '提醒'

#用户文件（图片、视频等）
class userfile(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='文件id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='所属用户')
    content = models.FileField(upload_to='Notebook/%Y/%m/%d/',verbose_name='文件内容')