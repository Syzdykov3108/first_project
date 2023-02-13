from django.shortcuts import render

pages = {
        'home': 'Главная',
        'about': 'О сайте',
        'contacts': 'Контакты',
}

def index(request):
    return render(request, 'main/index.html', pages)

def about(request):
    return render(request, 'main/about.html', pages)

def contacts(request):
    return render(request, 'main/contacts.html', pages)
