from django.http import HttpResponse

# Create your views here.
from AppProyecto.models import Curso

def curso(request, nombre, numero):
    curso = Curso(nombre= nombre, camada=int(numero))
    curso.save ()
    documento = f"curso:{curso.nombre}<br>camada: {curso.camada}"
    return HttpResponse(documento)