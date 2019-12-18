from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def home_page(request):
	context = {
		"title":"Merhaba!",
		"content": "Hoş geldiniz!",
		"premium_content": "Ohh Yeahhhhhh! Welcome to premium Homepage.",
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title":"Hakkımızda",
		"content": "Hakkında Sayfası"
	}
	return render(request, "home_page.html", context)	

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"İletişim",
		"content": "Formu doldurarak bize ulaşabilirsiniz.",
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
		if request.is_ajax():
			return JsonResponse({"message": "Teşekkürler..."})
	
	if contact_form.errors:
		errors = contact_form.errors.as_json()
		if request.is_ajax():
			return HttpResponse(errors, status=400, content_type='application/json')
	# if request.method == "POST":
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))

	return render(request, "contact/view.html", context)
