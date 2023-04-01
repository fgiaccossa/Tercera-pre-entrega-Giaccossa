from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def registro_pasajero (request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("account_login")

# form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "accounts/registro.html", context=context)

def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            user = authenticate(username=informacion['username'], password=informacion['password'])

            if user:
                login(request, user)

                return redirect("bienvenido")
            else:
                return redirect("loginerror")

    form = AuthenticationForm()

    context = {
            "form": form
    }

    return render(request, "accounts/login.html", context=context)
