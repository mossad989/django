from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from filmyweb.forms import FilmForm
from .models import Film 
from .forms import FilmForm

def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    ilosc = len(wszystkie)
    return render(request,'filmy.html',{'filmy': wszystkie})

@login_required
def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})

@login_required
def edytuj_film(request,id):
    film = get_object_or_404(Film,pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})

    
@login_required
def usun_film(request,id):
    film = get_object_or_404(Film,pk=id)


    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})