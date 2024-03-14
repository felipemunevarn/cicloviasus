from django_cron import CronJobBase, Schedule
from carro.models import Pedido, PedidoProducto
from datetime import datetime
from carro.views import send_mail_excel
from carro.create_excel import create_excel

class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['19:40']
    # RUN_EVERY_MINS = 1
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    # schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'viasus.my_cron_job'    # a unique code

    def do(self):
        today = datetime.now().date().strftime("%Y-%m-%d")
        day_checkouts = Pedido.objects.filter(fecha_pedido__contains=today)
        carro = {}
        for checkout in day_checkouts:
            asked_products = PedidoProducto.objects.filter(pedido_id=checkout.id).select_related()
            for product in asked_products:
                if (str(product.producto.id) in carro):
                    carro.get(str(product.producto.id)).update({ 'cantidad':carro.get(str(product.producto.id))["cantidad"] + product.cantidad})
                else:
                    carro.update({str(product.producto.id): {}})
                    carro.get(str(product.producto.id)).update({ 'cantidad': product.cantidad })
        create_excel(request="", daily_cart=carro)
        send_mail_excel("", "", "", True, today)
