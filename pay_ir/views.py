from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponse
from django.urls import reverse
from django.conf import settings
from .models import Payment
import json
import requests


def method_not_allowed():
    """ This function only used when only POST method availabe. """

    return HttpResponseNotAllowed(
        ["POST"],
        content=json.dumps({"details": "Method not allowed"}),
        content_type="application/json"
    )


def error_code_message(response):
    return HttpResponse(content="({}): {}".format(
        response["errorCode"], response["errorMessage"]
    ))


def index(request):
    """ First page of app. """

    return render(request, "index.html")


def req(request):
    """ This function call pay.ir API and redirect user to payment page. """

    if request.method == "POST":
        url = "https://pay.ir/payment/send"
        fullname = request.POST.get('fullname')
        headers = {
            "Content-Type": "application/json",
        }
        data_dict = {
            "api": settings.PAY_IR_CONFIG.get("api_key"),
            "amount": int(request.POST.get('amount')),
            "redirect": request.scheme+"://"+request.get_host()+reverse('verify'),
            "mobile": request.POST.get('mobile'),
            "description": request.POST.get('description')
        }

        request_api = requests.post(
            url, data=json.dumps(data_dict), headers=headers
        )
        response = request_api.json()
        if response["status"] == 1:
            trans_id = response["transId"]
            db = Payment(full_name=fullname, amount=data_dict["amount"],
                         mobile=data_dict["mobile"],
                         description=data_dict["description"],
                         transid=int(trans_id)
                         )
            db.save()
            return redirect("https://pay.ir/payment/gateway/{}".format(str(trans_id)))
        else:
            return error_code_message(response)
        return HttpResponse(content=redirect)

    else:
        return method_not_allowed()


def verfication(request):
    pass
