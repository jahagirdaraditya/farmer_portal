from django.shortcuts import render,  get_object_or_404
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
        if role == 1:
            return redirect('farmer-dashboard')
    return render(request, 'portal/home.html')
