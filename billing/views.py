from liqpay import LiqPay

from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

class PayView(TemplateView):
template_name = 'billing/pay.html'

def get(self, request, *args, **kwargs):
    liqpay = LiqPay(settings.sandbox_i26660223217, settings.sandbox_u3BM9ppkXfPn0Phd5ZNhpkzieRiVWHmq12iJUJYb)
    params = {
        'action': 'pay',
        'amount': '100',
        'currency': 'USD',
        'description': 'Payment for clothes',
        'order_id': 'order_id_1',
        'version': '3',
        'sandbox': 0, # sandbox mode, set to 1 to enable it
        'server_url': 'https://test.com/billing/pay-callback/', # url to callback view
    }
    signature = liqpay.cnb_signature(params)
    data = liqpay.cnb_data(params)
    return render(request, self.template_name, {'signature': signature, 'data': data})

@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)
        return HttpResponse()

