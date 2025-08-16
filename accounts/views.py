from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from accounts.models import User, RegisterForm


# Create your views here.

def home(request):
    return render(request, 'base.html')

# def user(request):
#     qs = User.objects.all()
#     context = {
#         'qs': qs,
#     }
#     return render(request, 'user_registration.html')

class RegisterView(View):
    queryset = RegisterForm.objects.all()
    template_name = 'register.html'

def register(request):
    register_form= RegisterForm(request.POST or None)
    if register_form.is_valid():
        # print(register_form.cleaned_data)
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)

    context = {
        'register_form': register_form,
    }
    return render(request, "register.html", context)
