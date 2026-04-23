from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    forgot_password,
    verify_otp,
    reset_password,
    resend_otp
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('forgot/', forgot_password, name='forgot_password'),
    path('verify/', verify_otp, name='verify_otp'),
    path('reset/', reset_password, name='reset_password'),
    path('resend/', resend_otp, name='resend_otp'),
]