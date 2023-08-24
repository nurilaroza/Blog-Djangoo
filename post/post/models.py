from django.db import models

#Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=55,verbose_name='Название поста')
    description = models.TextField(verbose_name='Описание поста')
    image = models. ImageField(upload_to='/post_image/', verbose_name='фото публикации')
    created = models.DateTimeField(verbose_name='Дата публикации поста')

class Meta:
    verbose_name = 'Пост'
    verbose_name_plural = 'Посты'

    def__str__(self) - > str:
       return f'{self.title}  - {self.created}'