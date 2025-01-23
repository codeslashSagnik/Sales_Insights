from .models import SalesData  
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SalesDataForm
from django.contrib import messages

def add_article(request):
    if request.method == 'POST':
        form = SalesDataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data added successfully!")
            return redirect('dashboard')  
    else:
        form = SalesDataForm()
    return render(request, 'add_article.html', {'form': form})
def dashboard(request):
    articles = SalesData.objects.all()  
    return render(request, 'dashboard.html', {'articles': articles})
def delete_article(request, pk):
    article = get_object_or_404(SalesData, pk=pk)
    article.delete()
    return redirect('dashboard')
def edit_article(request, pk):
    article = get_object_or_404(SalesData, pk=pk)
    if request.method == 'POST':
        form = SalesDataForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = SalesDataForm(instance=article)
    return render(request, 'edit_article.html', {'form': form, 'article': article})