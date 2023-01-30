from django.contrib import admin
from .models import masturbation

# Register your models here.
class admin_masturbation(admin.ModelAdmin):
	list_display = [
        'id',
		'name',
        'createDate',
]
admin.site.register(masturbation,admin_masturbation)