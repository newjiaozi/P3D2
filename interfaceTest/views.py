from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect,Http404
from . import forms
from . import models
from . import tools
from django.http import QueryDict
from django.forms.models import model_to_dict
# Create your views here.


def index(request):
    try:
        inter_data = models.InterfaceModel.objects.filter(host="http://192.168.3.20:8081",system_belong=1,is_delete=False)
        queryInterfaceForm = forms.QueryInterfaceForm()
        f_forms = forms.UploadFileForms()
        request.session["res_count"] = len(inter_data)
        return render(request,"interfaceTest/scanInterface.html",{"queryInterfaceForm":queryInterfaceForm,"inter_data":inter_data,"f_forms":f_forms})
    except Exception:
        raise Http404


def addInterface(request):
    data_form = forms.InterfaceForm()
    if request.method == "POST":
        data_post = request.POST
        data_form = forms.InterfaceForm(data_post)
        if data_form.is_valid():
            data_clean = data_form.cleaned_data
            try:
                models.InterfaceModel.objects.create(**data_clean)
                # models.InterfaceModel.objects.update_or_create(**data_clean)
                msg = "接口【%s】添加成功" % data_clean.get("name","null")
            except Exception:
                msg = "接口【%s】添加出现异常！" % data_clean.get("name","null")
        else:
            msg = "表单验证不通过！"

        request.session["msg"] = msg
        return HttpResponseRedirect(reverse("addInterface"))

    else:
        # request.session["msg"]="快来添加新接口吧！"
        return render(request,"interfaceTest/addinterface.html",{"data_form":data_form})



def delInterface(request):
    if request.method == "POST":
        id = request.POST.get("delname")
        inter = models.InterfaceModel.objects.get(pk=id)
        # inter.delete()
        inter.is_delete = True
        inter.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        raise Http404


def queryInterface(request):
    if request.method == "POST":
        data =  request.POST
        qif_data = forms.QueryInterfaceForm(data)

        f_forms = forms.UploadFileForms()
        if qif_data.is_valid():
            qif_data_clean = qif_data.cleaned_data

            inter_name = qif_data_clean["name"]
            inter_host = qif_data_clean["host"]
            inter_path = qif_data_clean["path"]
            inter_system = qif_data_clean["system_belong"]
            try:
                kwargs = tools.handleNullDict(**qif_data_clean)
                kwargs["is_delete"] = False
                inter_data = models.InterfaceModel.objects.filter(**kwargs)
                request.session["res_count"] = len(inter_data)
                return render(request,"interfaceTest/scanInterface.html",{"inter_data":inter_data,"queryInterfaceForm":qif_data,"f_forms":f_forms})
            except Exception:
                raise Http404
    else:
        return HttpResponseRedirect(reverse("index"))



def actionTest(request):
    if request.method == "POST":
        data_post = request.POST
        report_name = data_post.get("report_name","默认报告名称").strip()
        interdataId = data_post.getlist("interdataId")
        result = tools.getInterface(report_name,*interdataId)
        if result[0]:
            try:
                res = models.ResultModel.objects.get(pk=result[1].id)
                results = models.InterfaceTestResult.objects.filter(result_id = result[1].id)
                return render(request,"interfaceTest/scanReport.html",{"result":res,"results":results})
            except Exception as e:
                raise Http404
        else:
            request.session["msg"] = "接口测试执行失败！%s" % result[1]
            return HttpResponseRedirect(reverse("index"))
    else:
        raise Http404

def editInter(request):
    if  request.method == "GET":
        req_get = request.GET
        inter_id = req_get.get("id",None)
        if inter_id:
            data_form = forms.InterfaceForm()
            inter_data = models.InterfaceModel.objects.get(pk=inter_id)
            inter_data_dict = model_to_dict(inter_data)
            qd = QueryDict(mutable=True)
            qd.update(inter_data_dict)
            data_form = forms.InterfaceForm(qd)
            return render(request,"interfaceTest/editInter.html",{"data_form":data_form})
        else:
            raise Http404
    elif request.method == "POST":
        data_post = request.POST
        data_form = forms.InterfaceForm(data_post)
        if data_form.is_valid():
            data_clean = data_form.cleaned_data
            try:
                inter = models.InterfaceModel.objects.get(pk=12)
                inter.objects.update(**data_clean)

                msg = "接口【%s】修改成功" % data_clean.get("name","null")
            except Exception:
                msg = "接口【%s】修改出现异常！" % data_clean.get("name","null")
        else:
            msg = "表单验证不通过！"

        request.session["msg"] = msg
        return HttpResponseRedirect(reverse("addInterface"))

