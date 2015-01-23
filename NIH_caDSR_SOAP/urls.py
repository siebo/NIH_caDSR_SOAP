from django.conf.urls import patterns, include, url
from django.contrib import admin
from caDSR_SOAP_agent import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NIH_caDSR_SOAP.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url('^soap/', 'caDSR_SOAP_agent.views.DjangoSoapService', name='DjangoSoapService'),
    
    url(r'^wsdl/', 'caDSR_SOAP_agent.views.wsdl', name='wsdl'),
    
    url('^soap.wsdl', views.dispatcher_handler, name='soap'),
    
    
    url(r'^$', 'caDSR_SOAP_agent.views.demo', name='demo'),
    
    
)

