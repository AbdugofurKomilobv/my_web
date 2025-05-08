from django.shortcuts import render,redirect
from main.models import Portfolio
from main.models import ContactMe

def home(request):
    portfolios = Portfolio.objects.all()
    context = {
    'portfolios': portfolios,
}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        ContactMe.objects.create(
            u_name = name,
            email=email,
            subject=subject,
            message=message
        )
        return redirect('message')
    
   


    return render(request, template_name='index.html',context=context)

def message(request):
    return render(request, template_name='message.html')

