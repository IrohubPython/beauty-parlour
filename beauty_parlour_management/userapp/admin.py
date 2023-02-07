from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Cart)
admin.site.register(Checkout)
admin.site.register(Contact)

class abc(admin.ModelAdmin):
    list_display=['name','email','mobile','password1','password2']
    list_editable = ['email']
admin.site.register(Register,abc)