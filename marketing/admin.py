from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(services)
admin.site.register(courses)
admin.site.register(About)
admin.site.register(Tutor)
admin.site.register(courses_detiles)
admin.site.register(Contact)
 
