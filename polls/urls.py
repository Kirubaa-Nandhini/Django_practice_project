from django.urls import path
from . import views
urlpatterns=[
    path("",views.index, name="index"),
    path("<int:q_id>/",views.detail,name="detial"),
    path("<int:q_id>/results/",views.results,name="results"),
]