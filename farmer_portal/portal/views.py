from django.shortcuts import render,  get_object_or_404
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
    return render(request, 'portal/home.html', context)
