from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
# class ProfileView(r):
#     template_name = 'template/portfolio/index.html'


def get_portfolio(request):
    return render(request, 'portfolio/index.html')
