# -*- coding: utf-8 -*-

# # XXX fixme - In the provided files, adrenal had only a 'stub' for HTML.  Should be replaced with full file
adrenal_html = """
<?xml version="1.0" encoding="UTF-8"?>

<!-- 
******************************************************************************
RFD Retrieve Form Response (ITI-34) containing an HTML Response 

FORM NAME:  Adrenal_html_response_stub.xml
PURPOSE:    Response for an ADRENAL template using RFD (ITI-34) transaction.

REVISIONS: 
Ver        Date         Author              Description
1.0        12/01/2014   VP/RM               Added RFD wrapper and schema validation 
                                            Need to fix RFD schema to add <instanceID> for SDC          
1.1        12/11/2014  WS/SJ/VP/RM          InstanceID removed, schema location moved
******************************************************************************/
-->

<RetrieveFormResponse 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../../../Schemas/RFD.xsd" 
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form">

   <form>
      <Structured>
         <sdc:sdc_html_package>
            <sdc:supplemental_data>
               <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
            </sdc:supplemental_data>
            <sdc:form_info>
               <!-- Contains mapping, and administrative info; this is the same content as from the form design package -->
            </sdc:form_info>
            <sdc:sdc_html_form>
               <!-- USHIK will provide actual HTML content using automated transformation utility -->
            </sdc:sdc_html_form>
         </sdc:sdc_html_package>
      </Structured>
      
      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID/>
      
   </form>

   <contentType>HTML</contentType>
   
   <responseCode>Request succeeded</responseCode>
   <!-- Value is not required for the responseCode but will be useful  -->

</RetrieveFormResponse>
"""



demographic_html = """<?xml version="1.0" encoding="UTF-8"?>

<!-- 
******************************************************************************
RFD Retrieve Form Response (ITI-34) containing an HTML Response 

FORM NAME:     Demog_html_response.xml
PURPOSE:       Response for an Demographic template using RFD (ITI-34) transaction.

REVISIONS: 
Ver        Date         Author              Description
1.0        12/01/2014   VP/RM               Added RFD wrapper and schema validation 
                                            Need to fix RFD schema to add <instanceID> for SDC              

1.1        12/11/2014  WS/SJ/VP/RM          InstanceID removed, schema location moved
******************************************************************************/
-->

<RetrieveFormResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../../../Schemas/RFD.xsd" 
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form">

   <form>
      <Structured>
         <sdc:sdc_html_package>
            <sdc:supplemental_data>
               <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
            </sdc:supplemental_data>
            <sdc:form_info>
               <!-- Contains mapping, and administrative info; this is the same content as from the form design package -->
            </sdc:form_info>
            <sdc:sdc_html_form>
               <!-- USHIK will provide actual HTML content using automated transformation utility -->
            </sdc:sdc_html_form>
         </sdc:sdc_html_package>
      </Structured>
      
      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID/>
   </form>

   <contentType>HTML</contentType>

   <responseCode>Request succeeded</responseCode>
   <!-- Value is not required for the responseCode but will be useful  -->

</RetrieveFormResponse>
"""




