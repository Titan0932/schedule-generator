"""schedule_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main_app.views import display_form1,enter_subjects,delete_schedule,schedule_list
from main_app.calculation import sched_calc
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schedule_list),
    path('new/',display_form1),
    path('new/next/<int:id>-<int:numofSubs>/', enter_subjects),
    path('new/next/<int:id>-<int:numofSubs>-<str:subjects>-<str:start>-<str:end>/', sched_calc),
    path('delete/<int:del_id>/',delete_schedule)
]
