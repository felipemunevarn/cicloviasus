from django_cron import CronJobBase, Schedule
from carro.models import Pedido, PedidoProducto
from catalogo.models import Producto

class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['02:28']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)

    code = 'viasus.my_cron_job'    # a unique code

    def do(self):
        day_checkouts = Pedido.objects.filter(fecha_pedido__contains='2024-03-10')
        resume = {}
        for checkout in day_checkouts:
            asked_products = PedidoProducto.objects.filter(pedido_id=checkout.id).select_related()
            for product in asked_products:
                if (product.producto.id in resume):
                    resume.update({
                        product.producto.id: resume[product.producto.id] + product.cantidad
                    })
                else:
                    resume.update({
                        product.producto.id: product.cantidad
                    })
        print("resumen", resume)
        