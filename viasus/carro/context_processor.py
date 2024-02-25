def total(request):
    total = 0
    if (request.user.is_authenticated):
        for key, value in request.session["carro"].items():
            total += float(value["precio"]) * value["cantidad"]
    return {"total": total}
