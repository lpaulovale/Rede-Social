from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt

  #Página usuarios com os usuários já cadastrados
@csrf_exempt
def usuarios(request):
  myusuarios = Usuario.objects.all().values()
  template = loader.get_template('usuarios.html')
  context = {
    'myusuarios': myusuarios,
  }
  return HttpResponse(template.render(context, request))
  
  #Página de cadastro
@csrf_exempt
def usuarioCadastro(request):
  template = loader.get_template('cadastrar.html')
  return HttpResponse(template.render())
  
  #Página de avisar que sobrevivente foi infectado
@csrf_exempt
def avisar(request):
      template = loader.get_template('avisar.html')
      return HttpResponse(template.render())

  #Cadastrar usuário 
@csrf_exempt
def setUsuario(request):
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

   template = loader.get_template('usuarios.html')
   
   context = {
   'myusuarios': myusuarios,
   }
  
   return HttpResponse(template.render(context, request))

  #Atualiza número de aviso de infecção de um sobrevivente ou se foi infectado
@csrf_exempt
def atualizarInfectado(request):
   
   myusuario = Usuario.objects.get(nome=request.POST.get('nome'))
   
   #adiciona aviso de infecção
   if (myusuario.infectado == False):
    myusuario.aviso += 1
   
   #caso tenha 3 avisos está infectado
    if(myusuario.aviso==3):
       myusuario.infectado = True
       
    myusuario.save()  
  
   template = loader.get_template('usuarios.html')
   
   context = {
   'myusuario': myusuario,
   }
   
   return HttpResponse(template.render(context, request))

  #Página de trocar itens
@csrf_exempt
def trocar(request):
    template = loader.get_template('trocar.html')
    return HttpResponse(template.render())

  #Troca itens e pontos entre sobreviventes
@csrf_exempt
def atualizarTroca(request):
   
   myuser = Usuario.objects.get(nome=request.POST.get('nome'))
   myuser2 = Usuario.objects.get(nome=request.POST.get('nome2'))
   
     #Recupera a quantidade dos itens no request.POST e calcula os pontos 
   quantidade1 = request.POST.get('quantidade1')
   quantidade2 = request.POST.get('quantidade2')
   quantidade3 = request.POST.get('quantidade3')
   quantidade4 = request.POST.get('quantidade4')
   quantidade12 = request.POST.get('quantidade12')
   quantidade22 = request.POST.get('quantidade22')
   quantidade32 = request.POST.get('quantidade32')
   quantidade42 = request.POST.get('quantidade42')
     #Transforma para int
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
   
   #se algum usuario estiver infectado ou a quantidade de pontos dos itens não for a mesma, a ação retorna erro
   if(myuser.infectado or myuser2.infectado or pontos != pontos2):
    return HttpResponseNotFound('<h1>Incorrect request</h1>')
     #Caso contrario recalcula as novas quantidades de itens dos clientes
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
    
    #Página de Atualização de local
@csrf_exempt
def atualizarLocal(request):
   template = loader.get_template('atualizarLocal.html')
   return HttpResponse(template.render())

  #Atualiza o local do sobrevivente
@csrf_exempt
def atualizarLocalizacao(request):
   myuser = Usuario.objects.get(nome=request.POST.get('nome'))
   
   myuser.latitude = request.POST.get('latitude')
   myuser.longitude = request.POST.get('longitude')
   
   myuser.save()
   
   template = loader.get_template('usuarios.html')
   
   return HttpResponse(template.render())

#Calcula as funções de analytics e renderiza a página de analytics
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
  
  #Pontos perdidos
  for i in myusuarios:
    nUsuarios += 1
    if (i.infectado == True):
      nInfectados += 1
      pontosPerdidos = ((i.quantidade1 * 4) + (i.quantidade2 *3) + (i.quantidade3 *2) +i.quantidade4)
    #Calcula quantidades de itens
    quantAgua += i.quantidade1 
    quantAlimento += i.quantidade2 
    quantMedicamentos += i.quantidade3 
    quantMunicao += i.quantidade4

  porcentagemInfectados = (nInfectados/nUsuarios)*100
  porcentagemNaoInfectados = 100 - porcentagemInfectados
  
  #Quantidade dos itens por sobrevivente
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