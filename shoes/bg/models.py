from django.db import models
# 导入手机验证
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10, verbose_name="用户姓名")
    phone = models.CharField(max_length=11, validators=[RegexValidator(regex="^(138|176|184)\d{8}$", message="手机号不符合规范")], verbose_name="用户手机", unique=True)
    def __str__(self):
        return self.name

class Shoes(models.Model):
    shoes = models.ForeignKey(to=User, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, validators=[RegexValidator(regex="^(yellow|blue|red|green)$", message="颜色不符合规范")], verbose_name="鞋子颜色")
    size = models.CharField(max_length=10, verbose_name="鞋子大小")