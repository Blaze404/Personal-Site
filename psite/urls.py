from django.conf.urls import url
from . import views

app_name = "psite"

urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'add/$', views.AddProject.as_view(), name="add-project"),
]