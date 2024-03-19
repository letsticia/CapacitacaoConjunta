from django.shortcuts import render
from .forms import UsuarioForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def cadastro(request):
    form = UsuarioForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        form = UsuarioForm()
        
    return render(request, 'cadastro.html', {'form': form})