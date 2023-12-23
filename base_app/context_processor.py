from .models import *


def exp_requests(request):
    if "Adm_id" in request.session:
        if request.session.has_key("Adm_id"):
            Adm_id = request.session["Adm_id"]

        Adm = user_registration.objects.filter(id=Adm_id)
        admin = user_registration.objects.get(id=Adm_id)
        req = user_registration.objects.filter(
            branch=admin.branch, exp_certificate_status="pending"
        )
        return {"Adm": Adm, "exp_requests": req}
    else:
        return {"Adm": None, "exp_requests": None}
