from django.shortcuts import render
from django.http import HttpResponse
from AppFormulario.models import *
from django.template import loader
from AppFormulario.forms import *

# views de las templetes de la pagina
def inicio(request):
    
    return render(request,'AppFormulario/inicio.html')

def principiante(request):
    
    return render(request,'AppFormulario/principiante.html')

def intermedio(request):
    
    return render(request,'AppFormulario/intermedio.html')

def avanzado(request):
    
    return render(request,'AppFormulario/avanzado.html')

def profesional(request):
    
    return render(request,'AppFormulario/profesional.html')

#view de los formularios de las distintas clases que se imparten
def principiante(request):
    
    if request.method == 'POST':
        
        miFormulario = PrincipianteFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            principiante = Principiante(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            principiante.save()
        
            return render(request,"AppFormulario/inicio.html")
    else:
        miFormulario=PrincipianteFormulario()
    return render(request,"AppFormulario/principianteFormulario.html",{"miFormulario":miFormulario})

def intermedio(request):
    
    if request.method == 'POST':
        
        miFormulario = IntermedioFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            intermedio = Intermedio(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],peso=informacion['peso'])
            intermedio.save()
        
            return render(request,"AppFormulario/inicio.html")
    else:
        miFormulario=IntermedioFormulario()
    return render(request,"AppFormulario/intermedioFormulario.html",{"miFormulario":miFormulario})

def avanzado(request):
    
    if request.method == 'POST':
        
        miFormulario = AvanzadoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            avanzado = Avanzado(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],peso=informacion['peso'],nro_combates=informacion['nro_combates'])
            avanzado.save()
        
            return render(request,"AppFormulario/inicio.html")
    else:
        miFormulario=AvanzadoFormulario()
    return render(request,"AppFormulario/avanzadoFormulario.html",{"miFormulario":miFormulario})

def profesional(request):
    
    if request.method == 'POST':
    
        miFormulario = ProfesionalFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            profesional = Profesional(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],peso=informacion['peso'],nro_combates=informacion['nro_combates'],edad=informacion['edad'])
            profesional.save()
        
            return render(request,"AppFormulario/inicio.html")
    else:
        miFormulario=ProfesionalFormulario()
    return render(request,"AppFormulario/profesionalFormulario.html",{"miFormulario":miFormulario})

#busqueda de alumnos principiantes segun su email
def busquedaPrincipiante(request):
    
    return render(request, "busquedaPrincipiante.html",{})

def buscar(request):
    
    if request.GET["email"]:
        
        email = request.GET["email"]
        principiantes = Principiante.objects.get(email=email)
        
        return render(request, "resultadoBusquedaPrincipiante.html",{"principiante":principiantes,"email":email})
    
    else:
        return render(request, 'inicio.html', {"message":"No enviaste el mail correcto"})
