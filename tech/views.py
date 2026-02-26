from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TechModel
from .models import InhouseEmployee
from freelance_employee.models import FreelanceEmployee
from client.models import ClientRegInhouse
from client.models import ClientRegFreelance
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings('ignore')


# Create your views here.
def tech_home(request):
    return render(request, 'tech/tech_home.html')


def login_tech(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        try:
            tech_object = TechModel.objects.get(mail=email, password=password)
            request.session['tech'] = tech_object.mail
            messages.success(request, "Login Success")
            return redirect('/tech_home/')
        except:
            messages.error(request, "Given details not found")
            return redirect('/login_tech/')
    return render(request, 'tech/tech_sign.html')


def register_tech(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['mobile']
        date = request.POST['date']
        password = request.POST['password1']
        repeat_password = request.POST['password2']
        if password == repeat_password:
            TechModel(name=username, mail=email, phone=phone,
                      date=date, password=password).save()
            messages.success(request, 'Tech successfully Registered')
            return redirect('/login_tech/')
        else:
            messages.error(request, 'Passwords should be same')
    return render(request, 'tech/tech_sign.html')


def logout_tech(request):
    if 'tech' in request.session:
        request.session.pop('tech', None)
        messages.success(request, "Tech Logout Success")
        return redirect('/')
    else:
        return redirect('/tech_home/')


def tech_form_inhouse(request):
    return render(request, 'tech/tech_form_inhouse.html')


def inhouse_register(request):
    if 'tech' in request.session:
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
            InhouseEmployee(name=name, emp_id=emp_id, mail=email, gender=gender,
                            age=age, education=education, job_title=title, salary=salary,
                            location=location, experience=experience).save()
            messages.success(request, 'Freelance Employee Registered Successfully')
            return redirect('/freelance_employee_home/')
    return render(request, 'tech/tech_form_inhouse.html')


def tech_view_freelancer(request):
    return render(request, 'tech/tech_view_freelancer.html')


def tech_view_inhouse(request):
    return render(request, 'tech/tech_view_inhouse.html')


def tech_edit_freelancer(request):
    new = FreelanceEmployee.objects.filter(approve=True)
    return render(request, 'tech/tech_view_freelancer.html', {'new': new})


def tech_edit_inhouse(request):
    new = InhouseEmployee.objects.filter(approve=True)
    return render(request, 'tech/tech_view_inhouse.html', {'new': new})


def tech_view_client_freelance(request):
    return render(request, 'tech/tech_view_client_freelance.html')


def tech_view_client_inhouse(request):
    return render(request, 'tech/tech_view_client_inhouse.html')


def tech_edit_client_freelance(request):
    new = ClientRegFreelance.objects.filter(approve=True, to_employee=False)
    return render(request, 'tech/tech_view_client_freelance.html', {'new': new})


def tech_edit_client_inhouse(request):
    new = ClientRegInhouse.objects.filter(approve=True)
    return render(request, 'tech/tech_view_client_inhouse.html', {'new': new})


def send_to_employee(request, id):
    new = ClientRegFreelance.objects.get(id=id)
    new.to_employee = True
    new.save()
    messages.success(request, 'Client Details Sent To Freelance employee')
    return redirect('/tech_home/')


def price_analysis(request):
    new = ClientRegFreelance.objects.all()
    return render(request, 'tech/price_analysis.html', {'new': new})


def algorithm(datas,r):
    # da = AthleteHealthReport.objects.get(id=id)
    # print(da.age)
    # print(da.chol)
    print(datas)
    data = pd.read_csv('BI.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = KNeighborsClassifier()
    model.fit(data_x, data_y)
    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]


# a = algorithm([61, 1, 0, 148, 203, 0, 1, 160, 0, 0, 2, 1, 3])
# print(a)


def apply_algorithm(request, id):
    # if 'resource' in request.session:
    da = ClientRegFreelance.objects.get(id=id)
    r = da.id
    input_value = []
    # da.save()
    a = da.category
    b = da.industry
    c = da.business_scale
    d = da.user_type
    e = da.no_of_users
    f = da.deployment
    g = da.os
    h = da.mobile_app
    print(a)
    print(b)
    print(c)
    print(d)
    print(f'id: {r}')
    input_value.append(a)
    input_value.append(b)
    input_value.append(c)
    input_value.append(d)
    input_value.append(e)
    input_value.append(f)
    input_value.append(g)
    input_value.append(h)
    print(input_value)
    algo = algorithm(input_value,r)
    print(f'Output: {algo}')
    ClientRegFreelance.objects.filter(id=r).update(pricing=algo)
    print(da.pricing)
    return redirect('/resource_output/')


def resource_output(request):
    da = ClientRegFreelance.objects.filter(send_pricing=False)
    return render(request, 'tech/resource_output.html', {'da': da})


def send_pricing(request, id):
    da = ClientRegFreelance.objects.get(id=id)
    da.send_pricing = True
    da.save()
    messages.success(request, 'Pricing details Successfully Sent to Client')
    return redirect('/resource_output/')
