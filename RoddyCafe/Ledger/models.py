from django.db import models
from django.contrib.auth import settings

# 账本
class book(models.Model):
    class Meta:
        verbose_name = '账本'
        verbose_name_plural = '账本'
    def __str__(self):
        return str(self.user.username) + str(self.name)
    id = models.AutoField(primary_key=True, verbose_name='账本id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='所属用户')
    name = models.CharField(max_length=20, verbose_name='账本名')

# 账单分类
class bill_classification(models.Model):
    class Meta:
        verbose_name = '账单分类'
        verbose_name_plural = '账单分类'
    def __str__(self):
        return str(self.name) + " | " + str(self.book)
    
    id = models.AutoField(primary_key=True, verbose_name='分类id')
    book = models.ForeignKey(book, on_delete=models.CASCADE, verbose_name='所属账本')
    name = models.CharField(max_length=20, default="未分类", verbose_name='分类名')
    icon = models.CharField(max_length=30, default='bookmarks-fill', verbose_name='分类图标')

# 收支记录
class bill(models.Model):
    class Meta:
        verbose_name = '收支记录'
        verbose_name_plural = '收支记录'
    id = models.AutoField(primary_key=True, verbose_name='收支记录id')
    classification = models.ForeignKey(bill_classification, on_delete=models.CASCADE, verbose_name='所属分类')
    value = models.FloatField(default=0, verbose_name='收支数值')
    create_time = models.DateTimeField(verbose_name='记录时间')
    remark = models.CharField(max_length=50, blank=True, null=True, verbose_name='备注')

# 每月预算
class budget(models.Model):
    class Meta:
        verbose_name = '每月预算'
        verbose_name_plural = '每月预算'
        unique_together = (('user', 'year', 'month'),)
    id = models.AutoField(primary_key=True, verbose_name='每月预算id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='所属用户')
    year = models.PositiveBigIntegerField(verbose_name='年份')
    month = models.PositiveBigIntegerField(verbose_name='月份')
    budget = models.PositiveIntegerField(verbose_name="该月预算金额")

# 用户偏好
class preference(models.Model):
    class Meta:
        verbose_name = '用户偏好'
        verbose_name_plural = '用户偏好'
    def __str__(self):
        return str(self.user.username)

    id = models.AutoField(primary_key=True, verbose_name='用户偏好id')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='所属用户')
    default_book = models.ForeignKey(book, on_delete=models.CASCADE, verbose_name='默认账本')
    default_mode_choice = (
        ('day','按日显示'),
        ('month','按月显示'),
    )
    default_mode = models.CharField(choices=default_mode_choice, max_length=50, default='day', verbose_name='默认账本模式')