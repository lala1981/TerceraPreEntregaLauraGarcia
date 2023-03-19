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
    
    return render(request, "guardar_cliente_view.html")

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
    
    return render(request, "guardar_producto_view.html")