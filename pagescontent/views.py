from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages

#El home carga el login 1
def Home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')  
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
    return render(request, 'home.html')


# 404 error template
def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)


def custom_page_server_error(request, exception):
    return render(request, '500.html', status=500)

@login_required
def Admin_Page_Service_Center(request):
    return render(request, 'admin_template/index.html')

######################################################################################################################################################


@login_required
def Formularios_Implementaciones(request):
    return render(request, 'pages/formularios/formularios_implementaciones.html')




