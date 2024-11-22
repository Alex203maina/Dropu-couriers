from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name= 'home'),
    path('home/',views.home, name= 'home'),
    path('about/',views.about, name= 'about'),
    path('features/',views.features, name= 'features'),
    path('contact/',views.contact, name= 'contact'),
    path('services/',views.service, name= 'services'),
    path('teams/',views.team, name= 'teams'),
    path('search/', views.search_price, name='search_price'),

]