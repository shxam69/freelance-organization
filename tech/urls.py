from django.urls import path
from . import views

urlpatterns = [
    path('tech_home/', views.tech_home),
    path('login_tech/', views.login_tech),
    path('register_tech/', views.register_tech),
    path('logout_tech/', views.logout_tech),
    path('tech_form_inhouse/', views.tech_form_inhouse),
    path('inhouse_register/', views.inhouse_register),
    path('tech_view_freelancer/', views.tech_view_freelancer),
    path('tech_view_inhouse/', views.tech_view_inhouse),
    path('tech_edit_freelancer/', views.tech_edit_freelancer),
    path('tech_edit_inhouse/', views.tech_edit_inhouse),
    path('tech_view_client_inhouse/', views.tech_view_client_inhouse),
    path('tech_view_client_freelance/', views.tech_view_client_freelance),
    path('tech_edit_client_inhouse/', views.tech_edit_client_inhouse),
    path('tech_edit_client_freelance/', views.tech_edit_client_freelance),
    path('send_to_employee/<int:id>/', views.send_to_employee),
    path('price_analysis/', views.price_analysis),
    path('apply_algorithm/<int:id>/', views.apply_algorithm),
    path('algorithm/', views.algorithm),
    path('resource_output/', views.resource_output),
    path('send_pricing/<int:id>/', views.send_pricing),
]
