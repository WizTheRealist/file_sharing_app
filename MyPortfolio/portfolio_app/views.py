from django.shortcuts import render
from .models import Home, About, Category, Portfolio, Profile, Skills

# Create your views here.
def index(request):
    home = Home.objects.latest('updated')
    #home = Home.objects.order_by('-updated').first()

    about = About.objects.latest('updated')
    #about = About.objects.order_by('-id').first()

    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()


    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }

    return render(request, 'index.html', context)