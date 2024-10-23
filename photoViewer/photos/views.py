from django.shortcuts import render, redirect
from .forms import PhotoUploadForm, PhotoSearchForm
from .models import Photo


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = PhotoUploadForm()
    return render(request, 'photos/upload.html', {'form': form})

def gallery(request):
    search_form = PhotoSearchForm(request.GET or None)
    photos = Photo.objects.all()

    # »ñÈ¡ÅÅÐòË³Ðò
    ordering = request.GET.get('ordering', 'asc')  # Ä¬ÈÏÕýÐò
    if ordering == 'desc':
        photos = photos.order_by('-capture_date')
    else:
        photos = photos.order_by('capture_date')

    # ËÑË÷¹ýÂË
    if search_form.is_valid():
        location = search_form.cleaned_data.get('location')
        start_date = search_form.cleaned_data.get('start_date')
        end_date = search_form.cleaned_data.get('end_date')

        if location:
            photos = photos.filter(location__icontains=location)
        if start_date:
            photos = photos.filter(capture_date__gte=start_date)
        if end_date:
            photos = photos.filter(capture_date__lte=end_date)

    return render(request, 'photos/gallery.html', {'photos': photos, 'search_form': search_form})