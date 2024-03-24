from django.shortcuts import render, redirect
from .forms import UsuarioForm

# Create your views here.
def index(request):
    return render(request,'main.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'cadastrofun.html', {'form': form})