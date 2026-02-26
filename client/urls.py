from django.urls import path
from . import views

urlpatterns = [
    path('client_home/', views.client_home),
    path('login_client/', views.login_client),
    path('register_client/', views.register_client),
    path('logout_client/', views.logout_client),
    path('client_form_freelancer/', views.client_form_freelancer),
    path('client_form_inhouse/', views.client_form_inhouse),
    path('client_freelancer_register/', views.client_freelancer_register),
    path('client_inhouse_register/', views.client_inhouse_register),
    path('client_approve_employee/', views.client_approve_employee),
    path('accept_freelance_work/<int:id>/', views.accept_freelance_work),
    path('deny_freelance_work/<int:id>/', views.deny_freelance_work),
    path('client_final_view/', views.client_final_view),
  ]
