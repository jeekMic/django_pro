from django.db import models
# python manage.py inspectdb > booktest/modles.py 将数据库中的表导出成django的模型
class BookInfoManager(models.Manager):
    def get_queryset(self):
        # 在原来的基础上进行查询过滤
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)
    # 在自定义管理器中定义一个创建对象的方法
    def create(self,btitle,b_pub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = b_pub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False
        return b


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    # 后面这个属性表示的是数据库中的列名称
    bpub_date = models.DateField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    #相当于BookInfo有两个管理器
    books1 = models.Manager()
    books2 = BookInfoManager()
    class Meta:
        db_table = "bookinfo"
    # 这个不允许使用 __init__ 这个初始化方法，因为model里面使用了 __init__
    @classmethod
    def create(self,btitle,b_pub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = b_pub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False
        return b



class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE,)

# Create your models here.
