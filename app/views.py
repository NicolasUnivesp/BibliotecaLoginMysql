from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from app.forms import LivrosForm
from app.models import Livros


def form(request):
    data = {}
    data['form'] = LivrosForm()
    return render(request, 'form.html', data)


def home(request):
    data = {}
    all = Livros.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    search = request.GET.get('search')
    if search:
        data['db'] = Livros.objects.filter(titulo__icontains=search)
    else:
        data['db'] = Livros.objects.all()
    return render(request, 'index.html', data)


def create(request):
    # login_url = reverse_lazy('login')
    form = LivrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    data['form'] = LivrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    form = LivrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Livros.objects.get(pk=pk)
    db.delete()
    return redirect('home')


