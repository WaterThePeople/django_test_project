from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import LoginForm
from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Twoje konto zostało utworzone! Możesz się teraz zalogować!')
            return redirect('login')  
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm