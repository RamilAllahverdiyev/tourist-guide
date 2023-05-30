from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import City, Destination, Favorite
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.contrib.auth import logout

def home(request):
    cities = City.objects.all()
    return render(request, 'home.html', {'cities': cities})


def room(request):
    return render(request, 'room.html')


def register_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.last_name = surname
            user.save()
            return redirect('login')  # Redirect to the login page after successful registration
        
        except:
            error_message = 'An error occurred during registration. Please try again.'
            return render(request, 'register.html', {'error_message': error_message})

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid email or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
       
    return render(request, 'login.html')


def profile_page(request):
    user = request.user
    favorite_destinations = Favorite.objects.filter(user=user).select_related('destination')

    context = {
        'favorite_destinations': favorite_destinations
    }

    return render(request, 'profile.html', context)


def city_details(request, city_id):
    city = get_object_or_404(City, id=city_id)
    destinations = city.destination_set.all()
    return render(request, 'city_details.html', {'city': city, 'destinations': destinations})


def add_to_favorites(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, destination=destination)
    if created:
        # New favorite created
        # You can add additional logic or display a success message here
        pass
    else:
        # Favorite already exists
        # You can add additional logic or display a message here
        pass
    return redirect('city_details', city_id=destination.city.id)


def remove_from_favorites(request, destination_id):
    user = request.user
    try:
        favorite = Favorite.objects.get(user=user, destination_id=destination_id)
        favorite.delete()
        return redirect('profile')
    except Favorite.DoesNotExist:
        return redirect('profile')


def search_view(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        city_results = City.objects.filter(name__icontains=search_query)

        if city_results:
            city = city_results[0]  # Get the first city that matches the search query
            results = city.destination_set.all()

    return render(request, 'home.html', {'form': form, 'cities': results})

def help_page(request):
    return render(request, 'help.html')

def logout_page(request):
    user = request.user
    logout(request)
    return redirect('home', {'user': user})