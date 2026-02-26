from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FreelanceEmployeeModel
from .models import FreelanceEmployee
from client.models import ClientRegFreelance


# Create your views here.
def freelance_employee_home(request):
    return render(request, 'freelance_employee/freelance_employee_home.html')


def login_freelance_employee(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        try:
            freelance_employee_object = FreelanceEmployeeModel.objects.get(mail=email, password=password)
            request.session['freelance_employee'] = freelance_employee_object.mail
            messages.success(request, "Login Success")
            return redirect('/freelance_employee_home/')
        except:
            messages.error(request, "Given details not found")
            return redirect('/login_freelance_employee/')
    return render(request, 'freelance_employee/freelance_employee_sign.html')


def register_freelance_employee(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['mobile']
        date = request.POST['date']
        password = request.POST['password1']
        repeat_password = request.POST['password2']
        if password == repeat_password:
            FreelanceEmployeeModel(name=username, mail=email, phone=phone,
                                   date=date, password=password).save()
            messages.success(request, 'Freelance Employee successfully Registered')
            return redirect('/login_freelance_employee/')
        else:
            messages.error(request, 'Passwords should be same')
    return render(request, 'freelance_employee/freelance_employee_sign.html')


def logout_freelance_employee(request):
    if 'freelance_employee' in request.session:
        request.session.pop('freelance_employee', None)
        messages.success(request, "Freelance Employee Logout Success")
        return redirect('/')
    else:
        return redirect('/freelance_employee_home/')


def freelance_form(request):
    st = FreelanceEmployeeModel.objects.all()
    return render(request, 'freelance_employee/freelance_form.html', {'st': st})


def freelance_form_register(request):
    if 'freelance_employee' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            emp_id = request.POST['empid']
            email = request.POST['email']
            gender = request.POST['gender']
            age = request.POST['age']
            education = request.POST['education']
            title = request.POST['title']
            salary = request.POST['salary']
            location = request.POST['location']
            experience = request.POST['experience']
            FreelanceEmployee(name=name, emp_id=emp_id, mail=email, gender=gender,
                              age=age, education=education, job_title=title, salary=salary,
                              location=location, experience=experience).save()
            messages.success(request, 'Freelance Employee Registered Successfully')
            return redirect('/freelance_employee_home/')
        return render(request, 'freelance_employee/freelance_form.html')


def project(request):
    new = ClientRegFreelance.objects.filter(approve=True, to_employee=True, accept_project=False)
    return render(request, 'freelance_employee/freelance_employee_project.html', {'new': new})


def decline_project(request, id):
    new = ClientRegFreelance.objects.get(id=id)
    new.to_employee = False
    new.save()
    messages.info(request, 'Project Work not taken, reverted back to tech team')
    return redirect('/freelance_employee_home/')


def accept_project_work(request):
    new = ClientRegFreelance.objects.filter(accept_project=False)
    return render(request, 'freelance_employee/freelance_accept_work.html', {'new': new})


def start_project(request, id):
    new = ClientRegFreelance.objects.get(id=id)
    new.accept_project = True
    new.save()
    messages.info(request, 'Project Work Accepted, Now Admin Can Send Employee Stats to Client...')
    return redirect('/accept_project_work/')


def work_process(request):
    new = ClientRegFreelance.objects.filter(client_approve=False, finish_project=False)
    return render(request, 'freelance_employee/work_process.html', {'new': new})


def work_on_project(request, id):
    new = ClientRegFreelance.objects.get(id=id)
    with open('Project.txt', 'w') as f:
        f.write('Project file!')
    messages.success(request, 'Work Process Started Successfully...')
    return redirect('/work_process/')


def finish_project(request, id):
    new = ClientRegFreelance.objects.get(id=id)
    new.finish_project = True
    new.save()
    messages.success(request, 'Work Process Finished Successfully...')
    return redirect('/work_process/')
