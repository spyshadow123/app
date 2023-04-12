from django.contrib import admin

# Register your models here.
from bhopal.models import People
@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mobile','message']