from django.shortcuts import render, redirect
from django.views import View


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from lib.log import log

class Index(View):
    def get(self, request, id):
        return render(request, 'core/index.html', {"id":id})

class login(View):
    def get(self, request):
        return render(request, 'core/login.html') #Alterar o diretório da pagina de login dentro das ''

    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('passwd')
        user = authenticate(username=username, password=password)
        if username is not None:
            login(request, user)
            return redirect('index')

class register(View):
    def get(self, request):
        return render(request, 'core/register.html') #Alterar o diretório da pagina de registro dentro das ''

    def post(self, request):
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('passwd')
        if username is not '' and email is not '' and password is not '':
            try:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()
            except Exception as error:
                log(f'Exception: {Exception} -- Error: {error}')
                message = 'Email já cadastrado.'
                return render(request, 'diretório da pagina de registro', {'message' : message})

        else:
            message = 'Insira todos os campos!'
            return render(request, 'diretório da pagina de registro', {'message' : message})
        return redirect('login')


