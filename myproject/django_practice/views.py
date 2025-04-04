from django.http import HttpResponse
from django.shortcuts import render
from .models import Author

def upload_file(request):
    if request.method ==" POST" and request.FILES['file']:
        myfile = request.FILES['file']
        with open(f'media/{myfile.name}', 'wb+') as destination:
            for chunk in myfile.chunks():
                destination.write(chunk)
        return HttpResponse("File uploaded successfully")
    return render(request, 'upload.html')
