from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sajeena", views.sajeena, name="sajeena"),
    path("iloveanime", views.iloveanime, name="iloveanime")
]