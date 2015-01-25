import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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
from pysimplesoap.server import SoapDispatcher
from pysimplesoap.simplexml import SimpleXMLElement
from NIH_caDSR_SOAP import settings

forms = { 'Adrenal_xml': adrenal, 
          'Demog_xml': demographic, 
          'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/form_package_identifier#4617751v1.0/1': FDA, 
          'http://nci.nih.gov/xml/owl/cadsr#form_package/99999/1.0': HERF, 
          'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/form_package_identifier#2674812v4.0/1': NCI_Demographics, 
          'Adrenal_html': adrenal_html, 
          'Demog_html': demographic_html, 
          'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/form_package_identifier#4617751v1.0/1/html': FDA_html, 
          'http://nci.nih.gov/xml/owl/cadsr#form_package/99999/1.0/html': HERF_html, 
          'http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/form_package_identifier#2674812v4.0/1/html': NCI_Demographics_html};

def demo(request):
    return HttpResponse('NIH caDSR Web Services')

def wsdl(request):
    return HttpResponse('NIH caDSR WSDL')

def form_as_XML(request):
    formID = request.RetrieveFormRequest.workflow.formID
    valid_forms = forms.keys()
    
    if formID in valid_forms:
      form_xml = forms[formID]
      return SimpleXMLElement(form_xml)
    else:
      return SimpleXMLElement('<?xml version="1.0"?><error>There was an error delivering your request</error>')


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
