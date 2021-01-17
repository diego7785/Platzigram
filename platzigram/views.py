from django.http import HttpResponse

def home(req):
    return HttpResponse('Holi, que tal?')

def saludo(req,name,age):
    return HttpResponse('Hola, {name} tienes: {age} anios'.format(name=name, age=age))

def saludoQuery(req):
    return HttpResponse('Hola, {name}'.format(name=req.GET['nombre']))