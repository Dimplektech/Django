from django.shortcuts import render

# Create your views here.

def view_home(request):
    return render(request, 'home.html')

def welcome(request):  # request.GET will have all data from home.html in the form of dictionary
    name = request.POST['name']
    email = request.POST['email']
    birthday = request.POST['birthday']

    # dictionary to save data
    context_data = {
        'name': name,
        'email': email,
        'birthday': birthday
    }
    # render is going to send data to welcome page to print.
    return render(request, 'welcome.html', context=context_data)

def sports(request):
    sports = ["rugby", "cricket", "tennis", "golf", "cycling"]
    return render(request, 'sports.html', context={'sports': sports})