from django.conf.urls import patterns, include, url
from django.contrib import admin
from caDSR_SOAP_agent import views

urlpatterns = patterns('',

    # Used for the Django admin panels.  Don't change
    url(r'^admin/', include(admin.site.urls)),
    
    # Static WSDL based on provided file
    # url(r'^wsdl', 'caDSR_SOAP_agent.views.wsdl', name='wsdl'),
    
    # Dynamically generated WSDL from PySimpleSOAP
    url('^soap.wsdl', views.dispatcher_handler, name='soap'),
    
    # These two views point to the same method.  If you need to provision 
    # the FormManager view on a new URL, uncomment the last link and change the XXXXX
    url(r'^soap', 'caDSR_SOAP_agent.views.form_as_XML', name='form_as_XML'),
    url(r'^FormManager_RetrieveForm', 'caDSR_SOAP_agent.views.form_as_XML', name='form_as_XML'),
    #url(r'^XXXXX', 'caDSR_SOAP_agent.views.form_as_XML', name='form_as_XML'),
    
    url(r'^$', 'caDSR_SOAP_agent.views.demo', name='demo'),
    
    
)

