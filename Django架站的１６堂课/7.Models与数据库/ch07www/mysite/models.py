#! -*- encoding:utf-8  -*-

from django.db import models

# Create your models here.


class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
    # def __str__(self):
    #     return self.name



class PModel(models.Model):
    maker = models.ForeignKey(Maker,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://www.baidu.com')


    def __unicode__(self):
        return self.name
    #
    # def __str__(self):
    #     return self.name




class Product(models.Model):
    pmodel = models.ForeignKey(PModel,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15,default='超值二手机')
    description = models.TextField(default='暂无说明')
    year = models.PositiveIntegerField(default=2018)
    price = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.nickname

    # def __str__(self):
    #     return self.nickname



class PPhoto(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.CharField(max_length=20,default='产品照片')
    url = models.URLField(default='http://www.baidu.com')


    def __unicode__(self):
        return self.description
    # def __str__(self):
    #     return self.description
    #





