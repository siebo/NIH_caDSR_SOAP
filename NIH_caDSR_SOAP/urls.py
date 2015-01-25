from django.conf.urls import patterns, include, url
from django.contrib import admin
from caDSR_SOAP_agent import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^wsdl', 'caDSR_SOAP_agent.views.wsdl', name='wsdl'),
    
    url('^soap.wsdl', views.dispatcher_handler, name='soap'),
    
    url(r'^soap', 'caDSR_SOAP_agent.views.form_as_XML', name='form_as_XML'),
    
    url(r'^FormManager_RetrieveForm', 'caDSR_SOAP_agent.views.form_as_XML', name='form_as_XML'),
    
    url(r'^$', 'caDSR_SOAP_agent.views.demo', name='demo'),
    
    
)

