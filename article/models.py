from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    animal_type_choice = (
        ('Kedi','Kedi'),
        ('Köpek','Köpek'),
        ('Fare','Fare'),
        ('Kaplumbağa','Kaplumbağa'),
        ('Diğer','Diğer'),
    )

    animal_age_choice = (
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('Diğer','Diğer'),
    )

    animal_city_choice = (
        ('İstanbul','İstanbul'),
        ('Ankara','Ankara'),
        ('İzmir','İzmir'),
        ('Bursa','Bursa'),
        ('Antalya','Antalya'),
        ('Samsun','Samsun'),
        ('Eskişehir','Eskişehir'),
        ('Trabzon','Trabzon'),
        ('Manisa','Manisa'),
        ('Diğer','Diğer'),
    )

    animal_gender_choice = (
        ('erkek','erkek'),
        ('dişi','dişi'),
        ('Diğer','Diğer'),
    )

    author = models.ForeignKey("auth.User",on_delete=models.CASCADE , verbose_name="Kullanıcı")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    animal_type = models.CharField(max_length=30,blank=True,null=True,choices=animal_type_choice,verbose_name="Tür")
    animal_city = models.CharField(max_length=40,null = True,blank=True,choices=animal_city_choice,verbose_name="Şehir")
    animal_age = models.CharField(max_length=10,null = True,blank=True,choices=animal_age_choice,verbose_name="Yaş")
    animal_gender = models.CharField(max_length=10,null = True,blank=True,choices=animal_gender_choice,verbose_name="Cinsiyet")
    article_image = models.FileField(blank = True , null = True , verbose_name="Makaleye Fotoğraf Ekleyin")

    def __str__(self):
        return self.title 

