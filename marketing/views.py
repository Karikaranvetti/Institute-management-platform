from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings	
# Create your views here.

def index(request):
	services1=services.objects.all()
	courses1=courses.objects.all()
	courses_detiles1=courses_detiles.objects.all()
	Tutor1=Tutor.objects.all()
	About1=About.objects.all()

	if request.method == 'POST':
		name1 = request.POST.get('name')
		phone1 =request.POST.get('phone')
		email1 = request.POST.get('email')
		message1 =request.POST.get('message')
		print(name1)

		Contact.objects.create(
			name=name1,
			email=email1,
			phone=phone1,
			message=message1

			)

		heder='hello'+name1+'your message received'
		meg='Thanks for your information we will let you konw soon..  \n\nFrom New Success college Team\nThank you.'
		send_mail(heder,meg,settings.EMAIL_HOST_USER,[email1], fail_silently=False)
	 
		context = {'name1':name1 }
		return render(request, 'marketing/index1.html', context)





	context = {'services1':services1,'courses1':courses1,'courses_detiles1':courses_detiles1,'Tutor1':Tutor1,'About1':About1}
	return render(request, 'marketing/index.html', context)


def notfound(request):

	return HttpResponse('Page not Found')



 