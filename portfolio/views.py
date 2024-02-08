from django.shortcuts import render
from django.views import View
from .models import Profile,About,EducationAndExpericence,Skills,Services

# Create your views here.
# class ProfileView(r):
#     template_name = 'template/portfolio/index.html'

class Portfolio(View):
    def get(self, request):
        user = Profile.objects.first()
        about = About.objects.first()
        quality = EducationAndExpericence.objects.all()
        skills = Skills.objects.all()
        services = Services.objects.all()
        content={
            "user": user,
            "about": about,
            "quality": quality,
            "skills": skills,
            "services": services,
        }
        return render(request, 'portfolio/index.html',content)
