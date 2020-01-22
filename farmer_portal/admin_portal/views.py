from django.shortcuts import render
from django.shortcuts import render

farmers_details = [
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',
    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
]


buyers_details = [
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',
    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
]


services_details = [
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',
    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
    {
        'id' : 'IKJHTCI',
        'name':'Vivek Deshmukh',
        'location':'Nanded',
        'date_registered' : '12-Jan-2020',

    },
]

def dashboard(request):
    return render(request, 'admin_portal/dashboard.html')


def farmers(request):
    context={
        'farmers_details' : farmers_details,
    }
    return render(request, 'admin_portal/farmers.html', context)


def buyers(request):
    context={
        'buyers_details' : buyers_details,
    }
    return render(request, 'admin_portal/buyers.html', context)


def services(request):
    context={
        'services_details' : services_details,
    }
    return render(request, 'admin_portal/services.html', context)

def revenue(request):
    return render(request, 'admin_portal/revenue.html')

