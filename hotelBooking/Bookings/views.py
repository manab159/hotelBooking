from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Bookings.models import Status,Feature,Hotel,Customer,Booking,HotelFeature
from .forms import LoginForm, RegistrationForm,BookHotelForm
from django.db import transaction
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

def dashboard(request):
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
        customerObj = Customer.objects.get(contact=contact)
        request.session['customerPk']=customerObj.pk
        print(request.session)
        return render(request , 'booking/dashboard.html')


def bookHotel(request):
    return render(request, 'booking/bookHotel.html', {
        'form': BookHotelForm
    })

def bookingResult(request):
    if request.method == 'POST':
        hotelList = list(Hotel.objects.filter(location__iexact=request.POST['location']).values_list('name',flat=True))
        request.session['location'] = request.POST['location']
        if request.POST['amount']:
            request.session['amount']=request.POST['amount']

        if request.POST['checkInDate']:
            request.session['checkInDate'] = request.POST['checkInDate']

        if request.POST['checkOutDate']:
            request.session['checkOutDate'] = request.POST['checkOutDate']

        print(request.POST['location'])
        return render(request, 'booking/hotelList.html', {'hotelList': hotelList})

@transaction.atomic
def bookingConfirmation(request):
    request.session['hotelName']=request.POST['hotelName']
    hotelObj = Hotel.objects.get(name=request.session['hotelName'])

    customerObj = Customer.objects.get(pk=request.session['customerPk'])
    bookingObj = Booking(h_id=hotelObj,c_id=customerObj,amount=request.session['amount'],
                         status=Status.objects.get(status="COMPLETED"),checkInDate=request.session['checkInDate'],
                         checkOutDate=request.session['checkOutDate'])
    bookingObj.save()
    totalCount = hotelObj.visitorCount +1
    hotelObj.visitorCount=totalCount
    hotelObj.save()
    return HttpResponse('Your Booking has been Successfully Done')

def viewVisits(request):
    # hotelList=Hotel.objects.all().values_list('name',flat=True)
    hotelList = Hotel.objects.all()
    visitorCount=Hotel.objects.all().values_list('visitorCount',flat=True)
    return render(request,'booking/viewVisit.html',{'hotelList': hotelList,'visitorCount' : visitorCount})
