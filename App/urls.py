from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^main',views.main,name='main'),

]

