from django.test import TestCase
from welcome.views import welcome_message
from django.http import JsonResponse
from django.test import RequestFactory
import json


def test_welcome_message():
    factory = RequestFactory()
    request = factory.get('/welcome/', {'name': 'Rahul', 'age': '1'})

    response = welcome_message(request)

    expected_message = {'message': 'Welcome, Rahul! Your age is: 1'}

    # Get the JSON response content as a string
    response_content = response.content.decode('utf-8')

    # Parse the JSON response string
    response_data = json.loads(response_content)

    assert response_data == expected_message