def editInterPost(request,inter_id):
    msg = ""
    if request.method == "POST":
        data_post = request.POST
        data_form = forms.InterfaceForm(data_post)
        if data_form.is_valid():
            data_clean = data_form.cleaned_data
            try:
                models.InterfaceModel.objects.filter(pk=inter_id).update(**data_clean)
                msg = "接口修改成功"
            except Exception as e:
                msg = "接口修改异常"
                raise Http404(e)
        else:
            msg = "表单验证不通过！"
        request.session["msg"] = msg
        return HttpResponseRedirect(reverse("index"))
    elif request.method == "GET":
        req_get = request.GET
        if inter_id:
            data_form = forms.InterfaceForm()
            inter_data = models.InterfaceModel.objects.get(pk=inter_id)
            inter_data_dict = model_to_dict(inter_data)
            qd = QueryDict(mutable=True)
            qd.update(inter_data_dict)
            data_form = forms.InterfaceForm(qd)
            return render(request, "interfaceTest/editInter.html", {"data_form": data_form,"inter_id":inter_id})
        else:
            raise Http404("不支持的请求！")

def queryResult(request):
    try:
        results = models.ResultModel.objects.all().order_by("-date_time")
        return render(request,"interfaceTest/queryResult.html",{"results":results})
    except Exception as e:
        raise Http404(e)


def queryResultDetail(request,report_id):
    try:
        result = models.ResultModel.objects.get(pk=report_id)
        results = models.InterfaceTestResult.objects.filter(result_id = report_id)
        return render(request,"interfaceTest/scanReport.html",{"results":results,"result":result})
    except Exception as e:
        raise Http404(e)

def uploadInter(request):
    if request.method == "POST":
        file_form = forms.UploadFileForms(request.POST,request.FILES)
        if file_form.is_valid():
            request.session["msg"] = "添加成功%s条，共%s条！" % tools.handleExcel(request.FILES['up_file'].read())
            return HttpResponseRedirect(reverse("index"))
        else:
            request.session["msg"] = "上传文件格式不正确！"
            return HttpResponseRedirect(reverse("index"))
    else:
        request.session["msg"] = "不支持的请求！"
        return HttpResponseRedirect(reverse("index"))



def bulkEdit(request):
    if request.method == "POST":
        qd = QueryDict(mutable=True)
        data_post = request.POST
        # print(data_post)
        qd.update(data_post)
        interdataId = eval(data_post.get("interdataid"))
        qd.pop("interdataid")
        qd.pop("csrfmiddlewaretoken")
        qd = qd.dict()
        kwargs = tools.handleNullDict(**qd)
        # print(interdataId,type(interdataId),kwargs)
        update_count = models.InterfaceModel.objects.filter(id__in = interdataId).update(**kwargs)
        request.session["msg"] = "更新成功%s条接口" % update_count
        return HttpResponseRedirect(reverse("index"))
    else:
        request.session["msg"] = "不支持的请求类型！"
        return HttpResponseRedirect(reverse("index"))

def toBulkEdit(request):
    if request.method == "POST":
        data_post =  request.POST
        interdataId = data_post.getlist("interdataId")
        data_form = forms.BulkEditForms()
        return render(request, "interfaceTest/bulkEdit.html", {"data_form": data_form,"interdataId":interdataId})
    else:
        request.session["msg"] = "不支持的请求类型！"
        return HttpResponseRedirect(reverse("index"))



def toBulkDelete(request):
    if request.method == "POST":
        data_post = request.POST
        interdataId = data_post.getlist("interdataId")
        delete_count = models.InterfaceModel.objects.filter(id__in = interdataId).update(is_delete = True)
        request.session["msg"] = "删除成功，共删除%s个接口！" % delete_count
        return HttpResponseRedirect(reverse("index"))
