from django.contrib import admin
from .models import Profile,category_gallery,picture_gallery,About,Skills,Services,EducationAndExpericence


admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Services)
admin.site.register(EducationAndExpericence)
admin.site.register(category_gallery)
admin.site.register(picture_gallery)
# Register your models here.
