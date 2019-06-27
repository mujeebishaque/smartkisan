from django.shortcuts import render
from headlines.models import Headline
from rates.models import Rate
# Create your views here.

def index(request):
    # fetch and show the news from the official government website.
    # try:
    #     from bs4 import BeautifulSoup
    #     import requests
    # except ImportError:
    #     raise("""Can't locate required packages/libraries i.e. requests/BeautifulSoup. Please install them using >pip install BeautifulSoup
    #     and >pip install requests""")
    
    # websiteContent = requests.get('http://www.parc.gov.pk/index.php')
    # soup = BeautifulSoup(websiteContent.text, 'html.parser')
    # soup.find('div', attrs={'class': 'tContainer221'})
    items = Headline.objects.all()
    # itemsList = []
    # itemsList.append(items)

    return render(request, 'index.html',  {'Content': items})

def ratesList(request):
    items = Rate.objects.all()
    
    return render(request, 'rates.html', {'items': items})

def buyAndSell(request):
    return render(request, 'buyandsell.html')

def aboutUs(request):
    return render(request, 'about.html')

def contactUs(request):
    return render(request, 'contact.html')
