from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Bookings.models import Status,Feature,Hotel,Customer,Booking,HotelFeature
from .forms import LoginForm, RegistrationForm,BookHotelForm
# Create your views here.
def index(request):
	return render(request, 'booking/index.html')


def login(request):
	return render(request, 'booking/login.html', {
		'form': LoginForm
	})

def register(request):
    return render(request, 'booking/registration.html', {
        'form': RegistrationForm
    })

def registration(request):
    if request.method == 'POST':
        customerObj = Customer(name=request.POST['name'],contact=request.POST['contact'],
                               password=request.POST['password'],email=request.POST['email'],
                               address=request.POST['address'])
        customerObj.save()
    return render(request, 'booking/dashboard.html')

def validateUser(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        password = request.POST['password']
        customerValidate = Customer.objects.filter(contact=contact).exists()
        if not customerValidate:
            return render(request, 'booking/login.html', {
                'form': LoginForm(initial={'contact': contact,'name' :name}, auto_id=False),
                'error_message': 'Your Contact is not registered'
            })
        if Customer.objects.get(contact=contact).password != password :
            return render(request, 'booking/login.html', {
                'form': LoginForm(initial={'contact': contact , 'name' :name}, auto_id=False),
                'error_message': 'Credentials donot match. Please Try Again'
            })
        return render(request , 'booking/dashboard.html',{customerObj: Customer.objects.get()})


def bookHotel(request):
    return render(request, 'booking/bookHotel.html', {
        'form': BookHotelForm
    })

def bookingResult(request):
    if request.method == 'POST':
        hotelList = list(Hotel.objects.filter(location__iexact=request.POST['location']).values_list('name',flat=True))
        print(hotelList)
        return render(request, 'booking/hotelList.html', {'hotelList': hotelList})

def bookingConfirmation(request):
    return render(request)

def viewCount():
	pass