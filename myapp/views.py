from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
import random
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import *
# Create your views here.

def signup(request):
    return render(request, 'signuppage.html')

def forgot_password(request):
    print("Looking for template at:", 'forgotpassword.html')
    return render(request, 'forgotpassword.html')



# Temporary storage for OTPs (you should use a database in production)
otp_storage = {}

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp = str(random.randint(1000, 9999))  # Generate a random 4-digit OTP
        otp_storage[email] = otp  # Store OTP (Use a DB in real apps)

        # Simulating an email (Configure Django email settings in production)
        print(f"OTP for {email} is {otp}")

        return redirect(f"/otp/?email={email}")  # Redirect to OTP page

    return render(request, "forgot_password.html")

def enter_otp(request):
    email = request.GET.get("email", "")

    if request.method == "POST":
        otp_entered = request.POST.get("otp")
        if email in otp_storage and otp_storage[email] == otp_entered:
            del otp_storage[email]  # Clear OTP after verification
            return redirect("/")  # Redirect to a reset password page or home

        return render(request, "forgototp.html", {"email": email, "error": "Invalid OTP"})

    return render(request, "forgototp.html", {"email": email})



def set_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., save the new password)
            password = form.cleaned_data['password']
            # Add your logic to save the password (e.g., update the user's password)
            return redirect('done')  # Redirect to a success page
    else:
        form = SetPasswordForm()

    return render(request, 'setpassword.html', {'form': form})

def done(request):
    return render(request, 'passwordchangedone.html')


User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create a new user
            user = User.objects.create_user(
                username=email,  # Use email as the username
                email=email,
                password=password
            )
            user.save()

            # Redirect to a success page or login page
            return redirect('landing')  # Replace 'login' with your desired URL name
    else:
        form = SignUpForm()

    return render(request, 'signuppage.html', {'form': form})

def landingread(request):
    return render(request, 'landingpage.html' )