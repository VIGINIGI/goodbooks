from django.contrib import admin
from .models import User,Feedback,Book,Tag
# Register your models here.
admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(Book)
admin.site.register(Tag)