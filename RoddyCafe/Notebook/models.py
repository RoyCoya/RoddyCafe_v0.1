from django.db import models
# Create your models here.

#目录
#注意：本表采用森林转二叉树的数据结构存储，以便使目录能够手动排序而不用按标题字母等自动排序
class notebook_directory(models.Model):
    directory_id = models.AutoField(primary_key=True,verbose_name='目录id')
    directory_name = models.CharField(max_length=20,verbose_name='目录名')
    directory_discription = models.CharField(blank=True,null=True,max_length=200,verbose_name='目录描述')
    directory_first_child = models.ForeignKey('self',related_name='first_child',on_delete=models.CASCADE,blank=True,null=True,verbose_name='第一个子目录（左子树）')
    directory_next_brother = models.ForeignKey('self',related_name='next_brother',on_delete=models.CASCADE,blank=True,null=True,verbose_name='下一个同级目录（右子树）')
    def __str__(self):
        return str(self.directory_name)
    class Meta:
        verbose_name = '目录'
        verbose_name_plural = '目录'

#笔记
class notebook_note(models.Model):
    note_id = models.AutoField(primary_key=True,verbose_name='笔记id')
    #注：交互页面中，标题是直接根据笔记中的标题块、副标题块、第一句正文前20字等的优先级自动进行设置
    note_directory = models.ForeignKey(notebook_directory,blank=True,null=True,on_delete=models.CASCADE,verbose_name='所属目录')
    note_title = models.CharField(blank=True,null=True,max_length=50,verbose_name='笔记标题')
    note_content = models.TextField(blank=True,null=True,verbose_name='笔记内容')
    note_pinTop = models.BooleanField(default=False,verbose_name='置顶')
    note_pending = models.BooleanField(default=True,verbose_name='待编辑')
    note_createDate = models.DateTimeField(auto_now_add=True,verbose_name='笔记创建时间')
    note_editDate = models.DateTimeField(auto_now=True,verbose_name='笔记修改时间')
    def __str__(self):
        return str(self.note_title)
    class Meta:
        verbose_name = '笔记'
        verbose_name_plural = '笔记'

#笔记提醒
class notebook_note_alert(models.Model):
    note_alert_id = models.AutoField(primary_key=True,verbose_name='提醒id')
    note_alert_note_id = models.ForeignKey(notebook_note,on_delete=models.CASCADE,verbose_name='所属笔记')
    note_alert_datetime = models.DateTimeField(verbose_name='提醒时间')
    #TODO:重复提醒功能

    class Meta:
        verbose_name = '提醒'
        verbose_name_plural = '提醒'

#用户文件（图片、视频等）
class notebook_userfile(models.Model):
    userfile_id = models.AutoField(primary_key=True,verbose_name='文件id')
    userfile_content = models.FileField(upload_to='Notebook/%Y/%m/%d/',verbose_name='文件内容')