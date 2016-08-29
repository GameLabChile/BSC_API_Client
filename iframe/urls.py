from django.conf.urls import url
from . import views

urlpatterns = [
	#ej: /google/
    url(r'^$', views.index, name="index"),
    url(r'([^/]+)/([^/]+)/([^/]+)/([^/]+)/$', views.form, name="tile"),

]