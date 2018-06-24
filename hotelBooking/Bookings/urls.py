from django.urls import path

from . import views


app_name='Bookings'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration'),
    path('validateUser', views.validateUser, name='validateUser'),
    path('bookHotel', views.bookHotel, name='bookHotel'),
    path('bookingResult', views.bookingResult, name='bookingResult'),
    path('bookingConfirmation', views.bookingConfirmation, name='bookingConfirmation'),
]