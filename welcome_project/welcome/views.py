from django.shortcuts import render


# Program to ask name and age and return a welcome message.
def welcome_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        message = f"Welcome, {name}! You are {age} years old."
        return render(request, 'welcome/welcome.html', {'message': message})
    return render(request, 'welcome/welcome.html')
