
import  requests
from . import models
from datetime import datetime
import json
import xlrd

def handleNullDict(**kwargs):
    re_kwargs = {}
    for key,value in kwargs.items():
        if isinstance(value,str):
            if value.strip() == "" or value is None:
                continue
            else:
                re_kwargs[key] = value
    return re_kwargs



def getInterface(report_name,*xargs):
        data_time = datetime.now()

        try:
            res = models.ResultModel.objects.create(name=report_name, date_time=data_time)
        except Exception as e:
            return (False,"创建报告%s失败,时间为%s!异常为：%s" % (report_name,data_time,str(e)))
        pass_count = 0
        for i in xargs:
            try:
                inter = models.InterfaceModel.objects.get(pk = i)
            except Exception as e:
                json_string ="获取接口信息失败，接口主键为%s,异常信息为：%s" % (i,str(e))
                result_pass = False
            else:
                inter_checkpoint = eval(inter.checkpoint)
                result_resp = ""
                result_pass = True
                inter_method = inter.method
                headers_data = eval(inter.header)
                json_data = eval(inter.json_data)
                if isinstance(headers_data,dict) and isinstance(json_data,dict) and isinstance(inter_checkpoint,dict):
                    try:
                        if inter_method == "POST":
                            resp = requests.request("POST",inter.host+inter.path,headers=eval(inter.header),json=eval(inter.json_data))
                            resp_json = resp.json()
                            json_string = json.dumps(resp_json, indent=4, ensure_ascii=False)
                            for p in inter_checkpoint:
                                if inter_checkpoint[p] != resp_json.get(p, None):
                                    result_pass = False
                                    break
                        elif inter_method == "GET":
                            resp = requests.request("GET", inter.host + inter.path, headers=eval(inter.header), params=eval(inter.params))
                            resp_json = resp.json()
                            json_string = json.dumps(resp_json, indent=4, ensure_ascii=False)
                            for p in inter_checkpoint:
                                if inter_checkpoint[p] != resp_json.get(p, None):
                                    result_pass = False
                                    break
                        else:
                            json_string = "不支持的请求方法%s" % inter_method
                            result_pass = False
                    except Exception as e:
                        json_string = "请求失败,异常信息为：%s" % e
                        result_pass = False
                else:
                    json_string = "请求参数或头文件或检查点格式不正确！"
                    result_pass = False

                if result_pass:
                    pass_count += 1
            res.interfacetestresult_set.create(response_data=json_string,is_pass=result_pass)
        res.sum_count = len(xargs)
        res.pass_count = pass_count
        res.save()
        return (True,res)



def handleExcel(excel_data):
    data = xlrd.open_workbook(filename=None,file_contents=excel_data,encoding_override="gbk")
    table = data.sheet_by_index(0)
    inter_sum = table.nrows-1
    inter_success_count = 0
    for row in range(1,table.nrows):
        table_data =  table.row_values(row)
        try:
            name_scene = table_data[8].split(",")
            host = table_data[0]
            path = table_data[1]
            method = table_data[2]
            header = eval(table_data[3])
            json_data = eval(table_data[4])
            checkpoint = eval(table_data[7])
            scene_comment = name_scene[0]
            system_belong = name_scene[1]
        except Exception as e:
            continue
        list_keys = ["host","path","method","header","json_data","checkpoint","name","scene_comment","system_belong"]
        list_values = [host,path,method,header,json_data,checkpoint,scene_comment,system_belong,3]
        try:
            models.InterfaceModel.objects.create(**dict(zip(list_keys,list_values)))
            inter_success_count += 1
        except Exception as e:
            continue
    return (inter_success_count,inter_sum)


def basicModelConfig():
    HOST_CHOICES = (("http://192.168.3.20:8081","麦芽_STB"),
                    ("http://192.168.3.20:8082", "麦芽_SIT"),
                    ("http://192.168.3.20:8083", "麦芽_PRE"),
                    ("http://192.168.3.20:8084", "麦芽_PRD"),
                    ("http://192.168.3.20:8080", "征信_STB"),
                    ("https://scbgw.pre.nonobank.com", "征信_PRE"),
                    ("https://scbgw.nonobank.com", "征信_PRD"),

                    )
    REQUEST_METHOD = (("POST","POST请求"),
                      ("GET", "GET请求"),
                      )

    SYSTEM_CHOICE = ((1,"麦芽APP"),
                     (2, "麦芽后台"),
                     (3, "征信平台"),
                     (4, "反欺诈平台"),
                     (5, "贷后系统"),)

    return {"hc":HOST_CHOICES,"rm":REQUEST_METHOD,"sc":SYSTEM_CHOICE}
