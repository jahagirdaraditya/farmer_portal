from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from django.conf import settings
import os

import xlrd

all_orders = [
    {
        'Transaction_Id' : 'T1000',
        'Seller' : 'ABC',
        'Buyer' : 'CDE',
        'Status' : 'Incomplete',
    },
    {
        'Transaction_Id' : 'T1002',
        'Seller' : 'EFG',
        'Buyer' : 'MNB',
        'Status' : 'Incomplete',
    },
    {
        'Transaction_Id' : 'T1000',
        'Seller' : 'ABC',
        'Buyer' : 'CDE',
        'Status' : 'Complete',
    },
    {
        'Transaction_Id' : 'T1002',
        'Seller' : 'EFG',
        'Buyer' : 'MNB',
        'Status' : 'Incomplete',
    }
]

def dashboard(request):
    # return HttpResponse("<h1>fjgjgf fvg<h1>")
    return render(request, 'services/dashboard.html')

def statistics(request):
    return render(request, 'services/statistics.html')

def orders(request):
    context={
        'order_details': all_orders,
    }
    return render(request, 'services/orders.html' , context)

def profile(request):
    return render(request, 'services/profile.html')

def add_location(request):
    if(request.POST):
        location = request.POST.dict()
        print(location.get("address"))
        print(location.get("country"))
        print(location.get("state"))
        print(location.get("city"))
        print(location.get("pincode"))
        messages.success(request,f'Address successfully added!')
    return render(request, 'services/add_location.html')

def save_all_addresses(request):
    if(request.POST):
        # uploaded_file = request.POST.dict()
        uploaded_file = request.FILES['document']
        print(request.POST.get('sheet_name'))
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        # context={
        #     'url': fs.url(file_name),
        #  }
        # print(fs.url(file_name))
        base_dir =settings.MEDIA_ROOT    
        my_file = os.path.join(base_dir, uploaded_file.name)
        print(my_file)
        workbook =xlrd.open_workbook(my_file)

        #Open a sheet and If name is known
        worksheet = workbook.sheet_by_name(request.POST.get('sheet_name'))

        print(worksheet.cell_value(0, 0))

        for row in range(worksheet.nrows): 
            for col in range(worksheet.ncols): 
                print(worksheet.cell_value(row, col), end=" ")
            print()
        messages.success(request,f'File uploaded Successfully!')
        return redirect('service-add_location')
    return redirect('service-add_location')
