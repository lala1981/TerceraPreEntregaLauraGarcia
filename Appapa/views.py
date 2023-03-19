from django.shortcuts import render
from Appapa.models import Cliente, Producto, Pago

# Create your views here.
def guardar_cliente_view(request):
    
    if request.method == "POST":
        ultimo_cliente = Cliente.objects.last()
        ultimo_id = 0
        
        if ultimo_cliente:
            ultimo_id = ultimo_cliente.pk
            
        cliente = Cliente(ultimo_id + 1, request.POST["nombre"], request.POST["empresa"])
        cliente.save()
    
    clientes = Cliente.objects.all()
    context = {
        "clientes": clientes 
    }
    
    return render(request, "guardar_cliente_view.html", context)

def guardar_producto_view(request):
    
    if request.method == "POST":
        ultimo_producto = Producto.objects.last()
        ultimo_id = 0
        
        if ultimo_producto:
            ultimo_id = ultimo_producto.pk
            
        producto = Producto(ultimo_id + 1, request.POST["nombre"], request.POST["marca"], request.POST["precio"])
        producto.save()
    
    productos = Producto.objects.all()
    context = {
        "productos": productos 
    }
    return render(request, "guardar_producto_view.html", context)


def guardar_forma_pago_view(request):
    if request.method =="POST":
        ultima_forma = Pago.objects.last()
        ultimo_id = 0
    
        if ultima_forma:
            ultimo_id = ultima_forma.pk
            
        forma = Pago(ultimo_id + 1, request.POST["forma_pago"])
        forma.save()
    
    formas = Pago.objects.all()
    context  = {
        "formas" : formas
    }
    
    return render(request, "guardar_forma_pago_view.html", context)

def formulario_busqueda(request):
    if request.method == "POST":
        clientes = Cliente.objects.filter(nombre__contains = request.POST["busqueda"]).values() | Cliente.objects.filter(empresa__contains = request.POST["busqueda"]).values()
        context = {
            "coincidencias": clientes
        }
        
        return render(request, "formulario_busqueda.html", context)
    
    return render(request, "formulario_busqueda.html")