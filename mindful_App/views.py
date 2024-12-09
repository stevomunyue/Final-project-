from django.shortcuts import render
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    """Render the home page (index.html)."""
    return render(request, 'index.html')

def about(request):
    """Render the about page."""
    return render(request, 'about.html')

def articles(request):
    """Render the articles page."""
    return render(request, 'articles.html')

def booking(request):
    """Render the booking page."""
    return render(request, 'booking.html')

def community(request):
    """Render the community page."""
    return render(request, 'community.html')

def moodtracker(request):
    """Render the mood tracker page."""
    return render(request, 'moodtracker.html')

def register(request):
    """Render the registration page."""
    return render(request, 'register.html')

def resources(request):
    """Render the resources page."""
    return render(request, 'resources.html')

def tools(request):
    """Render the tools page."""
    return render(request, 'tools.html')

def videos(request):
    """Render the videos page."""
    return render(request, 'videos.html')
def podcasts(request):
    """Render the podcasts page."""
    return render(request, 'podcasts.html')
def therapists(request):
    """Render the therapists page."""
    return render(request, 'therapists.html')
def faq(request):
    """Render the faq page."""
    return render(request, 'faq.html')
def contact(request):
    """Render the faq page."""
    return render(request, 'contact.html')




# Registration View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Replace 'login' with your login URL name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
import requests
import requests
from requests.auth import HTTPBasicAuth

# Safaricom M-Pesa API credentials
MPESA_CONSUMER_KEY = "fAOaHd5RXh8UKyEyBfVkmOP8TwoGTFIJ8OSgK9MfLCDVkzAR"
MPESA_CONSUMER_SECRET = "GIQLx9IbQWWNch5JKLG0IFcdQrKA8Gv8yYyCPzeGSKXtTOrO9qpeATYXmLpaqPN8"
def get_mpesa_access_token():
    """
    Fetch the M-Pesa access token from Safaricom's API.
    """
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    try:
        response = requests.get(api_url, auth=HTTPBasicAuth(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET))
        response_data = response.json()
        
        if "access_token" in response_data:
            return response_data["access_token"]
        else:
            raise Exception("Unable to fetch access token: " + response_data.get("errorMessage", "Unknown Error"))
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching M-Pesa access token: {str(e)}")

# Create Appointment and Handle Payment
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from .mpesa_utils import get_mpesa_access_token, process_mpesa_payment  # Payment utility functions

def booking_view(request):
    if request.method == 'POST':
        # Retrieve form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        appointment_date = request.POST.get('appointment_date')
        session_type = request.POST.get('session_type')
        additional_notes = request.POST.get('additional_notes')
        amount = request.POST.get('amount')
        payment_phone = request.POST.get('payment_phone')
        uploaded_image = request.FILES.get('image')

        # Save appointment to the database
        appointment = Appointment(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            appointment_date=appointment_date,
            session_type=session_type,
            additional_notes=additional_notes,
            amount=amount,
            uploaded_image=uploaded_image
        )
        appointment.save()

        # Process M-Pesa payment
        try:
            access_token = get_mpesa_access_token()
            payment_response = process_mpesa_payment(access_token, payment_phone, appointment.id, amount)
            if payment_response.get("ResponseCode") == "0":  # Payment successful
                appointment.payment_status = True
                appointment.payment_reference = payment_response.get("CheckoutRequestID")
                appointment.save()
                messages.success(request, "Appointment successfully booked and payment confirmed!")
            else:
                messages.error(request, "Payment failed. Please try again.")
        except Exception as e:
            messages.error(request, f"Payment error: {str(e)}")
        
        return redirect('appointment_list.html')  # Redirect to an appointment list or success page
    
    return render(request, 'booking.html')  # Render the form template
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})
