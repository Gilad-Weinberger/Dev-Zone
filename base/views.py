from django.shortcuts import render

def generate_menu(n):
    menu = [
        {"name": "Home", "icon": "fa-regular fa-house", "now": False},
        {"name": "Projects", "icon": "fa-regular fa-house", "now": False},
        {"name": "Statistics", "icon": "fa-regular fa-house", "now": False},
        {"name": "Competitions", "icon": "fa-regular fa-house", "now": False},
        {"name": "FAQ", "icon": "fa-regular fa-house", "now": False},
        {"name": "Blog", "icon": "fa-regular fa-house", "now": False},
        {"name": "Club", "icon": "fa-regular fa-house", "now": False},
    ]
    if n >= len(menu):
        return
    menu[n]["now"] = True
    return menu

def home(request):
    menu = generate_menu(0)

    context = {
        "menu": menu,
    }

    return render(request, 'base/home.html', context)