FDA_html = """<?xml version="1.0" encoding="UTF-8"?>

<!-- 
******************************************************************************
RFD Retrieve Form Response (ITI-34) containing an HTML Response 

FORM NAME:      MedWatch 3500
PURPOSE:        Response for MedWatch 3500 form using RFD (ITI-34) transaction in SDC sample HTML format.

REVISIONS: 
Ver        Date         Author              Description
1.0        12/01/2014   VP/RM               Added RFD wrapper and schema validation 
                                            Need to fix RFD schema to add <instanceID> for SDC
1.1        12/03/2014   Denise Warzel       Populated the sdc_html_form section containing html content           
1.2        12/11/2014   DW/WS/SJ/VP/RM      InstanceID removed, schema location moved
******************************************************************************/
-->

<RetrieveFormResponse 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../../../Schemas/RFD.xsd" 
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form"
   xmlns:mfi13="http://www.iso.org/19763/13/2013"
   xmlns:dex="urn:ihe:qrph:dex:2013"
   xmlns:mfi6="http://www.iso.org/19763/6/2013"
   xmlns:mdr3="http://www.iso.org/11179/3/2013"
   >

   <!--Issue: We need an RFD element to specify the PackageID and formID , to help ensure the correct form response is included within this transaction-->
   <form>
       <Structured>
         <sdc:sdc_html_package>
            <sdc:supplemental_data>
               <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
                </sdc:supplemental_data>
            <sdc:form_info>
               <!-- Contains mapping, and administrative info; this is the same content as from the form design package -->
               <sdc:mapping_package
      mapping_package_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/mapping_package_identifier#4617751v1.0/1"
      form_design_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier#4617751v1.0">

      <sdc:mdr_mapping
         mdr_mapping_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/mdr_mapping_identifier#4617751v1.0/1">

         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#793v5.1</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619803v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#64799v3.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2003301v4.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619801v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2004152v3</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632824v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2004505v4</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626799v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179582v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179608v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179613v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619828v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179615v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179660v2</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626771v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179689v4</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619807v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2182728v2</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2182850v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619829v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2184687v2</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632819v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2188132v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632827v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192888v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632991v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192895v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626860v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192897v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626795v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192901v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192901v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626797v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2003746v6.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640053v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192987v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633056v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192991v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626803v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192999v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626801v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2196242v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626793v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2200604v3</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619804v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2433964v2</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633591v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2479726v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633042v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2540498v4</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2597216v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2748048v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633041v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2748053v2</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626915v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2998028v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3028750v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3101068v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3175751v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3631708v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3631708v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633040v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3761048v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633024v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4384931v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385191v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385738v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626859v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385747v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626914v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385754v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626858v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385757v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4461362v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4631994v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632832v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4632014v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632835v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4632039v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4632073v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632839v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4633453v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4633472v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2006128v2.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise1v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2201323v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise2v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385855v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise3v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385911v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise4v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385912v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385931v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise6v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385953v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise7v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385951v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise8v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179642v2.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise9v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385976v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise10v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4386110v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise11v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
         <sdc:question_element_data_element_association>
            <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4384931v1.0</mfi13:data_element_scoped_identifier>
            <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >related</mfi13:association_type>
            <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013"
               >http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise12v1.0</mfi13:question_element_identifier>
         </sdc:question_element_data_element_association>
      </sdc:mdr_mapping>
   </sdc:mapping_package>
               <sdc:administrative_package>
                  <sdc:submission_rule/>
                  <sdc:compliance_rule/>
                  <sdc:originating_registry_summary>
                     <mfi6:registry_organization xmlns:mfi6="http://www.iso.org/19763/6/2013">
                        <mdr3:name xmlns:mdr3="http://www.iso.org/11179/3/2013">NCI</mdr3:name>
                        <mdr3:uri xmlns:mdr3="http://www.iso.org/11179/3/2013"
                           >2.16.840.1.113883.3.26.2</mdr3:uri>
                     </mfi6:registry_organization>
                     <mfi6:reference_standard_identifier xmlns:mfi6="http://www.iso.org/19763/6/2013">ISO/IEC
                        19763-13 Form_Design</mfi6:reference_standard_identifier>
                     <mfi6:SLA_for_registry xmlns:mfi6="http://www.iso.org/19763/6/2013"/>
                     <mfi6:purpose_for_registry xmlns:mfi6="http://www.iso.org/19763/6/2013">
                        <mdr3:title xmlns:mdr3="http://www.iso.org/11179/3/2013">CDEs and Forms for Cancer
                           Clinical Trials</mdr3:title>
                     </mfi6:purpose_for_registry>
                     <mfi6:manual_for_registry xmlns:mfi6="http://www.iso.org/19763/6/2013">
                        <mdr3:title xmlns:mdr3="http://www.iso.org/11179/3/2013"
                           >https://wiki.nci.nih.gov/x/Q4EI</mdr3:title>
                     </mfi6:manual_for_registry>
                     <mfi6:specification_for_interface xmlns:mfi6="http://www.iso.org/19763/6/2013">
                        <mfi6:name>caDSR API</mfi6:name>
                        <mfi6:description>caDSR API Domain Class Browser</mfi6:description>
                        <mfi6:URL>http://cadsrapi.nci.nih.gov</mfi6:URL>
                        <mfi6:version>4.0</mfi6:version>
                     </mfi6:specification_for_interface>
                  </sdc:originating_registry_summary>
                  <sdc:form_language>
                     <mfi13:style_language xmlns:mfi13="http://www.iso.org/19763/13/2013"/>
                     <mfi13:logic_language xmlns:mfi13="http://www.iso.org/19763/13/2013"/>
                     <mfi13:format_language xmlns:mfi13="http://www.iso.org/19763/13/2013"/>
                     <sdc:textual_language>eng</sdc:textual_language>
                  </sdc:form_language>
                  <sdc:contacts/>
                  <sdc:registration>
                     <sdc:state>
                        <mdr3:registration_status xmlns:mdr3="http://www.iso.org/11179/3/2013"
                           >STANDARD</mdr3:registration_status>
                        <mdr3:effective_date xmlns:mdr3="http://www.iso.org/11179/3/2013"
                           >2014-12-09T00:07:20.0</mdr3:effective_date>
                        <mdr3:until_date xmlns:mdr3="http://www.iso.org/11179/3/2013"/>
                        <mdr3:administrative_note xmlns:mdr3="http://www.iso.org/11179/3/2013"/>
                        <mdr3:administrative_status xmlns:mdr3="http://www.iso.org/11179/3/2013">DRAFT
                           NEW</mdr3:administrative_status>
                     </sdc:state>
                     <sdc:stewardship_record>
                        <sdc:organization>
                           <sdc:name>National Cancer Institute (NCI)</sdc:name>
                           <sdc:fhir_mail_address>
                              <sdc:line>BG 9609 MSC 9760</sdc:line>
                              <sdc:line>9609 Medical Center Drive</sdc:line>
                              <sdc:city>Bethesda</sdc:city>
                              <sdc:state>MD</sdc:state>
                              <sdc:zip>20892-97609609</sdc:zip>
                              <sdc:country>USA</sdc:country>
                           </sdc:fhir_mail_address>
                        </sdc:organization>
                     </sdc:stewardship_record>
                     <sdc:creation_date>12-02-2014</sdc:creation_date>
                     <sdc:explanatory_comment/>
                  </sdc:registration>
               </sdc:administrative_package>
               <sdc:stylesheet/>
            
            </sdc:form_info>
             <sdc:sdc_html_form><![CDATA[
                <html>
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <title>MedWatch</title><style>
                    body {
                        color:          #333;
                        font-family:    "Helvetica Neue, Helvetica, Arial, sans-serif";
                        font-size:      14px;
                        line-height:   1.42857;
                    }
                    .panel-section {
                        margin:     3px;
                        padding:    0px;
                        border-radius:  4px;
                        border:   1px solid black;
                    }
                    .panel-question {
                        padding:    2px 0 2px 5px;
                        margin:     5px;
                        border:     1px solid #428bca;
                        border-radius:  4px;
                    
                    }
                    .form-header-instruction{
                        font-size:18px;
                    }
                    .section-header{
                        margin:0;
                        padding:5px 0 5px 5px;
                        border-radius:4px 4px 0 0;
                        background-color:#d4d8d1;
                    }
                    .form-cdeId{
                        font-size:12px;
                    }
                    .guarded-element-question{
                        text-indent:60px;
                        }
                    h4{
                        margin:2px 0 2px 0;
                    }</style></head>
   <body id="form">
      <form method="post" action="">
         <div id="form-heading-section">
            <h1 style="padding: 0 5px 0 5px"><span class="text-center"><strong>MedWatch</strong></span><br></h1>
         </div>
         <p style="padding: 0 5px 0 5px">
            For VOLUNTARY reporting of
            adverse events, product problems and product use errors.
            
         </p>
         <p class="form-header-instruction" style="padding: 0 5px 0 5px">
            U.S. Department of Health
            and Human Services - The FDA Safety Information and Adverse Event Reporting Program
            -
            Form Approved: OMB No. 0910-0291, Expires: 6/30/2015. See PRA
            Statement.
            
         </p>
         <div class="form-section panel-section">
            <h2 class="section-header"> FDA USE ONLY</h2>
            <p style="margin-left: 3px"></p>
         </div>
         <div class="form-section panel-section">
            <h2 class="section-header"> A. PATIENT
               INFORMATION
            </h2>
            <p style="margin-left: 3px"></p>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619801v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Patient
                  Identifier</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619801v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619801v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2003301v4.0</p></span><span style="margin-left: 1px">
                  <p>In
                     Confidence
                  </p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633591v1.0" class="question-prompt" style="display: block; font-weight: bold;">2. Age at Time of
                  Event</label><p style="margin: 0;">
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633591v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633591v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2433964v2</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619803v1.0" class="question-prompt" style="display: block; font-weight: bold;">or Date of
                  Birth</label><p style="margin: 0;">
                  
                  
               </p> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619803v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619803v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:793v5.1</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">3. Sex</h4>
               <p style="margin: 0;">
                  
                  
               </p>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619804v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2575551/1.0" value="Female">Female Gender</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619804v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2575550/1.0" value="Male">Male Gender</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2200604v3</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632819v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Weight (lb)</label><p style="margin: 0;">
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632819v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632819v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2184687v2</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619807v1.0" class="question-prompt" style="display: block; font-weight: bold;">or Weight (kg)</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619807v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619807v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2179689v4</p></span></div>
         </div>
         <div class="form-section panel-section">
            <h2 class="section-header"> B. ADVERSE EVENT, PRODUCT
               PROBLEM, OR ERROR
            </h2>
            <p style="margin-left: 3px"></p>
            <div class="panel-question">
               <h4 class="question-prompt">1. Check all that apply
                  (Report Type)
               </h4>
               <p style="margin: 0;">
                  
                  
               </p>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2570073/1.0" value="Adverse&#xA;                     Event">Adverse Event</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461360/1.0" value="Product Use&#xA;                     Error">Product Use Error</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461358/1.0" value="Product&#xA;                     Problem">Product Problem</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461356/1.0" value="Problem with Different&#xA;                     Manufacturer of Same Medicine">Problem with Different Manufacturer of Same Medicine</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:4461362v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">2. Outcomes Attributed to
                  Adverse Event
               </h4>
               <p style="margin: 0;">
                  
                  
               </p>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2992998/1.0" value="Death">Death</label><div class="guarded-element-question"><b> Date of
                           Death</b>
                        
                         (DD/MON/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632824v1.0" size="30"><span class="form-cdeId">
                           <p>CDE NCI:2004152v3</p></span></div>
                  </li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579210/1.0" value="Life&#xA;                     Threatening">Life Threatening</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2992999/1.0" value="Hospitalization">Hospitalization - initial or Prolonged</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993002/1.0" value="Required&#xA;                     Intervention">Required Intervention to Prevent Permanent Imapirment/Damage
                        (Devices)</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3003755/1.0" value="Disability">Disability or Permanent Damage</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993000/1.0" value="Congenital&#xA;                     Abnormality">Congenital Abnormality/Birth Defect</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993001/1.0" value="Other&#xA;                     Serious">Other Serious (Important Medical Events)</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2998028v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619828v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Date of
                  Event</label> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619828v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619828v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2179613v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619829v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Date of this
                  Report</label> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619829v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619829v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2182850v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632827v1.0" class="question-prompt" style="display: block; font-weight: bold;">5. Describe event, Problem
                  or Product Use Error</label><p style="margin: 0;">
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632827v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632827v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2188132v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640053v1.0" class="question-prompt" style="display: block; font-weight: bold;">6. Relevant Tests/Laboratory
                  Data, Including Dates</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640053v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640053v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2003746v6.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626771v1.0" class="question-prompt" style="display: block; font-weight: bold;">7. Other Relevant History,
                  Including Preexisting Medical Conditions</label><p style="margin: 0;">
                  (e.g. allergies, race,
                  pregnancy, smoking and alcohol use, liver/kidney problems, etc.) 
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626771v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626771v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2179660v2</p></span></div>
         </div>
         <div class="form-section panel-section">
            <h2 class="section-header"> C. PRODUCT
               AVAILABILITY
            </h2>
            <p style="margin-left: 3px"></p>
            <div class="panel-question">
               <h4 class="question-prompt">1. Product Available for
                  Evaluation?
               </h4>
               <p style="margin: 0;">
                  Do not send product to
                  FDA
                  
               </p>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632832v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" value="Yes">Yes</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632832v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" value="No">No</label><div class="guarded-element-question"><b> Returned
                           to Manufacturer on: (mm/dd/yyyy)</b> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632835v1.0" size="30"><span class="form-cdeId">
                           <p>CDE NCI:4632014v1.0</p></span></div>
                  </li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:4631994v1.0</p></span></div>
         </div>
         <div class="form-section panel-section">
            <h2 class="section-header"> D. SUSPECT
               PRODUCT(S)
            </h2>
            <p style="margin-left: 3px"></p>Repeat 2 times Response # 1
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Name</label><p style="margin: 0;">
                  (from product label)
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4632039v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Strength</label><p style="margin: 0;">
                  (from product label)
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3175751v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Manufacturer</label><p style="margin: 0;">
                  (from product label)
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3028750v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0" class="question-prompt" style="display: block; font-weight: bold;">2. Dose</label><p style="margin: 0;">
                  or Amount
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2182728v2</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt"> Dose Units</h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567635/1.0" value="%">Percent</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2732864/1.0" value="%">Percent Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569441/1.0" value="10^3">Thousand</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725086/1.0" value="10^5{Cells}/kg">Hundred Thousand Cells per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569409/1.0" value="10^6">Million</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569402/1.0" value="10^6eV">Million electron volt</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725088/1.0" value="10^6{Cells}/kg">Million Cells per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569408/1.0" value="10^6{pfu}">Million Plaque Forming Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569420/1.0" value="10^6{VP}">Million Viral Particles</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718641/1.0" value="10^7{Cells}/kg">Ten Million Cells per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725133/1.0" value="10^7{pfu}">Ten Million Plaque Forming Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725131/1.0" value="10^8{pfu}">Hundred Million Plaque Forming Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725073/1.0" value="10^9{Cells}/kg">Billion Cells per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725129/1.0" value="10^9{pfu}">Billion Plaque Forming Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569067/1.0" value="cGy">Centigray</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569376/1.0" value="Ci">Curie</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569378/1.0" value="dL">Deciliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725118/1.0" value="eq">Equivalent Weight</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567649/1.0" value="g">Gram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108593/1.0" value="g/d">Gram per Day</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725116/1.0" value="g/m2">Gram per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113233/1.0" value="g/wk">Gram per Week</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569066/1.0" value="Gy">Gray</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567650/1.0" value="h">Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569383/1.0" value="Hz">Hertz</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725075/1.0" value="J">Joule</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725109/1.0" value="J/cm2">Joule per Square Centimeter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725139/1.0" value="keV">Kiloelectronvolt</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581032/1.0" value="kg">KILOGRAM</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569389/1.0" value="kHz">Kilohertz</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569390/1.0" value="kPa">Kilopascal</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569391/1.0" value="kU">Kilounit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" value="kU/kg">Kilounit per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718864/1.0" value="kU/L">Kilounit per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569393/1.0" value="L">Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718880/1.0" value="L/min">Liter per Minute</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569397/1.0" value="mCi">Millicurie</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569399/1.0" value="meq">Milliequivalent</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719062/1.0" value="meq/24.h">Milliequivalent per 24 Hours</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719060/1.0" value="meq/dL">Milliequivalent per Deciliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725052/1.0" value="meq/h">Milliequivalent per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719056/1.0" value="meq/L">Milliequivalent per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569666/1.0" value="mg">Milligram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719054/1.0" value="mg/24.h">Milligram per 24 Hours</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719052/1.0" value="mg/dL">Milligram per Deciliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725048/1.0" value="mg/h">Milligram per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719050/1.0" value="mg/kg">Milligram per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108591/1.0" value="mg/kg/d">Milligram per Kilogram per Day</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725141/1.0" value="mg/m2">Milligram per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059688/1.0" value="mg/m2/24.h">Milligram per Square Meter per Day</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725076/1.0" value="mg/m2/h">Milligram per Square Meter per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059686/1.0" value="mg/m2/wk">Milligram per Square Meter per Week</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2685297/1.0" value="mg/mL">Kilogram per Cubic Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725107/1.0" value="mg/wk">Milligram per Week</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2573853/1.0" value="mg/{inhalation}">Milligram per Inhalation</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569407/1.0" value="MHz">Megahertz</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567660/1.0" value="min">Minute</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567406/1.0" value="mL">Milliliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725105/1.0" value="mL/h">Milliliter per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725151/1.0" value="mL/kg">Milliliter per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569413/1.0" value="mmol">Millimole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581580/1.0" value="mol">Mole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569415/1.0" value="mosm">Milliosmole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569410/1.0" value="mU">Milliunit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725171/1.0" value="MU">Million Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569419/1.0" value="mV">Millivolt</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719451/1.0" value="m[iU]">Milliinternational Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719449/1.0" value="m[iU]/m2">Milliinternational Unit per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569416/1.0" value="M[RAD]">Megarad</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569421/1.0" value="nCi">Nanocurie</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2672537/1.0" value="ng">Nanogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725165/1.0" value="ng/kg">Nanogram per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724560/1.0" value="ng/L">Nanogram per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719066/1.0" value="ng/mL">Microgram per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569427/1.0" value="nmol">Nanomole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569425/1.0" value="nm{light}">Nanometer</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725163/1.0" value="osm">Osmole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569430/1.0" value="Pa">Pascal</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567618/1.0" value="pg">Picogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577221/1.0" value="s">Second</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725127/1.0" value="u">Micro</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" value="U/g">Kilounit per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725175/1.0" value="U/kg">Unit per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725031/1.0" value="U/m2">Unit per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725147/1.0" value="uCi">Microcurie</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569394/1.0" value="ug">Microgram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725145/1.0" value="ug/cm2">Microgram per Square Centimeter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725050/1.0" value="ug/h">Microgram per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725144/1.0" value="ug/kg">Microgram per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059690/1.0" value="ug/kg/24.h">Microgram per Kilogram per Day</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113232/1.0" value="ug/kg/wk">Microgram per Kilogram per Week</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725082/1.0" value="ug/m2">Microgram per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108589/1.0" value="ug/m2/h">Microgram per Square Meter per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567626/1.0" value="uL">Microliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567136/1.0" value="umol">Micromole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719300/1.0" value="u[IU]/mL">Microinternational Unit per Milliliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725120/1.0" value="[drp]">Metric Drop</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725055/1.0" value="[gal_us]">Gallon US</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718872/1.0" value="[iU]">International Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725111/1.0" value="[iU]/kg">International Unit per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718870/1.0" value="[iU]/L">International Unit per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725078/1.0" value="[iU]/mg">International Unit per Milligram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725094/1.0" value="[iU]/mg{alpha-Tocopherol}">International Unit per Milligram of Alpha-Tocopherol</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725096/1.0" value="[iU]{Vitamin&#xA;                     A}">International Unit of Vitamin A</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569429/1.0" value="[oz_av]">Ounce</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725155/1.0" value="[psi]">Pound per Square Inch</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615202/1.0" value="[RAD]">Rad</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725185/1.0" value="[tbs_us]">Tablespoon Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725181/1.0" value="[tsp_us]">Teaspoon Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569373/1.0" value="{Application}">Application</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725089/1.0" value="{AUC}">Area under Curve</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725084/1.0" value="{Bottle}">Bottle Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725126/1.0" value="{Caplet}">Caplet Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725124/1.0" value="{Capsule}">Capsule Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615470/1.0" value="{Cells}">Cell</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569377/1.0" value="{Course}">Course</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2576428/1.0" value="{Course}">Cycle</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569379/1.0" value="{Dose}">Dose</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725113/1.0" value="{Inhalation}">Inhalation Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725091/1.0" value="{IV Bag}">Intravenous Bag Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725134/1.0" value="{Measure}">Measurement</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724564/1.0" value="{No&#xA;                     Scre}">Data Not Available</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725160/1.0" value="{packet}">Packet Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725103/1.0" value="{Patch}">Patch Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725157/1.0" value="{pfu}">Plaque Forming Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725153/1.0" value="{puff}">Puff Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725098/1.0" value="{RAE}">Retinol Activity Equivalent</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725100/1.0" value="{RE}">Retinol Equivalent</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725057/1.0" value="{Seed}">Radioactive Seed Implant Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2571186/1.0" value="{Session}">Session</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725189/1.0" value="{Spray}">Spray Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725187/1.0" value="{Suppository}">Suppository Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725183/1.0" value="{tbl}">Tablet Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725179/1.0" value="{TCID50}">Tissue Culture Infection Dose 50</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725177/1.0" value="{Troche}">Troche Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567622/1.0" value="{Unit}">Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565695/1.0" value="{Unknown}">Unknown</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725173/1.0" value="{VP}">Viral Particle Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579163/1.0" value="{Wafer}">Wafer Dosage Form</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2874130/1.0" value="{YU}">Yeast Units</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:3028750v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Frequency</label><p style="margin: 0;">
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2540498v4</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt"> Route</h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567786/1.0" value="Infusion">Infusion</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567787/1.0" value="Inhaled">Inhaled</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567783/1.0" value="Intradermal">Intradermal</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567788/1.0" value="Intramuscular">Intramuscular</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567785/1.0" value="Orally">Orally</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567790/1.0" value="Other">Other</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565646/1.0" value="Rectal">Rectal</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567789/1.0" value="Subcutaneous">Subcutaneous</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567782/1.0" value="Topical">Topical</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567784/1.0" value="Transdermal">Transdermal</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2179582v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Dates of Use
                  From:</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4633453v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Dates of Use
                  To:</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4633472v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0" class="question-prompt" style="display: block; font-weight: bold;"> (if unknown dates, give
                  duration in minutes)</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:64799v3.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Diagnosis or Reason for
                  Use (Indication)</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2597216v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">5. Event Abated After Use
                  Stopped or Dose Reduced?
               </h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" value="Yes">Yes</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" value="No">No</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" value="Doesn't&#xA;                     Apply">Doesn't Apply</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2179608v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0" class="question-prompt" style="display: block; font-weight: bold;">6. Lot #</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3631708v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0" class="question-prompt" style="display: block; font-weight: bold;">7. Expiration
                  Date</label> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2192901v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">8. Event Reappeared After
                  Reintroduction?
               </h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" value="Yes">Yes</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" value="No">No</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" value="Doesn't&#xA;                     Apply">Doesn't Apply</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2179615v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0" class="question-prompt" style="display: block; font-weight: bold;">9. NDC #</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3101068v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0" class="question-prompt" style="display: block; font-weight: bold;">OR  Unique ID</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4384931v1.0</p></span></div>Response # 2
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Name</label><p style="margin: 0;">
                  (from product label)
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4632039v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Strength</label><p style="margin: 0;">
                  (from product label)
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3175751v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Manufacturer</label><p style="margin: 0;">
                  (from product label)
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3028750v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0" class="question-prompt" style="display: block; font-weight: bold;">2. Dose</label><p style="margin: 0;">
                  or Amount
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2182728v2</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt"> Dose Units</h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567635/1.0" value="%">Percent</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2732864/1.0" value="%">Percent Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569441/1.0" value="10^3">Thousand</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725086/1.0" value="10^5{Cells}/kg">Hundred Thousand Cells per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569409/1.0" value="10^6">Million</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569402/1.0" value="10^6eV">Million electron volt</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725088/1.0" value="10^6{Cells}/kg">Million Cells per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569408/1.0" value="10^6{pfu}">Million Plaque Forming Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569420/1.0" value="10^6{VP}">Million Viral Particles</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718641/1.0" value="10^7{Cells}/kg">Ten Million Cells per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725133/1.0" value="10^7{pfu}">Ten Million Plaque Forming Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725131/1.0" value="10^8{pfu}">Hundred Million Plaque Forming Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725073/1.0" value="10^9{Cells}/kg">Billion Cells per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725129/1.0" value="10^9{pfu}">Billion Plaque Forming Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569067/1.0" value="cGy">Centigray</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569376/1.0" value="Ci">Curie</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569378/1.0" value="dL">Deciliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725118/1.0" value="eq">Equivalent Weight</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567649/1.0" value="g">Gram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108593/1.0" value="g/d">Gram per Day</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725116/1.0" value="g/m2">Gram per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113233/1.0" value="g/wk">Gram per Week</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569066/1.0" value="Gy">Gray</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567650/1.0" value="h">Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569383/1.0" value="Hz">Hertz</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725075/1.0" value="J">Joule</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725109/1.0" value="J/cm2">Joule per Square Centimeter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725139/1.0" value="keV">Kiloelectronvolt</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581032/1.0" value="kg">KILOGRAM</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569389/1.0" value="kHz">Kilohertz</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569390/1.0" value="kPa">Kilopascal</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569391/1.0" value="kU">Kilounit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" value="kU/kg">Kilounit per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718864/1.0" value="kU/L">Kilounit per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569393/1.0" value="L">Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718880/1.0" value="L/min">Liter per Minute</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569397/1.0" value="mCi">Millicurie</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569399/1.0" value="meq">Milliequivalent</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719062/1.0" value="meq/24.h">Milliequivalent per 24 Hours</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719060/1.0" value="meq/dL">Milliequivalent per Deciliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725052/1.0" value="meq/h">Milliequivalent per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719056/1.0" value="meq/L">Milliequivalent per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569666/1.0" value="mg">Milligram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719054/1.0" value="mg/24.h">Milligram per 24 Hours</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719052/1.0" value="mg/dL">Milligram per Deciliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725048/1.0" value="mg/h">Milligram per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719050/1.0" value="mg/kg">Milligram per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108591/1.0" value="mg/kg/d">Milligram per Kilogram per Day</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725141/1.0" value="mg/m2">Milligram per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059688/1.0" value="mg/m2/24.h">Milligram per Square Meter per Day</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725076/1.0" value="mg/m2/h">Milligram per Square Meter per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059686/1.0" value="mg/m2/wk">Milligram per Square Meter per Week</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2685297/1.0" value="mg/mL">Kilogram per Cubic Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725107/1.0" value="mg/wk">Milligram per Week</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2573853/1.0" value="mg/{inhalation}">Milligram per Inhalation</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569407/1.0" value="MHz">Megahertz</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567660/1.0" value="min">Minute</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567406/1.0" value="mL">Milliliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725105/1.0" value="mL/h">Milliliter per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725151/1.0" value="mL/kg">Milliliter per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569413/1.0" value="mmol">Millimole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581580/1.0" value="mol">Mole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569415/1.0" value="mosm">Milliosmole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569410/1.0" value="mU">Milliunit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725171/1.0" value="MU">Million Units</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569419/1.0" value="mV">Millivolt</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719451/1.0" value="m[iU]">Milliinternational Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719449/1.0" value="m[iU]/m2">Milliinternational Unit per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569416/1.0" value="M[RAD]">Megarad</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569421/1.0" value="nCi">Nanocurie</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2672537/1.0" value="ng">Nanogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725165/1.0" value="ng/kg">Nanogram per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724560/1.0" value="ng/L">Nanogram per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719066/1.0" value="ng/mL">Microgram per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569427/1.0" value="nmol">Nanomole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569425/1.0" value="nm{light}">Nanometer</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725163/1.0" value="osm">Osmole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569430/1.0" value="Pa">Pascal</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567618/1.0" value="pg">Picogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577221/1.0" value="s">Second</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725127/1.0" value="u">Micro</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" value="U/g">Kilounit per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725175/1.0" value="U/kg">Unit per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725031/1.0" value="U/m2">Unit per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725147/1.0" value="uCi">Microcurie</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569394/1.0" value="ug">Microgram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725145/1.0" value="ug/cm2">Microgram per Square Centimeter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725050/1.0" value="ug/h">Microgram per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725144/1.0" value="ug/kg">Microgram per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059690/1.0" value="ug/kg/24.h">Microgram per Kilogram per Day</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113232/1.0" value="ug/kg/wk">Microgram per Kilogram per Week</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725082/1.0" value="ug/m2">Microgram per Square Meter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108589/1.0" value="ug/m2/h">Microgram per Square Meter per Hour</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567626/1.0" value="uL">Microliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567136/1.0" value="umol">Micromole</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719300/1.0" value="u[IU]/mL">Microinternational Unit per Milliliter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725120/1.0" value="[drp]">Metric Drop</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725055/1.0" value="[gal_us]">Gallon US</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718872/1.0" value="[iU]">International Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725111/1.0" value="[iU]/kg">International Unit per Kilogram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718870/1.0" value="[iU]/L">International Unit per Liter</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725078/1.0" value="[iU]/mg">International Unit per Milligram</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725094/1.0" value="[iU]/mg{alpha-Tocopherol}">International Unit per Milligram of Alpha-Tocopherol</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725096/1.0" value="[iU]{Vitamin&#xA;                     A}">International Unit of Vitamin A</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569429/1.0" value="[oz_av]">Ounce</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725155/1.0" value="[psi]">Pound per Square Inch</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615202/1.0" value="[RAD]">Rad</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725185/1.0" value="[tbs_us]">Tablespoon Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725181/1.0" value="[tsp_us]">Teaspoon Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569373/1.0" value="{Application}">Application</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725089/1.0" value="{AUC}">Area under Curve</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725084/1.0" value="{Bottle}">Bottle Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725126/1.0" value="{Caplet}">Caplet Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725124/1.0" value="{Capsule}">Capsule Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615470/1.0" value="{Cells}">Cell</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569377/1.0" value="{Course}">Course</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2576428/1.0" value="{Course}">Cycle</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569379/1.0" value="{Dose}">Dose</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725113/1.0" value="{Inhalation}">Inhalation Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725091/1.0" value="{IV Bag}">Intravenous Bag Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725134/1.0" value="{Measure}">Measurement</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724564/1.0" value="{No&#xA;                     Scre}">Data Not Available</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725160/1.0" value="{packet}">Packet Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725103/1.0" value="{Patch}">Patch Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725157/1.0" value="{pfu}">Plaque Forming Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725153/1.0" value="{puff}">Puff Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725098/1.0" value="{RAE}">Retinol Activity Equivalent</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725100/1.0" value="{RE}">Retinol Equivalent</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725057/1.0" value="{Seed}">Radioactive Seed Implant Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2571186/1.0" value="{Session}">Session</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725189/1.0" value="{Spray}">Spray Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725187/1.0" value="{Suppository}">Suppository Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725183/1.0" value="{tbl}">Tablet Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725179/1.0" value="{TCID50}">Tissue Culture Infection Dose 50</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725177/1.0" value="{Troche}">Troche Dosing Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567622/1.0" value="{Unit}">Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565695/1.0" value="{Unknown}">Unknown</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725173/1.0" value="{VP}">Viral Particle Unit</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579163/1.0" value="{Wafer}">Wafer Dosage Form</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2874130/1.0" value="{YU}">Yeast Units</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:3028750v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Frequency</label><p style="margin: 0;">
                  
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2540498v4</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt"> Route</h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567786/1.0" value="Infusion">Infusion</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567787/1.0" value="Inhaled">Inhaled</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567783/1.0" value="Intradermal">Intradermal</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567788/1.0" value="Intramuscular">Intramuscular</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567785/1.0" value="Orally">Orally</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567790/1.0" value="Other">Other</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565646/1.0" value="Rectal">Rectal</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567789/1.0" value="Subcutaneous">Subcutaneous</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567782/1.0" value="Topical">Topical</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567784/1.0" value="Transdermal">Transdermal</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2179582v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Dates of Use
                  From:</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4633453v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Dates of Use
                  To:</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4633472v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0" class="question-prompt" style="display: block; font-weight: bold;"> (if unknown dates, give
                  duration in minutes)</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:64799v3.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Diagnosis or Reason for
                  Use (Indication)</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2597216v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">5. Event Abated After Use
                  Stopped or Dose Reduced?
               </h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" value="Yes">Yes</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" value="No">No</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" value="Doesn't&#xA;                     Apply">Doesn't Apply</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2179608v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0" class="question-prompt" style="display: block; font-weight: bold;">6. Lot #</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3631708v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0" class="question-prompt" style="display: block; font-weight: bold;">7. Expiration
                  Date</label> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2192901v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">8. Event Reappeared After
                  Reintroduction?
               </h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" value="Yes">Yes</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" value="No">No</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" value="Doesn't&#xA;                     Apply">Doesn't Apply</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2179615v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0" class="question-prompt" style="display: block; font-weight: bold;">9. NDC #</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3101068v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0" class="question-prompt" style="display: block; font-weight: bold;">OR  Unique ID</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4384931v1.0</p></span></div><br><br></div>
         <div class="form-section panel-section">
            <h2 class="section-header"> E. SUSPECT MEDICAL
               DEVICE
            </h2>
            <p style="margin-left: 3px"></p>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632991v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Brand name</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632991v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632991v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2192888v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633041v1.0" class="question-prompt" style="display: block; font-weight: bold;">2. Common Device
                  Name</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633041v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633041v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2748048v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633024v1.0" class="question-prompt" style="display: block; font-weight: bold;">2b. Procode</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633024v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633024v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3761048v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633042v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Manufacturer
                  Name</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633042v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633042v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2479726v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626915v1.0" class="question-prompt" style="display: block; font-weight: bold;"> City</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626915v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626915v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2748053v2</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt"> State</h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" value="AK">Alaska</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" value="AL">Alabama</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" value="AR">Arkansas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" value="AZ">Arizona</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" value="CA">California</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" value="CO">Colorado</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" value="CT">Connecticut</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" value="DC">District of Columbia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" value="DE">Delaware</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" value="FL">Florida</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" value="GA">Georgia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" value="HI">Hawaii</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" value="IA">Iowa</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" value="ID">Idaho</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" value="IL">Illinois</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" value="IN">Indiana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" value="KS">Kansas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" value="KY">Kentucky</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" value="LA">Louisiana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" value="MA">Massachusetts</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" value="MD">Maryland</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" value="ME">Maine</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" value="MI">Michigan</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" value="MN">Minnesota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" value="MO">Missouri</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" value="MS">Mississippi</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" value="MT">Montana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" value="NC">North Carolina</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" value="ND">North Dakota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" value="NE">Nebraska</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" value="NH">New Hampshire</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" value="NJ">New Jersey</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" value="NM">New Mexico</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" value="NV">Nevada</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" value="NY">New York</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" value="OH">Ohio</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" value="OK">Oklahoma</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" value="OR">Oregon</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" value="PA">Pennsylvania</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" value="RI">Rhode Island</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" value="SC">South Carolina</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" value="SD">South Dakota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" value="TN">Tennessee</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" value="TX">Texas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" value="UT">Utah</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" value="VA">Virginia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" value="VT">Vermont</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" value="WA">Washington</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" value="WI">Wisconsin</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" value="WV">West Virginia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" value="WY">Wyoming</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:4385191v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626860v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Model #</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626860v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626860v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2192895v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633040v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Lot #</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633040v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633040v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:3631708v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626795v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Catalog #</label><p style="margin: 0;">
                  Please type the catalog
                  number of the suspected medical device here. 
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626795v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626795v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2192897v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626797v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Expiration
                  Date</label><p style="margin: 0;">
                  Please type the
                  expiration date of the suspected medical device here in 2 digit month / 2 digit
                  day / 4 digit year here. 
                  
               </p> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626797v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626797v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2192901v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626793v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Serial #</label><p style="margin: 0;">
                  Please type the serial
                  number of the suspected medical device here. 
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626793v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626793v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2196242v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise12v1.0" class="question-prompt" style="display: block; font-weight: bold;">OR  Unique ID</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise12v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise12v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4384931v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626799v1.0" class="question-prompt" style="display: block; font-weight: bold;">6. If Implanted, Give
                  Date</label> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626799v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626799v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2004505v4</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633056v1.0" class="question-prompt" style="display: block; font-weight: bold;">7. If explanted, give
                  date</label> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633056v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633056v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2192987v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">8. Is this a single-use
                  device that was reprocessed and reused on a patient?
               </h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626803v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" value="No">No</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626803v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" value="Yes">Yes</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2192991v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626801v1.0" class="question-prompt" style="display: block; font-weight: bold;">9. Name of
                  reprocessor</label><p style="margin: 0;">
                  If Yes to Item No. 8,
                  Enter Name of the reprocessor here. 
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626801v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626801v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2192999v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626859v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Address</label><p style="margin: 0;">
                  If Yes to Item No. 8,
                  Enter Street Address of the reprocessor here 
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626859v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626859v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385738v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626914v1.0" class="question-prompt" style="display: block; font-weight: bold;"> City</label><p style="margin: 0;">
                  If Yes to Item No. 8,
                  Enter City of the reprocessor here 
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626914v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626914v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385747v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt"> State</h4>
               <p style="margin: 0;">
                  If Yes to Item No. 8,
                  Enter State of the reprocessor here 
                  
               </p>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" value="AK">Alaska</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" value="AL">Alabama</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" value="AR">Arkansas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" value="AZ">Arizona</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" value="CA">California</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" value="CO">Colorado</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" value="CT">Connecticut</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" value="DC">District of Columbia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" value="DE">Delaware</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" value="FL">Florida</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" value="GA">Georgia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" value="HI">Hawaii</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" value="IA">Iowa</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" value="ID">Idaho</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" value="IL">Illinois</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" value="IN">Indiana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" value="KS">Kansas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" value="KY">Kentucky</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" value="LA">Louisiana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" value="MA">Massachusetts</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" value="MD">Maryland</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" value="ME">Maine</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" value="MI">Michigan</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" value="MN">Minnesota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" value="MO">Missouri</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" value="MS">Mississippi</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" value="MT">Montana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" value="NC">North Carolina</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" value="ND">North Dakota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" value="NE">Nebraska</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" value="NH">New Hampshire</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" value="NJ">New Jersey</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" value="NM">New Mexico</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" value="NV">Nevada</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" value="NY">New York</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" value="OH">Ohio</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" value="OK">Oklahoma</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" value="OR">Oregon</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" value="PA">Pennsylvania</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" value="RI">Rhode Island</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" value="SC">South Carolina</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" value="SD">South Dakota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" value="TN">Tennessee</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" value="TX">Texas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" value="UT">Utah</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" value="VA">Virginia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" value="VT">Vermont</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" value="WA">Washington</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" value="WI">Wisconsin</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" value="WV">West Virginia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" value="WY">Wyoming</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:4385757v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626858v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Reprocessor Zip
                  Code</label><p style="margin: 0;">
                  If Yes to Item No. 8,
                  Enter Zipcode of the reprocessor here 
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626858v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626858v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385754v1.0</p></span></div>
         </div>
         <div class="form-section panel-section">
            <h2 class="section-header"> F. OTHER (CONCOMITANT)
               MEDICAL PRODUCTS
            </h2>
            <p style="margin-left: 3px"></p>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise1v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Product names and therapy
                  dates</label><p style="margin: 0;">
                  (exclude treatment of
                  event) 
                  
               </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise1v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise1v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2006128v2.0</p></span></div>
         </div>
         <div class="form-section panel-section">
            <h2 class="section-header"> G. REPORTER </h2>
            <p style="margin-left: 3px">(See confidentiality section
               on back)
            </p>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise2v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Name</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise2v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise2v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:2201323v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise3v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Address</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise3v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise3v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385855v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise4v1.0" class="question-prompt" style="display: block; font-weight: bold;"> City</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise4v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise4v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385911v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt"> State</h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" value="AK">Alaska</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" value="AL">Alabama</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" value="AR">Arkansas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" value="AZ">Arizona</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" value="CA">California</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" value="CO">Colorado</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" value="CT">Connecticut</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" value="DC">District of Columbia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" value="DE">Delaware</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" value="FL">Florida</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" value="GA">Georgia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" value="HI">Hawaii</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" value="IA">Iowa</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" value="ID">Idaho</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" value="IL">Illinois</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" value="IN">Indiana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" value="KS">Kansas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" value="KY">Kentucky</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" value="LA">Louisiana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" value="MA">Massachusetts</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" value="MD">Maryland</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" value="ME">Maine</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" value="MI">Michigan</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" value="MN">Minnesota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" value="MO">Missouri</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" value="MS">Mississippi</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" value="MT">Montana</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" value="NC">North Carolina</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" value="ND">North Dakota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" value="NE">Nebraska</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" value="NH">New Hampshire</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" value="NJ">New Jersey</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" value="NM">New Mexico</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" value="NV">Nevada</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" value="NY">New York</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" value="OH">Ohio</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" value="OK">Oklahoma</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" value="OR">Oregon</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" value="PA">Pennsylvania</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" value="RI">Rhode Island</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" value="SC">South Carolina</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" value="SD">South Dakota</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" value="TN">Tennessee</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" value="TX">Texas</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" value="UT">Utah</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" value="VA">Virginia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" value="VT">Vermont</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" value="WA">Washington</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" value="WI">Wisconsin</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" value="WV">West Virginia</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" value="WY">Wyoming</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:4385912v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise6v1.0" class="question-prompt" style="display: block; font-weight: bold;"> ZIP</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise6v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise6v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385931v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise7v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Phone #</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise7v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise7v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385953v1.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise8v1.0" class="question-prompt" style="display: block; font-weight: bold;"> E-mail</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise8v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise8v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385951v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">2. Health
                  Professional?
               </h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise9v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" value="Yes">Yes</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise9v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" value="No">No</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:2179642v2.0</p></span></div>
            <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise10v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Occupation</label><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise10v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise10v1.0" size="30"><span class="form-cdeId">
                  <p>CDE NCI:4385976v1.0</p></span></div>
            <div class="panel-question">
               <h4 class="question-prompt">4. Also Reported
                  to:
               </h4>
               <ul style="list-style-type: none; margin: 2px 0 0 0">
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise11v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386108/1.0" value="Manufacturer">Manufacturer</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise11v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386107/1.0" value="User&#xA;                     Facility">User Facility</label></li>
                  <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise11v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386105/1.0" value="Distributor/Importer">Distributor/Importer</label></li>
               </ul><span class="form-cdeId">
                  <p>CDE NCI:4386110v1.0</p></span></div>
         </div>Form FDA 3500 Submission of a report does not constitute an admission that medical
         personnel or the product caused or contributed to the event.<input type="submit" value="Send Info"><input type="reset"></form>
   </body>
</html>]]>
            </sdc:sdc_html_form>
         </sdc:sdc_html_package>
      </Structured>

      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID/>

   </form>

   <contentType>HTML</contentType>
   <responseCode>Request succeeded</responseCode>
   <!-- Value is not required for the responseCode but will be useful -->


</RetrieveFormResponse>
"""




