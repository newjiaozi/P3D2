from django import forms

from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

from .tools import basicModelConfig

hc = basicModelConfig()["hc"]
rm = basicModelConfig()["rm"]
sc = basicModelConfig()["sc"]


class InterfaceForm(forms.Form):

    name = forms.CharField(max_length=20,label="接口名称")
    scene_comment = forms.CharField(max_length=50,label="场景描述")
    host = forms.ChoiceField(choices=hc,label="接口地址")
    path = forms.CharField(max_length=200,label="接口路径",widget=forms.Textarea)
    system_belong = forms.ChoiceField(choices=sc,label="所属系统")
    method = forms.ChoiceField(choices=rm,label="请求方法")
    header = forms.CharField(max_length=200,label="头信息",required=False,widget=forms.Textarea(attrs={'required': False}))
    json_data = forms.CharField(max_length=2000,label="JSON格式数据（POST）",required=False,widget=forms.Textarea(attrs={'required': False}))
    params =  forms.CharField(max_length=2000,label="GET传参",required=False,widget=forms.Textarea(attrs={'required': False}))
    checkpoint = forms.CharField(max_length=1000,label="检查点",widget=forms.Textarea)



class ResultForm(forms.Form):
    name = forms.CharField(max_length=20,label="报告名称")
    interface = forms.CharField(max_length=20,label="对应接口")
    date_time = forms.DateTimeField(label="测试时间")
    response_data = forms.CharField(max_length=999999999,label="响应信息",widget=forms.Textarea)
    is_pass = forms.BooleanField(label="是否通过")

class QueryInterfaceForm(forms.Form):

    name = forms.CharField(max_length=20,label="接口描述",required=False)
    host = forms.ChoiceField(choices=hc,label="接口地址",required=False,initial=(("http://192.168.3.20:8081","麦芽_STB")))
    path = forms.CharField(max_length=200,label="接口路径",required=False)
    system_belong = forms.ChoiceField(choices=sc,label="所属系统",required=False,initial=(1,"麦芽APP"))



def validate_excel(value):
    if value.name.split('.')[-1] not in ['xls','xlsx']:
        raise ValidationError(_('Invalid File Type: %(value)s'),params={'value': value},)

class UploadFileForms(forms.Form):
    up_file = forms.FileField(label="从Excel文件导入",validators=[validate_excel])


class BulkEditForms(forms.Form):

    name = forms.CharField(max_length=20,label="接口名称",required=False)
    host = forms.ChoiceField(choices=hc,label="接口地址",required=False)
    path = forms.CharField(max_length=200,label="接口路径",widget=forms.Textarea,required=False)
    system_belong = forms.ChoiceField(choices=sc,label="所属系统",required=False)
    method = forms.ChoiceField(choices=rm,label="请求方法",required=False)
    header = forms.CharField(max_length=200,label="头信息",required=False,widget=forms.Textarea(attrs={'required': False}))
    checkpoint = forms.CharField(max_length=1000,label="检查点",widget=forms.Textarea,required=False)

