from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models




class UserProfile(AbstractUser):
    gender_choice = (
        ('male', '男'),
    )
    nick_name = models.CharField('昵称', max_length=50, default='')
    birthday = models.DateField('生日', null=True, blank=True)
    address = models.CharField('地址', max_length=100, default='')
    mobile = models.CharField('手机号', max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m', default='image/default.png', max_length=100)

    class Meta:
        db_table= 'userproperty_profile'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """
    邮箱验证码
    """
    send_choices = (
        ('register', '注册'),
        ('forget', '找回密码')
    )
    code = models.CharField('验证码', max_length= 20)
    email = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField(choices= send_choices,max_length=10)
    send_time = models.DateTimeField(default= datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name



class Banner(models.Model):
    """
    轮播图:　image上传到哪里, url是图片的路径, index控制轮播图的播放顺序
    """
    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', upload_to='banner/%Y%m',max_length=100)
    url = models.URLField('访问地址', max_length=200)
    index = models.IntegerField('顺序',default= 100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name