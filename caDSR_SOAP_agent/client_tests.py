from pysimplesoap.client import SoapClient

test_client = SoapClient(
    location = "http://localhost:8080/soap",
    action = "http://localhost:8080/soap",
    namespace = "http://nlm.nih.gov/sdc/form",
    soap_ns='soap', trace = False, ns = 'urn:ihe:iti:rfd:2007', exceptions=True)
    
# Load request XML from filesystem here
req_xml = 'xxx'

# For now, just dump the XML payload
response = test_client.soap(req_xml=req_xml)

print result

