"""P3D2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.addInterface,name="addInterface"),
    path('del/',views.delInterface,name="delInterface"),
    path('query/',views.queryInterface,name="queryInterface"),
    path('actionTest/',views.actionTest,name="actionTest"),
    path('editInter/<int:inter_id>/',views.editInterPost,name="editInterPost"),
    path('queryResult/',views.queryResult,name="queryResult"),
    path('uploadInter/',views.uploadInter,name="uploadInter"),
    path('queryResultDetail/<int:report_id>/',views.queryResultDetail,name="queryResultDetail"),
    path('bulkEdit/',views.bulkEdit,name="bulkEdit"),
    path('toBulkEdit/',views.toBulkEdit,name="toBulkEdit"),
    path('toBulkDelete/',views.toBulkDelete,name="toBulkDelete"),
    # path('bulkDelete/',views.bulkDelete,name="bulkDelete"),
]
