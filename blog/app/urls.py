from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.a.as_view(),name="home"),
    path('add',views.add,name="add"),
]