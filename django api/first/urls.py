"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url, include
from uni import  views

"""  router  """
from rest_framework import routers

r = routers.DefaultRouter()
r.register('' , views.user_list2)


rr = routers.DefaultRouter()
rr.register('' , views.users_json)


d = routers.DefaultRouter()
d.register('' , views.doctor_list)

ss = routers.DefaultRouter()
ss.register('' , views.us_list)


ff= routers.DefaultRouter()
#ff.register('' , views.us2_list)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('users/' , views.user_list.as_view()),
    path('user2/' , include(r.urls)),
    path('user/' , include(rr.urls)),
    path('doctor/', include(d.urls)),
    path('us/', include(ss.urls)),
    path('us2/', include(ff.urls)),
    url(r'^', include('uni.urls')),

]
