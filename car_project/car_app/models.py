from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering=['name',]
        verbose_name='category'
        verbose_name_plural='categories'
    def get_detail(self):
        return reverse('car_app:car_by_category',args=[self.slug])

    def __str__(self):
        return self.name

class Cars(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='pics',blank=True,null=True,default='pics/logo.png')
    price=models.TextField(max_length=100,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    link=models.CharField(max_length=500,unique=True)

    class Meta:
        ordering:['name',]
        verbose_name='car'
        verbose_name_plural='cars'

    def get_detail(self):
        return reverse('car_app:car_detail', args=[self.category.slug, self.slug])
    def get_update(self):
        return reverse('car_app:update',args=[self.category.slug,self.slug])
    def get_delete(self):
        return reverse('car_app:delete',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.name