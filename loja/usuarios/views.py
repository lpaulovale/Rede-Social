from django.http import HttpResponse
from django.template import loader
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def usuarios(request):
  myusuarios = Usuario.objects.all().values()
  template = loader.get_template('todos_os_usuarios.html')
  context = {
    'myusuarios': myusuarios,
  }
  return HttpResponse(template.render(context, request))
@csrf_exempt
def usuarioCadastro(request):
  template = loader.get_template('cadastrarUsuario.html')
  return HttpResponse(template.render())

@csrf_exempt
def setUsuario(request):
   print(request.body)
   usuario = Usuario(firstname=request.POST.get('firstName'), lastname=request.POST.get('lastName'))
   myusuario = usuario.save()
   myusuarios = Usuario.objects.all().values()
   print(myusuarios)
   template = loader.get_template('todos_os_usuarios.html')
   context = {
   'myusuarios': myusuarios,
   }
   return HttpResponse(template.render(context, request))
