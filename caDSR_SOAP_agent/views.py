from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pysimplesoap.server import SoapDispatcher
 
def demo(request):
    return HttpResponse('NIH caDSR Web Services')

def wsdl(request):
    return HttpResponse('NIH caDSR WSDL')

dispatcher = SoapDispatcher(
    'cadsr_soap_dispatcher',
    location = "http://localhost:8080/soap",
    action = "http://localhost:8080/soap",
    namespace = "http://nlm.nih.gov/sdc/form",
    prefix="ns0",
    ns = "urn:ihe:iti:rfd:2007")

class DjangoSoapService(SoapDispatcher):
    csrf_exempt = True

    def __call__(self, request):
        response = HttpResponse(mimetype='application/xml')
        superclass = super(DjangoSoapService, self)
        if request.method == 'POST':
            response.write(superclass.dispatch(request.raw_post_data))
        elif request.method == 'GET':
            if not self.location:
                self.location = request.build_absolute_uri()
            response.write(superclass.wsdl())
        else:
            response.status_code = 405
        response['Content-length'] = str(len(response.content))
        return response

    def soap(self, **kwargs):
        def wrapper(func):
            returns = kwargs.pop('returns', None)
            if returns and not isinstance(returns, dict):
                returns = {'result': returns}
            self.register_function(func.__name__, func, args=kwargs, returns=returns)
        return wrapper

