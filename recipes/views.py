from django.shortcuts import render, HttpResponse

recipes =[
    {
    'author': 'Me',
    'title': 'jerk chicken',
    'directions': 'add spices to chicken, mix, cook in oven',
    'date_posted': 'July 16th 2023',
    },
    {
    'author': 'Me',
    'title': 'lemon chicken',
    'directions': 'add spices to chicken, mix, cook in oven',
    'date_posted': 'July 19th 2023',
    },
    {
    'author': 'Me',
    'title': 'apicy chicken',
    'directions': 'add spices to chicken, mix, cook in oven',
    'date_posted': 'July 20th 2023',
    },
    
]

# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)
    

def about(request):
    return render(request, "recipes/about.html", {'title':'about us page'})
