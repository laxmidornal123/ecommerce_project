from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from .models import OTP
import random


# ================= REGISTER =================
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'accounts/register.html')


# ================= LOGIN =================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'accounts/login.html')


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('/')


# ================= FORGOT PASSWORD =================
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'accounts/forgot.html', {
                'error': 'Email not found ❌'
            })

        otp_code = str(random.randint(100000, 999999))

        # 🔥 DELETE OLD OTP
        OTP.objects.filter(user=user).delete()

        # CREATE NEW OTP
        OTP.objects.create(user=user, code=otp_code)

        send_mail(
            'Your OTP Code',
            f'Your OTP is {otp_code}',
            'your_email@gmail.com',
            [email],
            fail_silently=False,
        )

        # STORE USER IN SESSION
        request.session['reset_user'] = user.id

        return redirect('verify_otp')

    return render(request, 'accounts/forgot.html')


# ================= VERIFY OTP =================
def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        user_id = request.session.get('reset_user')

        if not user_id:
            return redirect('forgot_password')

        # GET LATEST OTP
        latest_otp = OTP.objects.filter(user_id=user_id).order_by('-created_at').first()

        if not latest_otp:
            return render(request, 'accounts/verify_otp.html', {
                'error': 'No OTP found ❌'
            })

        # ⏱️ CHECK EXPIRY (2 minutes)
        if latest_otp.created_at < now() - timedelta(minutes=2):
            latest_otp.delete()
            return render(request, 'accounts/verify_otp.html', {
                'error': 'OTP expired ❌'
            })

        # ✅ MATCH OTP
        if str(latest_otp.code).strip() == str(entered_otp).strip():
            request.session['otp_verified'] = True
            latest_otp.delete()

            # 🔥 REDIRECT TO RESET PAGE
            return redirect('reset_password')

        else:
            return render(request, 'accounts/verify_otp.html', {
                'error': 'Incorrect OTP ❌'
            })

    return render(request, 'accounts/verify_otp.html')


# ================= RESET PASSWORD =================
def reset_password(request):

    # 🔐 SECURITY CHECK
    if not request.session.get('otp_verified'):
        return redirect('forgot_password')

    if request.method == "POST":
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')
        user_id = request.session.get('reset_user')

        if password != confirm:
            return render(request, 'accounts/reset.html', {
                'error': 'Passwords do not match ❌'
            })

        user = User.objects.get(id=user_id)
        user.password = make_password(password)
        user.save()

        # CLEAR SESSION
        request.session.flush()

        return redirect('login')

    return render(request, 'accounts/reset.html')


# ================= RESEND OTP =================
def resend_otp(request):
    user_id = request.session.get('reset_user')

    if not user_id:
        return redirect('forgot_password')

    user = User.objects.get(id=user_id)

    otp_code = str(random.randint(100000, 999999))

    # 🔥 DELETE OLD OTP
    OTP.objects.filter(user=user).delete()

    # CREATE NEW OTP
    OTP.objects.create(user=user, code=otp_code)

    send_mail(
        'Your OTP Code',
        f'Your new OTP is {otp_code}',
        'your_email@gmail.com',
        [user.email],
        fail_silently=False,
    )

    return redirect('verify_otp')