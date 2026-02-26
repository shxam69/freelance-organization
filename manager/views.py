from django.shortcuts import render, redirect
from django.contrib import messages
from client.models import ClientRegInhouse
from client.models import ClientRegFreelance
from freelance_employee.models import FreelanceEmployee
from django.core.mail import send_mail
from tech.models import InhouseEmployee


# Create your views here.
def manager_home(request):
    return render(request, 'manager/manager_home.html')


def login_manager(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        if email == "admin@gmail.com" and password == "admin":
            request.session['manager'] = 'admin@gmail.com'
            messages.success(request, "Login Success")
            return redirect('/manager_home/')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Admin Email")
            return redirect('/login_manager/')
        elif password != "admin":
            messages.error(request, "Wrong Admin Password")
            return redirect('/login_manager/')
    return render(request, 'manager/manager_sign.html')


def logout_manager(request):
    if 'manager' in request.session:
        request.session.pop('manager', None)
        messages.success(request, "Manager Logout Success")
        return redirect('/')
    else:
        return redirect('/manager_home/')


def approve_client_freelance(request):
    if 'manager' in request.session:
        new = ClientRegFreelance.objects.filter(approve=False)
        return render(request, 'manager/manager_approve_client_freelance.html', {'new': new})


def approve_client_inhouse(request):
    if 'manager' in request.session:
        new = ClientRegInhouse.objects.filter(approve=False)
        return render(request, 'manager/manager_approve_client_inhouse.html', {'new': new})


def approved_freelance(request, id):
    if 'manager' in request.session:
        new = ClientRegFreelance.objects.get(id=id)
        new.approve = True
        new.save()
        messages.success(request, 'Client - Freelance approved successfully')
        return redirect('/approve_client_freelance/')


def approved_inhouse(request, id):
    if 'manager' in request.session:
        new = ClientRegInhouse.objects.get(id=id)
        new.approve = True
        new.save()
        messages.success(request, 'Client - Inhouse approved successfully')
        return redirect('/approve_client_inhouse/')


def approve_freelance_employee(request):
    if 'manager' in request.session:
        new = FreelanceEmployee.objects.filter(approve=False)
        return render(request, 'manager/manager_approve_freelance.html', {'new': new})


def approved_freelance_employee(request, id):
    if 'manager' in request.session:
        new = FreelanceEmployee.objects.get(id=id)
        new.approve = True
        new.save()
        messages.success(request, 'Client - Freelance approved successfully')
        return redirect('/approve_freelance_employee/')


def delete_employee(request, id):
    new = FreelanceEmployee.objects.get(id=id)
    send_mail(
        'Subject here',
        f'Sorry {new.name} Your registration with us is declined from our Organization...',
        'karthickmanimaran.surya@gmail.com',
        [new.mail],
        fail_silently=False,
    )
    new.delete()
    messages.success(request, 'Employee Declined and Mail sent successfully')
    return redirect('/approve_freelance_employee/')


def approve_inhouse_employee(request):
    if 'manager' in request.session:
        new = InhouseEmployee.objects.filter(approve=False)
        return render(request, 'manager/manager_approve_employee_inhouse.html', {'new': new})


def approved_inhouse_employee(request, id):
    if 'manager' in request.session:
        new = InhouseEmployee.objects.get(id=id)
        new.approve = True
        new.save()
        messages.success(request, 'In-house Employee approved successfully')
        return redirect('/approve_inhouse_employee/')


def manager_send_client(request):
    new = FreelanceEmployee.objects.all()
    return render(request, 'manager/manager_send_client.html', {'new': new})


def send_to_client(request, id):
    if 'manager' in request.session:
        new = FreelanceEmployee.objects.get(id=id)
        new.client_approve = True
        new.save()
        messages.success(request, 'Employee Stats sent to Client')
        return redirect('/manager_send_client/')


def employee_start_project(request, id):
    if 'manager' in request.session:
        new = FreelanceEmployee.objects.get(id=id)
        new.client_approve = True
        new.save()
        messages.success(request, 'Employee Can now Start The Project Work...')
        return redirect('/manager_home/')
