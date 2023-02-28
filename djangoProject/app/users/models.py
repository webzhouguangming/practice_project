from django.db import models

# Create your models here.


class BaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    real_name = models.CharField(max_length=255)
    QQ_code = models.IntegerField(blank=True, null=True)
    verify_code = models.IntegerField()

    class Meta:

        db_table = 'user_form'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

