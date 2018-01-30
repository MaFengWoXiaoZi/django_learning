from django.db import models
# Create your models here.

class Publisher(models.Model):
    name = models.CharField('出版商', max_length = 30)
    address = models.CharField('地址', max_length = 50)
    city = models.CharField('城市', max_length=60)
    state_province = models.CharField('省份', max_length=30)
    country = models.CharField('国家', max_length=50)
    website = models.URLField('网站')

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name

    def __str__(self):  # Python3 use __str__, while Python2 use __unicode__methods
        return self.name


class Author(models.Model):
    name = models.CharField('姓名', max_length=30)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    sex = models.BooleanField('性别', max_length=1, choices=((0, '男'), (1, '女'),))
    email = models.EmailField('电子邮件')
    address = models.CharField('地址', max_length=50)
    birthday = models.DateField('生日')
    author = models.OneToOneField(Author)

    class Meta:
        verbose_name = '作者详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author.name

class Book(models.Model):
    title = models.CharField('书名', max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField('出版日期')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=2)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title