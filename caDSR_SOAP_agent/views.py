from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pysimplesoap.server import SoapDispatcher
from pysimplesoap.simplexml import SimpleXMLElement
from NIH_caDSR_SOAP import settings
from forms_static import adrenal
from forms_static import demographic
from forms_static import FDA
from forms_static import HERF
from forms_static import NCI_Demographics
from forms_static_html import adrenal_html
from forms_static_html import demographic_html
from forms_static_html import FDA_html
from forms_static_html import HERF_html
from forms_static_html import NCI_Demographics_html


import os

def demo(request):
    return HttpResponse('NIH caDSR Web Services')

def wsdl(request):
    return HttpResponse('NIH caDSR WSDL')

def form_as_XML(request):
    formID = request.RetrieveFormRequest.workflow.formID
    if formID == 'Adrenal_xml':
      return SimpleXMLElement(adrenal)
    elif formID == 'Demog_xml':
      return SimpleXMLElement(demographic)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/form_package_identifier#4617751v1.0/1':
      return SimpleXMLElement(FDA)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr#form_package/99999/1.0':
      return SimpleXMLElement(HERF)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/form_package_identifier#2674812v4.0/1':
      return SimpleXMLElement(NCI_Demographics)
    elif formID == 'Adrenal_html':
      return SimpleXMLElement(adrenal_html)
    elif formID == 'Demog_html':
      return SimpleXMLElement(demographic_html)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/form_package_identifier#4617751v1.0/1/html':
      return SimpleXMLElement(FDA_html)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr#form_package/99999/1.0/html':
      return SimpleXMLElement(HERF_html)
    elif formID == 'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/form_package_identifier#2674812v4.0/1/html':
      return SimpleXMLElement(NCI_Demographics_html)
    else:
      return SimpleXMLElement('<xml>Error</xml>')

dispatcher = SoapDispatcher(
    'cadsr_soap_dispatcher',
    location = "https://localhost:8080/soap",
    action = "https://localhost:8080/soap",
    namespace = "http://nlm.nih.gov/sdc/form",
    prefix="ns0",
    ns = "urn:ihe:iti:rfd:2007")

# register func
dispatcher.register_function('soap', form_as_XML,
    returns={'FormResult': str},
    args={'formID': str})


#delete for csrf the POST for this view
@csrf_exempt
def dispatcher_handler(request):
    if request.method == "POST":
        response = HttpResponse(dispatcher.dispatch(request.body))
    else:
        response = HttpResponse(dispatcher.wsdl())
    response['Content-length'] = str(len(response.content))
    return response
