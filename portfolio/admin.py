from django.contrib import admin
from .models import Profile, category_gallery, picture_gallery, About, Skills, Services, EducationAndExpericence

MAX_OBJECTS = 1


class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Services)
admin.site.register(EducationAndExpericence)
admin.site.register(category_gallery)
admin.site.register(picture_gallery)
