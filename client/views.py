from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ClientModel
from .models import ClientRegFreelance
from .models import ClientRegInhouse
from freelance_employee.models import FreelanceEmployee
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.neighbors import KNeighborsClassifier
# import warnings
# warnings.filterwarnings('ignore')


# Create your views here.
def client_home(request):
    return render(request, 'client/client_home.html')


def login_client(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        try:
            client_object = ClientModel.objects.get(mail=email, password=password)
            request.session['client'] = client_object.mail
            messages.success(request, "Login Success")
            return redirect('/client_home/')
        except:
            messages.error(request, "Given details not found")
            return redirect('/login_client/')
    return render(request, 'client/client_sign.html')


def register_client(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['mobile']
        date = request.POST['date']
        password = request.POST['password1']
        repeat_password = request.POST['password2']
        if password == repeat_password:
            ClientModel(name=username, mail=email, phone=phone,
                        date=date, password=password).save()
            messages.success(request, 'Client successfully Registered')
            return redirect('/login_client/')
        else:
            messages.error(request, 'Passwords should be same')
    return render(request, 'client/client_sign.html')


def logout_client(request):
    if 'client' in request.session:
        request.session.pop('client', None)
        messages.success(request, "Client Logout Success")
        return redirect('/')
    else:
        return redirect('/client_home/')


def client_form_freelancer(request):
    st = ClientModel.objects.all()
    return render(request, 'client/client_form_freelancer.html', {'st': st})


def client_form_inhouse(request):
    st = ClientModel.objects.all()
    return render(request, 'client/client_form_inhouse.html', {'st': st})


def client_freelancer_register(request):
    if 'client' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            category = request.POST['category']
            industry = request.POST['industry']
            business_scale = request.POST['business_scale']
            user_type = request.POST['user_type']
            no_of_users = request.POST['no_of_users']
            deployment = request.POST['deployment']
            os = request.POST['os']
            mobile_app = request.POST['mobile_app']
            ClientRegFreelance(name=name, mail=email, mobile=mobile, category=category, industry=industry,
                               business_scale=business_scale, user_type=user_type, no_of_users=no_of_users,
                               deployment=deployment, os=os, mobile_app=mobile_app).save()
            messages.success(request, 'Client Registration for Freelancer is success')
            return redirect('/client_home/')
    return render(request, 'client/client_form_freelancer.html')


def client_inhouse_register(request):
    if 'client' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            category = request.POST['category']
            industry = request.POST['industry']
            business_scale = request.POST['business_scale']
            user_type = request.POST['user_type']
            no_of_users = request.POST['no_of_users']
            deployment = request.POST['deployment']
            os = request.POST['os']
            mobile_app = request.POST['mobile_app']
            ClientRegInhouse(name=name, mail=email, mobile=mobile, category=category, industry=industry,
                             business_scale=business_scale, user_type=user_type, no_of_users=no_of_users,
                             deployment=deployment, os=os, mobile_app=mobile_app).save()
            messages.success(request, 'Client Registration for In House Employee is success')
            return redirect('/client_home/')
    return render(request, 'client/client_form_freelancer.html')


def client_approve_employee(request):
    new = FreelanceEmployee.objects.filter(client_approve=True, from_client=False)
    return render(request, 'client/client_approve_employee.html', {'new': new})


def accept_freelance_work(request, id):
    if 'client' in request.session:
        new = FreelanceEmployee.objects.get(id=id)
        new.from_client = True
        new.save()
        messages.success(request, 'Freelance Employee Work Accepted')
        return redirect('/client_approve_employee/')


def deny_freelance_work(request, id):
    if 'client' in request.session:
        new = FreelanceEmployee.objects.get(id=id)
        new.client_approve = False
        new.save()
        messages.success(request, 'Freelance Employee Work reverted back to Manager')
        return redirect('/client_approve_employee/')


def client_final_view(request):
    new = ClientRegFreelance.objects.filter(send_pricing=True)
    return render(request, 'client/client_final_view.html', {'new': new})