HERF_html = """<?xml version="1.0" encoding="UTF-8"?>

<!-- 
******************************************************************************
RFD Retrieve Form Response (ITI-34) containing an HTML Response 

FORM NAME:      Healthcare Event Reporting Form (HERF) Hospital Version 1.2
PURPOSE:        Response for HERF form using RFD (ITI-34) transaction in SDC sample HTML format.

REVISIONS: 
Ver        Date         Author              Description
1.0        12/01/2014   Varsha Parekh/      Added RFD wrapper and schema validation 
                        Richard Moldwin     fixed RFD schema to add <instanceID> support
                        
1.1        12/03/2014   Denise Warzel       Populated the sdc_html_form section containing html content 
1.2        12/11/2014   DW/WS/SJ/VP/RM      InstanceID removed, schema location moved
******************************************************************************/
-->

<RetrieveFormResponse 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../../../Schemas/RFD.xsd" 
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form"
   xmlns:mfi13="http://www.iso.org/19763/13/2013"
   xmlns:dex="urn:ihe:qrph:dex:2013"
   xmlns:mfi6="http://www.iso.org/19763/6/2013"
   xmlns:mdr3="http://www.iso.org/11179/3/2013"
   >

   <form>
       <Structured>
         <sdc:sdc_html_package>
            <sdc:supplemental_data>
               <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
                </sdc:supplemental_data>
            <sdc:form_info>
               <!-- Contains mapping, and administrative info; this is the same content as from the form design package -->
               <sdc:mapping_package xmlns="http://nlm.nih.gov/sdc/form"
                  mapping_package_identifier="http://nci.nih.gov/xml/cadsr/form/mapping_package#1111v1_0"
                  form_design_identifier="http://AHRQ.org/form_design_identifier#HERFv1_2">
                  <mdr_mapping
                     mdr_mapping_identifier="http://nci.nih.gov/xml/owl/cadsr#mapping_package/8888/1.0/form_design_identifier#HERFv1_2" >
                     <question_element_data_element_association>
                        <mfi13:data_element_identifier>2.16.840.1.113883.3.263.1.12/DE3</mfi13:data_element_identifier>
                        <mfi13:association_type>same_as</mfi13:association_type>
                        <mfi13:question_element_identifier>http://AHRQ.org/form/question_identifier/HERF/1.2/DE3</mfi13:question_element_identifier>
                     </question_element_data_element_association>
                     <question_element_data_element_association>
                        <mfi13:data_element_identifier>2.16.840.1.113883.5.1008/DE9</mfi13:data_element_identifier>
                        <mfi13:association_type>related</mfi13:association_type>
                        <mfi13:question_element_identifier>http://AHRQ.org/form/question_identifier/HERF/1.2/DE9</mfi13:question_element_identifier>
                     </question_element_data_element_association>
                     <question_element_data_element_association>
                        <mfi13:data_element_identifier>2.16.840.1.113883.3.263.1.12/DE321</mfi13:data_element_identifier>
                        <mfi13:association_type>related</mfi13:association_type>
                        <mfi13:question_element_identifier>http://AHRQ.org/form/question_identifier/HERF/1.2/DE321</mfi13:question_element_identifier>
                     </question_element_data_element_association>
                     <question_element_data_element_association>
                        <mfi13:data_element_identifier>2.16.840.1.113883.3.263.1.12/DE03</mfi13:data_element_identifier>
                        <mfi13:association_type>related</mfi13:association_type>
                        <mfi13:question_element_identifier>http://AHRQ.org/form/question_identifier/HERF/1.2/DE03</mfi13:question_element_identifier>
                     </question_element_data_element_association>
                     <question_element_data_element_association>
                        <mfi13:data_element_identifier>2.16.840.1.113883.5.1/DE42 or
                           2.16.840.1.113883.5.1008/DE42</mfi13:data_element_identifier>
                        <mfi13:association_type>related</mfi13:association_type>
                        <mfi13:question_element_identifier>http://AHRQ.org/form/question_identifier/HERF/1.2/DE42</mfi13:question_element_identifier>
                        <sdc:dex_mapping_specification>
                           <dex:contentModel>
                              <dex:id>2.16.840.1.113883.10.20.1</dex:id>
                              <dex:name>HL7 CCD</dex:name>
                           </dex:contentModel>
                           <dex:type>XPATH</dex:type>
                           <dex:mappingScript>/cda:ClinicalDocument/cda:recordTarget/cda:patientRole/cda:patient/cda:administrativeGenderCode/@code</dex:mappingScript>
                        </sdc:dex_mapping_specification>
                     </question_element_data_element_association>
                     <question_element_data_element_association>
                        <mfi13:data_element_identifier>2.16.840.1.113883.5.1 or
                           2.16.840.1.113883.5.1008</mfi13:data_element_identifier>
                        <mfi13:association_type>related</mfi13:association_type>
                        <mfi13:question_element_identifier>http://AHRQ.org/form/question_identifier/HERF/1.2/DE43</mfi13:question_element_identifier>
                     </question_element_data_element_association>
                     <question_element_data_element_association>
                        <mfi13:data_element_identifier>2.16.840.1.113883.3.263.1.12</mfi13:data_element_identifier>
                        <mfi13:association_type>related</mfi13:association_type>
                        <mfi13:question_element_identifier>http://AHRQ.org/form/question_identifier/HERF/1.2/DE33</mfi13:question_element_identifier>
                     </question_element_data_element_association>
                     <!--  element mappings abbreviated... -->
                  </mdr_mapping>
               </sdc:mapping_package>
               
               <sdc:administrative_package>
                  <submission_rule rule_identifier="1v1"
                     form_identifier="http://AHRQ.org/form_design_identifier#HERFv1_2"
                     xmlns="http://nlm.nih.gov/sdc/form">
                     <destination>
                        <sdc:endpoint>http://cdc.gov</sdc:endpoint>
                        <sdc:description>This is intended to be a set of one or more submission
                           rules that pertain to this version of the form. e.g. "This is an FDA form
                           and it must be sent to FDA when completed</sdc:description>
                     </destination>
                  </submission_rule>
                  <sdc:compliance_rule/>
                  <originating_registry_summary xmlns="http://nlm.nih.gov/sdc/form">
                     <!-- This element is an ISO element describing where this particular instance of the form came from -->
                     <mfi6:registry_organization>
                        <mdr3:name>NLM Forms Registry</mdr3:name>
                        <mdr3:uri>NLMRegistrationAuthorityIdentifier</mdr3:uri>
                     </mfi6:registry_organization>
                     <mfi6:reference_standard_identifier>ISO/IEC
                        19763-13</mfi6:reference_standard_identifier>
                     <mfi6:purpose_for_registry>
                        <mdr3:title>Forms for Meaningful Use</mdr3:title>
                     </mfi6:purpose_for_registry>
                     <mfi6:manual_for_registry>
                        <mdr3:title>SDC Forms IG</mdr3:title>
                     </mfi6:manual_for_registry>
                  </originating_registry_summary>
                  <sdc:form_language>
                     <style_language>
                        <!-- Optional, single reference document describing the
                                style language used to place Form_Design_Element instances in place
                                on the form
                                e.g.: http://www.w3.org/TR/CSS3/ 
         SDC could consider providing a default style sheet? -->
                        <mdr3:identifier>http://www.w3.org/TR/CSS3/</mdr3:identifier>
                        <mdr3:document_type>
                           <mdr3:description>a description of the style language used in the form
                              design</mdr3:description>
                        </mdr3:document_type>
                     </style_language>
                     <logic_language>
                        <!-- one logic language for all SDC forms should be established -->
                        <mdr3:identifier>http://some.document.describing.the.logicLangauge.document</mdr3:identifier>
                        <mdr3:document_type>
                           <mdr3:description>a description of the logic document</mdr3:description>
                        </mdr3:document_type>
                     </logic_language>
                     <format_language>
                        <!-- SDC may want to determine whether one or more formatting languages will be supported.
            Forms group is leaning towards html4, but the SDC group needs to dsicuss which will be supported in SDC -->
                        <mdr3:identifier>http://regEx</mdr3:identifier>
                        <mdr3:document_type>
                           <mdr3:description>a description of the format document</mdr3:description>
                        </mdr3:document_type>
                     </format_language>
                     <textual_language>eng</textual_language>
                     <!-- The language used in the description of this form 
       is consistent with meaningful and is based on LANGUAGE CODE 639-2 (3 digit) -->
                  </sdc:form_language>
                  <sdc:contacts>
                     <contact xmlns="http://nlm.nih.gov/sdc/form">
                        <!-- SDC Template Contact: optional one or more, complex element allowing for different roles  [ Steward, Owning Authority, etc ] -->
                        <individual>
                           <mdr3:name>Amy Helwig</mdr3:name>
                           <mdr3:title>Ms.</mdr3:title>
                           <mdr3:email_address/>
                        </individual>
                        <organization>
                           <name>Agency for Healthcare Research and Quality (AHRQ)</name>
                           <fhir_mail_address>
                              <use/>
                              <text/>
                              <line/>
                              <line/>
                              <city/>
                              <state/>
                              <zip/>
                              <country/>
                           </fhir_mail_address>
                        </organization>
                        <role>
                           <mdr3:title>Creator</mdr3:title>
                        </role>
                     </contact>
                     
                     <contact xmlns="http://nlm.nih.gov/sdc/form">
                        <!-- SDC Template Contact: optional one or more, complex element allowing for different roles  [ Steward, Owning Authority, etc ] -->
                        <individual>
                           <mdr3:name>Susan Terrillion</mdr3:name>
                           <mdr3:title>Ms.</mdr3:title>
                           <mdr3:email_address/>
                        </individual>
                        <organization>
                           <name>Agency for Healthcare Research and Quality (AHRQ)</name>
                           <fhir_mail_address>
                              <use/>
                              <text/>
                              <line/>
                              <line/>
                              <city>Bethesda</city>
                              <state>MD</state>
                              <zip/>
                              <country>USA</country>
                           </fhir_mail_address>
                        </organization>
                        <role>
                           <mdr3:title>Data Steward</mdr3:title>
                        </role>
                     </contact>
                  </sdc:contacts>
                  <registration xmlns="http://nlm.nih.gov/sdc/form">
                     <!-- if this is not inside the form, then we need an element to point to the form it applies to -->
                     <state>
                        <mdr3:registration_status/>
                        <mdr3:effective_date/>
                        <mdr3:until_date/>
                        <mdr3:administrative_note/>
                        <mdr3:administrative_status/>
                     </state>
                     <submission_record>
                        <organization>
                           <name>Agency for Healthcare Research and Quality (AHRQ)</name>
                           <fhir_mail_address>
                              <use/>
                              <text/>
                              <line/>
                              <line/>
                              <city/>
                              <state/>
                              <zip/>
                              <country/>
                           </fhir_mail_address>
                        </organization>
                        <contact>
                           <organization>
                              <name>CAP</name>
                              <fhir_mail_address>
                                 <use/>
                                 <text/>
                                 <line/>
                                 <line/>
                                 <city/>
                                 <state/>
                                 <zip/>
                                 <country/>
                              </fhir_mail_address>
                              <phone_number>800-323-4040</phone_number>
                           </organization>
                           <role>
                              <mdr3:title>author</mdr3:title>
                           </role>
                        </contact>
                     </submission_record>
                     <registration_status_date/>
                     <stewardship_record>
                        <organization>
                           <name>Agency for Healthcare Research and Quality (AHRQ)</name>
                           <fhir_mail_address>
                              <use/>
                              <text/>
                              <line/>
                              <line/>
                              <city/>
                              <state/>
                              <zip/>
                              <country/>
                           </fhir_mail_address>
                        </organization>
                     </stewardship_record>
                     <creation_date/>
                  </registration>
               </sdc:administrative_package>
               <stylesheet xmlns="http://nlm.nih.gov/sdc/form"/>
            </sdc:form_info>
             <sdc:sdc_html_form><![CDATA[
                <html>
                   <head>
                      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                         <title>Healthcare Event Reporting Form (HERF) Hospital Version 1.2</title><style>
                            body {
                            color:          #333;
                            font-family:    "Helvetica Neue, Helvetica, Arial, sans-serif";
                            font-size:      14px;
                            line-height:   1.42857;
                            }
                            .panel-section {
                            margin:     3px;
                            padding:    0px;
                            border-radius:  4px;
                            border:   1px solid black;
                            }
                            .panel-question {
                            padding:    2px 0 2px 5px;
                            margin:     5px;
                            border:     1px solid #428bca;
                            border-radius:  4px;
                            
                            }
                            .form-header-instruction{
                            font-size:18px;
                            }
                            .section-header{
                            margin:0;
                            padding:5px 0 5px 5px;
                            border-radius:4px 4px 0 0;
                            background-color:#d4d8d1;
                            }
                            .form-cdeId{
                            font-size:12px;
                            }
                            .guarded-element-question{
                            text-indent:60px;
                            }
                            h4{
                            margin:2px 0 2px 0;
                            }</style></head>
                   <body id="form">
                      <form method="post" action="">
                         <div id="form-heading-section">
                            <h1 style="padding: 0 5px 0 5px"><span class="text-center"><strong>Healthcare Event Reporting Form (HERF) Hospital Version 1.2</strong></span><br></h1>
                         </div>
                         <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE2" class="question-prompt" style="display: block; font-weight: bold;"> Event ID</label><input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE2" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE2" size="30"><span class="form-cdeId">
                            <p>CDE USHIK:DE2</p></span></div>
                         <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE30" class="question-prompt" style="display: block; font-weight: bold;"> Initial Report Date</label> (MM/DD/YYYY) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE30" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE30" size="30"><span class="form-cdeId">
                            <p>CDE USHIK:DE30</p></span></div>
                         <div class="form-section panel-section">
                            <h2 class="section-header"> </h2>
                            <p style="margin-left: 3px"></p>
                            <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE30" class="question-prompt" style="display: block; font-weight: bold;">1. Report Date</label> (MM/DD/YYYY) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE30" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE30" size="30"><span class="form-cdeId">
                               <p>CDE USHIK:DE30</p></span></div>
                            <div class="panel-question">
                               <h4 class="question-prompt">2. What is being reported?</h4>
                               <p style="margin: 0;">
                                  CHECK ONE:
                                  
                                  
                               </p>
                               <ul style="list-style-type: none; margin: 2px 0 0 0">
                                  <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE3" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE3/A3" value="A3">Incident</label><div class="guarded-element-question">
                                     <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9a" class="question-prompt" style="display: block; font-weight: bold;">3. Event Discovery Date</label> (MM/DD/YYYY) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9a" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9a" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:DE9a</p></span></div>
                                     <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9b" class="question-prompt" style="display: block; font-weight: bold;">4. Event Discovery Time</label> (Default = Unknown) (HHMM) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9b" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9b" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:DE9b</p></span><span style="margin-left: 1px">
                                           <p>(MILITARY TIME)</p></span></div>
                                  </div>
                                     <div class="guarded-element-question">
                                        <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE46" class="question-prompt" style="display: block; font-weight: bold;">8. Patient's Name</label> (FIRST, MIDDLE, LAST) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE46" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE46" size="30"><span class="form-cdeId">
                                           <p>CDE USHIK:DE46</p></span></div>
                                        <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE47" class="question-prompt" style="display: block; font-weight: bold;">9. Patient's Date of Birth</label> (MM/DD/YYYY) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE47" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE47" size="30"><span class="form-cdeId">
                                           <p>CDE USHIK:DE47</p></span></div>
                                        <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE49" class="question-prompt" style="display: block; font-weight: bold;">10. Patient's Medical Record #</label><input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE49" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE49" size="30"><span class="form-cdeId">
                                           <p>CDE USHIK:DE49</p></span></div>
                                        <div class="panel-question">
                                           <h4 class="question-prompt">11. Patient's Gender</h4>
                                           <p style="margin: 0;">
                                              CHECK ONE:
                                              
                                              
                                           </p>
                                           <ul style="list-style-type: none; margin: 2px 0 0 0">
                                              <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE42" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE42/M" value="M">Male</label></li>
                                              <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE42" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE42/F" value="F">Female</label></li>
                                              <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE42" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE42/UNK" value="UNK">Unknown</label></li>
                                           </ul><span class="form-cdeId">
                                              <p>CDE USHIK:DE42</p></span></div>
                                     </div>
                                  </li>
                                  <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE3" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE3/A6" value="A6">Near Miss</label><div class="guarded-element-question">
                                     <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9a" class="question-prompt" style="display: block; font-weight: bold;">3. Event Discovery Date</label> (MM/DD/YYYY) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9a" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9a" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:DE9a</p></span></div>
                                     <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9b" class="question-prompt" style="display: block; font-weight: bold;">4. Event Discovery Time</label> (Default = Unknown) (HHMM) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9b" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE9b" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:DE9b</p></span><span style="margin-left: 1px">
                                           <p>(MILITARY TIME)</p></span></div>
                                  </div>
                                  </li>
                                  <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE3" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE3/A9" value="A9">Unsafe Condition</label></li>
                               </ul><span class="form-cdeId">
                                  <p>CDE USHIK:DE3</p></span></div>
                            <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE15" class="question-prompt" style="display: block; font-weight: bold;">5. Briefly describe the event that occurred or unsafe condition</label><input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE15" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE15" size="30"><span class="form-cdeId">
                               <p>CDE USHIK:DE15</p></span></div>
                            <div class="panel-question"><label for="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE18" class="question-prompt" style="display: block; font-weight: bold;">6. Briefly describe the location where the event occurred or where the unsafe condition
                               exists</label><input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE18" id="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE18" size="30"><span class="form-cdeId">
                                  <p>CDE USHIK:DE18</p></span></div>
                            <div class="panel-question">
                               <h4 class="question-prompt">7. Which of the following categories are associated with the event or unsafe
                                  condition?
                               </h4>
                               <p style="margin: 0;">
                                  FOR EACH CATEGORY SELECTED BELOW, EXCEPT “OTHER”, PLEASE COMPLETE THE
                                  CORRESPONDING CATEGORY-SPECIFIC FORM. ALL CATEGORIES INCLUDE REPORTING OF
                                  INCIDENTS. ANY CATEGORY WITH + ALSO INCLUDES REPORTING OF NEAR MISSES. ANY
                                  CATEGORY WITH asterick ALSO INCLUDES REPORTING OF UNSAFE CONDITIONS.
                                  
                               </p>
                               <div style="font-style: italic;">
                                  <p style="margin: 0;"> CHECK ALL THAT APPLY</p>
                                  <p style="margin: 0;"> For Incidents, use all of the answers. For Near Miss, use only answers: a, b,
                                     e, h, j. For Unsafe Conditions, use only answers: a, b, e, j.
                                  </p>
                               </div>
                               <ul style="list-style-type: none; margin: 2px 0 0 0">
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A42" value="A42">Blood or Blood Product</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A44" value="A44">Device or Medical/Surgical Supply, including Health Information
                                     Technology (HIT)</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A48" value="A48">Fall</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A51" value="A51">Healthcare-associated Infection</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A54" value="A54">Medication or Other Substance</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A57" value="A57">Perinatal</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A460" value="A60">Pressure Ulcer</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A63" value="A63">Surgery or Anesthesia (includes invasive procedure)</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A64" value="A64">Venous Thromboembolism</label></li>
                                  <li><label><input type="checkbox" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE21" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE21/A66" value="A66">Other: PLEASE SPECIFY</label>____________________
                                  </li>
                               </ul><span class="form-cdeId">
                                  <p>CDE USHIK:DE21</p></span></div>
                         </div>
                         <div class="form-section panel-section">
                            <h2 class="section-header"> Neonatal Patient Information:</h2>
                            <p style="margin-left: 3px">COMPLETE ONLY FOR NEONATE AFFECTED BY PERINATAL INCIDENT</p>
                            <div class="panel-question">
                               <h4 class="question-prompt"> Is this event a perinatal incident that affected a neonate?</h4>
                               <p style="margin: 0;">
                                  CHECK ONE:
                                  
                                  
                               </p>
                               <ul style="list-style-type: none; margin: 2px 0 0 0">
                                  <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#Hidden1" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE34/A15" value="A15">Yes</label><div class="guarded-element-question"><b>12. Neonate's Name</b> (FIRST, MIDDLE, LAST) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE34" size="30"><span class="form-cdeId">
                                     <p>CDE USHIK:DE34</p></span></div>
                                     <div class="guarded-element-question"><b>13. Neonate's Date of Birth</b> (MM/DD/YYYY) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE37" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:DE37</p></span></div>
                                     <div class="guarded-element-question"><b>14. Neonate's Medical Record #</b><input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE40" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:DE40</p></span></div>
                                     <div class="guarded-element-question"><b>15. Neonate's Gender</b>
                                        CHECK ONE:
                                        
                                        
                                        <ul style="list-style-type: none; margin: 2px 0 0 0">
                                           <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE43" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE43/M" value="M">Male</label></li>
                                           <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE43" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE43/F" value="F">Female</label></li>
                                           <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE43" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE43/UNK" value="UNK">Unknown</label></li>
                                        </ul><span class="form-cdeId">
                                           <p>CDE USHIK:D43</p></span></div>
                                  </li>
                                  <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#Hidden1" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE34/A18" value="A18">No</label></li>
                               </ul><span class="form-cdeId">
                                  <p>CDE USHIK:Hidden1</p></span></div>
                         </div>
                         <div class="form-section panel-section">
                            <h2 class="section-header"> REPORT AND EVENT REPORTER INFORMATION</h2>
                            <p style="margin-left: 3px"></p>
                            <div class="panel-question">
                               <h4 class="question-prompt">16. Anonymous Reporter</h4>
                               <ul style="list-style-type: none; margin: 2px 0 0 0">
                                  <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE33" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE33/A15" value="A15">Yes</label> (DONE)
                                  </li>
                                  <li><label><input type="radio" style="margin-right: 5px" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE33" id="http://AHRQ.org/form_design_identifier/HERFv1.2/list_item_identifier#HERF/DE33/A18" value="A18">No</label><div class="guarded-element-question"><b>17. Reporter's Name</b> (FIRST, MIDDLE, LAST) <input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE50" size="30"><span class="form-cdeId">
                                     <p>CDE USHIK:DE50</p></span></div>
                                     <div class="guarded-element-question"><b>18. Telephone Number</b><input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE52" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:DE52</p></span></div>
                                     <div class="guarded-element-question"><b>19. Email Address</b><input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE53" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:DE53</p></span></div>
                                     <div class="guarded-element-question"><b>20. Reporter's Job or Position</b><input type="text" name="http://AHRQ.org/form_design_identifier/HERFv1.2/question_identifier#DE36" size="30"><span class="form-cdeId">
                                        <p>CDE USHIK:D36</p></span></div>
                                  </li>
                               </ul><span class="form-cdeId">
                                  <p>CDE USHIK:D33</p></span></div>
                         </div>
                         <div class="form-section panel-section">
                            <h2 class="section-header"> Thank you for completing these questions.</h2>
                            <p style="margin-left: 3px">OMB No. 0935-0143 Exp. Date 10/31/2014 Public reporting burden for the collection
                               of information is estimated to average 10 minutes per response. An agency may not
                               conduct or sponsor, and a person is not required to respond to, a collection of
                               information unless it displays a currently valid OMB control number. Send comments
                               regarding this burden estimate or any other aspect of this collection of information,
                               including suggestions for reducing this burden, to: AHRQ Reports Clearance Officer,
                               Attention: PRA, Paperwork Reduction Project (0935-0143), AHRQ, 540 Gaither Road, Room
                               #5036, Rockville, MD 20850.
                            </p>
                         </div>AHRQ Common Formats - Hospital Version 1.2 - 2012 Medication or Other Substance<input type="submit" value="Send Info"><input type="reset"></form>
                   </body>
                </html>
            ]]>
             </sdc:sdc_html_form>
         </sdc:sdc_html_package>
      </Structured>

      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID/>

   </form>

   <contentType>HTML</contentType>
   <responseCode>Request succeeded</responseCode>
   <!-- Value is not required for the responseCode but will be useful -->

</RetrieveFormResponse>
"""




