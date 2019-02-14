# Create your models here.
from django.db import models
from django.urls import reverse
class Sungjuk(models.Model):
    name = models.CharField("이 름", max_length=50, unique=False) #문자열 저장 필드
    kor =  models.IntegerField("국 어", default=0) #초기치 = 0
    mat =  models.IntegerField("수 학", default=0)
    eng =  models.IntegerField("영 어", default=0)
    tot =  models.FloatField("총 점", default=0)
    avg =  models.FloatField("평 균", default=0)
    def __str__(self):
        return self.name
    @property
    def tot(self):
        return self.kor + self.mat + self. eng
    @property
    def avg(self):
        return round( self.kor + self.mat + self.eng/ 3 , 2)
    def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = '성적'
        verbose_name_plural = '성적셋'
        ordering = ['name']
