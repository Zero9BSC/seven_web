from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        query_text = request.POST['query_text']
        data = Contact(name=name, email=email, query_text=query_text)
        data.save()
        return render(request, 'success.html')
    else:
        return render(request,'contact.html')
