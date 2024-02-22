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
        if (producto.id not in self.carro.keys()):
            print(self.request.GET)
            # self.carro[producto.id] = producto.cantidad
        else:
            for key, value in self.carro.items():
                if key == producto.id:
                    value += producto.cantidad
                break
        self.guardar_carro()
