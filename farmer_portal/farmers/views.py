from django.shortcuts import render, redirect
import django.middleware.csrf
from django.contrib import messages
# from .forms import AddProduceForm

def orders(request):
    context={
        'details': farmer_details,
        'transactions':transactions,
    }
    return render(request, 'farmers/orders.html', context)

def dashboard(request):
    context={
        'details': farmer_details,
        'transactions':transactions,
    }
    return render(request, 'farmers/dashboard.html', context)

def addProduce(request):
    if request.method == 'POST':
        print(request.POST)
        messages.success(request, f'Post successfully created! Our Team will verify the post and update you shortly.')
        return redirect('farmer-dashboard')
    context={
        'details': farmer_details,
        'csrf-token': django.middleware.csrf.get_token(request),
    }
    return render(request, 'farmers/add_produce.html', context)

def farmerApplications(request):
    return render(request, 'farmers/farmer-applications.html')

def check(request):
    context={
        'details': farmer_details,
    }
    return render(request, 'farmers/dashboard00.html', context)


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
