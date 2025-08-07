# Django and DRF imports
from django.shortcuts import render 
from rest_framework.decorators import api_view
from django.contrib import messages
from datetime import datetime
from rest_framework import viewsets
from .models import Item
from rest_framework import generics
from .serializers import ItemSerializer

# For generating random captchas
import random


# Function to generate a random captcha string.
# It takes an optional argument 'n' for the length of the captcha.
def generate_captcha(n=6):
    # Defines the pool of characters to choose from for the captcha.
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    captcha = ""
    # Loops 'n' times to build the captcha string.
    for _ in range(n):
        # Appends a randomly selected character from 'chrs' to the captcha.
        captcha += random.choice(chrs)
    return captcha


# Home view: Generates a new captcha and renders the home page.
def home(request):
    # Generates a new 6-character captcha.
    captcha = generate_captcha(6)
    # Stores the generated captcha in the user's session for validation later.
    request.session['captcha'] = captcha
    # Renders the 'index.html' template, passing the captcha to the context.
    return render(request, 'index.html', {'captcha': captcha})


# Result view: Handles form submission, captcha validation, and item lookup.
def result(request):
    # Retrieves form data submitted via a GET request.
    case_number = request.GET.get('case_number')
    year = request.GET.get('year')
    user_captcha = request.GET.get('captcha')
    # Retrieves the captcha stored in the session.
    session_captcha = request.session.get('captcha', '')

    # Validates the user's entered captcha against the one stored in the session.
    if not user_captcha or user_captcha != session_captcha:
        # If invalid, adds an error message.
        messages.error(request, 'Invalid CAPTCHA')
        # Regenerates a new captcha for the user to try again.
        captcha = generate_captcha(6)
        request.session['captcha'] = captcha
        # Renders the home page again with the new captcha.
        return render(request, 'index.html', {'captcha': captcha})

    try:
        # Attempts to find an Item object in the database with the given case_number.
        item = Item.objects.get(case_number=case_number)
        # If successful, renders the 'as.html' template, passing the found item.
        return render(request, 'as.html', {'item': item})
    except Item.DoesNotExist:
        # If no item is found, adds an error message.
        messages.error(request, 'invalid case number')
        # Regenerates the captcha for a new attempt.
        captcha = generate_captcha(6)
        request.session['captcha'] = captcha
        # Renders the home page again with the new captcha.
        return render(request, 'index.html', {'captcha': captcha})


# API view for listing all items or creating a new item.
# It inherits from generics.ListCreateAPIView, which provides
# default behaviors for these actions.
class ItemListCreateView(generics.ListCreateAPIView):
    # Specifies the queryset to be used for the view (all Item objects).
    queryset = Item.objects.all()
    # Specifies the serializer class to be used for data conversion.
    serializer_class = ItemSerializer


# API view for retrieving, updating, or deleting a single item.
# It inherits from generics.RetrieveUpdateDestroyAPIView.
# The URL must contain a primary key (pk) to identify the item.
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Specifies the queryset to be used.
    queryset = Item.objects.all()
    # Specifies the serializer class.
    serializer_class = ItemSerializer