from signal import pthread_sigmask

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Email verification
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
    path('email-verification-sent/', views.email_verification_sent, name='email-verification-sent'),
    path('email-verification-success/', views.email_verification_success, name='email-verification-success'),
    path('email-verification-failed/', views.email_verification_failed, name='email-verification-failed'),
    # Login/logout
    path('login/', views.login, name='my-login'),
    path('logout/', views.logout, name='my-logout'),
    # Profile
    path('dashboard/', views.dashboard, name='my-dashboard'),
    path('settings/', views.profile_management, name='my-profile'),
    path('delete-account/', views.delete_account, name='delete-account'),
    path('track-orders/', views.track_orders, name='track-orders'),
    # Password management
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='account/password/password-reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='account/password/password-reset-sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password/password-reset-form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='account/password/password-reset-complete.html'), name='password_reset_complete'),
    # Shipping
    path('manage-shipping/', views.manage_shipping, name='manage-shipping'),
]