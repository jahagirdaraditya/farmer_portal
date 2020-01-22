from django.shortcuts import render, redirect
import django.middleware.csrf
from django.contrib import messages
# from .forms import AddProduceForm

def orders(request):
    context={
        'details': farmer_details,
        'transactions':transactions,
    }
    return render(request, 'fpo/orders.html', context)

def dashboard(request):
    context={
        'details': farmer_details,
        'transactions':transactions,
    }
    return render(request, 'fpo/dashboard.html', context)

def addProduce(request):
    if request.method == 'POST':
        print(request.POST)
        messages.success(request, f'Post successfully created! Our Team will verify the post and update you shortly.')
        return redirect('fpo-dashboard')
    context={
        'details': farmer_details,
        'csrf-token': django.middleware.csrf.get_token(request),
    }
    return render(request, 'fpo/add_produce.html', context)

def fpoApplications(request):
    return render(request, 'fpo/fpo-applications.html')


def services(request):
    return render(request, 'fpo/services.html')


def complaint(request):
    context={
        'complaints':complaints,
    }
    return render(request, 'fpo/complaints.html', context)


def check(request):
    context={
        'details': farmer_details,
    }
    return render(request, 'fpo/dashboard00.html', context)


def success_stories(request):
    return render(request, 'fpo/success_stories.html')


transactions = [
    {
        'name':'Omkar Deshpande',
        'location':'Nanded',
        'product':'Rice',
        'qty':20,
    },
    {
        'name':'Aditya Jahagirdar',
        'location':'Aurangabad',
        'product':'Corn',
        'qty':30,
    },
    {
        'name':'Omkar Deshpande',
        'location':'Nanded',
        'product':'Rice',
        'qty':20,
    },
    {
        'name':'Aditya Jahagirdar',
        'location':'Aurangabad',
        'product':'Corn',
        'qty':30,
    },
    {
        'name':'Omkar Deshpande',
        'location':'Nanded',
        'product':'Rice',
        'qty':20,
    },
    {
        'name':'Aditya Jahagirdar',
        'location':'Aurangabad',
        'product':'Corn',
        'qty':30,
    },
]

farmer_details = [
    {
    'name': 'Omkar Deshpande',
    },
    {
    'name': 'Samiksha Kulkarni',
    }
]

complaints = [
    {
        'id' : 'CID123',
        'role' : 'Service',
        'date_of_Complaint' : '15-01-2020'
    },

    {
        'id' : 'CID124',
        'role' : 'Farmer',
        'date_of_Complaint' : '25-01-2020'

    }
    
]