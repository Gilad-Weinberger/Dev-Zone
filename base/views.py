from django.shortcuts import render

def generate_menu(n):
    menu = [
        {"name": "בית", "icon": "fa-regular fa-house", "now": False},
        {"name": "פרוייקטים", "icon": "fa-regular fa-laptop", "now": False},
        {"name": "סטטיסטיקות", "icon": "fa-regular fa-signal-bars", "now": False},
        {"name": "תחרויות", "icon": "fa-regular fa-trophy", "now": False},
        {"name": "שאלות נפוצות", "icon": "fa-regular fa-circle-info", "now": False},
        {"name": "בלוג", "icon": "fa-regular fa-newspaper", "now": False},
        {"name": "מועדון", "icon": "fa-regular fa-users", "now": False},
        {"name": "הגדרות", "icon": "fa-regular fa-gear", "now": False},
    ]
    if n >= len(menu) or n < 0:
        return []
    menu[n]["now"] = True
    return menu

def home(request):
    menu = generate_menu(0)
    
    context = {
        "menu": menu,
    }

    return render(request, 'base/home.html', context)