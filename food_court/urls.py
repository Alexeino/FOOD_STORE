from django.urls import path
from . import views


urlpatterns= [
    path("",views.index,name="index"),
    path("<slug:slug>",views.food_detail,name="food_detail")
]