from django.urls import path
from . import views

urlpatterns = [
    path('freelance_employee_home/', views.freelance_employee_home),
    path('login_freelance_employee/', views.login_freelance_employee),
    path('register_freelance_employee/', views.register_freelance_employee),
    path('logout_freelance_employee/', views.logout_freelance_employee),
    path('freelance_form/', views.freelance_form),
    path('freelance_form_register/', views.freelance_form_register),
    path('project/', views.project),
    path('decline_project/<int:id>/', views.decline_project),
    path('accept_project_work/', views.accept_project_work),
    path('start_project/<int:id>/', views.start_project),
    path('work_process/', views.work_process),
    path('work_on_project/<int:id>/', views.work_on_project),
    path('finish_project/<int:id>/', views.finish_project),
]
