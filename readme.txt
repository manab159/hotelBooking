This is a Hotel Booking System

Here are the steps so that you could jump into the implementation part

You need to have installed Python3 on your System so that you could run this Application

Step 1:
Clone this Project on the the folder you want to run it from 
Here is the link : https://github.com/manab159/hotelBooking.git
run the command : git clone https://github.com/manab159/hotelBooking.git

Step 2:
>>cd hotelBooking
>>ls
Note : manage.py file is present

Step 3:
You need to run migrations to create the SqlLite Database
>>python3 manage.py makemigrations
>>python3 manage.py migration

Note: On Exceuting the above commands it will create your application Database

Step 4:
For Admin activities you need to create a super-user
>>python3 manage.py createsuperuser
>>username :
>>email:
>>password:
>>password:

Note : You need to populate the fields username,email,password to create the superuser
Remember the field beacuse you will need these fields for logging as a admin

Step 5:
You are ready yo Go now
>>python3 manage.py runserver
Note: By default the server will run at port 8000
You can change the port number by specifying the Port Number Explicitly
>> python3 manage.py runserver 8080
This will change the port number to 8080

We are ready to go:::::

Note: Few thing to remember before we start
You can start the application in any browser
Firstly hit the url http://127.0.0.1:8080/admin and login with the credentials you used earlier to create the superuser
You need to populate the required fields like Hotel,Status
Customer can be created by Registering
Bookings will be populated once you do a Transaction
For populating Status click on status on http://127.0.0.1:8080/admin and then click Add status and populate both the fields
Similarly Hotels can be Populated

Hit the url http://127.0.0.1:8000/booking/ To start the application
