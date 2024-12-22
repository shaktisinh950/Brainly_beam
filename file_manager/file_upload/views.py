from django.shortcuts import render, redirect
from .forms import FileUploadForm

def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileUploadForm()

    return render(request, 'index.html', {'form': form})
