import requests
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
import json

from django.views.decorators.csrf import csrf_exempt

from .access_token import generate_access_token
from .utils import timestamp_conversion
from  .encode_base64 import generate_password

def index(request):
    return HttpResponse("sfneo")

class TestView(APIView):

    def get(self, request, format=None):
        access_token = generate_access_token()
        formatted_time = timestamp_conversion()
        decoded_password = generate_password(formatted_time)
        
        return Response({"access_token": access_token, "password ": decoded_password})
    
    
class MakePayment(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        
        amount = request_data["amount"]
        phone_number = request_data["phone_number"]
        
        paymentResponseData = self.make_mpesa_payment_request(amount=amount, phone_number = phone_number)
        
        return Response(paymentResponseData)
        
    def make_mpesa_payment_request(self, amount:str, phone_number: str) -> dict:
        access_token = generate_access_token()
        formatted_time = timestamp_conversion()
        decoded_password = generate_password(formatted_time)
        
        headers = {"Authorization": "Bearer %s" % access_token}
        
        request = {
            "BusinessShortCode": settings.BUSINESS_SHORT_CODE,
            "Password": decoded_password,
            "Timestamp": formatted_time,
            "TransactionType": settings.TRANSACTION_TYPE,
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": settings.BUSINESS_SHORT_CODE,
            "CallBackURL": settings.CALL_BACK_URL,
            "AccountReference": settings.ACCOUNT_REFERENCE,
            "TransactionDesc": settings.TRANSACTION_DESCRIPTION
        }
        
        response = requests.post(settings.API_RESOURCE_URL, headers=headers, json=request)
        
        mystr = response.text
        objstr = json.loads(mystr)
        
        merchant_request_id = objstr["MerchantRequestID"]
        checkout_request_id = objstr["CheckoutRequestID"]
        response_description = objstr["ResponseDescription"]
        response_code = objstr["ResponseCode"]
        
        data = {
            "merchant_request_id": merchant_request_id,
            "checkout_request_id": checkout_request_id,
            "response_description": response_description,
            "response_code": response_code
        }
        
        return data