# How to Load Static Files in Django

## Step 1: Create Static Directories:
Inside your app directory (e.g., myproject), create a static folder:
```
myproject/
    static/
      style.css
      script.js
      images.png
    templates/
```
## Step 2: Configure Settings
Ensure these settings in `myproject/settings.py`:
```python
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',  # Should already be included
    'myproject',  # Your app must be registered here
]

STATIC_URL = '/static/'  # Default setting (verify it exists)
```
  
## Step 3: Use Static Files in Templates
Modify your template (e.g., templates/index.html) to load static files:
```html
{% load static %}  <!-- Add this at the top -->
<!DOCTYPE html>
<html>
<head>
    <title>My Django App</title>
    <link rel="stylesheet" href="{% static 'myproject/css/style.css' %}">
</head>
<body>
    <h1>Welcome Kyle</h1>
    <img src="{% static 'myproject/images/logo.png' %}" alt="Logo">
    <script src="{% static 'myproject/js/script.js' %}"></script>
</body>
</html>
```

## Step 4: Run the Development Server
`python manage.py runserver`
  
Visit `http://127.0.0.1:8000` to see your styled page.
