from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageModel
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Convert the image to black and white
            original_image = Image.open(image_instance.original_image)
            bw_image = original_image.convert('L')  # Convert to grayscale

            # Save the black-and-white image
            buffer = BytesIO()
            bw_image.save(buffer, format='PNG')
            image_instance.bw_image.save(
                f"bw_{image_instance.original_image.name}",
                ContentFile(buffer.getvalue()),
                save=True
            )
            return redirect('image_list')
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = ImageModel.objects.all()
    return render(request, 'image_list.html', {'images': images})