NCI_Demographics_html = """<?xml version="1.0" encoding="UTF-8"?>

<!-- 
******************************************************************************
RFD Retrieve Form Response (ITI-34) containing an HTML Response 

FORM NAME:  NCI Demography
PURPOSE:    Response for an NCI Demography template using RFD (ITI-34) transaction in SDC sample HTML format.

REVISIONS: 
Ver        Date         Author              Description
1.0        12/01/2014   Varsha Parekh/      Added RFD wrapper and schema validation 
                        Richard Moldwin     Need to fix RFD schema to add <instanceID> for SDC
                        
1.1        12/03/2014   Denise Warzel       Populated the sdc_html_form section containing html content         
1.2        12/11/2014   DW/WS/SJ/VP/RM      InstanceID removed, schema location added
******************************************************************************/
-->

<RetrieveFormResponse 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../../../Schemas/RFD.xsd" 
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form"
   xmlns:mfi13="http://www.iso.org/19763/13/2013"
   xmlns:dex="urn:ihe:qrph:dex:2013"
   xmlns:mfi6="http://www.iso.org/19763/6/2013"
   xmlns:mdr3="http://www.iso.org/11179/3/2013"
   >

   <form>
      <Structured>
         <sdc:sdc_html_package>
            <sdc:supplemental_data>
               <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
            </sdc:supplemental_data>
            <sdc:form_info>
               <!-- Contains mapping, and administrative info; this is the same content as from the form design package -->
               <sdc:mapping_package mapping_package_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/mapping_package_identifier#2674812v4.0/1"
                  form_design_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier#2674812v4.0">
                  <sdc:mdr_mapping mdr_mapping_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/mdr_mapping_identifier#2674812v4.0/1">
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2200604v3.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192199v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#793v5.1</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702903v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192217v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179606v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702914v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2865130v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#315v4.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702932v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2003745v5.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702934v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2200286v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702936v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2200284v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702938v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2681552v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2001708v5.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2674076v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2943243v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702984v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2188083v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                  </sdc:mdr_mapping>
               </sdc:mapping_package>
               <sdc:administrative_package>
                  <sdc:submission_rule/>
                  <sdc:compliance_rule/>
                  <sdc:originating_registry_summary>
                     <mfi6:registry_organization xmlns:mfi6="http://www.iso.org/19763/6/2013">
                        <mdr3:name xmlns:mdr3="http://www.iso.org/11179/3/2013">NCI</mdr3:name>
                        <mdr3:uri xmlns:mdr3="http://www.iso.org/11179/3/2013">2.16.840.1.113883.3.26.2</mdr3:uri>
                     </mfi6:registry_organization>
                     <mfi6:reference_standard_identifier xmlns:mfi6="http://www.iso.org/19763/6/2013">ISO/IEC 19763-13 Form_Design</mfi6:reference_standard_identifier>
                     <mfi6:SLA_for_registry xmlns:mfi6="http://www.iso.org/19763/6/2013"/>
                     <mfi6:purpose_for_registry xmlns:mfi6="http://www.iso.org/19763/6/2013">
                        <mdr3:title xmlns:mdr3="http://www.iso.org/11179/3/2013">CDEs and Forms for Cancer Clinical Trials</mdr3:title>
                     </mfi6:purpose_for_registry>
                     <mfi6:manual_for_registry xmlns:mfi6="http://www.iso.org/19763/6/2013">
                        <mdr3:title xmlns:mdr3="http://www.iso.org/11179/3/2013">https://wiki.nci.nih.gov/x/Q4EI</mdr3:title>
                     </mfi6:manual_for_registry>
                     <mfi6:specification_for_interface xmlns:mfi6="http://www.iso.org/19763/6/2013">
                        <mfi6:name>caDSR API</mfi6:name>
                        <mfi6:description>caDSR API Domain Class Browser</mfi6:description>
                        <mfi6:URL>http://cadsrapi.nci.nih.gov</mfi6:URL>
                        <mfi6:version>4.0</mfi6:version>
                     </mfi6:specification_for_interface>
                  </sdc:originating_registry_summary>
                  <sdc:form_language>
                     <mfi13:style_language xmlns:mfi13="http://www.iso.org/19763/13/2013"/>
                     <mfi13:logic_language xmlns:mfi13="http://www.iso.org/19763/13/2013"/>
                     <mfi13:format_language xmlns:mfi13="http://www.iso.org/19763/13/2013"/>
                     <sdc:textual_language>eng</sdc:textual_language>
                  </sdc:form_language>
                  <sdc:contacts/>
                  <sdc:registration>
                     <sdc:state>
                        <mdr3:registration_status xmlns:mdr3="http://www.iso.org/11179/3/2013">STANDARD</mdr3:registration_status>
                        <mdr3:effective_date xmlns:mdr3="http://www.iso.org/11179/3/2013">2013-03-22T09:28:17.0</mdr3:effective_date>
                        <mdr3:until_date xmlns:mdr3="http://www.iso.org/11179/3/2013"/>
                        <mdr3:administrative_note xmlns:mdr3="http://www.iso.org/11179/3/2013">Versioned to update the PV Meanings and Instructional text on Race to include "check all that apply".</mdr3:administrative_note>
                        <mdr3:administrative_status xmlns:mdr3="http://www.iso.org/11179/3/2013">RELEASED</mdr3:administrative_status>
                     </sdc:state>
                     <sdc:document_reference>
                        <mdr3:identifier xmlns:mdr3="http://www.iso.org/11179/3/2013"/>
                        <mdr3:document_type xmlns:mdr3="http://www.iso.org/11179/3/2013">
                           <mdr3:description>PDF</mdr3:description>
                        </mdr3:document_type>
                        <mdr3:title xmlns:mdr3="http://www.iso.org/11179/3/2013">caBIG Case Report Form Manual</mdr3:title>
                        <mdr3:provider xmlns:mdr3="http://www.iso.org/11179/3/2013">
                           <mdr3:name>NCIP</mdr3:name>
                        </mdr3:provider>
                        <mdr3:uri xmlns:mdr3="http://www.iso.org/11179/3/2013"/>
                     </sdc:document_reference>
                     <sdc:stewardship_record>
                        <sdc:organization>
                           <sdc:name>National Cancer Institute (NCI)</sdc:name>
                           <sdc:fhir_mail_address>
                              <sdc:line>BG 9609 MSC 9760</sdc:line>
                              <sdc:line>9609 Medical Center Drive</sdc:line>
                              <sdc:city>Bethesda</sdc:city>
                              <sdc:state>MD</sdc:state>
                              <sdc:zip>20892-97609609</sdc:zip>
                              <sdc:country>USA</sdc:country>
                           </sdc:fhir_mail_address>
                        </sdc:organization>
                     </sdc:stewardship_record>
                     <sdc:creation_date>2013-03-22T09:20:27.0</sdc:creation_date>
                     <sdc:explanatory_comment>Variables in Demography CRF module balloted by caBIG community October 1 through October 30, 2009. Variables approved as Standards by caBIG community October 30, 2009.</sdc:explanatory_comment>
                  </sdc:registration>
               </sdc:administrative_package>
               <sdc:stylesheet/>
            </sdc:form_info>
            <sdc:sdc_html_form>
              <![CDATA[
               <html>
                  <head>
                     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                        <title>Demography NCI Standard Template</title><style>
                           body {
                           color:          #333;
                           font-family:    "Helvetica Neue, Helvetica, Arial, sans-serif";
                           font-size:      14px;
                           line-height:   1.42857;
                           }
                           .panel-section {
                           margin:     3px;
                           padding:    0px;
                           border-radius:  4px;
                           border:   1px solid black;
                           }
                           .panel-question {
                           padding:    2px 0 2px 5px;
                           margin:     5px;
                           border:     1px solid #428bca;
                           border-radius:  4px;
                           
                           }
                           .form-header-instruction{
                           font-size:18px;
                           }
                           .section-header{
                           margin:0;
                           padding:5px 0 5px 5px;
                           border-radius:4px 4px 0 0;
                           background-color:#d4d8d1;
                           }
                           .form-cdeId{
                           font-size:12px;
                           }
                           .guarded-element-question{
                           text-indent:60px;
                           }
                           h4{
                           margin:2px 0 2px 0;
                           }</style></head> 
                  <body id="form">
                     <form method="post" action="http:cdc">
                        <div id="form-heading-section">
                           <h1 style="padding: 0 5px 0 5px"><span class="text-center"><strong>Demography NCI Standard Template</strong></span><br></h1>
                        </div>
                        <div class="form-section panel-section">
                           <h2 class="section-header"> Mandatory Demography Questions</h2>
                           <p style="margin-left: 3px">These items must be included when this data is collected for reporting</p>
                           <div class="panel-question">
                              <h4 class="question-prompt"> Gender</h4>
                              <p style="margin: 0;">
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575551/1.0" value="Female">Female Gender</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575550/1.0" value="Male">Male Gender</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575365/1.0" value="Unknown">Unknown</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2573360/1.0" value="Unspecified">Unspecified</label></li>
                              </ul><span class="form-cdeId">
                                 <p>CDE NCI:2200604v3.0</p></span></div>
                           <div class="panel-question">
                              <h4 class="question-prompt"> Race</h4>
                              <p style="margin: 0;">
                                 
                                 Check all that apply
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="checkbox" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572232/1.0" value="American Indian or Alaska Native">American Indian or Alaska Native</label></li>
                                 <li><label><input type="checkbox" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572233/1.0" value="Asian">Asian</label></li>
                                 <li><label><input type="checkbox" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572313/1.0" value="Black or African American">Black or African American</label></li>
                                 <li><label><input type="checkbox" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572235/1.0" value="Native Hawaiian or other Pacific Islander">Native Hawaiian or Other Pacific Islander</label></li>
                                 <li><label><input type="checkbox" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572578/1.0" value="Not Reported">Not Reported</label></li>
                                 <li><label><input type="checkbox" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572577/1.0" value="Unknown">Unknown</label></li>
                                 <li><label><input type="checkbox" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572236/1.0" value="White">White</label></li>
                              </ul><span class="form-cdeId">
                                 <p>CDE NCI:2192199v1.0</p></span></div>
                           <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702903v4.0" class="question-prompt" style="display: block; font-weight: bold;"> Patient's Date of Birth</label><p style="margin: 0;">
                              
                              
                           </p> (MM/DD/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702903v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702903v4.0" size="30"><span class="form-cdeId">
                              <p>CDE NCI:793v5.1</p></span></div>
                           <div class="panel-question">
                              <h4 class="question-prompt"> Ethnicity</h4>
                              <p style="margin: 0;">
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581176/1.0" value="Hispanic or Latino">Hispanic or Latino</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2567110/1.0" value="Not Hispanic or Latino">Not Hispanic or Latino</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572578/1.0" value="Not reported">Not Reported</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572577/1.0" value="Unknown">Unknown</label></li>
                              </ul><span class="form-cdeId">
                                 <p>CDE NCI:2192217v2.0</p></span></div>
                        </div>
                        <div class="form-section panel-section">
                           <h2 class="section-header"> Conditional Demography Questions</h2>
                           <p style="margin-left: 3px">There are business rules to indicate situations under which these elements should
                              be used on a case report form.
                           </p>
                           <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702914v4.0" class="question-prompt" style="display: block; font-weight: bold;"> ZIP Code</label><p style="margin: 0;">
                              
                              Conditionality Rule: Requirement for collection is imposed by the trial sponsor.
                              
                              
                           </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702914v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702914v4.0" size="30"><span class="form-cdeId">
                              <p>CDE NCI:2179606v2.0</p></span></div>
                           <div class="panel-question">
                              <h4 class="question-prompt"> Payment Method</h4>
                              <p style="margin: 0;">
                                 
                                 Conditionality Rule: Requirement for collection is imposed by the trial sponsor. Sponsor
                                 now stipulates the use of codes with the values.
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936647/1.0" value="Managed Care/Medicare">Managed Care/Medicare</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865123/1.0" value="Medicaid">Medicaid</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865124/1.0" value="Medicaid and Medicare">Medicare And Medicaid</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932789/1.0" value="Medicare">Medicare</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932791/1.0" value="Medicare and Private Insurance">Medicare And Private Insurance</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936649/1.0" value="Military or Veterans Sponsored, NOS">Military Or Veterans Sponsored Insurance, Not Otherwise Specified</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865126/1.0" value="Military Sponsored (Including CHAMPUS &amp; TriCare)">Military Insurance</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865128/1.0" value="No Means of Payment (No Insurance)">No Insurance</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2559653/1.0" value="Other">Other</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865120/1.0" value="Private Insurance">Private Insurance</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932793/1.0" value="Self-Pay (No Insurance)">Self Payment</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936648/1.0" value="State Supplemental Health Insurance">State Supplemental Health Insurance</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575365/1.0" value="Unknown">Unknown</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865127/1.0" value="Veterans Sponsored">Veterans Administration Sponsor Insurance</label></li>
                              </ul><span class="form-cdeId">
                                 <p>CDE NCI:2865130v1.0</p></span></div>
                           <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702932v4.0" class="question-prompt" style="display: block; font-weight: bold;"> Country of Residence</label><p style="margin: 0;">
                              
                              Conditionality Rule: Requirement for collection is imposed by the trial sponsor.
                              
                              
                           </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702932v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702932v4.0" size="30"><span class="form-cdeId">
                              <p>CDE NCI:315v4.0</p></span></div>
                           <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702934v4.0" class="question-prompt" style="display: block; font-weight: bold;"> Date Completed</label><p style="margin: 0;">
                              
                              Conditionality Rule: Data Collection is done using paper Case Report Forms (CRFs)
                              instead of an Electronic Data Capture system.
                              
                              
                           </p> (DD/MON/YYYY) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702934v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702934v4.0" size="30"><span class="form-cdeId">
                              <p>CDE NCI:2003745v5.0</p></span></div>
                           <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702936v4.0" class="question-prompt" style="display: block; font-weight: bold;"> CDC Race Code</label><p style="margin: 0;">
                              
                              Conditionality Rule: In the event the sponsor requires the data be collected using
                              the CDC codes, use this CDE instead of 2192199. Do NOT collect both items.
                              
                              
                           </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702936v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702936v4.0" size="30"><span class="form-cdeId">
                              <p>CDE NCI:2200286v1.0</p></span></div>
                           <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702938v4.0" class="question-prompt" style="display: block; font-weight: bold;"> CDC Ethnicity Code</label><p style="margin: 0;">
                              
                              Conditionality Rule: In the event the sponsor requires the data be collected using
                              the CDC codes, use this CDE instead of 2192217. Do NOT collect both items.
                              
                              
                           </p><input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702938v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702938v4.0" size="30"><span class="form-cdeId">
                              <p>CDE NCI:2200284v2.0</p></span></div>
                        </div>
                        <div class="form-section panel-section">
                           <h2 class="section-header"> Optional Demography Questions</h2>
                           <p style="margin-left: 3px">There is no requirement for inclusion of these elements on the case report form. If
                              the design and scientific questions posed in the study dictate the need to collect
                              this type of data, these elements should be included.
                           </p>
                           <div class="panel-question">
                              <h4 class="question-prompt"> Highest Education Level</h4>
                              <p style="margin: 0;">
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2671182/1.0" value="Bachelor's Degree">Bachelor's Degree</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936654/1.0" value="Doctoral degree or professional degree">Professional Doctorate or Doctorate Degree</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936655/1.0" value="Grade School">Grade School</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936656/1.0" value="Graduate or professional degree">Graduation Or Professional Degree</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936657/1.0" value="High school graduate (including equivalency)">High School Completion or General Equivalency Diploma (GED) Completion</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654055/1.0" value="Master's Degree">Master's Degree</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936661/1.0" value="No formal education">No Formal Schooling</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2947076/1.0" value="Not high school graduate">Not High School Graduate</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936660/1.0" value="Some college or associate degree">Some College or Associates Degree</label></li>
                              </ul><span class="form-cdeId">
                                 <p>CDE NCI:2681552v1.0</p></span></div>
                           <div class="panel-question">
                              <h4 class="question-prompt"> Country of Birth</h4>
                              <p style="margin: 0;">
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2571959/1.0" value="Other country">Other country</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561053/1.0" value="Other country, specify">Other Country, Specify</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2564081/1.0" value="USA">USA</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561052/1.0" value="USA, specify the 2 letter State code, eg NY">USA, Specify the 2 letter state code, eg NY </label></li>
                              </ul><span class="form-cdeId">
                                 <p>CDE NCI:2001708v5.0</p></span></div>
                           <div class="panel-question">
                              <h4 class="question-prompt"> Highest Education Level</h4>
                              <p style="margin: 0;">
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581475/1.0" value="10th Grade">10th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581476/1.0" value="11th Grade">11th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654051/1.0" value="12th Grade No Diploma">12th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581466/1.0" value="1st Grade">1st Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581467/1.0" value="2nd Grade">2nd Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581468/1.0" value="3rd Grade">3rd Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581469/1.0" value="4th Grade">4th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581470/1.0" value="5th Grade">5th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581471/1.0" value="6th Grade">6th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581472/1.0" value="7th Grade">7th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581473/1.0" value="8th Grade">8th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581474/1.0" value="9th Grade">9th Grade</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688040/1.0" value="Academic Doctorate Degree">Academic Doctorate Degree Completion</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654054/1.0" value="Associate Degree">Associate Degree</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688041/1.0" value="Bachelor Degree">Bachelor's Degree Completion</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654058/1.0" value="Don't Know">Does Not Know</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654052/1.0" value="General Equivalency Diploma">General Equivalency Diploma</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2681432/1.0" value="High School Graduate">High School Graduate</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2718906/1.0" value="Kindergarten">Kindergarten Completion</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688039/1.0" value="Master's Degree">Master's Degree Completion</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654050/1.0" value="No Formal Schooling">Never Attended</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2718907/1.0" value="Preschool">Preschool Completion</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688038/1.0" value="Professional Doctorate Degree">Professional Doctorate Degree Completion</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2579385/1.0" value="Refused">Refuse</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2569309/1.0" value="Some College, No Degree">Some College</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654053/1.0" value="VoTech Program">Vocational Degree</label></li>
                              </ul><span class="form-cdeId">
                                 <p>CDE NCI:2674076v2.0</p></span></div>
                           <div class="panel-question"><label for="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702984v4.0" class="question-prompt" style="display: block; font-weight: bold;"> Census Tract Code at Enrollment</label><p style="margin: 0;">
                              
                              
                           </p> (9999.99) <input type="text" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702984v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702984v4.0" size="30"><span class="form-cdeId">
                              <p>CDE NCI:2943243v1.0</p></span></div>
                           <div class="panel-question">
                              <h4 class="question-prompt"> Marital Status</h4>
                              <p style="margin: 0;">
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578101/1.0" value="Divorced">Divorced</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578103/1.0" value="Domestic Partnership">Domestic Partner</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578102/1.0" value="Married">Married</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2576696/1.0" value="Never Married">Never married</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561620/1.0" value="Separated">Separated</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561048/1.0" value="Widowed">Widowed</label></li>
                              </ul><span class="form-cdeId">
                                 <p>CDE NCI:2188083v2.0</p></span></div>
                        </div><input type="submit" value="Send Info"><input type="reset"></form>
                  </body>
               </html>]]>
               
            </sdc:sdc_html_form>
         </sdc:sdc_html_package>
      </Structured>
      
      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID></instanceID>
      
   </form>

   <contentType>HTML</contentType>

   <responseCode>Request succeeded</responseCode>
   <!-- Value is not required for the responseCode but will be useful -->

</RetrieveFormResponse>
"""



