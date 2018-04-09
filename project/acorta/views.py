from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#https://docs.djangoproject.com/es/2.0/intro/tutorial04/
#Después de incrementar el conteo de la elección, el código retorna
#una HttpResponseRedirect en lugar de una HttpResponse normal HttpResponseRedirect toma un único argumento:
#La URL a la que el usuario será redirigido (vea el siguiente aspecto de cómo construimos la URL en este caso).

from django.views.decorators.csrf import csrf_exempt
from acorta.models import list_urls

# Create your views here.
#https://docs.djangoproject.com/en/2.0/topics/http/views/

@csrf_exempt

def pagprincipal(request):
	lista = list_urls.objects.all() #para mostrar todos nuestras urls https://tutorial.djangogirls.org/es/django_orm/
	if request.method == "GET": 
	#escribo formulario http://world-it.ro/web/creeaza-ti-propriul-site/curs-html/lectia-10-html-formular
		respuesta = ("<form method='POST'>" + "Introduce Url" + "input type='text' name='url'><br>" + 
					"input type='submit' value='Send'></form>")
		if len(lista) == 0:
			respuesta = ("<form method='POST'>" + "Introduce Url" + "input type='text' name='url'><br>" + 
					"input type='submit' value='Send'></form>") + "<br> esta vacio" #agrego que esta vacio
		else:
			for url in lista:
				url_acortada = "http://localhost:1234/" + str(url.id)
				respuesta += ("<br>url: " + url.url_larga + "url acortada: " "<a href"+ url_acortada + ">" + url_acortada + "</a>") #aumento
	elif request.method == "POST":
		url_larga = request.POST['url']	 #http://docs.python-requests.org/es/latest/user/quickstart.html 	
		if (url_larga[0:8] != "https://" and url_larga[0:7] != "http://"): #pueede haber de las dos maneras
			url_larga = "http://" + url_larga
			try:
				url_acortada = list_urls.objects.get(url_larga=url_larga) #es igual que ne docs.python anterior
			except list_urls.DoesNotExist: #https://docs.djangoproject.com/en/2.0/ref/exceptions/
				url = list_urls(url_larga=url_larga)
				url.save() #lo guardo
				url_acortada = list_urls.objects.get(url_larga=url_larga)
				
			url_acortada = "http://localhost:1234/" + str(url_acortada.id)
			respuesta = ("url acortada de " + url_larga + "es" + "<a href"+ url_acortada + ">" + url_acortada + "</a>")
	else:
		return HttpResponse("metodo incorrecto", status=405)
	
	return HttpResponse(respuesta, status=200)
	
def redirigir(request,resource):
	try:
		url_larga = list_urls.objects.get(id=resource).url_larga
		return HttpResponseRedirect(url_larga)
	except list_urls.DoesNotExist:
		respuesta = "recurso no disponible"
		return HttpResponse(respuesta,status=404)