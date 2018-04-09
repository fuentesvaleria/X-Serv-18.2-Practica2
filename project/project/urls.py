from django.conf.urls import include, url
from django.contrib import admin
from acorta import views

    #nombre de los def que usamos en views.py

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.pagprincipal, name="Pag Inicial"), 
	url(r'^(\d+)$', views.redirigir, name="Redirigir a la web pedida")
]
