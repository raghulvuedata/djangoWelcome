from django.shortcuts import render
from django.http import JsonResponse


# Program to ask name and age and return a welcome message.
# def welcome_message(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         message = f"Welcome, {name}! You are {age} years old."
#         return render(request, 'welcome/welcome.html', {'message': message})
#     return render(request, 'welcome/welcome.html')


def welcome_message(request):
    # Retrieve the name parameter from the request
    name = request.GET.get('name', '')
    # Retrieve the value parameter from the request
    age = request.GET.get('age', '')

    welcome_msg = f"Welcome, {name}! Your age is: {age}"
    return JsonResponse({'message': welcome_msg})
