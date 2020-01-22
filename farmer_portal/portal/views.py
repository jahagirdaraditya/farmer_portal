from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
# Create your views here.
posts = [
    {
        'farmerName' : 'Omkar Deshpande',
        'crop' : 'Pomatoes',
        'qty' : 10,
        'area' : 'Nanded',
        'date_posted': 'August 27, 2019'
    },
    {
        'farmerName' : 'Satish Deshpande',
        'crop' : 'Potatoes',
        'qty' : 20,
        'area' : 'Parbhani',
        'date_posted': 'September 27, 2019'
    }
]

all_posts = [
    {
        'product':'Soyabean Oil Seed',
        'id' : 'IKJHTCI',
        'rs':'4500/Quintal',
        'ava_qty' : '350Quintal',
        'name':'FPO',
        'contact' : '9988776655',
        'location':'Latur',
        'date_posted' : '12-Jan-2020 05:37 pm',
    },
    {
        'product':'Wheat',
        'id' : 'UHGYTCI',
        'rs':'4500/Quintal',
        'ava_qty' : '350Quintal',
        'name':'FPO',
        'contact' : '9988776655',
        'location':'Latur',
        'date_posted' : '12-Jan-2020 05:37 pm',

    },
    {
        'product':'Jowar',
        'id' : 'EDXYTCI',
        'rs':'4500/Quintal',
        'ava_qty' : '350Quintal',
        'name':'FPO',
        'contact' : '9988776655',
        'location':'Latur',
        'date_posted' : '12-Jan-2020 05:37 pm',

    },
    {
        'product':'Soyabean Oil Seed',
        'id' : 'JZXYTCI',
        'rs':'4500/Quintal',
        'ava_qty' : '350Quintal',
        'name':'FPO',
        'contact' : '9988776655',
        'location':'Nanded',
        'date_posted' : '12-Jan-2020 05:37 pm',

    },
    {
        'product':'Soyabean Oil Seed',
        'id' : 'BZXYTCI',
        'rs':'4500/Quintal',
        'ava_qty' : '350Quintal',
        'name':'FPO',
        'contact' : '9988776655',
        'location':'Beed',
        'date_posted' : '12-Jan-2020 05:37 pm',

    },
    {
        'product':'Soyabean Oil Seed',
        'id' : 'VAXYTCI',
        'rs':'4500/Quintal',
        'ava_qty' : '350Quintal',
        'name':'FPO',
        'contact' : '9988776655',
        'location':'Nanded',
        'date_posted' : '12-Jan-2020 05:37 pm',

    },
]


def home(request):
    context = {
        'posts' : posts
    }
    if request.POST:
        # data = request.POST
        # print(data)
        messages.success(request, f'Account Registered successfully')
    return render(request, 'portal/home.html', context)

def login(request):
    if request.POST:
        data = request.POST.dict()
        role = (data.get("role"))
        print(role)
        if role == '1':
            print(role)
            return redirect('farmer-dashboard')
        elif role == '2':
            print(role)
            return redirect('buyer-dashboard')
        elif role == '3':
            print(role)
            return redirect('service-dashboard')
        else:
            messages.warning(request, f'Please select a role.')
    return render(request, 'portal/home.html')

def view_post(request):
    context = {
        'posts' : all_posts
    }
    # if request.POST:
    #     # data = request.POST
    #     # print(data)
    #     messages.success(request, f'Account Registered successfully')
    return render(request, 'portal/view_post.html', context)