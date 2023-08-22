from django.shortcuts import render,HttpResponse

# Create your views here.
from django.shortcuts import render
import requests
import json

def bitbucket_data(request):
    # Set your Bitbucket credentials and repository details
    username = 'your_username'
    app_password = 'your_app_password'
    repository_slug = 'your_repository_slug'
    api_base_url = f'https://api.bitbucket.org/2.0/repositories/{username}/{repository_slug}'

    # Make a GET request to retrieve repository information
    response = requests.get(api_base_url, auth=(username, app_password))

    if response.status_code == 200:
        repository_info = response.json()
    else:
        repository_info = None

    return render(request, 'bitbucket_data.html', {'repository_info': repository_info})