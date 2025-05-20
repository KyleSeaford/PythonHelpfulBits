# How to Start a Django Project

## Before you begin, ensure you have the following installed:

`Python (version 3.6 or above)`
`pip (Python package installer)`

## Step 1: Install Django:
`pip install django`

## Step 2: Create a New Django Project
`python -m django startproject myproject`
  
Navigate into the project directory:
`cd myproject`
  
## Step 3: Run the Development Server
`python manage.py runserver`
  
Access the application by going to: `http://127.0.0.1:8000/` You should see the Django welcome page.


Register the app by opening settings.py in your project directory (myproject/myproject/settings.py) and adding myproject to the INSTALLED_APPS list:
```python
INSTALLED_APPS = [
    ...
    'myproject',
]
```
## Step 5: Create Views and Templates
You can now define views and create templates for your app.
Define a view by editing `views.py` in myapp:

```pyhton
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```
Map the view to a URL by creating a file named urls.py in your app directory (myapp/urls.py) and defining your URLs:

```pyhon
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

# Step 6: TEMPLATE FOLDER IN PROJECT FOLDER
- Within myapp folder, create a folder called `templates` and in that create `index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Django App</title>
</head>
<body>
    <h1>Welcome Kyle</h1>
</body>
</html>
```

- Edit `views.py` to render the template:
```python
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')
```

Congratulations! You have successfully created a basic Django project and app. You can now explore Django's features, such as models, templates, forms, and more.

Happy coding!
