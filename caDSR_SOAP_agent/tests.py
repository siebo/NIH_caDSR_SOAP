from caDSR_SOAP_agent.local_settings import server_url
from pysimplesoap.client import SoapClient

client = SoapClient(location=server_url,
                    namespace=server_url, trace=True)

headers = SimpleXMLElement(""""<?xml version="1.0" encoding="UTF-8"?>
<RetrieveFormRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../../../Schemas/RFD.xsd"
    xmlns="urn:ihe:iti:rfd:2007">

    <prepopData xsi:nil="true" />
    <workflowData> 
        <formID>Adrenal_xml</formID>
        <encodedResponse>true</encodedResponse>
        <archiveURL /> 
        <context xsi:nil="true"/> 

        <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
        <instanceID></instanceID>
    </workflowData> 
</RetrieveFormRequest>""")

client.FormManager_RetrieveForm(headers=headers)
