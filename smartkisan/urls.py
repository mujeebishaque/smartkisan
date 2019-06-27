"""smartkisan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from headlines import views

urlpatterns = [

    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('rates/', views.ratesList, name='rateslist'),
    path('buyandsell/', views.buyAndSell, name='buyandsell'),
    path('aboutus/', views.aboutUs, name='aboutus'),
    path('contactus/', views.contactUs, name='contactus'),

]

# admin panel modifications
admin.site.site_title = 'Smart Kisan L G U'
admin.site.index_title = 'Smart Kisan L G U'
admin.site.site_header = 'Smart Kisan L G U'
# modification to admin panel ends here
