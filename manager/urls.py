from django.urls import path
from . import views

urlpatterns = [
    path('manager_home/', views.manager_home),
    path('login_manager/', views.login_manager),
    path('logout_manager/', views.logout_manager),
    path('approve_client_freelance/', views.approve_client_freelance),
    path('approve_client_inhouse/', views.approve_client_inhouse),
    path('approved_freelance/<int:id>/', views.approved_freelance),
    path('approved_inhouse/<int:id>/', views.approved_inhouse),
    path('approve_freelance_employee/', views.approve_freelance_employee),
    path('approved_freelance_employee/<int:id>/', views.approved_freelance_employee),
    path('delete_employee/<int:id>/', views.delete_employee),
    path('approve_inhouse_employee/', views.approve_inhouse_employee),
    path('approved_inhouse_employee/<int:id>/', views.approved_inhouse_employee),
    path('manager_send_client/', views.manager_send_client),
    path('send_to_client/<int:id>/', views.send_to_client),
    path('employee_start_project/<int:id>/', views.employee_start_project),
]
