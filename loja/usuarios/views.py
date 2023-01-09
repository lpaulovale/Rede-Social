from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def usuarios(request):
  myusuarios = Usuario.objects.all().values()
  template = loader.get_template('usuarios.html')
  context = {
    'myusuarios': myusuarios,
  }
  return HttpResponse(template.render(context, request))
@csrf_exempt
def usuarioCadastro(request):
  template = loader.get_template('cadastrarUsuario.html')
  return HttpResponse(template.render())

@csrf_exempt
def avisar(request):
      template = loader.get_template('avisar.html')
      return HttpResponse(template.render())

@csrf_exempt
def setUsuario(request):
   print(request.body)
   usuario = Usuario(
   nome = request.POST.get('nome'),
   idade = request.POST.get('idade'),
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
   template = loader.get_template('usuarios.html')
   context = {
   'myusuarios': myusuarios,
   }
   return HttpResponse(template.render(context, request))

@csrf_exempt
def atualizarInfectado(request):
   print(request.body)
   myusuario = Usuario.objects.get(nome=request.POST.get('nome'))
   if(request.POST.get('avisar') == 1 and myusuario.infectado == False):
     myusuario.avisar += 1
     if(myusuario==3):
       myusuario.infectado = True
     myusuario.save()  
   template = loader.get_template('usuarios.html')
   return HttpResponse(template.render())

@csrf_exempt
def trocar(request):
    template = loader.get_template('trocar.html')
    return HttpResponse(template.render())

@csrf_exempt
def atualizarTroca(request):
   myuser = Usuario.objects.get(nome=request.POST.get('nome'))
   myuser2 = Usuario.objects.get(nome=request.POST.get('nome2'))
   print(request.body)
   quantidade1 = request.POST.get('quantidade1')
   quantidade2 = request.POST.get('quantidade2')
   quantidade3 = request.POST.get('quantidade3')
   quantidade4 = request.POST.get('quantidade4')
   quantidade12 = request.POST.get('quantidade12')
   quantidade22 = request.POST.get('quantidade22')
   quantidade32 = request.POST.get('quantidade32')
   quantidade42 = request.POST.get('quantidade42')
   quantidade1 = int(quantidade1)
   quantidade2 = int(quantidade2)
   quantidade3 = int(quantidade3)
   quantidade4 = int(quantidade4)
   quantidade12 = int(quantidade12)
   quantidade22 = int(quantidade22)
   quantidade32 = int(quantidade32)
   quantidade42 = int(quantidade42)
   pontos=0
   pontos2=0
   pontos+= (quantidade1*4)
   pontos+= quantidade2*3
   pontos+=quantidade3*2 
   pontos+=quantidade4 
   pontos2+=quantidade12*4 
   pontos2+=quantidade22*3 
   pontos2+=quantidade32*2 
   pontos2+=quantidade42 
   
   if(myuser.infectado or myuser2.infectado or pontos != pontos2):
    return HttpResponseNotFound('<h1>Incorrect request</h1>')
   else:
    myuser.quantidade1 -= quantidade1
    myuser.quantidade2 -= quantidade2
    myuser.quantidade3 -= quantidade3
    myuser.quantidade4 -= quantidade4
    myuser.quantidade1 += quantidade12
    myuser.quantidade2 += quantidade22
    myuser.quantidade3 += quantidade32
    myuser.quantidade4 += quantidade42
   
    myuser2.quantidade1 -= quantidade12
    myuser2.quantidade2 -= quantidade22
    myuser2.quantidade3 -= quantidade32
    myuser2.quantidade4 -= quantidade42
    myuser2.quantidade1 += quantidade1
    myuser2.quantidade2 += quantidade2
    myuser2.quantidade3 += quantidade3
    myuser2.quantidade4 += quantidade4
   
    myuser.save()
    myuser2.save()
   
    template = loader.get_template('usuarios.html')
    return HttpResponse(template.render())
    
@csrf_exempt
def atualizarLocal(request):
   template = loader.get_template('atualizarLocal.html')
   return HttpResponse(template.render())

@csrf_exempt
def atualizarLocalizacao(request):
   myuser = Usuario.objects.get(nome=request.POST.get('nome'))
   myuser.latitude = request.POST.get('latitude')
   myuser.longitude = request.POST.get('longitude')
   myuser.save()
   template = loader.get_template('usuarios.html')
   return HttpResponse(template.render())

@csrf_exempt
def analytics(request):
  myusuarios = Usuario.objects.all()
  
  nInfectados =0
  nUsuarios =0
  pontosPerdidos=0
  quantAgua=0
  quantAlimento=0
  quantMedicamentos=0
  quantMunicao=0
  
  for i in myusuarios:
    nUsuarios += 1
    
    if (i.infectado == True):
      nInfectados += 1
      pontosPerdidos(i.quantidade1 * 4) + (i.quantidade2 *3) + (i.quantidade3 *2) +i.quantidade4
    
    quantAgua += i.quantidade1 
    quantAlimento += i.quantidade2 
    quantMedicamentos += i.quantidade3 
    quantMunicao += i.quantidade4
  
  porcentagemInfectados = (nInfectados/nUsuarios)*100
  porcentagemNaoInfectados = 100 - porcentagemInfectados
  quantAguaM = quantAgua/nUsuarios
  quantAlimentoM = quantAlimento/nUsuarios
  quantMedicamentosM = quantMedicamentos/nUsuarios
  quantMunicaoM = quantMunicao/nUsuarios
  
  context = {
   'porcentagemInfectados': porcentagemInfectados,
   'porcentagemNaoInfectados': porcentagemNaoInfectados,
   'pontosPerdidos': pontosPerdidos,
   'quantAguaM':  quantAguaM,
   'quantAlimentoM': quantAlimentoM,
   'quantMedicamentosM': quantMedicamentosM,
   'quantMunicaoM': quantMunicaoM
   }
   
  template = loader.get_template('analytics.html')
  return HttpResponse(template.render(context, request))