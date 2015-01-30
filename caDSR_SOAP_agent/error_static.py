error_xml = """
"""



error_html = """<?xml version="1.0" encoding="UTF-8"?>

<!-- 
******************************************************************************
NAME:       Error_html_request.xml
PURPOSE:    error example
VERSION:    1.000.000

REVISIONS: 
Ver        Date            Author            Description
1.0        12/01/2014      Varsha Parekh	   Error Template Response	(Waiting for IHE based Standard Error Templates from Steve Moore, if exist)
1.1        12/11/2014      WS/SJ/VP/RM       InstanceID added, schema location moved
******************************************************************************/
-->

<!-- Generic Error Message Information -->
<RetrieveFormResponse 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../../Schemas/RFD.xsd"
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form">
   
  
   <form>
      <URL>
         <!--Requested URL Not Found -->        
      </URL>
      
      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID></instanceID>
      
   </form>
   
   <contentType>Unstructured</contentType>
   
   <!-- Form Filler can parse the responseCode and display the text to the screen -->
   <responseCode>Requested URL is not found: [insert URL here] </responseCode>
   
   
</RetrieveFormResponse>

"""