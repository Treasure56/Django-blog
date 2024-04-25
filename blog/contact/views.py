from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Contact

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']
        
        contact = Contact(name=name, email=email, subject=sub, message=msg)
        contact.save()
        messages.success(request, 'your message has been recieved...')
        return redirect('contact')
        
    else:
        return render(request, 'contact/contact.html')
