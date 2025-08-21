from django.shortcuts import render , redirect
from .models import Cosmetic
from .forms import LoginForm
# Create your views here.

def Home(request):
    if request.method == 'POST':
        dataform = LoginForm(request.POST, request.FILES) # تأكد أن الاسم صحيح

        if dataform.is_valid():
           
            dataform.save()
            return redirect('Home')
        
    else:
        dataform = LoginForm()

    products= Cosmetic.objects.all()

    
    return render(request, 'cosmetics/index.html',{'dataform':dataform, 'products': products })
