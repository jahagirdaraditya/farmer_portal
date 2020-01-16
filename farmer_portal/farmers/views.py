from django.shortcuts import render
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
def dashboard(request):
    context={
        'details': farmer_details,
        'transactions':transactions,
    }
    return render(request, 'farmers/dashboard.html', context)

def addProduce(request):
    context={
        'details': farmer_details,
    }
    return render(request, 'farmers/add_produce.html', context)
def check(request):
    context={
        'details': farmer_details,
    }
    return render(request, 'farmers/dashboard00.html', context)
