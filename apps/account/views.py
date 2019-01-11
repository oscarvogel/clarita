from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.account.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm

#
# def login_usuario(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             usuario = authenticate(username=cd['usuario'],
#                                    password=cd['password'])
#             if usuario is not None:
#                 if usuario.is_active:
#                     login(request, usuario)
#                     return HttpResponse('Usuario Autenticado')
#                 else:
#                     return HttpResponse('Cuenta deshabilitada')
#             else:
#                 return HttpResponse('Login invalido')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html',{
#         'form':form
#     })
from apps.account.models import Profile


@login_required
def dashboard(request):
    profile = Profile.objects.get(usuario=request.user)
    user = User.objects.get(username=request.user)
    return render(request,'account/dashboard.html',{
        'section': 'dashboard',
        'profile':profile,
        'user':user
    })

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(usuario=new_user)
            return render(request,'account/register_done.html',{
                'new_user': new_user
            })
    else:
        user_form = UserRegistrationForm()

    return render(request,'account/register.html',{
        'user_form': user_form
    })

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Datos actualizados')
        else:
            messages.error(request, 'Error actualizando sus datos')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})