from django.db import models

# Create your models here.

class services(models.Model):
	 
	name = models.CharField(max_length=200, null=True)
	detiles = models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.name



class courses_detiles(models.Model):
	 
	name = models.CharField(max_length=200, null=True)
	detiles = models.CharField(max_length=500, null=True)
	Date=models.CharField(max_length=200, null=True)
	Tutor=models.CharField(max_length=200, null=True)
	Category=models.CharField(max_length=200, null=True)
	detiles_img= models.ImageField(upload_to='pics',default= "defoult.jpg"	,null=True,blank=True)
	 
	

	def __str__(self):
		return self.name



class courses(models.Model):
	 
	name = models.CharField(max_length=200, null=True)
	detiles = models.CharField(max_length=200, null=True)
	img= models.ImageField(upload_to='pics',default= "defoult.jpg"	,null=True,blank=True)
	courses_detiles = models.ForeignKey(courses_detiles, on_delete=models.SET_NULL, null=True, blank=True)


	def __str__(self):
		return self.name






class About(models.Model):
	 
	period  = models.CharField(max_length=200, null=True)
	titel = models.CharField(max_length=200, null=True)
	info = models.CharField(max_length=500, null=True)
	pic= models.ImageField(upload_to='pics',default= "defoult.jpg"	,null=True,blank=True)

	def __str__(self):
		return self.titel



class Tutor(models.Model):
	 
	name  = models.CharField(max_length=200, null=True)
	role = models.CharField(max_length=200, null=True)
	profile_pic= models.ImageField(upload_to='pics', default= "defoult.jpg"	,null=True,blank=True)
	facebook  = models.CharField(max_length=200,default='NotFound', null=True,blank=True)
	twitter  = models.CharField(max_length=200,default='NotFound', null=True,blank=True)
	linkedin  = models.CharField(max_length=200,default='NotFound', null=True,blank=True)



	def __str__(self):
		return self.name


class Contact(models.Model):
	 
	name  = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200, null=True)
	message  = models.CharField(max_length=1000, null=True)


	def __str__(self):
		return self.name




	 
 