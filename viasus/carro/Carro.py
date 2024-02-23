class Carro():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")

        if not carro:
            carro = self.session["carro"] = {}
        
        self.carro = carro
    
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
            
    def agregar(self, producto):
        cantidad = int(self.request.POST.get(producto.codigo))
        if (str(producto.id) not in self.carro.keys()):
            self.carro[str(producto.id)] = {
                "imagen": producto.imagen,
                "codigo": producto.codigo,
                "titulo": producto.titulo,
                "cantidad": cantidad,
                "precio": producto.precio
            }
        else:
            for key, value in self.carro.items():
                if (key == str(producto.id)):
                    self.carro[key]["cantidad"] = int(value) + cantidad
                    break
        self.guardar_carro()
        print(self.carro)

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

