from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("sajeena", views.sajeena, name="sajeena"),
    path("iloveanime", views.iloveanime, name="iloveanime")
]