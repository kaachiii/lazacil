from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'tagline': 'Siap Melayani Para Lazy Pacil!',
        'name' : 'Ischika Afrilla',
        'npm' : '2306227955',
        'class' : 'PBP F'
    }

    return render(request, "main.html", context)
