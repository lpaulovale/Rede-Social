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
   usuario = Usuario(
   nome = request.POST.get('nome'),
   sexo = request.POST.get('sexo'),
   longitude = request.POST.get('longitude'),
   latitude = request.POST.get('latitude'),
   aviso = request.POST.get('aviso'),
   quantidade1 = request.POST.get('quantidade1'),
   quantidade2 = request.POST.get('quantidade2'),
   quantidade3 = request.POST.get('quantidade3'),
   quantidade4 = request.POST.get('quantidade4'))
   myusuario = usuario.save()
   myusuarios = Usuario.objects.all().values()
   print(myusuarios)
   template = loader.get_template('todos_os_usuarios.html')
   context = {
   'myusuarios': myusuarios,
   }
   return HttpResponse(template.render(context, request))
