from django.shortcuts import render

def generate_menu(n):
    menu = [
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
    ]
    if n >= len(menu):
        return
    menu[n]["now"] = True
    return menu

def home(request):
    return render(request, 'base/home.html')