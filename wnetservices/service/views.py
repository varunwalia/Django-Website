# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from crispy_forms.utils import render_crispy_form

from django import forms
from django.conf import settings
from django.http import HttpResponse , HttpResponseRedirect,  Http404 
from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin




from forms import ContactForm

# Create your views here.

def page(request):
	return render(request , 'home1.html' , {})




def contact(request):
	form_contact = ContactForm(request.POST or None)
	if form_contact.is_valid():
		name         = form_contact.cleaned_data.get('name')
		contact      = form_contact.cleaned_data.get('contact')
		email   	 = form_contact.cleaned_data.get('email')
		query	     = form_contact.cleaned_data.get('query')

		subject = 'Thanks For Visit'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email , from_email]
		message = """ Thanks  %s For providing us your valuable time . We will be in touch soon .
		             
		             For Further queries , you can contact on : 9811011051 or

		              reach us at wnetservices@netlive.com """ %(name)   

		send_mail(subject , message , from_email , to_email , fail_silently= False)	
		messages.success(request, 'Your Response was recorded.') 


		return redirect('contact')
		

	return render(request,  'contact_form.html', {'form':form_contact})
	# ctx = {}
	# ctx.update(csrf(request))
	# form_html = render_crispy_form(form_contact , context=ctx)