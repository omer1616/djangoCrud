from django.urls import path
from . import views


urlpatterns = [
    path('',  views.main,  name='main'),
    path('main/',  views.main,  name='main'),
    path('store/',  views.store,  name='store'),
    path('card/',  views.card,  name='card'),
    path('checkout/',  views.checkout,  name='checkout'),

]