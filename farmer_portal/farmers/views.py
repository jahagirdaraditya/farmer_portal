from django.shortcuts import render

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
    }
    return render(request, 'farmers/dashboard.html', context)
