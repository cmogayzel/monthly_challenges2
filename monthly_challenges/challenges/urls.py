from django.urls import path
from . import views


urlpatterns = [

    path("",views.home),
    path("<int:month>",views.number_month),
    path("<str:month>/",views.monthly_challenge, name="month-challenge"),

  

]