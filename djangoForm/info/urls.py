from django.urls import path
from . import views

app_name = "info"
urlpatterns = [
  path("get", views.get, name = "get"),
  path("post", views.post, name="post"),
  path("printget", views.printget, name="printget" ),
  path("printpost", views.printpost, name="printpost" )

]