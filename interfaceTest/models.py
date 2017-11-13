from django.db import models
from .tools import basicModelConfig

# Create your models here.



class InterfaceModel(models.Model):
    name = models.CharField(max_length=20)
    scene_comment = models.CharField(max_length=50)
    host = models.CharField(choices=basicModelConfig()["hc"],max_length=200)
    path = models.CharField(max_length=200)
    system_belong = models.IntegerField(choices=basicModelConfig()["rm"])
    method = models.CharField(choices=basicModelConfig()["sc"],max_length=20)
    header = models.CharField(max_length=200,null=True,blank=True)
    json_data = models.CharField(max_length=2000,null=True,blank=True)
    params =  models.CharField(max_length=2000,null=True,blank=True)
    checkpoint = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + "," + self.scene_comment

class ResultModel(models.Model):
    name = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    sum_count = models.IntegerField(default=0)
    pass_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class InterfaceTestResult(models.Model):
    result = models.ForeignKey(ResultModel,on_delete=models.CASCADE)
    response_data = models.CharField(max_length=999999999)
    is_pass = models.BooleanField()







