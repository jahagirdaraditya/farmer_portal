from django.shortcuts import render, redirect
from django.contrib import messages
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


my_orders = [
    {
        'product':'Soyabean Oil Seed',
        'id' : 'IKJHTCI',
        'rs':'4500/Quintal',
        'ava_qty' : '350Quintal',
        'name':'Vivek Deshmukh',
        'contact' : '9988776655',
        'location':'Nanded',
        'date_posted' : '12-Jan-2020 05:37 pm',
    },
    {
        'product':'Groundnuts Oil Seed',
        'id' : 'UHGYTCI',
        'rs':'5500/Quintal',
        'ava_qty' : '390Quintal',
        'name':'Shubham Deshmukh',
        'contact' : '9944336655',
        'location':'Aurangabad',
        'date_posted' : '12-Feb-2019 05:37 am',
    }
]


buy_now_details = [
    {
    'transaction_id':'OD123456789',
    'product':'Wheat',
    'rs':'5500',
    'name':'Nanded FPO',
    'date_posted' : 'Fri, Oct 18th 2019',
    'status' : 'Out for delivery',
    'reason' : 'Packaging done',
    
    },
    {
    'transaction_id':'OD989877666',
    'product':'Soyabean Oil Seed',
    'rs':'6600',
    'name':'Aurangabad FPO',
    'date_posted' : 'Fri, Oct 18th 2019',
    'status' : 'Delivered on Nov 02, 2019',
    'reason' : 'Your item has been delivered',
    }
]
def dashboard(request):
    context={
        'all_posts':all_posts,
        
    }
    return render(request, 'buyer/dashboard.html', context)

def my_order(request):
    context={
        'buy_now_details' : buy_now_details,
    }
    return render(request, 'buyer/my_orders.html', context)
def complaint(request):
    return render(request, 'buyer/complaints.html')

def buy_now(request):
    context={
        'buy_now_details' : buy_now_details,
    }
    return render(request, 'buyer/buy_now.html',context)

def checkout(request):
    if request.POST:
        messages.success(request,f'Thank you!')   
        return redirect('buyer-dashboard')
    return render(request, 'buyer/checkout.html')

def profile(request):
    return render(request, 'buyer/profile.html')


def success_stories(request):
    return render(request, 'buyer/success_stories.html')


def feedback(request):
    return render(request, 'buyer/feedback.html')


def out_for_delivery(request):
    return render(request, 'buyer/out_for_delivery.html')

