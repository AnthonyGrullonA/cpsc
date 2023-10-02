from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Acl_Permanent_View(request):
    return render(request, 'pages/cosmos/acl_permanent.html')

@login_required
def Acl_Temporary_View(request):
    return render(request, 'pages/cosmos/acl_temporary.html')

@login_required
def Restridted_Client_View(request):
    return render(request, 'pages/cosmos/restridted_client.html')

@login_required
def Formularios_ACL(request):
    return render(request, 'pages/formularios/formularios_acl.html')