from django.shortcuts import render

# Create your views here.


def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('year'))
        
    return render(request, 'create.html')


def list(request):
    movie_data = {
        'movies': [
            {
                'title': 'Godfather',
                'year': 1990,
                'summary': 'story of an underworld king',
                'success': True,
                'img': 'godfather.jpeg'
            }, {
                'title': 'Titanic',
                'year': 1990,
                'success': True,
                'img': 'titanic.jpeg'
            }, {
                'title': 'Into the wild',
                'year': 1980,
                'summary': 'story of an underworld king',
                'success': True,
                'img': 'wild.jpeg'
            }]
    }
    return render(request, 'list.html', movie_data)


def edit(request):
    return render(request, 'edit.html')
