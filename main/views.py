from django.shortcuts import render,HttpResponse
from django.views.generic import View

class Sabado(View):
	def get(self,request):
		#return HttpResponse('Quiobole!')
		return render(request,'hola.html')