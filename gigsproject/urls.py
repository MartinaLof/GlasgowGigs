from django.conf.urls import url
from gigsproject import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about')]
