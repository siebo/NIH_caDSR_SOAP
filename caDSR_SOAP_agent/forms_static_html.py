# -*- coding: utf-8 -*-
adrenal_html = """<RetrieveFormResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form"
   xmlns:mfi13="http://www.iso.org/19763/13/2013"
   xmlns:dex="urn:ihe:qrph:dex:2013"
   xmlns:mfi6="http://www.iso.org/19763/6/2013"
   xmlns:mdr3="http://www.iso.org/11179/3/2013"
   >
   <form>
      <Structured>
         <sdc_html_package>
            
            <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
            <sdc:supplemental_data>               
               <anyXMLContentType></anyXMLContentType>
            </sdc:supplemental_data>
            
            <!-- Contains mapping, and administrative info; this is the same content as from the form design package -->
            <sdc:form_info>
               <anyXMLContentType></anyXMLContentType>               
            </sdc:form_info>
            
            <!-- USHIK will provide actual HTML content using automated transformation utility -->
            <sdc:sdc_html_form>     
               <![CDATA[
<!DOCTYPE html
  SYSTEM "about:legacy-compat">
                  
<html>
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <title>ADRENAL GLAND: Biopsy (Core Needle, Incisional, Excisional); Resection</title><style>
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
                    }</style><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script><script type="text/javascript">//
$(function () {
	/*
	 * Process checkboxes and radio buttons so if a parent checkbox/radio button is unchecked, children are unchecked,
	 * if child checked then check parent, etc.
	 */
	var $parentCheckboxes = $('.guarded-element-question').parent().find('input[type=checkbox]:first');
	$parentCheckboxes.each(function () {
		var $parentCheckbox = $(this);
		var $childrenCheckboxes = $parentCheckbox.closest('li').find('ul li input[type=checkbox], input[type=radio]');

		if ($childrenCheckboxes.length > 0) {
			$childrenCheckboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=checkbox], input[type=radio]').is(':checked');
				$parentCheckbox.prop('checked', $anyChildrenChecked);
			});

			$parentCheckbox.click(function () {
				if (!($(this).is(':checked'))) {
					$(this).closest('li').find('ul li input[type=checkbox], input[type=radio]').prop('checked', $(this).prop('checked'));
				}
			})
		}
	});

	var $parentRadioboxes = $('.guarded-element-question').parent().find('input[type=radio]:first');
	$parentRadioboxes.each(function () {
		var $parentRadiobox = $(this);

		var $childrenRadioboxes = $parentRadiobox.closest('li').find('ul li input[type=radio]');
		if ($childrenRadioboxes.length > 0) {
			$childrenRadioboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=radio]').is(':checked');
				$parentRadiobox.prop('checked', $anyChildrenChecked);
			});

			$parentRadiobox.closest('li').siblings().find('input[type=radio]').change(function () {
				$childrenRadioboxes.each(function () {
					$(this).prop('checked', false);
				});
			});
		}
	})
});

var getXmlOutput = (function () {
	'use strict'
	function formatAttributes(attributes) {
		var
		SINGLE_QUOTE = "'",
		DOUBLE_QUOTE = '"',
		ESCAPED_QUOTE = {
			SINGLE_QUOTE : '&quot;',
			DOUBLE_QUOTE : '&apos;'
		};
		var
		att_value,
		single_quote_pos,
		double_quote_pos,
		use_quote,
		escape,
		quote_to_escape,
		att_str,
		re,
		result = '';
		for (var att in attributes) {
			att_value = '' + attributes[att];
			single_quote_pos = att_value.indexOf(SINGLE_QUOTE);
			double_quote_pos = att_value.indexOf(DOUBLE_QUOTE);
			if (single_quote_pos !=  - 1 && double_quote_pos !=  - 1) {
				att_str = ' ' + att + "='" + att_value + "'";
				result += att_str;
				continue;
			}
			if (double_quote_pos !=  - 1 && double_quote_pos < apos_pos) {
				use_quote = SINGLE_QUOTE;
			} else {
				use_quote = DOUBLE_QUOTE;
			}
			escape = ESCAPED_QUOTE[use_quote];
			re = new RegExp(use_quote, 'g');
			att_str = '\n' + '  ' + att + '=' + use_quote + att_value.replace(re, escape) + use_quote;
			result += att_str;
		}
		return result;
	}
	/*
	 *	Public functions
	 */
	function createElement(name, content, attributes) {
		var att_str = '';
		if (attributes) {
			att_str = formatAttributes(attributes);
		}
		var xml;
		if (!content) {
			xml = '<' + name + att_str + '>' + '</' + name + '>';
		} else {
			xml = '<' + name + att_str + '>' + content + '</' + name + '>';
		}
		return xml;
	}
	var repeat_master_list = {};
	function recordRepeatOfQuestion(questionId) {
		var count = repeat_master_list[questionId];
		if (count == null || count == undefined) {
			count = 0;
		}
		++count;
		repeat_master_list[questionId] = count;
		return count;
	}

	function createPayload() {
		var testSection = "";
		$('input').each(function (index, item) {
			var addQuestion = true;

			/* Skip the last two inputs - submit & reset */
			if ($(item).attr('type') != 'submit' && $(item).attr('type') != 'reset') {
				var attrs = [];
				attrs.section_identifier = $(item).attr('data-section-identifier');
				attrs.question_identifier = $(item).attr('data-question-identifier');
				attrs.question_prompt = $(item).attr('data-question-prompt');

				var dtype = $(item).attr('data-datatype');
				if (dtype != undefined && dtype != null && dtype != '') {
					attrs.datatype = $(item).attr('data-datatype');
				}
				var nestedElement = '';
				if ($(item).attr('type') == 'radio' || $(item).attr('type') == 'checkbox') {
					if ($(item).prop('checked')) {

						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						var responseAttrs = [];
						responseAttrs.itemPrompt = $(item).attr('data-responsePrompt');
						responseAttrs.itemIdentifier = $(item).attr('data-responseIdentifier');
						var fillInNum = parseInt($(item).attr('data-fillin'), 10);
						if (fillInNum != NaN && fillInNum > 0) {
							var fillInId = '#' + $(item).attr('id') + '-fillin';
							responseAttrs.fill_in = $(fillInId).val();
						}

						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					} else {
						addQuestion = false;
					}
				} else {
					// Regular text field
					// Skip the fill-in input element
					if ($(item).attr('id').indexOf('fillin') > 0) {
						addQuestion = false;
					}
					// Skip text fields if no text
					var text = $(item).val();
					if (addQuestion && (text == undefined || text == null || text == '')) {
						addQuestion = false;
					}
					if (addQuestion) {
						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					}
				}
				if ($(item).attr('data-pattern')) {
					nestedElement += '\n' + " <!--  " + getXmlOutput.createElement('pattern', $(item).attr('data-pattern')) + " --> ";
				}
				if (addQuestion) {
					testSection += getXmlOutput.createElement('question', nestedElement, attrs) + '\n';
				}
			}
		});

		return testSection;
	}

	return {
		createElement : createElement,
		createPayload : createPayload
	};
})();

function buildRequest(payload, endpoint) {
	var submitUrl = endpoint;
	var formDesignIdentifier = $('#sdc_form').attr('data-formDesignIdentifier');
	var formRepresentationIdentifier = $('#sdc_form').attr('data-formRepresentationIdentifier');
	var requestString =
		'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">\n' +
		'  <soap:Header>\n' +
		'    <Action xmlns="http://www.w3.org/2005/08/addressing">urn:ihe:iti:2007:SubmitForm</Action>\n' +
		'    <MessageID xmlns="http://www.w3.org/2005/08/addressing">urn:uuid:' + guid() + '</MessageID>\n' +
		'    <To xmlns="http://www.w3.org/2005/08/addressing">' + submitUrl + '</To>\n' +
		'    <ReplyTo xmlns="http://www.w3.org/2005/08/addressing">\n' +
		'      <Address>http://www.w3.org/2005/08/addressing/anonymous</Address>\n' +
		'    </ReplyTo>\n' +
		'  </soap:Header>\n' +
		'  <soap:Body>\n' +
		'<SubmitFormRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
		'    xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../Schemas/RFD.xsd" xmlns="urn:ihe:iti:rfd:2007"\n' +
		'    xmlns:sdc="http://nlm.nih.gov/sdc/form">\n' +
		'       <form_data xmlns="http://nlm.nih.gov/sdc/form" form_design_identifier="' + formDesignIdentifier + '"\n' +
		'            form_representation_identifier="' + formRepresentationIdentifier + '">\n' +
		'<body>\n' + payload + '\n' +
		'    </body>\n' +
		'    </form_data>\n' +
		' </SubmitFormRequest>\n' +
		'  </soap:Body>\n' +
		'</soap:Envelope>';

	//console.log(requestString);

	return requestString;
}
var statusMsg = '';
function buildStatusMsg(statusCode, endpoint) {
	if (statusCode === 200 || statusCode == 304) {
		statusMsg += 'SUCCESSFUL Sending status=: ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	
	} else {
		statusMsg += 'ERROR Sending status= ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	}
}

function sendRequest(request, endpoint, msg) {

	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open('POST', endpoint, true);
	xmlhttp.setRequestHeader('Content-Type', 'application/soap+xml');

	xmlhttp.onreadystatechange = function (event) {
		if (xmlhttp.readyState === 4) {
			buildStatusMsg(xmlhttp.status, endpoint);
		}
	};

	xmlhttp.send(request);
}

function submitForm(e, endpoint) {
	if (jQuery.support.opacity == false) {
		//  alert('OLD browser');
		event.returnValue = false;
	} else {
		//   alert('NEW browser');
		e.preventDefault();
		e.stopPropagation();
	}
	// endpoint may contain multiple url's separated by '|', last char will always be '|'
	endpoint = endpoint.replace(/\s+/g, '');
	endpoint = endpoint.substr(0, endpoint.length - 1);
	var endpointArray = endpoint.split('|');

	var payload = getXmlOutput.createPayload();

	for (var i = 0; i < endpointArray.length; i++) {
		var request = buildRequest(payload, endpointArray[i]);
		sendRequest(request, endpointArray[i]);
	}
	setTimeout(function () {
		alert(statusMsg);
	}, 2000);
	return false;
}

/**
 * Generates a GUID string.
 * @returns {String} The generated GUID.
 * @example af8a8416-6e18-a307-bd9c-f2c947bbb3aa
 * @author Slavik Meltser (slavik@meltser.info).
 * @link http://slavik.meltser.info/?p=142
 */
function guid() {
	function _p8(s) {
		var p = (Math.random().toString(16) + "000000000").substr(2, 8);
		return s ? "-" + p.substr(0, 4) + "-" + p.substr(4, 4) : p;
	}
	return _p8() + _p8(true) + _p8(true) + _p8();
}
//
</script></head>
   <body id="form">
      <form method="post" id="sdc_form" data-formDesignIdentifier="Adrenal_xml_form" data-formRepresentationIdentifier="Adrenal_xml" action="#" onsubmit="submitForm(event,&#34;http://10.242.63.50:8080/RFD/Form/RFDSubmitForm_Service|https://10.242.63.50:8181/RFD/Form/RFDSubmitForm_Service|http://spojiti.crgmedical.com/SDCService_v3.asmx?WSDL|https://10.242.63.42:8080/SDCservice.asmx|http://10.242.63.42/SDCservice.asmx|https://10.242.63.41:7443/iheReceiver/services/receive|http://10.242.63.41:7080/iheReceiver/services/receive|https://10.242.63.36:8080/emarcreceiver|http://10.242.63.36/emarcreceiver|http://107.170.9.164:8080/SubmitFormTestService/SubmitForm_Service|&#34;)">
         <div id="form-heading-section">
            <h1 style="padding: 0 5px 0 5px"><span class="text-center"><strong>ADRENAL GLAND: Biopsy (Core Needle, Incisional, Excisional); Resection</strong></span><br></h1>
         </div>
         <p style="padding: 0 5px 0 5px">
            ADRENAL GLAND: Biopsy (Core Needle, Incisional, Excisional);
            Resection
            title
            
         </p>
         <p class="form-header-instruction" style="padding: 0 5px 0 5px">
            Surgical Pathology Cancer Case Summary
            (Checklist)
            subtitle
            
         </p>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Locked Section</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Tumor Site</h4>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> This question is not editable</p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2118" id="2119" value="2119" data-question-prompt="Tumor Site" data-question-identifier="2118" data-responsePrompt="Adrenal structure" data-responseIdentifier="2119" data-section-identifier="4257" data-fillin="">Adrenal structure</label></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> CLINICAL</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Non-Pathology Findings</h4>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> Note J</p>
                     <p style="margin: 0;"> Note K</p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20899" id="20900" value="20900" data-question-prompt="Non-Pathology Findings" data-question-identifier="20899" data-responsePrompt="Urinary 17-ketosteroids increased " data-responseIdentifier="20900" data-section-identifier="17537" data-fillin="">Urinary 17-ketosteroids increased </label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20899" id="20901" value="20901" data-question-prompt="Non-Pathology Findings" data-question-identifier="20899" data-responsePrompt="Hormone production" data-responseIdentifier="20901" data-section-identifier="17537" data-fillin="">Hormone production</label><div class="guarded-element-question"><b></b><p style="margin: 0;"> Non-Pathology Findings</p>
                           <p style="margin: 0;"> Note J</p>
                           <p style="margin: 0;"> Note K</p>
                           <ul style="list-style-type: none; margin: 2px 0 0 0">
                              <li><label><input type="checkbox" style="margin-right: 5px" name="24853" id="20902" value="" data-question-prompt="Non-Pathology Findings" data-question-identifier="24853" data-responsePrompt="Cushing syndrome" data-responseIdentifier="20902" data-section-identifier="17537" data-fillin="">Cushing syndrome</label></li>
                              <li><label><input type="checkbox" style="margin-right: 5px" name="24853" id="20904" value="" data-question-prompt="Non-Pathology Findings" data-question-identifier="24853" data-responsePrompt="Conn syndrome" data-responseIdentifier="20904" data-section-identifier="17537" data-fillin="">Conn syndrome</label></li>
                              <li><label><input type="checkbox" style="margin-right: 5px" name="24853" id="20905" value="" data-question-prompt="Non-Pathology Findings" data-question-identifier="24853" data-responsePrompt="Virilization / feminization" data-responseIdentifier="20905" data-section-identifier="17537" data-fillin="">Virilization / feminization</label></li>
                           </ul>
                        </div>
                     </li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20899" id="20906" value="" data-question-prompt="Non-Pathology Findings" data-question-identifier="20899" data-responsePrompt="Weight loss" data-responseIdentifier="20906" data-section-identifier="17537" data-fillin="">Weight loss</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20899" id="20906" value="" data-question-prompt="Non-Pathology Findings" data-question-identifier="20899" data-responsePrompt="Other (specify)" data-responseIdentifier="20906" data-section-identifier="17537" data-fillin="20">Other (specify)</label><input type="text" id="20906-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Neoadjuvant Therapy</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="20911" id="24854" value="" data-question-prompt="Neoadjuvant Therapy" data-question-identifier="20911" data-responsePrompt="Yes (specify type)" data-responseIdentifier="24854" data-section-identifier="17537" data-fillin="20">Yes (specify type)</label><input type="text" id="24854-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20911" id="20914" value="" data-question-prompt="Neoadjuvant Therapy" data-question-identifier="20911" data-responsePrompt="No" data-responseIdentifier="20914" data-section-identifier="17537" data-fillin="">No</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20911" id="20915" value="" data-question-prompt="Neoadjuvant Therapy" data-question-identifier="20911" data-responsePrompt="Indeterminate" data-responseIdentifier="20915" data-section-identifier="17537" data-fillin="20">Indeterminate</label><input type="text" id="20915-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question"><label for="d1e1008" class="question-prompt" style="display: block; font-weight: bold;">Other (specify)</label><input type="text" name="4156" id="d1e1025" size="4000" maxlength="4000" data-question-prompt="Other (specify)" data-datatype="string" data-section-identifier="17537" data-pattern="" data-question-repeat="1" data-question-identifier="4156"></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> SPECIMEN</h1>
               <div class="form-contained-section">
                  <h2> Specimen Size</h2>
                  <div class="form-contained-section">
                     <h2> Additional dimensions</h2>Repeat 10 timesResponse # 1
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 2
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 3
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 4
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 5
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 6
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 7
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 8
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 9
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>Response # 10
                     <div class="panel-question"><label for="d1e1129" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24069" id="d1e1148" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24069"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1173" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="20912" id="d1e1181" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="20912"><span style="margin-left: 1px">cm</span></div>
                     <div class="panel-question"><label for="d1e1204" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1212" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div><br><br><br><br><br><br><br><br><br><br><p style="margin: 0;"> repeat section if more than one part</p>
                  </div>
                  <div class="panel-question"><label for="d1e1242" class="question-prompt" style="display: block; font-weight: bold;">Greatest Dimension</label><input type="text" name="24068" id="d1e1259" size="30" maxlength="30" data-question-prompt="Greatest Dimension" data-datatype="decimal" data-section-identifier="20860" data-pattern="" data-question-repeat="1" data-question-identifier="24068"><span style="margin-left: 1px">cm</span></div>
                  <div class="panel-question"><label for="d1e1286" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24856" id="d1e1303" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="20860" data-pattern="" data-question-repeat="1" data-question-identifier="24856"><span style="margin-left: 1px">cm</span></div>
                  <div class="panel-question"><label for="d1e1327" class="question-prompt" style="display: block; font-weight: bold;">Additional Dimension</label><input type="text" name="24857" id="d1e1344" size="30" maxlength="30" data-question-prompt="Additional Dimension" data-datatype="decimal" data-section-identifier="20860" data-pattern="" data-question-repeat="1" data-question-identifier="24857"><span style="margin-left: 1px">cm</span></div>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Adrenal Gland Received</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="20850" id="20848" value="" data-question-prompt="Adrenal Gland Received" data-question-identifier="20850" data-responsePrompt="Fresh" data-responseIdentifier="20848" data-section-identifier="17875" data-fillin="">Fresh</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20850" id="20849" value="" data-question-prompt="Adrenal Gland Received" data-question-identifier="20850" data-responsePrompt="In formalin" data-responseIdentifier="20849" data-section-identifier="17875" data-fillin="">In formalin</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20850" id="20855" value="" data-question-prompt="Adrenal Gland Received" data-question-identifier="20850" data-responsePrompt="Other (specify)" data-responseIdentifier="20855" data-section-identifier="17875" data-fillin="20">Other (specify)</label><input type="text" id="20855-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Procedure</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2120" id="20856" value="" data-question-prompt="Procedure" data-question-identifier="2120" data-responsePrompt="Needle biopsy (radiographically guided)" data-responseIdentifier="20856" data-section-identifier="17875" data-fillin="">Needle biopsy (radiographically guided)</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2120" id="2122" value="" data-question-prompt="Procedure" data-question-identifier="2120" data-responsePrompt="Adrenalectomy, total" data-responseIdentifier="2122" data-section-identifier="17875" data-fillin="">Adrenalectomy, total</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2120" id="2121" value="" data-question-prompt="Procedure" data-question-identifier="2120" data-responsePrompt="Adrenalectomy, partial" data-responseIdentifier="2121" data-section-identifier="17875" data-fillin="">Adrenalectomy, partial</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2120" id="2123" value="" data-question-prompt="Procedure" data-question-identifier="2120" data-responsePrompt="Other (specify)" data-responseIdentifier="2123" data-section-identifier="17875" data-fillin="20">Other (specify)</label><input type="text" id="2123-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2120" id="2124" value="" data-question-prompt="Procedure" data-question-identifier="2120" data-responsePrompt="Not specified" data-responseIdentifier="2124" data-section-identifier="17875" data-fillin="20">Not specified</label><input type="text" id="2124-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Specimen Integrity</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="20858" id="20857" value="" data-question-prompt="Specimen Integrity" data-question-identifier="20858" data-responsePrompt="Intact" data-responseIdentifier="20857" data-section-identifier="17875" data-fillin="">Intact</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20858" id="20859" value="" data-question-prompt="Specimen Integrity" data-question-identifier="20858" data-responsePrompt="Fragmented" data-responseIdentifier="20859" data-section-identifier="17875" data-fillin="">Fragmented</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Specimen Laterality</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2125" id="2126" value="" data-question-prompt="Specimen Laterality" data-question-identifier="2125" data-responsePrompt="Right" data-responseIdentifier="2126" data-section-identifier="17875" data-fillin="">Right</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2125" id="2127" value="" data-question-prompt="Specimen Laterality" data-question-identifier="2125" data-responsePrompt="Left" data-responseIdentifier="2127" data-section-identifier="17875" data-fillin="">Left</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2125" id="2128" value="" data-question-prompt="Specimen Laterality" data-question-identifier="2125" data-responsePrompt="Not specified" data-responseIdentifier="2128" data-section-identifier="17875" data-fillin="20">Not specified</label><input type="text" id="2128-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2125" id="20866" value="" data-question-prompt="Specimen Laterality" data-question-identifier="2125" data-responsePrompt="Other (specify)" data-responseIdentifier="20866" data-section-identifier="17875" data-fillin="20">Other (specify)</label><input type="text" id="20866-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Tumor Size</h4>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> Note A</p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2130" id="2133" value="" data-question-prompt="Tumor Size" data-question-identifier="2130" data-responsePrompt="Greatest dimension" data-responseIdentifier="2133" data-section-identifier="17875" data-fillin="20">Greatest dimension</label><input type="text" id="2133-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"><div class="guarded-element-question"><b>Additional Dimension (cm)</b><input type="text" name="" id="d1e1843" size="30" maxlength="30" data-question-prompt="Additional Dimension (cm)" data-datatype="decimal" data-question-identifier="2133" data-pattern="" data-section-identifier="17875" data-question-repeat="1">cm
                        </div>
                        <div class="guarded-element-question"><b>Additional Dimension (cm)</b><input type="text" name="" id="d1e1884" size="30" maxlength="30" data-question-prompt="Additional Dimension (cm)" data-datatype="decimal" data-question-identifier="2132" data-pattern="" data-section-identifier="17875" data-question-repeat="1"></div>
                     </li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2130" id="20866" value="" data-question-prompt="Additional Dimension (cm)" data-question-identifier="2130" data-responsePrompt="Cannot be determined (fragmented specimen)" data-responseIdentifier="20866" data-section-identifier="17875" data-fillin="20">Cannot be determined (fragmented specimen)</label><input type="text" id="20866-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Tumor Gland Weight (Note B)</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="26236" id="26237" value="" data-question-prompt="Tumor Gland Weight (Note B)" data-question-identifier="26236" data-responsePrompt="Not applicable" data-responseIdentifier="26237" data-section-identifier="17875" data-fillin="20">Not applicable</label><input type="text" id="26237-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"><div class="guarded-element-question"><b>Specify Weight </b><input type="text" name="" id="d1e2000" size="30" maxlength="30" data-question-prompt="Specify Weight " data-datatype="decimal" data-question-identifier="2134" data-pattern="" data-section-identifier="17875" data-question-repeat="1">gram
                        </div>
                     </li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> TUMOR</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Histologic Type (Notes C through E)</h4>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> Note C</p>
                     <p style="margin: 0;"> Note D</p>
                     <p style="margin: 0;"> Note E</p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2116" id="2117" value="" data-question-prompt="Histologic Type (Notes C through E)" data-question-identifier="2116" data-responsePrompt="Adrenal cortical carcinoma" data-responseIdentifier="2117" data-section-identifier="17876" data-fillin="">Adrenal cortical carcinoma</label></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> EXTENT</h1>
               <div class="panel-question"><label for="d1e2192" class="question-prompt" style="display: block; font-weight: bold;">Microscopic Tumor Extension</label><input type="text" name="20873" id="d1e2212" size="30" maxlength="30" data-question-prompt="Microscopic Tumor Extension" data-datatype="string" data-section-identifier="17877" data-pattern="" data-question-repeat="1" data-question-identifier="20873"><span style="margin-left: 1px">Specify</span></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> MARGINS</h1>
               <div class="panel-question">
                  <h4 class="question-prompt"></h4>
                  <p style="margin: 0;">
                     This is a hidden question
                     
                  </p>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> Margin Status</p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2154" id="26365" value="" data-question-prompt="" data-question-identifier="2154" data-responsePrompt="Margins uninvolved by tumor" data-responseIdentifier="26365" data-section-identifier="17878" data-fillin="">Margins uninvolved by tumor</label><div class="guarded-element-question"><b>Distance from Closest Margin</b><ul style="list-style-type: none; margin: 2px 0 0 0">
                              <li><label><input type="radio" style="margin-right: 5px" name="26358" id="26359" value="" data-question-prompt="Distance from Closest Margin" data-question-identifier="26358" data-responsePrompt="Specify" data-responseIdentifier="26359" data-section-identifier="17878" data-fillin="">Specify</label></li>
                              <li><label><input type="radio" style="margin-right: 5px" name="26358" id="26361" value="" data-question-prompt="Distance from Closest Margin" data-question-identifier="26358" data-responsePrompt="Cannot be assessed" data-responseIdentifier="26361" data-section-identifier="17878" data-fillin="">Cannot be assessed</label></li>
                           </ul>
                        </div>
                        <div class="guarded-element-question"><b>Specify Margin, if possible</b><ul style="list-style-type: none; margin: 2px 0 0 0">
                              <li><label><input type="radio" style="margin-right: 5px" name="26362" id="26363" value="" data-question-prompt="Specify Margin, if possible" data-question-identifier="26362" data-responsePrompt="Specify margin" data-responseIdentifier="26363" data-section-identifier="17878" data-fillin="">Specify margin</label></li>
                              <li><label><input type="radio" style="margin-right: 5px" name="26362" id="26364" value="" data-question-prompt="Specify Margin, if possible" data-question-identifier="26362" data-responsePrompt="Cannot be determined" data-responseIdentifier="26364" data-section-identifier="17878" data-fillin="">Cannot be determined</label></li>
                           </ul>
                        </div>
                     </li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2154" id="2157" value="" data-question-prompt="Specify Margin, if possible" data-question-identifier="2154" data-responsePrompt="Cannot be determined" data-responseIdentifier="2157" data-section-identifier="17878" data-fillin="20">Cannot be determined</label><input type="text" id="2157-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2154" id="20852" value="" data-question-prompt="Specify Margin, if possible" data-question-identifier="2154" data-responsePrompt="Not applicable" data-responseIdentifier="20852" data-section-identifier="17878" data-fillin="20">Not applicable</label><input type="text" id="20852-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> ACCESSORY FINDINGS</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Treatment Effect </h4>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> applicable to carcinomas treated with neoadjuvant therapy</p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="20875" id="20876" value="" data-question-prompt="Treatment Effect " data-question-identifier="20875" data-responsePrompt="Not identified" data-responseIdentifier="20876" data-section-identifier="17879" data-fillin="20">Not identified</label><input type="text" id="20876-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20875" id="20877" value="" data-question-prompt="Treatment Effect " data-question-identifier="20875" data-responsePrompt="Present (specify)" data-responseIdentifier="20877" data-section-identifier="17879" data-fillin="20">Present (specify)</label><input type="text" id="20877-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20875" id="20878" value="" data-question-prompt="Treatment Effect " data-question-identifier="20875" data-responsePrompt="Indeterminate" data-responseIdentifier="20878" data-section-identifier="17879" data-fillin="20">Indeterminate</label><input type="text" id="20878-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Tumor Description</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20875" id="20863" value="" data-question-prompt="Tumor Description" data-question-identifier="20875" data-responsePrompt="Hemorrhagic" data-responseIdentifier="20863" data-section-identifier="17879" data-fillin="">Hemorrhagic</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20875" id="20864" value="" data-question-prompt="Tumor Description" data-question-identifier="20875" data-responsePrompt="Necrotic" data-responseIdentifier="20864" data-section-identifier="17879" data-fillin="">Necrotic</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20875" id="17883" value="" data-question-prompt="Tumor Description" data-question-identifier="20875" data-responsePrompt="Invasion" data-responseIdentifier="17883" data-section-identifier="17879" data-fillin="">Invasion</label><div class="guarded-element-question"><b></b><p style="margin: 0;"> Extent of Invasion</p>
                           <ul style="list-style-type: none; margin: 2px 0 0 0">
                              <li><label><input type="checkbox" style="margin-right: 5px" name="22900" id="20870" value="" data-question-prompt="No Question Prompt" data-question-identifier="22900" data-responsePrompt="Capsule" data-responseIdentifier="20870" data-section-identifier="17879" data-fillin="">Capsule</label></li>
                              <li><label><input type="checkbox" style="margin-right: 5px" name="22900" id="20871" value="" data-question-prompt="No Question Prompt" data-question-identifier="22900" data-responsePrompt="Vessels" data-responseIdentifier="20871" data-section-identifier="17879" data-fillin="">Vessels</label></li>
                              <li><label><input type="checkbox" style="margin-right: 5px" name="22900" id="20872" value="" data-question-prompt="No Question Prompt" data-question-identifier="22900" data-responsePrompt="Extra-adrenal (specify)" data-responseIdentifier="20872" data-section-identifier="17879" data-fillin="20">Extra-adrenal (specify)</label><input type="text" id="20872-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                           </ul>
                        </div>
                     </li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20875" id="20865" value="" data-question-prompt="No Question Prompt" data-question-identifier="20875" data-responsePrompt="Other (specify)" data-responseIdentifier="20865" data-section-identifier="17879" data-fillin="20">Other (specify)</label><input type="text" id="20865-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Lymph-Vascular Invasion</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2158" id="2159" value="" data-question-prompt="Lymph-Vascular Invasion" data-question-identifier="2158" data-responsePrompt="Not identified" data-responseIdentifier="2159" data-section-identifier="17879" data-fillin="20">Not identified</label><input type="text" id="2159-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2158" id="2160" value="" data-question-prompt="Lymph-Vascular Invasion" data-question-identifier="2158" data-responsePrompt="Present" data-responseIdentifier="2160" data-section-identifier="17879" data-fillin="">Present</label><div class="guarded-element-question"><b></b>
                           Lymph-Vascular Invasion 
                           
                           <p style="margin: 0;"> Note F</p>
                           <ul style="list-style-type: none; margin: 2px 0 0 0">
                              <li><label><input type="checkbox" style="margin-right: 5px" name="20861" id="20853" value="" data-question-prompt="No Question Prompt" data-question-identifier="20861" data-responsePrompt="Large vessel (venous)" data-responseIdentifier="20853" data-section-identifier="17879" data-fillin="">Large vessel (venous)</label></li>
                              <li><label><input type="checkbox" style="margin-right: 5px" name="20861" id="20881" value="" data-question-prompt="No Question Prompt" data-question-identifier="20861" data-responsePrompt="Small vessel (capillary lymphatic)" data-responseIdentifier="20881" data-section-identifier="17879" data-fillin="">Small vessel (capillary lymphatic)</label></li>
                           </ul>
                        </div>
                     </li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2158" id="2161" value="" data-question-prompt="No Question Prompt" data-question-identifier="2158" data-responsePrompt="Indeterminate" data-responseIdentifier="2161" data-section-identifier="17879" data-fillin="20">Indeterminate</label><input type="text" id="2161-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Perineural Invasion</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="20882" id="20879" value="" data-question-prompt="Perineural Invasion" data-question-identifier="20882" data-responsePrompt="Not identified" data-responseIdentifier="20879" data-section-identifier="17879" data-fillin="20">Not identified</label><input type="text" id="20879-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20882" id="20884" value="" data-question-prompt="Perineural Invasion" data-question-identifier="20882" data-responsePrompt="Present" data-responseIdentifier="20884" data-section-identifier="17879" data-fillin="">Present</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20882" id="20883" value="" data-question-prompt="Perineural Invasion" data-question-identifier="20882" data-responsePrompt="Indeterminate" data-responseIdentifier="20883" data-section-identifier="17879" data-fillin="20">Indeterminate</label><input type="text" id="20883-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> SPECIAL STUDIES</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Ancillary Studies</h4>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> Note L</p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="checkbox" style="margin-right: 5px" name="6202" id="20908" value="" data-question-prompt="Ancillary Studies" data-question-identifier="6202" data-responsePrompt="Specify type (s)" data-responseIdentifier="20908" data-section-identifier="17880" data-fillin="20">Specify type (s)</label><input type="text" id="20908-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="6202" id="20909" value="" data-question-prompt="Ancillary Studies" data-question-identifier="6202" data-responsePrompt="Specify result(s)" data-responseIdentifier="20909" data-section-identifier="17880" data-fillin="20">Specify result(s)</label><input type="text" id="20909-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> LYMPH NODES</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Lymph Nodes, Extranodal Extension</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="20885" id="1850" value="" data-question-prompt="Lymph Nodes, Extranodal Extension" data-question-identifier="20885" data-responsePrompt="No nodes submitted or found" data-responseIdentifier="1850" data-section-identifier="17881" data-fillin="">No nodes submitted or found</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20885" id="20886" value="" data-question-prompt="Lymph Nodes, Extranodal Extension" data-question-identifier="20885" data-responsePrompt="Specify result(s)" data-responseIdentifier="20886" data-section-identifier="17881" data-fillin="20">Specify result(s)</label><input type="text" id="20886-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20885" id="20887" value="" data-question-prompt="Lymph Nodes, Extranodal Extension" data-question-identifier="20885" data-responsePrompt="Present" data-responseIdentifier="20887" data-section-identifier="17881" data-fillin="">Present</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="20885" id="20888" value="" data-question-prompt="Lymph Nodes, Extranodal Extension" data-question-identifier="20885" data-responsePrompt="Indeterminate" data-responseIdentifier="20888" data-section-identifier="17881" data-fillin="20">Indeterminate</label><input type="text" id="20888-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> STAGE</h1>
               <p style="margin-left: 3px">pTNM Note G</p>
               <div class="panel-question">
                  <h4 class="question-prompt">?TNM Descriptors</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20880" id="22897" value="" data-question-prompt="?TNM Descriptors" data-question-identifier="20880" data-responsePrompt="?Not applicable" data-responseIdentifier="22897" data-section-identifier="2136" data-fillin="20">?Not applicable</label><input type="text" id="22897-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20880" id="20890" value="" data-question-prompt="?TNM Descriptors" data-question-identifier="20880" data-responsePrompt="m (multiple primary tumors)" data-responseIdentifier="20890" data-section-identifier="2136" data-fillin="">m (multiple primary tumors)</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20880" id="20891" value="" data-question-prompt="?TNM Descriptors" data-question-identifier="20880" data-responsePrompt="r (recurrent)" data-responseIdentifier="20891" data-section-identifier="2136" data-fillin="">r (recurrent)</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="20880" id="20892" value="" data-question-prompt="?TNM Descriptors" data-question-identifier="20880" data-responsePrompt="y (post-treatment)" data-responseIdentifier="20892" data-section-identifier="2136" data-fillin="">y (post-treatment)</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Primary Tumor (pT)</h4>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> Note: There is no category of carcinoma in situ (pTis) relative to
                        carcinomas of the adrenal gland.
                     </p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2137" id="2142" value="" data-question-prompt="Primary Tumor (pT)" data-question-identifier="2137" data-responsePrompt="pTX: Cannot be determined" data-responseIdentifier="2142" data-section-identifier="2136" data-fillin="20">pTX: Cannot be determined</label><input type="text" id="2142-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2137" id="20889" value="" data-question-prompt="Primary Tumor (pT)" data-question-identifier="2137" data-responsePrompt="pT0: No evidence of primary tumor" data-responseIdentifier="20889" data-section-identifier="2136" data-fillin="">pT0: No evidence of primary tumor</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2137" id="2138" value="" data-question-prompt="Primary Tumor (pT)" data-question-identifier="2137" data-responsePrompt="pT1: Tumor 5 cm or less in greatest dimension, no&#xA;                                    extra-adrenal invasion" data-responseIdentifier="2138" data-section-identifier="2136" data-fillin="">pT1: Tumor 5 cm or less in greatest dimension, no
                           extra-adrenal invasion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2137" id="2139" value="" data-question-prompt="Primary Tumor (pT)" data-question-identifier="2137" data-responsePrompt="pT2: Tumor greater than 5 cm, no extra-adrenal&#xA;                                    invasion" data-responseIdentifier="2139" data-section-identifier="2136" data-fillin="">pT2: Tumor greater than 5 cm, no extra-adrenal
                           invasion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2137" id="20893" value="" data-question-prompt="Primary Tumor (pT)" data-question-identifier="2137" data-responsePrompt="" data-responseIdentifier="20893" data-section-identifier="2136" data-fillin=""></label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2137" id="2140" value="" data-question-prompt="Primary Tumor (pT)" data-question-identifier="2137" data-responsePrompt="pT3: Tumor of any size with local invasion, but not invading&#xA;                                    adjacent organs#" data-responseIdentifier="2140" data-section-identifier="2136" data-fillin="">pT3: Tumor of any size with local invasion, but not invading
                           adjacent organs#</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2137" id="2141" value="" data-question-prompt="Primary Tumor (pT)" data-question-identifier="2137" data-responsePrompt="pT4: Tumor of any size with invasion of adjacent&#xA;                                    organs#" data-responseIdentifier="2141" data-section-identifier="2136" data-fillin="">pT4: Tumor of any size with invasion of adjacent
                           organs#</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Distant Metastasis (pM)</h4>
                  <p style="margin: 0;">
                     Note I
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2149" id="20895" value="" data-question-prompt="Distant Metastasis (pM)" data-question-identifier="2149" data-responsePrompt="Not applicable" data-responseIdentifier="20895" data-section-identifier="2136" data-fillin="20">Not applicable</label><input type="text" id="20895-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2149" id="2151" value="" data-question-prompt="Distant Metastasis (pM)" data-question-identifier="2149" data-responsePrompt="pM1: Distant metastasis" data-responseIdentifier="2151" data-section-identifier="2136" data-fillin="">pM1: Distant metastasis</label><div class="guarded-element-question"><b>Specify Site(s), if known</b><input type="text" name="" id="d1e4153" size="30" maxlength="30" data-question-prompt="Specify Site(s), if known" data-datatype="string" data-question-identifier="2152" data-pattern="" data-section-identifier="2136" data-question-repeat="1"></div>
                     </li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Regional Lymph Nodes (pN)</h4>
                  <div style="font-style: italic;">
                     <p style="margin: 0;"> Note H</p>
                  </div>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2143" id="2144" value="" data-question-prompt="Regional Lymph Nodes (pN)" data-question-identifier="2143" data-responsePrompt="pNX: Cannot be assessed" data-responseIdentifier="2144" data-section-identifier="2136" data-fillin="20">pNX: Cannot be assessed</label><input type="text" id="2144-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2143" id="12600" value="" data-question-prompt="Regional Lymph Nodes (pN)" data-question-identifier="2143" data-responsePrompt="pN0: No regional lymph node metastasis" data-responseIdentifier="12600" data-section-identifier="2136" data-fillin="">pN0: No regional lymph node metastasis</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2143" id="2146" value="" data-question-prompt="Regional Lymph Nodes (pN)" data-question-identifier="2143" data-responsePrompt="pN1: Regional lymph node metastasis" data-responseIdentifier="2146" data-section-identifier="2136" data-fillin="">pN1: Regional lymph node metastasis</label><div class="guarded-element-question"><b></b><p style="margin: 0;"> Status of Regional Lymph Nodes</p>
                           <ul style="list-style-type: none; margin: 2px 0 0 0">
                              <li><label><input type="checkbox" style="margin-right: 5px" name="1867" id="1868" value="" data-question-prompt="Regional Lymph Nodes (pN)" data-question-identifier="1867" data-responsePrompt="No nodes submitted or found" data-responseIdentifier="1868" data-section-identifier="2136" data-fillin="">No nodes submitted or found</label><div class="guarded-element-question"><b>Number of Lymph Nodes Examined</b><ul style="list-style-type: none; margin: 2px 0 0 0">
                                       <li><label><input type="radio" style="margin-right: 5px" name="1869" id="1870" value="" data-question-prompt="Number of Lymph Nodes Examined" data-question-identifier="1869" data-responsePrompt="Specify" data-responseIdentifier="1870" data-section-identifier="2136" data-fillin="">Specify</label></li>
                                       <li><label><input type="radio" style="margin-right: 5px" name="1869" id="1871" value="" data-question-prompt="Number of Lymph Nodes Examined" data-question-identifier="1869" data-responsePrompt="Number cannot be determined&#xA;                                                  (explain)" data-responseIdentifier="1871" data-section-identifier="2136" data-fillin="">Number cannot be determined
                                             (explain)</label></li>
                                    </ul>
                                 </div>
                                 <div class="guarded-element-question"><b>Number of Lymph Nodes Involved</b><ul style="list-style-type: none; margin: 2px 0 0 0">
                                       <li><label><input type="radio" style="margin-right: 5px" name="1872" id="1873" value="" data-question-prompt="Number of Lymph Nodes Involved" data-question-identifier="1872" data-responsePrompt="Specify" data-responseIdentifier="1873" data-section-identifier="2136" data-fillin="">Specify</label></li>
                                       <li><label><input type="radio" style="margin-right: 5px" name="1872" id="1874" value="" data-question-prompt="Number of Lymph Nodes Involved" data-question-identifier="1872" data-responsePrompt="Number cannot be determined&#xA;                                                  (explain)" data-responseIdentifier="1874" data-section-identifier="2136" data-fillin="">Number cannot be determined
                                             (explain)</label></li>
                                    </ul>
                                 </div>
                              </li>
                           </ul>
                        </div>
                     </li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> ADDITIONAL NON-TUMOR</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Additional Pathologic Findings</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="checkbox" style="margin-right: 5px" name="2162" id="2163" value="" data-question-prompt="Additional Pathologic Findings" data-question-identifier="2162" data-responsePrompt="None identified" data-responseIdentifier="2163" data-section-identifier="17884" data-fillin="">None identified</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="2162" id="14300" value="" data-question-prompt="Additional Pathologic Findings" data-question-identifier="2162" data-responsePrompt="Tumor necrosis" data-responseIdentifier="14300" data-section-identifier="17884" data-fillin="">Tumor necrosis</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="2162" id="20896" value="" data-question-prompt="Additional Pathologic Findings" data-question-identifier="2162" data-responsePrompt="Degenerative changes" data-responseIdentifier="20896" data-section-identifier="17884" data-fillin="">Degenerative changes</label><div class="guarded-element-question"><b></b><p style="margin: 0;"> Type of Degenerative Changes</p>
                           <ul style="list-style-type: none; margin: 2px 0 0 0">
                              <li><label><input type="checkbox" style="margin-right: 5px" name="22900" id="20854" value="" data-question-prompt="Additional Pathologic Findings" data-question-identifier="22900" data-responsePrompt="Calcifications" data-responseIdentifier="20854" data-section-identifier="17884" data-fillin="">Calcifications</label></li>
                              <li><label><input type="checkbox" style="margin-right: 5px" name="22900" id="20897" value="" data-question-prompt="Additional Pathologic Findings" data-question-identifier="22900" data-responsePrompt="Hemorrhage" data-responseIdentifier="20897" data-section-identifier="17884" data-fillin="">Hemorrhage</label></li>
                              <li><label><input type="checkbox" style="margin-right: 5px" name="22900" id="20898" value="" data-question-prompt="Additional Pathologic Findings" data-question-identifier="22900" data-responsePrompt="Cystic change" data-responseIdentifier="20898" data-section-identifier="17884" data-fillin="">Cystic change</label></li>
                           </ul>
                        </div>
                     </li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="2162" id="2167" value="" data-question-prompt="Additional Pathologic Findings" data-question-identifier="2162" data-responsePrompt="Other (specify)" data-responseIdentifier="2167" data-section-identifier="17884" data-fillin="20">Other (specify)</label><input type="text" id="2167-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <div class="panel-question"><label for="d1e4913" class="question-prompt" style="display: block; font-weight: bold;">Comment(s)</label><input type="text" name="2168" id="d1e4933" size="30" maxlength="30" data-question-prompt="Comment(s)" data-datatype="string" data-section-identifier="99999" data-pattern="" data-question-repeat="1" data-question-identifier="2168"></div>
            </div>
         </section>College of American Pathologist (CAP)<input type="submit" value="Send Info"><input type="reset"></form>
   </body>
</html>
]]>   
            </sdc:sdc_html_form>
         </sdc_html_package>
      </Structured>
      
      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID></instanceID>
   </form>

   <contentType>HTML</contentType>
   
   <responseCode>Request succeeded</responseCode>
</RetrieveFormResponse>

"""



demographic_html = """<RetrieveFormResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form"
   xmlns:mfi13="http://www.iso.org/19763/13/2013"
   xmlns:dex="urn:ihe:qrph:dex:2013"
   xmlns:mfi6="http://www.iso.org/19763/6/2013"
   xmlns:mdr3="http://www.iso.org/11179/3/2013"
   >
   <form>
      <Structured>
         <sdc_html_package>
            
            <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
            <sdc:supplemental_data>
               <anyXMLContentType></anyXMLContentType>          
            </sdc:supplemental_data>
            
            <!-- Contains mapping, and administrative info; this is the same content as from the form design package -->
            <sdc:form_info>               
               <anyXMLContentType></anyXMLContentType>          
            </sdc:form_info>
            <!-- USHIK will provide actual HTML content using automated transformation utility -->
            <sdc:sdc_html_form>
               
               <![CDATA[
<!DOCTYPE html
  SYSTEM "about:legacy-compat">

<html>
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <title>Administration and Demographic Data for Public Health Reporting</title><style>
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
                    }</style><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script><script type="text/javascript">//
$(function () {
	/*
	 * Process checkboxes and radio buttons so if a parent checkbox/radio button is unchecked, children are unchecked,
	 * if child checked then check parent, etc.
	 */
	var $parentCheckboxes = $('.guarded-element-question').parent().find('input[type=checkbox]:first');
	$parentCheckboxes.each(function () {
		var $parentCheckbox = $(this);
		var $childrenCheckboxes = $parentCheckbox.closest('li').find('ul li input[type=checkbox], input[type=radio]');

		if ($childrenCheckboxes.length > 0) {
			$childrenCheckboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=checkbox], input[type=radio]').is(':checked');
				$parentCheckbox.prop('checked', $anyChildrenChecked);
			});

			$parentCheckbox.click(function () {
				if (!($(this).is(':checked'))) {
					$(this).closest('li').find('ul li input[type=checkbox], input[type=radio]').prop('checked', $(this).prop('checked'));
				}
			})
		}
	});

	var $parentRadioboxes = $('.guarded-element-question').parent().find('input[type=radio]:first');
	$parentRadioboxes.each(function () {
		var $parentRadiobox = $(this);

		var $childrenRadioboxes = $parentRadiobox.closest('li').find('ul li input[type=radio]');
		if ($childrenRadioboxes.length > 0) {
			$childrenRadioboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=radio]').is(':checked');
				$parentRadiobox.prop('checked', $anyChildrenChecked);
			});

			$parentRadiobox.closest('li').siblings().find('input[type=radio]').change(function () {
				$childrenRadioboxes.each(function () {
					$(this).prop('checked', false);
				});
			});
		}
	})
});

var getXmlOutput = (function () {
	'use strict'
	function formatAttributes(attributes) {
		var
		SINGLE_QUOTE = "'",
		DOUBLE_QUOTE = '"',
		ESCAPED_QUOTE = {
			SINGLE_QUOTE : '&quot;',
			DOUBLE_QUOTE : '&apos;'
		};
		var
		att_value,
		single_quote_pos,
		double_quote_pos,
		use_quote,
		escape,
		quote_to_escape,
		att_str,
		re,
		result = '';
		for (var att in attributes) {
			att_value = '' + attributes[att];
			single_quote_pos = att_value.indexOf(SINGLE_QUOTE);
			double_quote_pos = att_value.indexOf(DOUBLE_QUOTE);
			if (single_quote_pos !=  - 1 && double_quote_pos !=  - 1) {
				att_str = ' ' + att + "='" + att_value + "'";
				result += att_str;
				continue;
			}
			if (double_quote_pos !=  - 1 && double_quote_pos < apos_pos) {
				use_quote = SINGLE_QUOTE;
			} else {
				use_quote = DOUBLE_QUOTE;
			}
			escape = ESCAPED_QUOTE[use_quote];
			re = new RegExp(use_quote, 'g');
			att_str = '\n' + '  ' + att + '=' + use_quote + att_value.replace(re, escape) + use_quote;
			result += att_str;
		}
		return result;
	}
	/*
	 *	Public functions
	 */
	function createElement(name, content, attributes) {
		var att_str = '';
		if (attributes) {
			att_str = formatAttributes(attributes);
		}
		var xml;
		if (!content) {
			xml = '<' + name + att_str + '>' + '</' + name + '>';
		} else {
			xml = '<' + name + att_str + '>' + content + '</' + name + '>';
		}
		return xml;
	}
	var repeat_master_list = {};
	function recordRepeatOfQuestion(questionId) {
		var count = repeat_master_list[questionId];
		if (count == null || count == undefined) {
			count = 0;
		}
		++count;
		repeat_master_list[questionId] = count;
		return count;
	}

	function createPayload() {
		var testSection = "";
		$('input').each(function (index, item) {
			var addQuestion = true;

			/* Skip the last two inputs - submit & reset */
			if ($(item).attr('type') != 'submit' && $(item).attr('type') != 'reset') {
				var attrs = [];
				attrs.section_identifier = $(item).attr('data-section-identifier');
				attrs.question_identifier = $(item).attr('data-question-identifier');
				attrs.question_prompt = $(item).attr('data-question-prompt');

				var dtype = $(item).attr('data-datatype');
				if (dtype != undefined && dtype != null && dtype != '') {
					attrs.datatype = $(item).attr('data-datatype');
				}
				var nestedElement = '';
				if ($(item).attr('type') == 'radio' || $(item).attr('type') == 'checkbox') {
					if ($(item).prop('checked')) {

						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						var responseAttrs = [];
						responseAttrs.itemPrompt = $(item).attr('data-responsePrompt');
						responseAttrs.itemIdentifier = $(item).attr('data-responseIdentifier');
						var fillInNum = parseInt($(item).attr('data-fillin'), 10);
						if (fillInNum != NaN && fillInNum > 0) {
							var fillInId = '#' + $(item).attr('id') + '-fillin';
							responseAttrs.fill_in = $(fillInId).val();
						}

						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					} else {
						addQuestion = false;
					}
				} else {
					// Regular text field
					// Skip the fill-in input element
					if ($(item).attr('id').indexOf('fillin') > 0) {
						addQuestion = false;
					}
					// Skip text fields if no text
					var text = $(item).val();
					if (addQuestion && (text == undefined || text == null || text == '')) {
						addQuestion = false;
					}
					if (addQuestion) {
						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					}
				}
				if ($(item).attr('data-pattern')) {
					nestedElement += '\n' + " <!--  " + getXmlOutput.createElement('pattern', $(item).attr('data-pattern')) + " --> ";
				}
				if (addQuestion) {
					testSection += getXmlOutput.createElement('question', nestedElement, attrs) + '\n';
				}
			}
		});

		return testSection;
	}

	return {
		createElement : createElement,
		createPayload : createPayload
	};
})();

function buildRequest(payload, endpoint) {
	var submitUrl = endpoint;
	var formDesignIdentifier = $('#sdc_form').attr('data-formDesignIdentifier');
	var formRepresentationIdentifier = $('#sdc_form').attr('data-formRepresentationIdentifier');
	var requestString =
		'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">\n' +
		'  <soap:Header>\n' +
		'    <Action xmlns="http://www.w3.org/2005/08/addressing">urn:ihe:iti:2007:SubmitForm</Action>\n' +
		'    <MessageID xmlns="http://www.w3.org/2005/08/addressing">urn:uuid:' + guid() + '</MessageID>\n' +
		'    <To xmlns="http://www.w3.org/2005/08/addressing">' + submitUrl + '</To>\n' +
		'    <ReplyTo xmlns="http://www.w3.org/2005/08/addressing">\n' +
		'      <Address>http://www.w3.org/2005/08/addressing/anonymous</Address>\n' +
		'    </ReplyTo>\n' +
		'  </soap:Header>\n' +
		'  <soap:Body>\n' +
		'<SubmitFormRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
		'    xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../Schemas/RFD.xsd" xmlns="urn:ihe:iti:rfd:2007"\n' +
		'    xmlns:sdc="http://nlm.nih.gov/sdc/form">\n' +
		'       <form_data xmlns="http://nlm.nih.gov/sdc/form" form_design_identifier="' + formDesignIdentifier + '"\n' +
		'            form_representation_identifier="' + formRepresentationIdentifier + '">\n' +
		'<body>\n' + payload + '\n' +
		'    </body>\n' +
		'    </form_data>\n' +
		' </SubmitFormRequest>\n' +
		'  </soap:Body>\n' +
		'</soap:Envelope>';

	//console.log(requestString);

	return requestString;
}
var statusMsg = '';
function buildStatusMsg(statusCode, endpoint) {
	if (statusCode === 200 || statusCode == 304) {
		statusMsg += 'SUCCESSFUL Sending status=: ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	
	} else {
		statusMsg += 'ERROR Sending status= ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	}
}

function sendRequest(request, endpoint, msg) {

	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open('POST', endpoint, true);
	xmlhttp.setRequestHeader('Content-Type', 'application/soap+xml');

	xmlhttp.onreadystatechange = function (event) {
		if (xmlhttp.readyState === 4) {
			buildStatusMsg(xmlhttp.status, endpoint);
		}
	};

	xmlhttp.send(request);
}

function submitForm(e, endpoint) {
	if (jQuery.support.opacity == false) {
		//  alert('OLD browser');
		event.returnValue = false;
	} else {
		//   alert('NEW browser');
		e.preventDefault();
		e.stopPropagation();
	}
	// endpoint may contain multiple url's separated by '|', last char will always be '|'
	endpoint = endpoint.replace(/\s+/g, '');
	endpoint = endpoint.substr(0, endpoint.length - 1);
	var endpointArray = endpoint.split('|');

	var payload = getXmlOutput.createPayload();

	for (var i = 0; i < endpointArray.length; i++) {
		var request = buildRequest(payload, endpointArray[i]);
		sendRequest(request, endpointArray[i]);
	}
	setTimeout(function () {
		alert(statusMsg);
	}, 2000);
	return false;
}

/**
 * Generates a GUID string.
 * @returns {String} The generated GUID.
 * @example af8a8416-6e18-a307-bd9c-f2c947bbb3aa
 * @author Slavik Meltser (slavik@meltser.info).
 * @link http://slavik.meltser.info/?p=142
 */
function guid() {
	function _p8(s) {
		var p = (Math.random().toString(16) + "000000000").substr(2, 8);
		return s ? "-" + p.substr(0, 4) + "-" + p.substr(4, 4) : p;
	}
	return _p8() + _p8(true) + _p8(true) + _p8();
}
//
</script></head>
   <body id="form">
      <form method="post" id="sdc_form" data-formDesignIdentifier="EHR_Demog_xml_form" data-formRepresentationIdentifier="EHR_Demog_xml_response.xml" action="#" onsubmit="submitForm(event,&#34;http://http://cdc8/emarcreceiver2/Service.asmx&#34;)">
         <div id="form-heading-section">
            <h1 style="padding: 0 5px 0 5px"><span class="text-center"><strong>Administration and Demographic Data for Public Health Reporting</strong></span><br></h1>
         </div>
         <p style="padding: 0 5px 0 5px">
            Patient's Identification
            title
            
         </p>
         <div class="panel-question"><label for="d1e526" class="question-prompt" style="display: block; font-weight: bold;">Date/Time of Report</label><div style="font-style: italic;">
               <p style="margin: 0;"> Value should be generated by computer</p>
            </div><input type="text" name="2036873" id="d1e545" size="30" maxlength="30" data-question-prompt="Date/Time of Report" data-datatype="string_date" data-section-identifier="" data-pattern="(YYYYMMDDHHMMSS.UUUU[+|-ZZzz])" data-question-repeat="" data-question-identifier="2036873"></div>
         <div class="panel-question"><label for="d1e571" class="question-prompt" style="display: block; font-weight: bold;">Patient's First Name</label><input type="text" name="2036874" id="d1e582" size="40" maxlength="40" data-question-prompt="Patient's First Name" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="2036874"></div>
         <div class="panel-question"><label for="d1e603" class="question-prompt" style="display: block; font-weight: bold;">Patient's Last Name</label><input type="text" name="2036875" id="d1e614" size="40" maxlength="40" data-question-prompt="Patient's Last Name" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="2036875"></div>
         <div class="panel-question"><label for="d1e635" class="question-prompt" style="display: block; font-weight: bold;">Patient's Middle Name</label><input type="text" name="2036876" id="d1e655" size="40" maxlength="40" data-question-prompt="Patient's Middle Name" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="1" data-question-identifier="2036876"></div>
         <div class="panel-question">
            <h4 class="question-prompt">Patient's Gender Code</h4>
            <ul style="list-style-type: none; margin: 2px 0 0 0">
               <li><label><input type="radio" style="margin-right: 5px" name="2036901" id="27839" value="F" data-question-prompt="Patient's Gender Code" data-question-identifier="2036901" data-responsePrompt="Female" data-responseIdentifier="27839" data-section-identifier="" data-fillin="">Female</label></li>
               <li><label><input type="radio" style="margin-right: 5px" name="2036901" id="27844" value="M" data-question-prompt="Patient's Gender Code" data-question-identifier="2036901" data-responsePrompt="Male" data-responseIdentifier="27844" data-section-identifier="" data-fillin="">Male</label></li>
               <li><label><input type="radio" style="margin-right: 5px" name="2036901" id="27845" value="UN" data-question-prompt="Patient's Gender Code" data-question-identifier="2036901" data-responsePrompt="Undifferentiated" data-responseIdentifier="27845" data-section-identifier="" data-fillin="">Undifferentiated</label></li>
            </ul>
         </div>
         <div class="panel-question">
            <h4 class="question-prompt">Gender</h4>
            <ul style="list-style-type: none; margin: 2px 0 0 0">
               <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575551/1.0" value="Female" data-question-prompt="Gender" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" data-responsePrompt="Female Gender" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575551/1.0" data-section-identifier="" data-fillin="">Female Gender</label></li>
               <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575550/1.0" value="Male" data-question-prompt="Gender" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" data-responsePrompt="Male Gender" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575550/1.0" data-section-identifier="" data-fillin="">Male Gender</label></li>
               <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575365/1.0" value="Unknown" data-question-prompt="Gender" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" data-responsePrompt="Unknown" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575365/1.0" data-section-identifier="" data-fillin="">Unknown</label></li>
               <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2573360/1.0" value="Unspecified" data-question-prompt="Gender" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" data-responsePrompt="Unspecified" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2573360/1.0" data-section-identifier="" data-fillin="">Unspecified</label></li>
            </ul>
         </div>
         <div class="panel-question"><label for="d1e1012" class="question-prompt" style="display: block; font-weight: bold;">Patient's Date of Birth</label><input type="text" name="2036877" id="d1e1023" size="30" maxlength="30" data-question-prompt="Patient's Date of Birth" data-datatype="string_date" data-section-identifier="" data-pattern="(YYYYMMDD)" data-question-repeat="" data-question-identifier="2036877"></div>
         <div class="panel-question"><label for="d1e1047" class="question-prompt" style="display: block; font-weight: bold;">Patient's Social Security Number</label><input type="text" name="27841" id="d1e1058" size="30" maxlength="30" data-question-prompt="Patient's Social Security Number" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="27841"></div>
         <div class="panel-question"><label for="d1e1079" class="question-prompt" style="display: block; font-weight: bold;">Patient's Medical Record Number</label><input type="text" name="2036878" id="d1e1090" size="30" maxlength="30" data-question-prompt="Patient's Medical Record Number" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="2036878"></div>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Patient's Contact Information</h1>
               <div class="panel-question"><label for="d1e1133" class="question-prompt" style="display: block; font-weight: bold;">Patient's Street Address</label><input type="text" name="2036880" id="d1e1146" size="30" maxlength="30" data-question-prompt="Patient's Street Address" data-datatype="string" data-section-identifier="2036879" data-pattern="" data-question-repeat="" data-question-identifier="2036880"></div>
               <div class="panel-question">
                  <h4 class="question-prompt">Patient's City</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2036881" id="2036882" value="351615" data-question-prompt="Patient's City" data-question-identifier="2036881" data-responsePrompt="Atlanta, GA, Fulton" data-responseIdentifier="2036882" data-section-identifier="2036879" data-fillin="">Atlanta, GA, Fulton</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2036881" id="2036883" value="655030" data-question-prompt="Patient's City" data-question-identifier="2036881" data-responsePrompt="Minneapolis, MN, Hennepin" data-responseIdentifier="2036883" data-section-identifier="2036879" data-fillin="">Minneapolis, MN, Hennepin</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2036881" id="2200" value="423587" data-question-prompt="Patient's City" data-question-identifier="2036881" data-responsePrompt="Chicago, IL, Cook" data-responseIdentifier="2200" data-section-identifier="2036879" data-fillin="">Chicago, IL, Cook</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Patient's State</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2036885" id="2036886" value="13" data-question-prompt="Patient's State" data-question-identifier="2036885" data-responsePrompt="Georgia" data-responseIdentifier="2036886" data-section-identifier="2036879" data-fillin="">Georgia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2036885" id="2036887" value="27" data-question-prompt="Patient's State" data-question-identifier="2036885" data-responsePrompt="Minnesota" data-responseIdentifier="2036887" data-section-identifier="2036879" data-fillin="">Minnesota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2036885" id="2036888" value="17" data-question-prompt="Patient's State" data-question-identifier="2036885" data-responsePrompt="Illinois" data-responseIdentifier="2036888" data-section-identifier="2036879" data-fillin="">Illinois</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Patient's Zip Code</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2036890" id="2036891" value="30301" data-question-prompt="Patient's Zip Code" data-question-identifier="2036890" data-responsePrompt="30301" data-responseIdentifier="2036891" data-section-identifier="2036879" data-fillin="">30301</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2036890" id="2036892" value="60609" data-question-prompt="Patient's Zip Code" data-question-identifier="2036890" data-responsePrompt="60609" data-responseIdentifier="2036892" data-section-identifier="2036879" data-fillin="">60609</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2036890" id="2036893" value="55401" data-question-prompt="Patient's Zip Code" data-question-identifier="2036890" data-responsePrompt="55401" data-responseIdentifier="2036893" data-section-identifier="2036879" data-fillin="">55401</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Patient's Country</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="2036895" id="2036896" value="USA" data-question-prompt="Patient's Country" data-question-identifier="2036895" data-responsePrompt="United States" data-responseIdentifier="2036896" data-section-identifier="2036879" data-fillin="">United States</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2036895" id="2036897" value="CAN" data-question-prompt="Patient's Country" data-question-identifier="2036895" data-responsePrompt="CANADA" data-responseIdentifier="2036897" data-section-identifier="2036879" data-fillin="">CANADA</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="2036895" id="2036898" value="MEX" data-question-prompt="Patient's Country" data-question-identifier="2036895" data-responsePrompt="MEXICO" data-responseIdentifier="2036898" data-section-identifier="2036879" data-fillin="">MEXICO</label></li>
                  </ul>
               </div>
               <div class="panel-question"><label for="d1e1531" class="question-prompt" style="display: block; font-weight: bold;">Patient's Phone Number</label><input type="text" name="2036900" id="d1e1544" size="30" maxlength="30" data-question-prompt="Patient's Phone Number" data-datatype="string" data-section-identifier="2036879" data-pattern="" data-question-repeat="" data-question-identifier="2036900"></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Other Patient Information</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Patient's Race Code</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="checkbox" style="margin-right: 5px" name="26487" id="27842" value="1002-5" data-question-prompt="Patient's Race Code" data-question-identifier="26487" data-responsePrompt="American Indian or Alaska Native" data-responseIdentifier="27842" data-section-identifier="26486" data-fillin="">American Indian or Alaska Native</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="26487" id="27843" value="2028-9" data-question-prompt="Patient's Race Code" data-question-identifier="26487" data-responsePrompt="Asian" data-responseIdentifier="27843" data-section-identifier="26486" data-fillin="">Asian</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="26487" id="27846" value="2054-5" data-question-prompt="Patient's Race Code" data-question-identifier="26487" data-responsePrompt="Black or African American" data-responseIdentifier="27846" data-section-identifier="26486" data-fillin="">Black or African American</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="26487" id="27847" value="2076-8" data-question-prompt="Patient's Race Code" data-question-identifier="26487" data-responsePrompt="Native Hawaiian or other Pacific&#xA;                                    Islander" data-responseIdentifier="27847" data-section-identifier="26486" data-fillin="">Native Hawaiian or other Pacific
                           Islander</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="26487" id="29035" value="2106-3" data-question-prompt="Patient's Race Code" data-question-identifier="26487" data-responsePrompt="White" data-responseIdentifier="29035" data-section-identifier="26486" data-fillin="">White</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Patient's Ethnicity Code</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="checkbox" style="margin-right: 5px" name="27762" id="29036" value="2135-2" data-question-prompt="Patient's Ethnicity Code" data-question-identifier="27762" data-responsePrompt="Hispanic or Latino" data-responseIdentifier="29036" data-section-identifier="26486" data-fillin="">Hispanic or Latino</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="27762" id="29037" value="2186-5" data-question-prompt="Patient's Ethnicity Code" data-question-identifier="27762" data-responsePrompt="Not Hispanic or Latino (specify)" data-responseIdentifier="29037" data-section-identifier="26486" data-fillin="20">Not Hispanic or Latino (specify)</label><input type="text" id="29037-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Highest Education Level</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29056" value="Bachelor's Degree" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="Bachelor's Degree" data-responseIdentifier="29056" data-section-identifier="26486" data-fillin="">Bachelor's Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29061" value="Doctoral degree or professional degree" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="Professional Doctorate or Doctorate&#xA;                                    Degree" data-responseIdentifier="29061" data-section-identifier="26486" data-fillin="">Professional Doctorate or Doctorate
                           Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29057" value="Grade School" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="Grade School" data-responseIdentifier="29057" data-section-identifier="26486" data-fillin="">Grade School</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29058" value="Graduate or professional degree" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="Graduation Or Professional Degree" data-responseIdentifier="29058" data-section-identifier="26486" data-fillin="">Graduation Or Professional Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29059" value="High school graduate (including&#xA;                                 equivalency)" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="High School Completion or General Equivalency Diploma&#xA;                                    (GED) Completion" data-responseIdentifier="29059" data-section-identifier="26486" data-fillin="">High School Completion or General Equivalency Diploma
                           (GED) Completion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29062" value="Master's Degree" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="Master's Degree" data-responseIdentifier="29062" data-section-identifier="26486" data-fillin="">Master's Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29063" value="No formal education" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="No Formal Schooling" data-responseIdentifier="29063" data-section-identifier="26486" data-fillin="">No Formal Schooling</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29064" value="Not high school graduate" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="Not High School Graduate" data-responseIdentifier="29064" data-section-identifier="26486" data-fillin="">Not High School Graduate</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27763" id="29065" value="Some college or associate degree" data-question-prompt="Highest Education Level" data-question-identifier="27763" data-responsePrompt="Some College or Associates Degree" data-responseIdentifier="29065" data-section-identifier="26486" data-fillin="">Some College or Associates Degree</label></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Provider Information</h1>
               <div class="form-contained-section">
                  <h2> Provider Address</h2>Repeat 3 timesResponse # 1
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Address Type</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29033" value="Home" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Home Address" data-responseIdentifier="29033" data-section-identifier="" data-fillin="">Home Address</label></li>
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29034" value="Office1" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Office1 Address" data-responseIdentifier="29034" data-section-identifier="" data-fillin="">Office1 Address</label></li>
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29076" value="Office2" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Office2 Address" data-responseIdentifier="29076" data-section-identifier="" data-fillin="">Office2 Address</label></li>
                     </ul>
                  </div>
                  <div class="panel-question"><label for="d1e2228" class="question-prompt" style="display: block; font-weight: bold;">Provider Street Address</label><input type="text" name="27814" id="d1e2241" size="30" maxlength="30" data-question-prompt="Provider Street Address" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="27814"></div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider City</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29038" value="351615" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Atlanta, GA, Fulton" data-responseIdentifier="29038" data-section-identifier="" data-fillin="">Atlanta, GA, Fulton</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29039" value="655030" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Minneapolis, MN, Hennepin" data-responseIdentifier="29039" data-section-identifier="" data-fillin="">Minneapolis, MN, Hennepin</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29040" value="423587" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Chicago, IL, Cook" data-responseIdentifier="29040" data-section-identifier="" data-fillin="">Chicago, IL, Cook</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider State</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29041" value="13" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Georgia" data-responseIdentifier="29041" data-section-identifier="" data-fillin="">Georgia</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29043" value="17" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Illinois" data-responseIdentifier="29043" data-section-identifier="" data-fillin="">Illinois</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29042" value="27" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Minnesota" data-responseIdentifier="29042" data-section-identifier="" data-fillin="">Minnesota</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Zip Code</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29044" value="30301" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="30301" data-responseIdentifier="29044" data-section-identifier="" data-fillin="">30301</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29046" value="60609" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="60609" data-responseIdentifier="29046" data-section-identifier="" data-fillin="">60609</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29045" value="55401" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="55401" data-responseIdentifier="29045" data-section-identifier="" data-fillin="">55401</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Country</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29047" value="USA" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="United States" data-responseIdentifier="29047" data-section-identifier="" data-fillin="">United States</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29048" value="CAN" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="CANADA" data-responseIdentifier="29048" data-section-identifier="" data-fillin="">CANADA</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29049" value="MEX" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="MEXICO" data-responseIdentifier="29049" data-section-identifier="" data-fillin="">MEXICO</label></li>
                     </ul>
                  </div>
                  <div class="panel-question"><label for="d1e2616" class="question-prompt" style="display: block; font-weight: bold;">Provider Telephone #</label><input type="text" name="27821" id="d1e2627" size="30" maxlength="30" data-question-prompt="Provider Telephone #" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="27821"></div>Response # 2
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Address Type</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29033" value="Home" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Home Address" data-responseIdentifier="29033" data-section-identifier="" data-fillin="">Home Address</label></li>
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29034" value="Office1" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Office1 Address" data-responseIdentifier="29034" data-section-identifier="" data-fillin="">Office1 Address</label></li>
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29076" value="Office2" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Office2 Address" data-responseIdentifier="29076" data-section-identifier="" data-fillin="">Office2 Address</label></li>
                     </ul>
                  </div>
                  <div class="panel-question"><label for="d1e2228" class="question-prompt" style="display: block; font-weight: bold;">Provider Street Address</label><input type="text" name="27814" id="d1e2241" size="30" maxlength="30" data-question-prompt="Provider Street Address" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="27814"></div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider City</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29038" value="351615" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Atlanta, GA, Fulton" data-responseIdentifier="29038" data-section-identifier="" data-fillin="">Atlanta, GA, Fulton</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29039" value="655030" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Minneapolis, MN, Hennepin" data-responseIdentifier="29039" data-section-identifier="" data-fillin="">Minneapolis, MN, Hennepin</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29040" value="423587" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Chicago, IL, Cook" data-responseIdentifier="29040" data-section-identifier="" data-fillin="">Chicago, IL, Cook</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider State</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29041" value="13" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Georgia" data-responseIdentifier="29041" data-section-identifier="" data-fillin="">Georgia</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29043" value="17" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Illinois" data-responseIdentifier="29043" data-section-identifier="" data-fillin="">Illinois</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29042" value="27" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Minnesota" data-responseIdentifier="29042" data-section-identifier="" data-fillin="">Minnesota</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Zip Code</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29044" value="30301" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="30301" data-responseIdentifier="29044" data-section-identifier="" data-fillin="">30301</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29046" value="60609" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="60609" data-responseIdentifier="29046" data-section-identifier="" data-fillin="">60609</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29045" value="55401" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="55401" data-responseIdentifier="29045" data-section-identifier="" data-fillin="">55401</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Country</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29047" value="USA" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="United States" data-responseIdentifier="29047" data-section-identifier="" data-fillin="">United States</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29048" value="CAN" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="CANADA" data-responseIdentifier="29048" data-section-identifier="" data-fillin="">CANADA</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29049" value="MEX" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="MEXICO" data-responseIdentifier="29049" data-section-identifier="" data-fillin="">MEXICO</label></li>
                     </ul>
                  </div>
                  <div class="panel-question"><label for="d1e2616" class="question-prompt" style="display: block; font-weight: bold;">Provider Telephone #</label><input type="text" name="27821" id="d1e2627" size="30" maxlength="30" data-question-prompt="Provider Telephone #" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="27821"></div>Response # 3
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Address Type</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29033" value="Home" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Home Address" data-responseIdentifier="29033" data-section-identifier="" data-fillin="">Home Address</label></li>
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29034" value="Office1" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Office1 Address" data-responseIdentifier="29034" data-section-identifier="" data-fillin="">Office1 Address</label></li>
                        <li><label><input type="checkbox" style="margin-right: 5px" name="27813" id="29076" value="Office2" data-question-prompt="Provider Address Type" data-question-identifier="27813" data-responsePrompt="Office2 Address" data-responseIdentifier="29076" data-section-identifier="" data-fillin="">Office2 Address</label></li>
                     </ul>
                  </div>
                  <div class="panel-question"><label for="d1e2228" class="question-prompt" style="display: block; font-weight: bold;">Provider Street Address</label><input type="text" name="27814" id="d1e2241" size="30" maxlength="30" data-question-prompt="Provider Street Address" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="27814"></div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider City</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29038" value="351615" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Atlanta, GA, Fulton" data-responseIdentifier="29038" data-section-identifier="" data-fillin="">Atlanta, GA, Fulton</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29039" value="655030" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Minneapolis, MN, Hennepin" data-responseIdentifier="29039" data-section-identifier="" data-fillin="">Minneapolis, MN, Hennepin</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27815" id="29040" value="423587" data-question-prompt="Provider City" data-question-identifier="27815" data-responsePrompt="Chicago, IL, Cook" data-responseIdentifier="29040" data-section-identifier="" data-fillin="">Chicago, IL, Cook</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider State</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29041" value="13" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Georgia" data-responseIdentifier="29041" data-section-identifier="" data-fillin="">Georgia</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29043" value="17" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Illinois" data-responseIdentifier="29043" data-section-identifier="" data-fillin="">Illinois</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27818" id="29042" value="27" data-question-prompt="Provider State" data-question-identifier="27818" data-responsePrompt="Minnesota" data-responseIdentifier="29042" data-section-identifier="" data-fillin="">Minnesota</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Zip Code</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29044" value="30301" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="30301" data-responseIdentifier="29044" data-section-identifier="" data-fillin="">30301</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29046" value="60609" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="60609" data-responseIdentifier="29046" data-section-identifier="" data-fillin="">60609</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27819" id="29045" value="55401" data-question-prompt="Provider Zip Code" data-question-identifier="27819" data-responsePrompt="55401" data-responseIdentifier="29045" data-section-identifier="" data-fillin="">55401</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Country</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29047" value="USA" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="United States" data-responseIdentifier="29047" data-section-identifier="" data-fillin="">United States</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29048" value="CAN" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="CANADA" data-responseIdentifier="29048" data-section-identifier="" data-fillin="">CANADA</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27820" id="29049" value="MEX" data-question-prompt="Provider Country" data-question-identifier="27820" data-responsePrompt="MEXICO" data-responseIdentifier="29049" data-section-identifier="" data-fillin="">MEXICO</label></li>
                     </ul>
                  </div>
                  <div class="panel-question"><label for="d1e2616" class="question-prompt" style="display: block; font-weight: bold;">Provider Telephone #</label><input type="text" name="27821" id="d1e2627" size="30" maxlength="30" data-question-prompt="Provider Telephone #" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="" data-question-identifier="27821"></div><br><br><br><p style="margin: 0;"> repeat section more than once for various address
                     type
                  </p>
               </div>
               <div class="form-contained-section">
                  <h2> Provider Organization</h2>
                  <div class="panel-question"><label for="d1e2671" class="question-prompt" style="display: block; font-weight: bold;">Provider Organization NPI</label><div style="font-style: italic;">
                        <p style="margin: 0;"> This number should be a 10 digit integer</p>
                     </div><input type="text" name="27822" id="d1e2691" size="30" maxlength="30" data-question-prompt="Provider Organization NPI" data-datatype="integer" data-section-identifier="27816" data-pattern="" data-question-repeat="" data-question-identifier="27822"></div>
                  <div class="panel-question"><label for="d1e2716" class="question-prompt" style="display: block; font-weight: bold;">Provider Organization Name</label><input type="text" name="27824" id="d1e2727" size="30" maxlength="30" data-question-prompt="Provider Organization Name" data-datatype="string" data-section-identifier="27816" data-pattern="" data-question-repeat="" data-question-identifier="27824"></div>
                  <div class="panel-question"><label for="d1e2744" class="question-prompt" style="display: block; font-weight: bold;">Provider Organization Street Address</label><input type="text" name="27825" id="d1e2755" size="30" maxlength="30" data-question-prompt="Provider Organization Street Address" data-datatype="string" data-section-identifier="27816" data-pattern="" data-question-repeat="" data-question-identifier="27825"></div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Organization City</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27828" id="29066" value="351615" data-question-prompt="Provider Organization City" data-question-identifier="27828" data-responsePrompt="Atlanta, GA, Fulton" data-responseIdentifier="29066" data-section-identifier="27816" data-fillin="">Atlanta, GA, Fulton</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27828" id="29067" value="655030" data-question-prompt="Provider Organization City" data-question-identifier="27828" data-responsePrompt="Minneapolis, MN, Hennepin" data-responseIdentifier="29067" data-section-identifier="27816" data-fillin="">Minneapolis, MN, Hennepin</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27828" id="29068" value="423587" data-question-prompt="Provider Organization City" data-question-identifier="27828" data-responsePrompt="Chicago, IL, Cook" data-responseIdentifier="29068" data-section-identifier="27816" data-fillin="">Chicago, IL, Cook</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Organization State</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27829" id="29069" value="13" data-question-prompt="Provider Organization State" data-question-identifier="27829" data-responsePrompt="Georgia" data-responseIdentifier="29069" data-section-identifier="27816" data-fillin="">Georgia</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27829" id="29071" value="17" data-question-prompt="Provider Organization State" data-question-identifier="27829" data-responsePrompt="Illinois" data-responseIdentifier="29071" data-section-identifier="27816" data-fillin="">Illinois</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27829" id="29070" value="27" data-question-prompt="Provider Organization State" data-question-identifier="27829" data-responsePrompt="Minnesota" data-responseIdentifier="29070" data-section-identifier="27816" data-fillin="">Minnesota</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Organization Zip Code</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27830" id="29072" value="30301" data-question-prompt="Provider Organization Zip Code" data-question-identifier="27830" data-responsePrompt="30301" data-responseIdentifier="29072" data-section-identifier="27816" data-fillin="">30301</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27830" id="29073" value="60609" data-question-prompt="Provider Organization Zip Code" data-question-identifier="27830" data-responsePrompt="60609" data-responseIdentifier="29073" data-section-identifier="27816" data-fillin="">60609</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27830" id="29074" value="55401" data-question-prompt="Provider Organization Zip Code" data-question-identifier="27830" data-responsePrompt="55401" data-responseIdentifier="29074" data-section-identifier="27816" data-fillin="">55401</label></li>
                     </ul>
                  </div>
                  <div class="panel-question">
                     <h4 class="question-prompt">Provider Organization Country</h4>
                     <ul style="list-style-type: none; margin: 2px 0 0 0">
                        <li><label><input type="radio" style="margin-right: 5px" name="27832" id="29050" value="USA" data-question-prompt="Provider Organization Country" data-question-identifier="27832" data-responsePrompt="United States" data-responseIdentifier="29050" data-section-identifier="27816" data-fillin="">United States</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27832" id="29054" value="CAN" data-question-prompt="Provider Organization Country" data-question-identifier="27832" data-responsePrompt="CANADA" data-responseIdentifier="29054" data-section-identifier="27816" data-fillin="">CANADA</label></li>
                        <li><label><input type="radio" style="margin-right: 5px" name="27832" id="29055" value="MEX" data-question-prompt="Provider Organization Country" data-question-identifier="27832" data-responsePrompt="MEXICO" data-responseIdentifier="29055" data-section-identifier="27816" data-fillin="">MEXICO</label></li>
                     </ul>
                  </div>
                  <div class="panel-question"><label for="d1e3130" class="question-prompt" style="display: block; font-weight: bold;">Provider Organization Telephone #</label><input type="text" name="27831" id="d1e3141" size="30" maxlength="30" data-question-prompt="Provider Organization Telephone #" data-datatype="string" data-section-identifier="27816" data-pattern="" data-question-repeat="" data-question-identifier="27831"></div>
               </div>
               <div class="panel-question"><label for="d1e3171" class="question-prompt" style="display: block; font-weight: bold;">Provider NPI</label><div style="font-style: italic;">
                     <p style="margin: 0;"> This number should be a 10 digit integer</p>
                  </div><input type="text" name="27799" id="d1e3193" size="30" maxlength="30" data-question-prompt="Provider NPI" data-datatype="integer" data-section-identifier="27798" data-pattern="" data-question-repeat="" data-question-identifier="27799"></div>
               <div class="panel-question"><label for="d1e3218" class="question-prompt" style="display: block; font-weight: bold;">Provider First Name</label><input type="text" name="27808" id="d1e3229" size="30" maxlength="30" data-question-prompt="Provider First Name" data-datatype="string" data-section-identifier="27798" data-pattern="" data-question-repeat="" data-question-identifier="27808"></div>
               <div class="panel-question"><label for="d1e3246" class="question-prompt" style="display: block; font-weight: bold;">Provider Last Name</label><input type="text" name="27809" id="d1e3257" size="30" maxlength="30" data-question-prompt="Provider Last Name" data-datatype="string" data-section-identifier="27798" data-pattern="" data-question-repeat="" data-question-identifier="27809"></div>
               <div class="panel-question"><label for="d1e3274" class="question-prompt" style="display: block; font-weight: bold;">Provider Name Suffix</label><input type="text" name="27811" id="d1e3287" size="30" maxlength="30" data-question-prompt="Provider Name Suffix" data-datatype="string" data-section-identifier="27798" data-pattern="" data-question-repeat="" data-question-identifier="27811"></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Custodian Organization</h1>
               <div class="panel-question"><label for="d1e3326" class="question-prompt" style="display: block; font-weight: bold;">Reporting Organization Name (Custodian)</label><input type="text" name="27823" id="d1e3337" size="30" maxlength="30" data-question-prompt="Reporting Organization Name (Custodian)" data-datatype="string" data-section-identifier="27817" data-pattern="" data-question-repeat="" data-question-identifier="27823"></div>
               <div class="panel-question"><label for="d1e3355" class="question-prompt" style="display: block; font-weight: bold;">Reporting Organization NPI (Custodian)</label><div style="font-style: italic;">
                     <p style="margin: 0;"> This number should be a 10 digit integer</p>
                  </div><input type="text" name="27840" id="d1e3375" size="30" maxlength="30" data-question-prompt="Reporting Organization NPI (Custodian)" data-datatype="integer" data-section-identifier="27817" data-pattern="" data-question-repeat="" data-question-identifier="27840"></div>
               <div class="panel-question"><label for="d1e3399" class="question-prompt" style="display: block; font-weight: bold;">Reporting Organization Street Address
                     (Custodian)</label><input type="text" name="27833" id="d1e3410" size="30" maxlength="30" data-question-prompt="Reporting Organization Street Address&#xA;                              (Custodian)" data-datatype="string" data-section-identifier="27817" data-pattern="" data-question-repeat="" data-question-identifier="27833"></div>
               <div class="panel-question">
                  <h4 class="question-prompt">Reporting Organization City (Custodian)</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="27834" id="29075" value="351615" data-question-prompt="Reporting Organization City (Custodian)" data-question-identifier="27834" data-responsePrompt="Atlanta, GA, Fulton" data-responseIdentifier="29075" data-section-identifier="27817" data-fillin="">Atlanta, GA, Fulton</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27834" id="29077" value="655030" data-question-prompt="Reporting Organization City (Custodian)" data-question-identifier="27834" data-responsePrompt="Minneapolis, MN, Hennepin" data-responseIdentifier="29077" data-section-identifier="27817" data-fillin="">Minneapolis, MN, Hennepin</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27834" id="29078" value="423587" data-question-prompt="Reporting Organization City (Custodian)" data-question-identifier="27834" data-responsePrompt="Chicago, IL, Cook" data-responseIdentifier="29078" data-section-identifier="27817" data-fillin="">Chicago, IL, Cook</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Reporting Organization State (Custodian)</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="27835" id="29079" value="13" data-question-prompt="Reporting Organization State (Custodian)" data-question-identifier="27835" data-responsePrompt="Georgia" data-responseIdentifier="29079" data-section-identifier="27817" data-fillin="">Georgia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27835" id="29081" value="17" data-question-prompt="Reporting Organization State (Custodian)" data-question-identifier="27835" data-responsePrompt="Illinois" data-responseIdentifier="29081" data-section-identifier="27817" data-fillin="">Illinois</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27835" id="29080" value="27" data-question-prompt="Reporting Organization State (Custodian)" data-question-identifier="27835" data-responsePrompt="Minnesota" data-responseIdentifier="29080" data-section-identifier="27817" data-fillin="">Minnesota</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Reporting Organization Zip Code (Custodian)</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="27836" id="29082" value="30301" data-question-prompt="Reporting Organization Zip Code (Custodian)" data-question-identifier="27836" data-responsePrompt="30301" data-responseIdentifier="29082" data-section-identifier="27817" data-fillin="">30301</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27836" id="29083" value="60609" data-question-prompt="Reporting Organization Zip Code (Custodian)" data-question-identifier="27836" data-responsePrompt="60609" data-responseIdentifier="29083" data-section-identifier="27817" data-fillin="">60609</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27836" id="29084" value="55401" data-question-prompt="Reporting Organization Zip Code (Custodian)" data-question-identifier="27836" data-responsePrompt="55401" data-responseIdentifier="29084" data-section-identifier="27817" data-fillin="">55401</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Reporting Organization Country (Custodian)</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="27837" id="29085" value="USA" data-question-prompt="Reporting Organization Country (Custodian)" data-question-identifier="27837" data-responsePrompt="United States" data-responseIdentifier="29085" data-section-identifier="27817" data-fillin="">United States</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27837" id="29086" value="CAN" data-question-prompt="Reporting Organization Country (Custodian)" data-question-identifier="27837" data-responsePrompt="CANADA" data-responseIdentifier="29086" data-section-identifier="27817" data-fillin="">CANADA</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="27837" id="29087" value="MEX" data-question-prompt="Reporting Organization Country (Custodian)" data-question-identifier="27837" data-responsePrompt="MEXICO" data-responseIdentifier="29087" data-section-identifier="27817" data-fillin="">MEXICO</label></li>
                  </ul>
               </div>
               <div class="panel-question"><label for="d1e3787" class="question-prompt" style="display: block; font-weight: bold;">Reporting Organization Telephone # (Custodian)</label><input type="text" name="27838" id="d1e3798" size="30" maxlength="30" data-question-prompt="Reporting Organization Telephone # (Custodian)" data-datatype="string" data-section-identifier="27817" data-pattern="" data-question-repeat="" data-question-identifier="27838"></div>
            </div>
         </section>IHE Connectathon: Structure Data Capture<input type="submit" value="Send Info"><input type="reset"></form>
   </body>
</html>
   ]]>
            </sdc:sdc_html_form>
         </sdc_html_package>
      </Structured>
      
      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID></instanceID>
   </form>
<contentType>HTML</contentType>
<responseCode>Request succeeded</responseCode>
</RetrieveFormResponse>
"""



FDA_html = """<RetrieveFormResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form"
   xmlns:mfi13="http://www.iso.org/19763/13/2013"
   xmlns:dex="urn:ihe:qrph:dex:2013"
   xmlns:mfi6="http://www.iso.org/19763/6/2013"
   xmlns:mdr3="http://www.iso.org/11179/3/2013"
   >
   <form>
       <Structured>
         <sdc_html_package>
            <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
            <sdc:supplemental_data>
               <anyXMLContentType></anyXMLContentType>          
            </sdc:supplemental_data>
            
            <sdc:form_info>
               <!-- Contains mapping, and administrative info; this is the same content as from the form design package -->
               <sdc:mapping_package mapping_package_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/mapping_package_identifier#4617751v1.0/1"
                  form_design_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier#4617751v1.0">
                  <sdc:mdr_mapping mdr_mapping_identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/mdr_mapping_identifier#4617751v1.0/1">
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2003301v4.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619801v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2423393v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619812v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#793v5.1</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619803v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2200604v3.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619804v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2184687v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632819v1</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179689v4.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619807v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4461362v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2998028v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2004152v3.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632824v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179613v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619828	v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2182850v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619829v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2188132v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632827v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179660v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626771v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4631994v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632832v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4632014v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632835v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4632039v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3175751v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4632073v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632839v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2540498v4.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2182728v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3028750v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2179582v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3631708v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192901v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192888v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632991v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2748048v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633041v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3761048v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633024v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2479726v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633042v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2748053v2.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626915v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385191v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192895v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626860v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3631708v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633040v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192897v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626795v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192901v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626797v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2196242v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626793v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2004505v4.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626799v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192987v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633056v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192991v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626803v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#2192999v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626801v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385738v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626859v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385747v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626914v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385757v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                     <sdc:question_element_data_element_association>
                        <mfi13:data_element_scoped_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#4385754v1.0</mfi13:data_element_scoped_identifier>
                        <mfi13:association_type xmlns:mfi13="http://www.iso.org/19763/13/2013">related</mfi13:association_type>
                        <mfi13:question_element_identifier xmlns:mfi13="http://www.iso.org/19763/13/2013">http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626858v1.0</mfi13:question_element_identifier>
                     </sdc:question_element_data_element_association>
                  </sdc:mdr_mapping>
               </sdc:mapping_package>
               <sdc:administrative_package>
                  <sdc:submission_rule rule_id_and_version="Version1">
                     <sdc:destination>
                        <sdc:endpoint>http:cdc</sdc:endpoint>
                        <sdc:description>CDC Form Receiver URL</sdc:description>
                     </sdc:destination>
                  </sdc:submission_rule>
                  <sdc:compliance_rule/>
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
                        <mdr3:effective_date xmlns:mdr3="http://www.iso.org/11179/3/2013">2014-12-09T00:07:20.0</mdr3:effective_date>
                        <mdr3:until_date xmlns:mdr3="http://www.iso.org/11179/3/2013"/>
                        <mdr3:administrative_note xmlns:mdr3="http://www.iso.org/11179/3/2013"/>
                        <mdr3:administrative_status xmlns:mdr3="http://www.iso.org/11179/3/2013">DRAFT NEW</mdr3:administrative_status>
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
                     <sdc:creation_date/>
                     <sdc:explanatory_comment/>
                  </sdc:registration>
               </sdc:administrative_package>
               <sdc:stylesheet/>
            
            </sdc:form_info>
             <sdc:sdc_html_form>
			 <![CDATA[
<!DOCTYPE html
  SYSTEM "about:legacy-compat">

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
                    }</style><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script><script type="text/javascript">//
$(function () {
	/*
	 * Process checkboxes and radio buttons so if a parent checkbox/radio button is unchecked, children are unchecked,
	 * if child checked then check parent, etc.
	 */
	var $parentCheckboxes = $('.guarded-element-question').parent().find('input[type=checkbox]:first');
	$parentCheckboxes.each(function () {
		var $parentCheckbox = $(this);
		var $childrenCheckboxes = $parentCheckbox.closest('li').find('ul li input[type=checkbox], input[type=radio]');

		if ($childrenCheckboxes.length > 0) {
			$childrenCheckboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=checkbox], input[type=radio]').is(':checked');
				$parentCheckbox.prop('checked', $anyChildrenChecked);
			});

			$parentCheckbox.click(function () {
				if (!($(this).is(':checked'))) {
					$(this).closest('li').find('ul li input[type=checkbox], input[type=radio]').prop('checked', $(this).prop('checked'));
				}
			})
		}
	});

	var $parentRadioboxes = $('.guarded-element-question').parent().find('input[type=radio]:first');
	$parentRadioboxes.each(function () {
		var $parentRadiobox = $(this);

		var $childrenRadioboxes = $parentRadiobox.closest('li').find('ul li input[type=radio]');
		if ($childrenRadioboxes.length > 0) {
			$childrenRadioboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=radio]').is(':checked');
				$parentRadiobox.prop('checked', $anyChildrenChecked);
			});

			$parentRadiobox.closest('li').siblings().find('input[type=radio]').change(function () {
				$childrenRadioboxes.each(function () {
					$(this).prop('checked', false);
				});
			});
		}
	})
});

var getXmlOutput = (function () {
	'use strict'
	function formatAttributes(attributes) {
		var
		SINGLE_QUOTE = "'",
		DOUBLE_QUOTE = '"',
		ESCAPED_QUOTE = {
			SINGLE_QUOTE : '&quot;',
			DOUBLE_QUOTE : '&apos;'
		};
		var
		att_value,
		single_quote_pos,
		double_quote_pos,
		use_quote,
		escape,
		quote_to_escape,
		att_str,
		re,
		result = '';
		for (var att in attributes) {
			att_value = '' + attributes[att];
			single_quote_pos = att_value.indexOf(SINGLE_QUOTE);
			double_quote_pos = att_value.indexOf(DOUBLE_QUOTE);
			if (single_quote_pos !=  - 1 && double_quote_pos !=  - 1) {
				att_str = ' ' + att + "='" + att_value + "'";
				result += att_str;
				continue;
			}
			if (double_quote_pos !=  - 1 && double_quote_pos < apos_pos) {
				use_quote = SINGLE_QUOTE;
			} else {
				use_quote = DOUBLE_QUOTE;
			}
			escape = ESCAPED_QUOTE[use_quote];
			re = new RegExp(use_quote, 'g');
			att_str = '\n' + '  ' + att + '=' + use_quote + att_value.replace(re, escape) + use_quote;
			result += att_str;
		}
		return result;
	}
	/*
	 *	Public functions
	 */
	function createElement(name, content, attributes) {
		var att_str = '';
		if (attributes) {
			att_str = formatAttributes(attributes);
		}
		var xml;
		if (!content) {
			xml = '<' + name + att_str + '>' + '</' + name + '>';
		} else {
			xml = '<' + name + att_str + '>' + content + '</' + name + '>';
		}
		return xml;
	}
	var repeat_master_list = {};
	function recordRepeatOfQuestion(questionId) {
		var count = repeat_master_list[questionId];
		if (count == null || count == undefined) {
			count = 0;
		}
		++count;
		repeat_master_list[questionId] = count;
		return count;
	}

	function createPayload() {
		var testSection = "";
		$('input').each(function (index, item) {
			var addQuestion = true;

			/* Skip the last two inputs - submit & reset */
			if ($(item).attr('type') != 'submit' && $(item).attr('type') != 'reset') {
				var attrs = [];
				attrs.section_identifier = $(item).attr('data-section-identifier');
				attrs.question_identifier = $(item).attr('data-question-identifier');
				attrs.question_prompt = $(item).attr('data-question-prompt');

				var dtype = $(item).attr('data-datatype');
				if (dtype != undefined && dtype != null && dtype != '') {
					attrs.datatype = $(item).attr('data-datatype');
				}
				var nestedElement = '';
				if ($(item).attr('type') == 'radio' || $(item).attr('type') == 'checkbox') {
					if ($(item).prop('checked')) {

						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						var responseAttrs = [];
						responseAttrs.itemPrompt = $(item).attr('data-responsePrompt');
						responseAttrs.itemIdentifier = $(item).attr('data-responseIdentifier');
						var fillInNum = parseInt($(item).attr('data-fillin'), 10);
						if (fillInNum != NaN && fillInNum > 0) {
							var fillInId = '#' + $(item).attr('id') + '-fillin';
							responseAttrs.fill_in = $(fillInId).val();
						}

						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					} else {
						addQuestion = false;
					}
				} else {
					// Regular text field
					// Skip the fill-in input element
					if ($(item).attr('id').indexOf('fillin') > 0) {
						addQuestion = false;
					}
					// Skip text fields if no text
					var text = $(item).val();
					if (addQuestion && (text == undefined || text == null || text == '')) {
						addQuestion = false;
					}
					if (addQuestion) {
						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					}
				}
				if ($(item).attr('data-pattern')) {
					nestedElement += '\n' + " <!--  " + getXmlOutput.createElement('pattern', $(item).attr('data-pattern')) + " --> ";
				}
				if (addQuestion) {
					testSection += getXmlOutput.createElement('question', nestedElement, attrs) + '\n';
				}
			}
		});

		return testSection;
	}

	return {
		createElement : createElement,
		createPayload : createPayload
	};
})();

function buildRequest(payload, endpoint) {
	var submitUrl = endpoint;
	var formDesignIdentifier = $('#sdc_form').attr('data-formDesignIdentifier');
	var formRepresentationIdentifier = $('#sdc_form').attr('data-formRepresentationIdentifier');
	var requestString =
		'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">\n' +
		'  <soap:Header>\n' +
		'    <Action xmlns="http://www.w3.org/2005/08/addressing">urn:ihe:iti:2007:SubmitForm</Action>\n' +
		'    <MessageID xmlns="http://www.w3.org/2005/08/addressing">urn:uuid:' + guid() + '</MessageID>\n' +
		'    <To xmlns="http://www.w3.org/2005/08/addressing">' + submitUrl + '</To>\n' +
		'    <ReplyTo xmlns="http://www.w3.org/2005/08/addressing">\n' +
		'      <Address>http://www.w3.org/2005/08/addressing/anonymous</Address>\n' +
		'    </ReplyTo>\n' +
		'  </soap:Header>\n' +
		'  <soap:Body>\n' +
		'<SubmitFormRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
		'    xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../Schemas/RFD.xsd" xmlns="urn:ihe:iti:rfd:2007"\n' +
		'    xmlns:sdc="http://nlm.nih.gov/sdc/form">\n' +
		'       <form_data xmlns="http://nlm.nih.gov/sdc/form" form_design_identifier="' + formDesignIdentifier + '"\n' +
		'            form_representation_identifier="' + formRepresentationIdentifier + '">\n' +
		'<body>\n' + payload + '\n' +
		'    </body>\n' +
		'    </form_data>\n' +
		' </SubmitFormRequest>\n' +
		'  </soap:Body>\n' +
		'</soap:Envelope>';

	console.log(requestString);

	return requestString;
}
var statusMsg = '';
function buildStatusMsg(statusCode, endpoint) {
	if (statusCode === 200 || statusCode == 304) {
		statusMsg += 'SUCCESSFUL Sending status=: ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
		console.log('SUCCESS HTTP Status: ');
	} else {
		statusMsg += 'ERROR Sending status= ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	}
}

function sendRequest(request, endpoint, msg) {

	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open('POST', endpoint, true);
	xmlhttp.setRequestHeader('Content-Type', 'application/soap+xml');

	xmlhttp.onreadystatechange = function (event) {
		if (xmlhttp.readyState === 4) {
			buildStatusMsg(xmlhttp.status, endpoint);
		}
	};

	xmlhttp.send(request);
}

function submitForm(e, endpoint) {
	if (jQuery.support.opacity == false) {
		//  alert('OLD browser');
		event.returnValue = false;
	} else {
		//   alert('NEW browser');
		e.preventDefault();
		e.stopPropagation();
	}
	// endpoint may contain multiple url's separated by '|', last char will always be '|'
	endpoint = endpoint.replace(/\s+/g, '');
	endpoint = endpoint.substr(0, endpoint.length - 1);
	var endpointArray = endpoint.split('|');

	var payload = getXmlOutput.createPayload();

	for (var i = 0; i < endpointArray.length; i++) {
		var request = buildRequest(payload, endpointArray[i]);
		sendRequest(request, endpointArray[i]);
	}
	setTimeout(function () {
		alert(statusMsg);
	}, 2000);
	return false;
}

/**
 * Generates a GUID string.
 * @returns {String} The generated GUID.
 * @example af8a8416-6e18-a307-bd9c-f2c947bbb3aa
 * @author Slavik Meltser (slavik@meltser.info).
 * @link http://slavik.meltser.info/?p=142
 */
function guid() {
	function _p8(s) {
		var p = (Math.random().toString(16) + "000000000").substr(2, 8);
		return s ? "-" + p.substr(0, 4) + "-" + p.substr(4, 4) : p;
	}
	return _p8() + _p8(true) + _p8(true) + _p8();
}
//
</script></head>
   <body id="form">
      <form method="post" id="sdc_form" data-formDesignIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier#4617751v1.0" data-formRepresentationIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/form_package_identifier#4617751v1.0/1" action="#" onsubmit="submitForm(event,&#34;http://10.242.63.50:8080/RFD/Form/RFDSubmitForm_Service|https://10.242.63.50:8181/RFD/Form/RFDSubmitForm_Service|http://spojiti.crgmedical.com/SDCService_v3.asmx?WSDL|https://10.242.63.42:8080/SDCservice.asmx|http://10.242.63.42/SDCservice.asmx|https://10.242.63.41:7443/iheReceiver/services/receive|http://10.242.63.41:7080/iheReceiver/services/receive|https://10.242.63.36:8080/emarcreceiver|http://10.242.63.36/emarcreceiver|http://107.170.9.164:8080/SubmitFormTestService/SubmitForm_Service|&#34;)">
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
         <section>
            <div class="form-section panel-section">
               <h2 class="section-header"> FDA USE ONLY</h2>
               <p style="margin-left: 3px"></p>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h2 class="section-header"> A. PATIENT
                  INFORMATION
               </h2>
               <p style="margin-left: 3px"></p>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619801v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Patient
                     Identifier</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619801v1.0" id="d1e1256" size="20" maxlength="20" data-question-prompt="Patient&#xA;                  Identifier" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619800v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619801v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2003301v4.0</p></span><span style="margin-left: 1px">In
                     Confidence</span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633591v1.0" class="question-prompt" style="display: block; font-weight: bold;">2. Age at Time of
                     Event</label><p style="margin: 0;">
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633591v1.0" id="d1e1319" size="9" maxlength="9" data-question-prompt="Age at Time of&#xA;                  Event" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619800v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633591v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2433964v2</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619803v1.0" class="question-prompt" style="display: block; font-weight: bold;">or Date of
                     Birth</label><p style="margin: 0;">
                     
                     
                  </p> (MM/DD/YYYY) <input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619803v1.0" id="d1e1378" size="30" maxlength="30" data-question-prompt="Date of&#xA;                  Birth" data-datatype="string_date" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619800v1.0" data-pattern=" (MM/DD/YYYY) " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619803v1.0"><span class="form-cdeId">
                     <p>CDE NCI:793v5.1</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">3. Sex</h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619804v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2575551/1.0" value="Female" data-question-prompt="Sex" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619804v1.0" data-responsePrompt="Female Gender" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2575551/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619800v1.0" data-fillin="">Female Gender</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619804v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2575550/1.0" value="Male" data-question-prompt="Sex" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619804v1.0" data-responsePrompt="Male Gender" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2575550/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619800v1.0" data-fillin="">Male Gender</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2200604v3</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632819v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Weight (lb)</label><p style="margin: 0;">
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632819v1.0" id="d1e1587" size="30" maxlength="30" data-question-prompt="Weight (lb)" data-datatype="decimal" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619800v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632819v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2184687v2</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619807v1.0" class="question-prompt" style="display: block; font-weight: bold;">or Weight (kg)</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619807v1.0" id="d1e1638" size="30" maxlength="30" data-question-prompt="Weight (kg)" data-datatype="decimal" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619800v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619807v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2179689v4</p></span></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h2 class="section-header"> B. ADVERSE EVENT, PRODUCT
                  PROBLEM, OR ERROR
               </h2>
               <p style="margin-left: 3px"></p>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">1. Check all that apply
                     (Report Type)
                  </h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619815v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2570073/1.0" value="Adverse&#xA;                     Event" data-question-prompt="Check all that apply&#xA;                  (Report Type)" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0" data-responsePrompt="Adverse Event" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2570073/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Adverse Event</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619815v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461360/1.0" value="Product Use&#xA;                     Error" data-question-prompt="Check all that apply&#xA;                  (Report Type)" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0" data-responsePrompt="Product Use Error" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461360/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Product Use Error</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619815v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461358/1.0" value="Product&#xA;                     Problem" data-question-prompt="Check all that apply&#xA;                  (Report Type)" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0" data-responsePrompt="Product Problem" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461358/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Product Problem</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619815v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461356/1.0" value="Problem with Different&#xA;                     Manufacturer of Same Medicine" data-question-prompt="Check all that apply&#xA;                  (Report Type)" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619815v1.0" data-responsePrompt="Problem with Different Manufacturer of Same Medicine" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4461356/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Problem with Different Manufacturer of Same Medicine</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:4461362v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">2. Outcomes Attributed to
                     Adverse Event
                  </h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2992998/1.0" value="Death" data-question-prompt="Outcomes Attributed to&#xA;                  Adverse Event" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" data-responsePrompt="Death" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2992998/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Death</label><div class="guarded-element-question"><b> Date of
                              Death</b>
                           
                            (DD/MON/YYYY) <input type="text" name="4632824v1.0" id="d1e1987" size="30" maxlength="30" data-question-prompt="Date of&#xA;                                 Death" data-datatype="string_date" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632824v1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-question-repeat="1"><span class="form-cdeId">
                              <p>CDE NCI:2004152v3</p></span></div>
                     </li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579210/1.0" value="Life&#xA;                     Threatening" data-question-prompt="Date of&#xA;                                 Death" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" data-responsePrompt="Life Threatening" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579210/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Life Threatening</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2992999/1.0" value="Hospitalization" data-question-prompt="Date of&#xA;                                 Death" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" data-responsePrompt="Hospitalization - initial or Prolonged" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2992999/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Hospitalization - initial or Prolonged</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993002/1.0" value="Required&#xA;                     Intervention" data-question-prompt="Date of&#xA;                                 Death" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" data-responsePrompt="Required Intervention to Prevent Permanent Imapirment/Damage&#xA;                        (Devices)" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993002/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Required Intervention to Prevent Permanent Imapirment/Damage
                           (Devices)</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3003755/1.0" value="Disability" data-question-prompt="Date of&#xA;                                 Death" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" data-responsePrompt="Disability or Permanent Damage" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3003755/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Disability or Permanent Damage</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993000/1.0" value="Congenital&#xA;                     Abnormality" data-question-prompt="Date of&#xA;                                 Death" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" data-responsePrompt="Congenital Abnormality/Birth Defect" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993000/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Congenital Abnormality/Birth Defect</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619820v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993001/1.0" value="Other&#xA;                     Serious" data-question-prompt="Date of&#xA;                                 Death" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619820v1.0" data-responsePrompt="Other Serious (Important Medical Events)" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2993001/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-fillin="">Other Serious (Important Medical Events)</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2998028v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619828v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Date of
                     Event</label> (MM/DD/YYYY) <input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619828v1.0" id="d1e2369" size="30" maxlength="30" data-question-prompt="Date of&#xA;                  Event" data-datatype="string_date" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-pattern=" (MM/DD/YYYY) " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619828v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2179613v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619829v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Date of this
                     Report</label> (MM/DD/YYYY) <input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4619829v1.0" id="d1e2420" size="30" maxlength="30" data-question-prompt="Date of this&#xA;                  Report" data-datatype="string_date" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-pattern=" (MM/DD/YYYY) " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4619829v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2182850v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632827v1.0" class="question-prompt" style="display: block; font-weight: bold;">5. Describe event, Problem
                     or Product Use Error</label><p style="margin: 0;">
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632827v1.0" id="d1e2477" size="200" maxlength="200" data-question-prompt="Describe event, Problem&#xA;                  or Product Use Error" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632827v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2188132v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640053v1.0" class="question-prompt" style="display: block; font-weight: bold;">6. Relevant Tests/Laboratory
                     Data, Including Dates</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640053v1.0" id="d1e2528" size="600" maxlength="600" data-question-prompt="Relevant Tests/Laboratory&#xA;                  Data, Including Dates" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640053v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2003746v6.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626771v1.0" class="question-prompt" style="display: block; font-weight: bold;">7. Other Relevant History,
                     Including Preexisting Medical Conditions</label><p style="margin: 0;">
                     (e.g. allergies, race,
                     pregnancy, smoking and alcohol use, liver/kidney problems, etc.) 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626771v1.0" id="d1e2585" size="600" maxlength="600" data-question-prompt="Other Relevant History,&#xA;                  Including Preexisting Medical Conditions" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4619814v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626771v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2179660v2</p></span></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h2 class="section-header"> C. PRODUCT
                  AVAILABILITY
               </h2>
               <p style="margin-left: 3px"></p>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">1. Product Available for
                     Evaluation?
                  </h4>
                  <p style="margin: 0;">
                     Do not send product to
                     FDA
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632832v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" value="Yes" data-question-prompt="Product Available for&#xA;                  Evaluation?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632832v1.0" data-responsePrompt="Yes" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626631v1.0" data-fillin="">Yes</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632832v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" value="No" data-question-prompt="Product Available for&#xA;                  Evaluation?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632832v1.0" data-responsePrompt="No" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626631v1.0" data-fillin="">No</label><div class="guarded-element-question"><b> Returned
                              to Manufacturer on: (mm/dd/yyyy)</b> (MM/DD/YYYY) <input type="text" name="4632835v1.0" id="d1e2764" size="30" maxlength="30" data-question-prompt="Returned&#xA;                                 to Manufacturer on: (mm/dd/yyyy)" data-datatype="string_date" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632835v1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626631v1.0" data-question-repeat="1"><span class="form-cdeId">
                              <p>CDE NCI:4632014v1.0</p></span></div>
                     </li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:4631994v1.0</p></span></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h2 class="section-header"> D. SUSPECT
                  PRODUCT(S)
               </h2>
               <p style="margin-left: 3px"></p>Repeat 2 timesResponse # 1
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632837v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Name</label><p style="margin: 0;">
                     (from product label)
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632837v1.0" id="d1e2902" size="200" maxlength="200" data-question-prompt="Name" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4632039v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632836v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Strength</label><p style="margin: 0;">
                     (from product label)
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632836v1.0" id="d1e2952" size="200" maxlength="200" data-question-prompt="Strength" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3175751v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Manufacturer</label><p style="margin: 0;">
                     (from product label)
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="d1e2998" size="100" maxlength="100" data-question-prompt="Manufacturer" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3028750v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632842v1.0" class="question-prompt" style="display: block; font-weight: bold;">2. Dose</label><p style="margin: 0;">
                     or Amount
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632842v1.0" id="d1e3055" size="30" maxlength="30" data-question-prompt="Dose" data-datatype="decimal" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2182728v2</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;"> Dose Units</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567635/1.0" value="%" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Percent" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567635/1.0" data-section-identifier="" data-fillin="">Percent</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2732864/1.0" value="%" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Percent Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2732864/1.0" data-section-identifier="" data-fillin="">Percent Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569441/1.0" value="10^3" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Thousand" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569441/1.0" data-section-identifier="" data-fillin="">Thousand</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725086/1.0" value="10^5{Cells}/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Hundred Thousand Cells per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725086/1.0" data-section-identifier="" data-fillin="">Hundred Thousand Cells per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569409/1.0" value="10^6" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569409/1.0" data-section-identifier="" data-fillin="">Million</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569402/1.0" value="10^6eV" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million electron volt" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569402/1.0" data-section-identifier="" data-fillin="">Million electron volt</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725088/1.0" value="10^6{Cells}/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million Cells per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725088/1.0" data-section-identifier="" data-fillin="">Million Cells per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569408/1.0" value="10^6{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million Plaque Forming Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569408/1.0" data-section-identifier="" data-fillin="">Million Plaque Forming Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569420/1.0" value="10^6{VP}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million Viral Particles" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569420/1.0" data-section-identifier="" data-fillin="">Million Viral Particles</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718641/1.0" value="10^7{Cells}/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Ten Million Cells per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718641/1.0" data-section-identifier="" data-fillin="">Ten Million Cells per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725133/1.0" value="10^7{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Ten Million Plaque Forming Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725133/1.0" data-section-identifier="" data-fillin="">Ten Million Plaque Forming Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725131/1.0" value="10^8{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Hundred Million Plaque Forming Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725131/1.0" data-section-identifier="" data-fillin="">Hundred Million Plaque Forming Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725073/1.0" value="10^9{Cells}/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Billion Cells per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725073/1.0" data-section-identifier="" data-fillin="">Billion Cells per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725129/1.0" value="10^9{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Billion Plaque Forming Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725129/1.0" data-section-identifier="" data-fillin="">Billion Plaque Forming Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569067/1.0" value="cGy" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Centigray" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569067/1.0" data-section-identifier="" data-fillin="">Centigray</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569376/1.0" value="Ci" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Curie" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569376/1.0" data-section-identifier="" data-fillin="">Curie</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569378/1.0" value="dL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Deciliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569378/1.0" data-section-identifier="" data-fillin="">Deciliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725118/1.0" value="eq" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Equivalent Weight" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725118/1.0" data-section-identifier="" data-fillin="">Equivalent Weight</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567649/1.0" value="g" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567649/1.0" data-section-identifier="" data-fillin="">Gram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108593/1.0" value="g/d" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gram per Day" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108593/1.0" data-section-identifier="" data-fillin="">Gram per Day</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725116/1.0" value="g/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gram per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725116/1.0" data-section-identifier="" data-fillin="">Gram per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113233/1.0" value="g/wk" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gram per Week" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113233/1.0" data-section-identifier="" data-fillin="">Gram per Week</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569066/1.0" value="Gy" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gray" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569066/1.0" data-section-identifier="" data-fillin="">Gray</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567650/1.0" value="h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567650/1.0" data-section-identifier="" data-fillin="">Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569383/1.0" value="Hz" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Hertz" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569383/1.0" data-section-identifier="" data-fillin="">Hertz</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725075/1.0" value="J" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Joule" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725075/1.0" data-section-identifier="" data-fillin="">Joule</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725109/1.0" value="J/cm2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Joule per Square Centimeter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725109/1.0" data-section-identifier="" data-fillin="">Joule per Square Centimeter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725139/1.0" value="keV" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kiloelectronvolt" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725139/1.0" data-section-identifier="" data-fillin="">Kiloelectronvolt</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581032/1.0" value="kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="KILOGRAM" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581032/1.0" data-section-identifier="" data-fillin="">KILOGRAM</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569389/1.0" value="kHz" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilohertz" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569389/1.0" data-section-identifier="" data-fillin="">Kilohertz</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569390/1.0" value="kPa" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilopascal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569390/1.0" data-section-identifier="" data-fillin="">Kilopascal</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569391/1.0" value="kU" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilounit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569391/1.0" data-section-identifier="" data-fillin="">Kilounit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" value="kU/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilounit per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" data-section-identifier="" data-fillin="">Kilounit per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718864/1.0" value="kU/L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilounit per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718864/1.0" data-section-identifier="" data-fillin="">Kilounit per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569393/1.0" value="L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569393/1.0" data-section-identifier="" data-fillin="">Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718880/1.0" value="L/min" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Liter per Minute" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718880/1.0" data-section-identifier="" data-fillin="">Liter per Minute</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569397/1.0" value="mCi" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Millicurie" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569397/1.0" data-section-identifier="" data-fillin="">Millicurie</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569399/1.0" value="meq" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569399/1.0" data-section-identifier="" data-fillin="">Milliequivalent</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719062/1.0" value="meq/24.h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent per 24 Hours" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719062/1.0" data-section-identifier="" data-fillin="">Milliequivalent per 24 Hours</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719060/1.0" value="meq/dL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent per Deciliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719060/1.0" data-section-identifier="" data-fillin="">Milliequivalent per Deciliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725052/1.0" value="meq/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725052/1.0" data-section-identifier="" data-fillin="">Milliequivalent per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719056/1.0" value="meq/L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719056/1.0" data-section-identifier="" data-fillin="">Milliequivalent per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569666/1.0" value="mg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569666/1.0" data-section-identifier="" data-fillin="">Milligram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719054/1.0" value="mg/24.h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per 24 Hours" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719054/1.0" data-section-identifier="" data-fillin="">Milligram per 24 Hours</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719052/1.0" value="mg/dL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Deciliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719052/1.0" data-section-identifier="" data-fillin="">Milligram per Deciliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725048/1.0" value="mg/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725048/1.0" data-section-identifier="" data-fillin="">Milligram per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719050/1.0" value="mg/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719050/1.0" data-section-identifier="" data-fillin="">Milligram per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108591/1.0" value="mg/kg/d" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Kilogram per Day" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108591/1.0" data-section-identifier="" data-fillin="">Milligram per Kilogram per Day</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725141/1.0" value="mg/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725141/1.0" data-section-identifier="" data-fillin="">Milligram per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059688/1.0" value="mg/m2/24.h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Square Meter per Day" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059688/1.0" data-section-identifier="" data-fillin="">Milligram per Square Meter per Day</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725076/1.0" value="mg/m2/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Square Meter per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725076/1.0" data-section-identifier="" data-fillin="">Milligram per Square Meter per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059686/1.0" value="mg/m2/wk" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Square Meter per Week" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059686/1.0" data-section-identifier="" data-fillin="">Milligram per Square Meter per Week</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2685297/1.0" value="mg/mL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilogram per Cubic Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2685297/1.0" data-section-identifier="" data-fillin="">Kilogram per Cubic Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725107/1.0" value="mg/wk" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Week" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725107/1.0" data-section-identifier="" data-fillin="">Milligram per Week</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2573853/1.0" value="mg/{inhalation}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Inhalation" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2573853/1.0" data-section-identifier="" data-fillin="">Milligram per Inhalation</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569407/1.0" value="MHz" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Megahertz" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569407/1.0" data-section-identifier="" data-fillin="">Megahertz</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567660/1.0" value="min" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Minute" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567660/1.0" data-section-identifier="" data-fillin="">Minute</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567406/1.0" value="mL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567406/1.0" data-section-identifier="" data-fillin="">Milliliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725105/1.0" value="mL/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliliter per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725105/1.0" data-section-identifier="" data-fillin="">Milliliter per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725151/1.0" value="mL/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliliter per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725151/1.0" data-section-identifier="" data-fillin="">Milliliter per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569413/1.0" value="mmol" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Millimole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569413/1.0" data-section-identifier="" data-fillin="">Millimole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581580/1.0" value="mol" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Mole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581580/1.0" data-section-identifier="" data-fillin="">Mole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569415/1.0" value="mosm" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliosmole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569415/1.0" data-section-identifier="" data-fillin="">Milliosmole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569410/1.0" value="mU" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliunit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569410/1.0" data-section-identifier="" data-fillin="">Milliunit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725171/1.0" value="MU" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725171/1.0" data-section-identifier="" data-fillin="">Million Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569419/1.0" value="mV" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Millivolt" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569419/1.0" data-section-identifier="" data-fillin="">Millivolt</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719451/1.0" value="m[iU]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliinternational Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719451/1.0" data-section-identifier="" data-fillin="">Milliinternational Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719449/1.0" value="m[iU]/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliinternational Unit per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719449/1.0" data-section-identifier="" data-fillin="">Milliinternational Unit per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569416/1.0" value="M[RAD]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Megarad" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569416/1.0" data-section-identifier="" data-fillin="">Megarad</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569421/1.0" value="nCi" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanocurie" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569421/1.0" data-section-identifier="" data-fillin="">Nanocurie</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2672537/1.0" value="ng" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2672537/1.0" data-section-identifier="" data-fillin="">Nanogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725165/1.0" value="ng/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanogram per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725165/1.0" data-section-identifier="" data-fillin="">Nanogram per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724560/1.0" value="ng/L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanogram per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724560/1.0" data-section-identifier="" data-fillin="">Nanogram per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719066/1.0" value="ng/mL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719066/1.0" data-section-identifier="" data-fillin="">Microgram per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569427/1.0" value="nmol" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanomole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569427/1.0" data-section-identifier="" data-fillin="">Nanomole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569425/1.0" value="nm{light}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanometer" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569425/1.0" data-section-identifier="" data-fillin="">Nanometer</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725163/1.0" value="osm" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Osmole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725163/1.0" data-section-identifier="" data-fillin="">Osmole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569430/1.0" value="Pa" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Pascal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569430/1.0" data-section-identifier="" data-fillin="">Pascal</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567618/1.0" value="pg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Picogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567618/1.0" data-section-identifier="" data-fillin="">Picogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577221/1.0" value="s" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Second" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577221/1.0" data-section-identifier="" data-fillin="">Second</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725127/1.0" value="u" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Micro" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725127/1.0" data-section-identifier="" data-fillin="">Micro</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" value="U/g" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilounit per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" data-section-identifier="" data-fillin="">Kilounit per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725175/1.0" value="U/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Unit per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725175/1.0" data-section-identifier="" data-fillin="">Unit per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725031/1.0" value="U/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Unit per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725031/1.0" data-section-identifier="" data-fillin="">Unit per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725147/1.0" value="uCi" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microcurie" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725147/1.0" data-section-identifier="" data-fillin="">Microcurie</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569394/1.0" value="ug" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569394/1.0" data-section-identifier="" data-fillin="">Microgram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725145/1.0" value="ug/cm2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Square Centimeter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725145/1.0" data-section-identifier="" data-fillin="">Microgram per Square Centimeter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725050/1.0" value="ug/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725050/1.0" data-section-identifier="" data-fillin="">Microgram per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725144/1.0" value="ug/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725144/1.0" data-section-identifier="" data-fillin="">Microgram per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059690/1.0" value="ug/kg/24.h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Kilogram per Day" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059690/1.0" data-section-identifier="" data-fillin="">Microgram per Kilogram per Day</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113232/1.0" value="ug/kg/wk" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Kilogram per Week" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113232/1.0" data-section-identifier="" data-fillin="">Microgram per Kilogram per Week</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725082/1.0" value="ug/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725082/1.0" data-section-identifier="" data-fillin="">Microgram per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108589/1.0" value="ug/m2/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Square Meter per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108589/1.0" data-section-identifier="" data-fillin="">Microgram per Square Meter per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567626/1.0" value="uL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567626/1.0" data-section-identifier="" data-fillin="">Microliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567136/1.0" value="umol" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Micromole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567136/1.0" data-section-identifier="" data-fillin="">Micromole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719300/1.0" value="u[IU]/mL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microinternational Unit per Milliliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719300/1.0" data-section-identifier="" data-fillin="">Microinternational Unit per Milliliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725120/1.0" value="[drp]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Metric Drop" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725120/1.0" data-section-identifier="" data-fillin="">Metric Drop</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725055/1.0" value="[gal_us]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gallon US" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725055/1.0" data-section-identifier="" data-fillin="">Gallon US</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718872/1.0" value="[iU]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718872/1.0" data-section-identifier="" data-fillin="">International Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725111/1.0" value="[iU]/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725111/1.0" data-section-identifier="" data-fillin="">International Unit per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718870/1.0" value="[iU]/L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718870/1.0" data-section-identifier="" data-fillin="">International Unit per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725078/1.0" value="[iU]/mg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit per Milligram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725078/1.0" data-section-identifier="" data-fillin="">International Unit per Milligram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725094/1.0" value="[iU]/mg{alpha-Tocopherol}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit per Milligram of Alpha-Tocopherol" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725094/1.0" data-section-identifier="" data-fillin="">International Unit per Milligram of Alpha-Tocopherol</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725096/1.0" value="[iU]{Vitamin&#xA;                     A}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit of Vitamin A" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725096/1.0" data-section-identifier="" data-fillin="">International Unit of Vitamin A</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569429/1.0" value="[oz_av]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Ounce" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569429/1.0" data-section-identifier="" data-fillin="">Ounce</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725155/1.0" value="[psi]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Pound per Square Inch" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725155/1.0" data-section-identifier="" data-fillin="">Pound per Square Inch</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615202/1.0" value="[RAD]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Rad" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615202/1.0" data-section-identifier="" data-fillin="">Rad</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725185/1.0" value="[tbs_us]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Tablespoon Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725185/1.0" data-section-identifier="" data-fillin="">Tablespoon Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725181/1.0" value="[tsp_us]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Teaspoon Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725181/1.0" data-section-identifier="" data-fillin="">Teaspoon Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569373/1.0" value="{Application}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Application" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569373/1.0" data-section-identifier="" data-fillin="">Application</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725089/1.0" value="{AUC}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Area under Curve" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725089/1.0" data-section-identifier="" data-fillin="">Area under Curve</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725084/1.0" value="{Bottle}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Bottle Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725084/1.0" data-section-identifier="" data-fillin="">Bottle Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725126/1.0" value="{Caplet}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Caplet Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725126/1.0" data-section-identifier="" data-fillin="">Caplet Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725124/1.0" value="{Capsule}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Capsule Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725124/1.0" data-section-identifier="" data-fillin="">Capsule Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615470/1.0" value="{Cells}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Cell" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615470/1.0" data-section-identifier="" data-fillin="">Cell</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569377/1.0" value="{Course}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Course" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569377/1.0" data-section-identifier="" data-fillin="">Course</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2576428/1.0" value="{Course}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Cycle" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2576428/1.0" data-section-identifier="" data-fillin="">Cycle</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569379/1.0" value="{Dose}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Dose" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569379/1.0" data-section-identifier="" data-fillin="">Dose</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725113/1.0" value="{Inhalation}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Inhalation Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725113/1.0" data-section-identifier="" data-fillin="">Inhalation Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725091/1.0" value="{IV Bag}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Intravenous Bag Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725091/1.0" data-section-identifier="" data-fillin="">Intravenous Bag Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725134/1.0" value="{Measure}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Measurement" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725134/1.0" data-section-identifier="" data-fillin="">Measurement</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724564/1.0" value="{No&#xA;                     Scre}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Data Not Available" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724564/1.0" data-section-identifier="" data-fillin="">Data Not Available</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725160/1.0" value="{packet}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Packet Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725160/1.0" data-section-identifier="" data-fillin="">Packet Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725103/1.0" value="{Patch}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Patch Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725103/1.0" data-section-identifier="" data-fillin="">Patch Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725157/1.0" value="{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Plaque Forming Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725157/1.0" data-section-identifier="" data-fillin="">Plaque Forming Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725153/1.0" value="{puff}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Puff Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725153/1.0" data-section-identifier="" data-fillin="">Puff Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725098/1.0" value="{RAE}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Retinol Activity Equivalent" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725098/1.0" data-section-identifier="" data-fillin="">Retinol Activity Equivalent</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725100/1.0" value="{RE}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Retinol Equivalent" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725100/1.0" data-section-identifier="" data-fillin="">Retinol Equivalent</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725057/1.0" value="{Seed}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Radioactive Seed Implant Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725057/1.0" data-section-identifier="" data-fillin="">Radioactive Seed Implant Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2571186/1.0" value="{Session}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Session" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2571186/1.0" data-section-identifier="" data-fillin="">Session</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725189/1.0" value="{Spray}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Spray Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725189/1.0" data-section-identifier="" data-fillin="">Spray Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725187/1.0" value="{Suppository}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Suppository Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725187/1.0" data-section-identifier="" data-fillin="">Suppository Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725183/1.0" value="{tbl}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Tablet Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725183/1.0" data-section-identifier="" data-fillin="">Tablet Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725179/1.0" value="{TCID50}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Tissue Culture Infection Dose 50" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725179/1.0" data-section-identifier="" data-fillin="">Tissue Culture Infection Dose 50</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725177/1.0" value="{Troche}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Troche Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725177/1.0" data-section-identifier="" data-fillin="">Troche Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567622/1.0" value="{Unit}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567622/1.0" data-section-identifier="" data-fillin="">Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565695/1.0" value="{Unknown}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Unknown" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565695/1.0" data-section-identifier="" data-fillin="">Unknown</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725173/1.0" value="{VP}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Viral Particle Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725173/1.0" data-section-identifier="" data-fillin="">Viral Particle Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579163/1.0" value="{Wafer}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Wafer Dosage Form" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579163/1.0" data-section-identifier="" data-fillin="">Wafer Dosage Form</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2874130/1.0" value="{YU}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Yeast Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2874130/1.0" data-section-identifier="" data-fillin="">Yeast Units</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:3028750v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632841v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Frequency</label><p style="margin: 0;">
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632841v1.0" id="d1e9612" size="100" maxlength="100" data-question-prompt="Frequency" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2540498v4</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;"> Route</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567786/1.0" value="Infusion" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Infusion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567786/1.0" data-section-identifier="" data-fillin="">Infusion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567787/1.0" value="Inhaled" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Inhaled" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567787/1.0" data-section-identifier="" data-fillin="">Inhaled</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567783/1.0" value="Intradermal" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Intradermal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567783/1.0" data-section-identifier="" data-fillin="">Intradermal</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567788/1.0" value="Intramuscular" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Intramuscular" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567788/1.0" data-section-identifier="" data-fillin="">Intramuscular</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567785/1.0" value="Orally" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Orally" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567785/1.0" data-section-identifier="" data-fillin="">Orally</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567790/1.0" value="Other" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Other" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567790/1.0" data-section-identifier="" data-fillin="">Other</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565646/1.0" value="Rectal" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Rectal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565646/1.0" data-section-identifier="" data-fillin="">Rectal</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567789/1.0" value="Subcutaneous" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Subcutaneous" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567789/1.0" data-section-identifier="" data-fillin="">Subcutaneous</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567782/1.0" value="Topical" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Topical" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567782/1.0" data-section-identifier="" data-fillin="">Topical</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567784/1.0" value="Transdermal" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Transdermal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567784/1.0" data-section-identifier="" data-fillin="">Transdermal</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2179582v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640825v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Dates of Use
                     From:</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640825v1.0" id="d1e10171" size="24" maxlength="24" data-question-prompt="Dates of Use&#xA;                  From:" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="24" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4633453v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640823v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Dates of Use
                     To:</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640823v1.0" id="d1e10211" size="24" maxlength="24" data-question-prompt="Dates of Use&#xA;                  To:" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="24" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4633472v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640827v1.0" class="question-prompt" style="display: block; font-weight: bold;"> (if unknown dates, give
                     duration in minutes)</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640827v1.0" id="d1e10250" size="4" maxlength="4" data-question-prompt="(if unknown dates, give&#xA;                  duration in minutes)" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="24" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0"><span class="form-cdeId">
                     <p>CDE NCI:64799v3.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640851v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Diagnosis or Reason for
                     Use (Indication)</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640851v1.0" id="d1e10297" size="200" maxlength="200" data-question-prompt="Diagnosis or Reason for&#xA;                  Use (Indication)" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="200" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2597216v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">5. Event Abated After Use
                     Stopped or Dose Reduced?
                  </h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" value="Yes" data-question-prompt="Event Abated After Use&#xA;                  Stopped or Dose Reduced?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" data-responsePrompt="Yes" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" data-section-identifier="" data-fillin="">Yes</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" value="No" data-question-prompt="Event Abated After Use&#xA;                  Stopped or Dose Reduced?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" data-responsePrompt="No" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" data-section-identifier="" data-fillin="">No</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" value="Doesn't&#xA;                     Apply" data-question-prompt="Event Abated After Use&#xA;                  Stopped or Dose Reduced?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" data-responsePrompt="Doesn't Apply" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" data-section-identifier="" data-fillin="">Doesn't Apply</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2179608v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632985v1.0" class="question-prompt" style="display: block; font-weight: bold;">6. Lot #</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632985v1.0" id="d1e10511" size="30" maxlength="30" data-question-prompt="Lot #" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3631708v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632986v1.0" class="question-prompt" style="display: block; font-weight: bold;">7. Expiration
                     Date</label> (MM/DD/YYYY) <input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632986v1.0" id="d1e10556" size="30" maxlength="30" data-question-prompt="Expiration&#xA;                  Date" data-datatype="string_date" data-section-identifier="" data-pattern=" (MM/DD/YYYY) " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2192901v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">8. Event Reappeared After
                     Reintroduction?
                  </h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" value="Yes" data-question-prompt="Event Reappeared After&#xA;                  Reintroduction?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" data-responsePrompt="Yes" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" data-section-identifier="" data-fillin="">Yes</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" value="No" data-question-prompt="Event Reappeared After&#xA;                  Reintroduction?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" data-responsePrompt="No" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" data-section-identifier="" data-fillin="">No</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" value="Doesn't&#xA;                     Apply" data-question-prompt="Event Reappeared After&#xA;                  Reintroduction?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" data-responsePrompt="Doesn't Apply" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" data-section-identifier="" data-fillin="">Doesn't Apply</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2179615v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640839v1.0" class="question-prompt" style="display: block; font-weight: bold;">9. NDC #</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640839v1.0" id="d1e10773" size="30" maxlength="30" data-question-prompt="NDC #" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3101068v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640841v1.0" class="question-prompt" style="display: block; font-weight: bold;">OR  Unique ID</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640841v1.0" id="d1e10817" size="30" maxlength="30" data-question-prompt="Unique ID" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4384931v1.0</p></span></div>Response # 2
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632837v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Name</label><p style="margin: 0;">
                     (from product label)
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632837v1.0" id="d1e2902" size="200" maxlength="200" data-question-prompt="Name" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632837v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4632039v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632836v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Strength</label><p style="margin: 0;">
                     (from product label)
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632836v1.0" id="d1e2952" size="200" maxlength="200" data-question-prompt="Strength" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632836v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3175751v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Manufacturer</label><p style="margin: 0;">
                     (from product label)
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="d1e2998" size="100" maxlength="100" data-question-prompt="Manufacturer" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3028750v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632842v1.0" class="question-prompt" style="display: block; font-weight: bold;">2. Dose</label><p style="margin: 0;">
                     or Amount
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632842v1.0" id="d1e3055" size="30" maxlength="30" data-question-prompt="Dose" data-datatype="decimal" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632842v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2182728v2</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;"> Dose Units</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567635/1.0" value="%" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Percent" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567635/1.0" data-section-identifier="" data-fillin="">Percent</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2732864/1.0" value="%" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Percent Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2732864/1.0" data-section-identifier="" data-fillin="">Percent Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569441/1.0" value="10^3" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Thousand" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569441/1.0" data-section-identifier="" data-fillin="">Thousand</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725086/1.0" value="10^5{Cells}/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Hundred Thousand Cells per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725086/1.0" data-section-identifier="" data-fillin="">Hundred Thousand Cells per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569409/1.0" value="10^6" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569409/1.0" data-section-identifier="" data-fillin="">Million</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569402/1.0" value="10^6eV" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million electron volt" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569402/1.0" data-section-identifier="" data-fillin="">Million electron volt</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725088/1.0" value="10^6{Cells}/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million Cells per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725088/1.0" data-section-identifier="" data-fillin="">Million Cells per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569408/1.0" value="10^6{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million Plaque Forming Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569408/1.0" data-section-identifier="" data-fillin="">Million Plaque Forming Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569420/1.0" value="10^6{VP}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million Viral Particles" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569420/1.0" data-section-identifier="" data-fillin="">Million Viral Particles</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718641/1.0" value="10^7{Cells}/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Ten Million Cells per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718641/1.0" data-section-identifier="" data-fillin="">Ten Million Cells per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725133/1.0" value="10^7{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Ten Million Plaque Forming Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725133/1.0" data-section-identifier="" data-fillin="">Ten Million Plaque Forming Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725131/1.0" value="10^8{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Hundred Million Plaque Forming Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725131/1.0" data-section-identifier="" data-fillin="">Hundred Million Plaque Forming Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725073/1.0" value="10^9{Cells}/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Billion Cells per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725073/1.0" data-section-identifier="" data-fillin="">Billion Cells per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725129/1.0" value="10^9{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Billion Plaque Forming Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725129/1.0" data-section-identifier="" data-fillin="">Billion Plaque Forming Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569067/1.0" value="cGy" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Centigray" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569067/1.0" data-section-identifier="" data-fillin="">Centigray</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569376/1.0" value="Ci" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Curie" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569376/1.0" data-section-identifier="" data-fillin="">Curie</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569378/1.0" value="dL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Deciliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569378/1.0" data-section-identifier="" data-fillin="">Deciliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725118/1.0" value="eq" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Equivalent Weight" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725118/1.0" data-section-identifier="" data-fillin="">Equivalent Weight</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567649/1.0" value="g" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567649/1.0" data-section-identifier="" data-fillin="">Gram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108593/1.0" value="g/d" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gram per Day" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108593/1.0" data-section-identifier="" data-fillin="">Gram per Day</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725116/1.0" value="g/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gram per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725116/1.0" data-section-identifier="" data-fillin="">Gram per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113233/1.0" value="g/wk" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gram per Week" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113233/1.0" data-section-identifier="" data-fillin="">Gram per Week</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569066/1.0" value="Gy" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gray" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569066/1.0" data-section-identifier="" data-fillin="">Gray</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567650/1.0" value="h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567650/1.0" data-section-identifier="" data-fillin="">Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569383/1.0" value="Hz" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Hertz" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569383/1.0" data-section-identifier="" data-fillin="">Hertz</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725075/1.0" value="J" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Joule" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725075/1.0" data-section-identifier="" data-fillin="">Joule</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725109/1.0" value="J/cm2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Joule per Square Centimeter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725109/1.0" data-section-identifier="" data-fillin="">Joule per Square Centimeter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725139/1.0" value="keV" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kiloelectronvolt" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725139/1.0" data-section-identifier="" data-fillin="">Kiloelectronvolt</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581032/1.0" value="kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="KILOGRAM" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581032/1.0" data-section-identifier="" data-fillin="">KILOGRAM</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569389/1.0" value="kHz" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilohertz" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569389/1.0" data-section-identifier="" data-fillin="">Kilohertz</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569390/1.0" value="kPa" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilopascal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569390/1.0" data-section-identifier="" data-fillin="">Kilopascal</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569391/1.0" value="kU" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilounit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569391/1.0" data-section-identifier="" data-fillin="">Kilounit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" value="kU/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilounit per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" data-section-identifier="" data-fillin="">Kilounit per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718864/1.0" value="kU/L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilounit per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718864/1.0" data-section-identifier="" data-fillin="">Kilounit per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569393/1.0" value="L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569393/1.0" data-section-identifier="" data-fillin="">Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718880/1.0" value="L/min" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Liter per Minute" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718880/1.0" data-section-identifier="" data-fillin="">Liter per Minute</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569397/1.0" value="mCi" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Millicurie" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569397/1.0" data-section-identifier="" data-fillin="">Millicurie</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569399/1.0" value="meq" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569399/1.0" data-section-identifier="" data-fillin="">Milliequivalent</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719062/1.0" value="meq/24.h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent per 24 Hours" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719062/1.0" data-section-identifier="" data-fillin="">Milliequivalent per 24 Hours</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719060/1.0" value="meq/dL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent per Deciliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719060/1.0" data-section-identifier="" data-fillin="">Milliequivalent per Deciliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725052/1.0" value="meq/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725052/1.0" data-section-identifier="" data-fillin="">Milliequivalent per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719056/1.0" value="meq/L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliequivalent per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719056/1.0" data-section-identifier="" data-fillin="">Milliequivalent per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569666/1.0" value="mg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569666/1.0" data-section-identifier="" data-fillin="">Milligram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719054/1.0" value="mg/24.h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per 24 Hours" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719054/1.0" data-section-identifier="" data-fillin="">Milligram per 24 Hours</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719052/1.0" value="mg/dL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Deciliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719052/1.0" data-section-identifier="" data-fillin="">Milligram per Deciliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725048/1.0" value="mg/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725048/1.0" data-section-identifier="" data-fillin="">Milligram per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719050/1.0" value="mg/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719050/1.0" data-section-identifier="" data-fillin="">Milligram per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108591/1.0" value="mg/kg/d" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Kilogram per Day" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108591/1.0" data-section-identifier="" data-fillin="">Milligram per Kilogram per Day</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725141/1.0" value="mg/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725141/1.0" data-section-identifier="" data-fillin="">Milligram per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059688/1.0" value="mg/m2/24.h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Square Meter per Day" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059688/1.0" data-section-identifier="" data-fillin="">Milligram per Square Meter per Day</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725076/1.0" value="mg/m2/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Square Meter per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725076/1.0" data-section-identifier="" data-fillin="">Milligram per Square Meter per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059686/1.0" value="mg/m2/wk" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Square Meter per Week" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059686/1.0" data-section-identifier="" data-fillin="">Milligram per Square Meter per Week</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2685297/1.0" value="mg/mL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilogram per Cubic Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2685297/1.0" data-section-identifier="" data-fillin="">Kilogram per Cubic Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725107/1.0" value="mg/wk" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Week" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725107/1.0" data-section-identifier="" data-fillin="">Milligram per Week</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2573853/1.0" value="mg/{inhalation}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milligram per Inhalation" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2573853/1.0" data-section-identifier="" data-fillin="">Milligram per Inhalation</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569407/1.0" value="MHz" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Megahertz" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569407/1.0" data-section-identifier="" data-fillin="">Megahertz</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567660/1.0" value="min" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Minute" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567660/1.0" data-section-identifier="" data-fillin="">Minute</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567406/1.0" value="mL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567406/1.0" data-section-identifier="" data-fillin="">Milliliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725105/1.0" value="mL/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliliter per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725105/1.0" data-section-identifier="" data-fillin="">Milliliter per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725151/1.0" value="mL/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliliter per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725151/1.0" data-section-identifier="" data-fillin="">Milliliter per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569413/1.0" value="mmol" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Millimole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569413/1.0" data-section-identifier="" data-fillin="">Millimole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581580/1.0" value="mol" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Mole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581580/1.0" data-section-identifier="" data-fillin="">Mole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569415/1.0" value="mosm" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliosmole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569415/1.0" data-section-identifier="" data-fillin="">Milliosmole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569410/1.0" value="mU" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliunit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569410/1.0" data-section-identifier="" data-fillin="">Milliunit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725171/1.0" value="MU" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Million Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725171/1.0" data-section-identifier="" data-fillin="">Million Units</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569419/1.0" value="mV" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Millivolt" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569419/1.0" data-section-identifier="" data-fillin="">Millivolt</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719451/1.0" value="m[iU]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliinternational Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719451/1.0" data-section-identifier="" data-fillin="">Milliinternational Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719449/1.0" value="m[iU]/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Milliinternational Unit per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719449/1.0" data-section-identifier="" data-fillin="">Milliinternational Unit per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569416/1.0" value="M[RAD]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Megarad" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569416/1.0" data-section-identifier="" data-fillin="">Megarad</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569421/1.0" value="nCi" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanocurie" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569421/1.0" data-section-identifier="" data-fillin="">Nanocurie</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2672537/1.0" value="ng" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2672537/1.0" data-section-identifier="" data-fillin="">Nanogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725165/1.0" value="ng/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanogram per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725165/1.0" data-section-identifier="" data-fillin="">Nanogram per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724560/1.0" value="ng/L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanogram per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724560/1.0" data-section-identifier="" data-fillin="">Nanogram per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719066/1.0" value="ng/mL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719066/1.0" data-section-identifier="" data-fillin="">Microgram per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569427/1.0" value="nmol" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanomole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569427/1.0" data-section-identifier="" data-fillin="">Nanomole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569425/1.0" value="nm{light}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Nanometer" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569425/1.0" data-section-identifier="" data-fillin="">Nanometer</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725163/1.0" value="osm" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Osmole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725163/1.0" data-section-identifier="" data-fillin="">Osmole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569430/1.0" value="Pa" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Pascal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569430/1.0" data-section-identifier="" data-fillin="">Pascal</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567618/1.0" value="pg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Picogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567618/1.0" data-section-identifier="" data-fillin="">Picogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577221/1.0" value="s" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Second" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577221/1.0" data-section-identifier="" data-fillin="">Second</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725127/1.0" value="u" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Micro" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725127/1.0" data-section-identifier="" data-fillin="">Micro</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" value="U/g" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Kilounit per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725080/1.0" data-section-identifier="" data-fillin="">Kilounit per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725175/1.0" value="U/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Unit per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725175/1.0" data-section-identifier="" data-fillin="">Unit per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725031/1.0" value="U/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Unit per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725031/1.0" data-section-identifier="" data-fillin="">Unit per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725147/1.0" value="uCi" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microcurie" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725147/1.0" data-section-identifier="" data-fillin="">Microcurie</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569394/1.0" value="ug" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569394/1.0" data-section-identifier="" data-fillin="">Microgram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725145/1.0" value="ug/cm2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Square Centimeter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725145/1.0" data-section-identifier="" data-fillin="">Microgram per Square Centimeter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725050/1.0" value="ug/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725050/1.0" data-section-identifier="" data-fillin="">Microgram per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725144/1.0" value="ug/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725144/1.0" data-section-identifier="" data-fillin="">Microgram per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059690/1.0" value="ug/kg/24.h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Kilogram per Day" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3059690/1.0" data-section-identifier="" data-fillin="">Microgram per Kilogram per Day</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113232/1.0" value="ug/kg/wk" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Kilogram per Week" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3113232/1.0" data-section-identifier="" data-fillin="">Microgram per Kilogram per Week</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725082/1.0" value="ug/m2" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Square Meter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725082/1.0" data-section-identifier="" data-fillin="">Microgram per Square Meter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108589/1.0" value="ug/m2/h" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microgram per Square Meter per Hour" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3108589/1.0" data-section-identifier="" data-fillin="">Microgram per Square Meter per Hour</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567626/1.0" value="uL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567626/1.0" data-section-identifier="" data-fillin="">Microliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567136/1.0" value="umol" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Micromole" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567136/1.0" data-section-identifier="" data-fillin="">Micromole</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719300/1.0" value="u[IU]/mL" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Microinternational Unit per Milliliter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2719300/1.0" data-section-identifier="" data-fillin="">Microinternational Unit per Milliliter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725120/1.0" value="[drp]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Metric Drop" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725120/1.0" data-section-identifier="" data-fillin="">Metric Drop</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725055/1.0" value="[gal_us]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Gallon US" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725055/1.0" data-section-identifier="" data-fillin="">Gallon US</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718872/1.0" value="[iU]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718872/1.0" data-section-identifier="" data-fillin="">International Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725111/1.0" value="[iU]/kg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit per Kilogram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725111/1.0" data-section-identifier="" data-fillin="">International Unit per Kilogram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718870/1.0" value="[iU]/L" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit per Liter" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2718870/1.0" data-section-identifier="" data-fillin="">International Unit per Liter</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725078/1.0" value="[iU]/mg" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit per Milligram" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725078/1.0" data-section-identifier="" data-fillin="">International Unit per Milligram</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725094/1.0" value="[iU]/mg{alpha-Tocopherol}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit per Milligram of Alpha-Tocopherol" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725094/1.0" data-section-identifier="" data-fillin="">International Unit per Milligram of Alpha-Tocopherol</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725096/1.0" value="[iU]{Vitamin&#xA;                     A}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="International Unit of Vitamin A" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725096/1.0" data-section-identifier="" data-fillin="">International Unit of Vitamin A</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569429/1.0" value="[oz_av]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Ounce" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569429/1.0" data-section-identifier="" data-fillin="">Ounce</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725155/1.0" value="[psi]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Pound per Square Inch" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725155/1.0" data-section-identifier="" data-fillin="">Pound per Square Inch</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615202/1.0" value="[RAD]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Rad" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615202/1.0" data-section-identifier="" data-fillin="">Rad</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725185/1.0" value="[tbs_us]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Tablespoon Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725185/1.0" data-section-identifier="" data-fillin="">Tablespoon Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725181/1.0" value="[tsp_us]" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Teaspoon Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725181/1.0" data-section-identifier="" data-fillin="">Teaspoon Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569373/1.0" value="{Application}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Application" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569373/1.0" data-section-identifier="" data-fillin="">Application</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725089/1.0" value="{AUC}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Area under Curve" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725089/1.0" data-section-identifier="" data-fillin="">Area under Curve</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725084/1.0" value="{Bottle}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Bottle Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725084/1.0" data-section-identifier="" data-fillin="">Bottle Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725126/1.0" value="{Caplet}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Caplet Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725126/1.0" data-section-identifier="" data-fillin="">Caplet Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725124/1.0" value="{Capsule}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Capsule Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725124/1.0" data-section-identifier="" data-fillin="">Capsule Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615470/1.0" value="{Cells}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Cell" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2615470/1.0" data-section-identifier="" data-fillin="">Cell</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569377/1.0" value="{Course}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Course" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569377/1.0" data-section-identifier="" data-fillin="">Course</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2576428/1.0" value="{Course}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Cycle" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2576428/1.0" data-section-identifier="" data-fillin="">Cycle</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569379/1.0" value="{Dose}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Dose" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2569379/1.0" data-section-identifier="" data-fillin="">Dose</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725113/1.0" value="{Inhalation}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Inhalation Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725113/1.0" data-section-identifier="" data-fillin="">Inhalation Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725091/1.0" value="{IV Bag}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Intravenous Bag Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725091/1.0" data-section-identifier="" data-fillin="">Intravenous Bag Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725134/1.0" value="{Measure}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Measurement" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725134/1.0" data-section-identifier="" data-fillin="">Measurement</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724564/1.0" value="{No&#xA;                     Scre}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Data Not Available" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2724564/1.0" data-section-identifier="" data-fillin="">Data Not Available</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725160/1.0" value="{packet}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Packet Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725160/1.0" data-section-identifier="" data-fillin="">Packet Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725103/1.0" value="{Patch}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Patch Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725103/1.0" data-section-identifier="" data-fillin="">Patch Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725157/1.0" value="{pfu}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Plaque Forming Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725157/1.0" data-section-identifier="" data-fillin="">Plaque Forming Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725153/1.0" value="{puff}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Puff Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725153/1.0" data-section-identifier="" data-fillin="">Puff Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725098/1.0" value="{RAE}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Retinol Activity Equivalent" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725098/1.0" data-section-identifier="" data-fillin="">Retinol Activity Equivalent</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725100/1.0" value="{RE}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Retinol Equivalent" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725100/1.0" data-section-identifier="" data-fillin="">Retinol Equivalent</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725057/1.0" value="{Seed}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Radioactive Seed Implant Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725057/1.0" data-section-identifier="" data-fillin="">Radioactive Seed Implant Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2571186/1.0" value="{Session}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Session" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2571186/1.0" data-section-identifier="" data-fillin="">Session</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725189/1.0" value="{Spray}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Spray Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725189/1.0" data-section-identifier="" data-fillin="">Spray Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725187/1.0" value="{Suppository}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Suppository Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725187/1.0" data-section-identifier="" data-fillin="">Suppository Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725183/1.0" value="{tbl}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Tablet Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725183/1.0" data-section-identifier="" data-fillin="">Tablet Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725179/1.0" value="{TCID50}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Tissue Culture Infection Dose 50" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725179/1.0" data-section-identifier="" data-fillin="">Tissue Culture Infection Dose 50</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725177/1.0" value="{Troche}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Troche Dosing Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725177/1.0" data-section-identifier="" data-fillin="">Troche Dosing Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567622/1.0" value="{Unit}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567622/1.0" data-section-identifier="" data-fillin="">Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565695/1.0" value="{Unknown}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Unknown" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565695/1.0" data-section-identifier="" data-fillin="">Unknown</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725173/1.0" value="{VP}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Viral Particle Unit" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2725173/1.0" data-section-identifier="" data-fillin="">Viral Particle Unit</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579163/1.0" value="{Wafer}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Wafer Dosage Form" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2579163/1.0" data-section-identifier="" data-fillin="">Wafer Dosage Form</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632843v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2874130/1.0" value="{YU}" data-question-prompt="Dose Units" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632843v1.0" data-responsePrompt="Yeast Units" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2874130/1.0" data-section-identifier="" data-fillin="">Yeast Units</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:3028750v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632841v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Frequency</label><p style="margin: 0;">
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632841v1.0" id="d1e9612" size="100" maxlength="100" data-question-prompt="Frequency" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632841v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2540498v4</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;"> Route</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567786/1.0" value="Infusion" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Infusion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567786/1.0" data-section-identifier="" data-fillin="">Infusion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567787/1.0" value="Inhaled" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Inhaled" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567787/1.0" data-section-identifier="" data-fillin="">Inhaled</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567783/1.0" value="Intradermal" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Intradermal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567783/1.0" data-section-identifier="" data-fillin="">Intradermal</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567788/1.0" value="Intramuscular" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Intramuscular" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567788/1.0" data-section-identifier="" data-fillin="">Intramuscular</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567785/1.0" value="Orally" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Orally" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567785/1.0" data-section-identifier="" data-fillin="">Orally</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567790/1.0" value="Other" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Other" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567790/1.0" data-section-identifier="" data-fillin="">Other</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565646/1.0" value="Rectal" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Rectal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2565646/1.0" data-section-identifier="" data-fillin="">Rectal</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567789/1.0" value="Subcutaneous" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Subcutaneous" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567789/1.0" data-section-identifier="" data-fillin="">Subcutaneous</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567782/1.0" value="Topical" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Topical" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567782/1.0" data-section-identifier="" data-fillin="">Topical</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626718v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567784/1.0" value="Transdermal" data-question-prompt="Route" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626718v1.0" data-responsePrompt="Transdermal" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567784/1.0" data-section-identifier="" data-fillin="">Transdermal</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2179582v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640825v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Dates of Use
                     From:</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640825v1.0" id="d1e10171" size="24" maxlength="24" data-question-prompt="Dates of Use&#xA;                  From:" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="24" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640825v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4633453v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640823v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Dates of Use
                     To:</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640823v1.0" id="d1e10211" size="24" maxlength="24" data-question-prompt="Dates of Use&#xA;                  To:" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="24" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640823v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4633472v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640827v1.0" class="question-prompt" style="display: block; font-weight: bold;"> (if unknown dates, give
                     duration in minutes)</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640827v1.0" id="d1e10250" size="4" maxlength="4" data-question-prompt="(if unknown dates, give&#xA;                  duration in minutes)" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="24" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640827v1.0"><span class="form-cdeId">
                     <p>CDE NCI:64799v3.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640851v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Diagnosis or Reason for
                     Use (Indication)</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640851v1.0" id="d1e10297" size="200" maxlength="200" data-question-prompt="Diagnosis or Reason for&#xA;                  Use (Indication)" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="200" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640851v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2597216v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">5. Event Abated After Use
                     Stopped or Dose Reduced?
                  </h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" value="Yes" data-question-prompt="Event Abated After Use&#xA;                  Stopped or Dose Reduced?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" data-responsePrompt="Yes" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" data-section-identifier="" data-fillin="">Yes</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" value="No" data-question-prompt="Event Abated After Use&#xA;                  Stopped or Dose Reduced?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" data-responsePrompt="No" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" data-section-identifier="" data-fillin="">No</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640831v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" value="Doesn't&#xA;                     Apply" data-question-prompt="Event Abated After Use&#xA;                  Stopped or Dose Reduced?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640831v1.0" data-responsePrompt="Doesn't Apply" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" data-section-identifier="" data-fillin="">Doesn't Apply</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2179608v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632985v1.0" class="question-prompt" style="display: block; font-weight: bold;">6. Lot #</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632985v1.0" id="d1e10511" size="30" maxlength="30" data-question-prompt="Lot #" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632985v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3631708v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632986v1.0" class="question-prompt" style="display: block; font-weight: bold;">7. Expiration
                     Date</label> (MM/DD/YYYY) <input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632986v1.0" id="d1e10556" size="30" maxlength="30" data-question-prompt="Expiration&#xA;                  Date" data-datatype="string_date" data-section-identifier="" data-pattern=" (MM/DD/YYYY) " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632986v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2192901v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">8. Event Reappeared After
                     Reintroduction?
                  </h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" value="Yes" data-question-prompt="Event Reappeared After&#xA;                  Reintroduction?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" data-responsePrompt="Yes" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567168/1.0" data-section-identifier="" data-fillin="">Yes</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" value="No" data-question-prompt="Event Reappeared After&#xA;                  Reintroduction?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" data-responsePrompt="No" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2559515/1.0" data-section-identifier="" data-fillin="">No</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640835v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" value="Doesn't&#xA;                     Apply" data-question-prompt="Event Reappeared After&#xA;                  Reintroduction?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640835v1.0" data-responsePrompt="Doesn't Apply" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2581003/1.0" data-section-identifier="" data-fillin="">Doesn't Apply</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2179615v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640839v1.0" class="question-prompt" style="display: block; font-weight: bold;">9. NDC #</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640839v1.0" id="d1e10773" size="30" maxlength="30" data-question-prompt="NDC #" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640839v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3101068v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640841v1.0" class="question-prompt" style="display: block; font-weight: bold;">OR  Unique ID</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4640841v1.0" id="d1e10817" size="30" maxlength="30" data-question-prompt="Unique ID" data-datatype="string" data-section-identifier="" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4640841v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4384931v1.0</p></span></div><br><br></div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h2 class="section-header"> E. SUSPECT MEDICAL
                  DEVICE
               </h2>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632991v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Brand name</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4632991v1.0" id="d1e10886" size="200" maxlength="200" data-question-prompt="Brand name" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4632991v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2192888v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633041v1.0" class="question-prompt" style="display: block; font-weight: bold;">2. Common Device
                     Name</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633041v1.0" id="d1e10937" size="200" maxlength="200" data-question-prompt="Common Device&#xA;                  Name" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633041v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2748048v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633024v1.0" class="question-prompt" style="display: block; font-weight: bold;">2b. Procode</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633024v1.0" id="d1e10986" size="200" maxlength="200" data-question-prompt="Procode" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633024v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3761048v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633042v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Manufacturer
                     Name</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633042v1.0" id="d1e11034" size="100" maxlength="100" data-question-prompt="Manufacturer&#xA;                  Name" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633042v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2479726v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626915v1.0" class="question-prompt" style="display: block; font-weight: bold;"> City</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626915v1.0" id="d1e11077" size="30" maxlength="30" data-question-prompt="City" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626915v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2748053v2</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;"> State</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" value="AK" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Alaska" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Alaska</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" value="AL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Alabama" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Alabama</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" value="AR" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Arkansas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Arkansas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" value="AZ" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Arizona" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Arizona</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" value="CA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="California" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">California</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" value="CO" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Colorado" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Colorado</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" value="CT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Connecticut" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Connecticut</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" value="DC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="District of Columbia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">District of Columbia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" value="DE" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Delaware" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Delaware</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" value="FL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Florida" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Florida</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" value="GA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Georgia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Georgia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" value="HI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Hawaii" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Hawaii</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" value="IA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Iowa" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Iowa</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" value="ID" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Idaho" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Idaho</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" value="IL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Illinois" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Illinois</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" value="IN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Indiana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Indiana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" value="KS" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Kansas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Kansas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" value="KY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Kentucky" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Kentucky</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" value="LA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Louisiana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Louisiana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" value="MA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Massachusetts" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Massachusetts</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" value="MD" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Maryland" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Maryland</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" value="ME" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Maine" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Maine</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" value="MI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Michigan" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Michigan</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" value="MN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Minnesota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Minnesota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" value="MO" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Missouri" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Missouri</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" value="MS" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Mississippi" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Mississippi</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" value="MT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Montana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Montana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" value="NC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="North Carolina" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">North Carolina</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" value="ND" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="North Dakota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">North Dakota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" value="NE" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Nebraska" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Nebraska</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" value="NH" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="New Hampshire" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">New Hampshire</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" value="NJ" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="New Jersey" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">New Jersey</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" value="NM" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="New Mexico" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">New Mexico</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" value="NV" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Nevada" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Nevada</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" value="NY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="New York" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">New York</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" value="OH" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Ohio" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Ohio</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" value="OK" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Oklahoma" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Oklahoma</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" value="OR" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Oregon" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Oregon</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" value="PA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Pennsylvania" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Pennsylvania</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" value="RI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Rhode Island" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Rhode Island</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" value="SC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="South Carolina" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">South Carolina</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" value="SD" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="South Dakota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">South Dakota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" value="TN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Tennessee" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Tennessee</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" value="TX" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Texas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Texas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" value="UT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Utah" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Utah</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" value="VA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Virginia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Virginia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" value="VT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Vermont" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Vermont</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" value="WA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Washington" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Washington</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" value="WI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Wisconsin" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Wisconsin</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" value="WV" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="West Virginia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">West Virginia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626862v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" value="WY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626862v1.0" data-responsePrompt="Wyoming" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Wyoming</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:4385191v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626860v1.0" class="question-prompt" style="display: block; font-weight: bold;">4. Model #</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626860v1.0" id="d1e13520" size="35" maxlength="35" data-question-prompt="Model #" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626860v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2192895v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633040v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Lot #</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633040v1.0" id="d1e13563" size="30" maxlength="30" data-question-prompt="Lot #" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633040v1.0"><span class="form-cdeId">
                     <p>CDE NCI:3631708v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626795v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Catalog #</label><p style="margin: 0;">
                     Please type the catalog
                     number of the suspected medical device here. 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626795v1.0" id="d1e13605" size="35" maxlength="35" data-question-prompt="Catalog #" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626795v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2192897v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626797v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Expiration
                     Date</label><p style="margin: 0;">
                     Please type the
                     expiration date of the suspected medical device here in 2 digit month / 2 digit
                     day / 4 digit year here. 
                     
                  </p> (MM/DD/YYYY) <input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626797v1.0" id="d1e13654" size="30" maxlength="30" data-question-prompt="Expiration&#xA;                  Date" data-datatype="string_date" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" (MM/DD/YYYY) " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626797v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2192901v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626793v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Serial #</label><p style="margin: 0;">
                     Please type the serial
                     number of the suspected medical device here. 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626793v1.0" id="d1e13703" size="30" maxlength="30" data-question-prompt="Serial #" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626793v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2196242v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise12v1.0" class="question-prompt" style="display: block; font-weight: bold;">OR  Unique ID</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise12v1.0" id="d1e13757" size="30" maxlength="30" data-question-prompt="Unique ID" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise12v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4384931v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626799v1.0" class="question-prompt" style="display: block; font-weight: bold;">6. If Implanted, Give
                     Date</label> (MM/DD/YYYY) <input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626799v1.0" id="d1e13801" size="30" maxlength="30" data-question-prompt="If Implanted, Give&#xA;                  Date" data-datatype="string_date" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" (MM/DD/YYYY) " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626799v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2004505v4</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633056v1.0" class="question-prompt" style="display: block; font-weight: bold;">7. If explanted, give
                     date</label> (MM/DD/YYYY) <input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4633056v1.0" id="d1e13852" size="30" maxlength="30" data-question-prompt="If explanted, give&#xA;                  date" data-datatype="string_date" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" (MM/DD/YYYY) " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4633056v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2192987v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">8. Is this a single-use
                     device that was reprocessed and reused on a patient?
                  </h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626803v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" value="No" data-question-prompt="Is this a single-use&#xA;                  device that was reprocessed and reused on a patient?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626803v1.0" data-responsePrompt="No" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">No</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626803v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" value="Yes" data-question-prompt="Is this a single-use&#xA;                  device that was reprocessed and reused on a patient?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626803v1.0" data-responsePrompt="Yes" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Yes</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2192991v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626801v1.0" class="question-prompt" style="display: block; font-weight: bold;">9. Name of
                     reprocessor</label><p style="margin: 0;">
                     If Yes to Item No. 8,
                     Enter Name of the reprocessor here. 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626801v1.0" id="d1e14056" size="100" maxlength="100" data-question-prompt="Name of&#xA;                  reprocessor" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626801v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2192999v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626859v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Address</label><p style="margin: 0;">
                     If Yes to Item No. 8,
                     Enter Street Address of the reprocessor here 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626859v1.0" id="d1e14105" size="200" maxlength="200" data-question-prompt="Address" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626859v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385738v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626914v1.0" class="question-prompt" style="display: block; font-weight: bold;"> City</label><p style="margin: 0;">
                     If Yes to Item No. 8,
                     Enter City of the reprocessor here 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626914v1.0" id="d1e14154" size="30" maxlength="30" data-question-prompt="City" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626914v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385747v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;"> State</h4>
                  <p style="margin: 0;">
                     If Yes to Item No. 8,
                     Enter State of the reprocessor here 
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" value="AK" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Alaska" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Alaska</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" value="AL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Alabama" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Alabama</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" value="AR" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Arkansas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Arkansas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" value="AZ" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Arizona" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Arizona</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" value="CA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="California" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">California</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" value="CO" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Colorado" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Colorado</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" value="CT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Connecticut" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Connecticut</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" value="DC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="District of Columbia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">District of Columbia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" value="DE" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Delaware" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Delaware</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" value="FL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Florida" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Florida</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" value="GA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Georgia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Georgia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" value="HI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Hawaii" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Hawaii</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" value="IA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Iowa" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Iowa</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" value="ID" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Idaho" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Idaho</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" value="IL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Illinois" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Illinois</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" value="IN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Indiana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Indiana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" value="KS" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Kansas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Kansas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" value="KY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Kentucky" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Kentucky</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" value="LA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Louisiana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Louisiana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" value="MA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Massachusetts" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Massachusetts</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" value="MD" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Maryland" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Maryland</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" value="ME" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Maine" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Maine</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" value="MI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Michigan" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Michigan</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" value="MN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Minnesota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Minnesota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" value="MO" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Missouri" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Missouri</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" value="MS" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Mississippi" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Mississippi</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" value="MT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Montana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Montana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" value="NC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="North Carolina" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">North Carolina</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" value="ND" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="North Dakota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">North Dakota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" value="NE" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Nebraska" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Nebraska</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" value="NH" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="New Hampshire" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">New Hampshire</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" value="NJ" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="New Jersey" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">New Jersey</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" value="NM" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="New Mexico" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">New Mexico</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" value="NV" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Nevada" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Nevada</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" value="NY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="New York" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">New York</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" value="OH" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Ohio" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Ohio</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" value="OK" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Oklahoma" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Oklahoma</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" value="OR" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Oregon" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Oregon</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" value="PA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Pennsylvania" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Pennsylvania</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" value="RI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Rhode Island" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Rhode Island</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" value="SC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="South Carolina" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">South Carolina</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" value="SD" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="South Dakota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">South Dakota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" value="TN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Tennessee" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Tennessee</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" value="TX" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Texas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Texas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" value="UT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Utah" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Utah</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" value="VA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Virginia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Virginia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" value="VT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Vermont" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Vermont</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" value="WA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Washington" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Washington</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" value="WI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Wisconsin" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Wisconsin</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" value="WV" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="West Virginia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">West Virginia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626806v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" value="WY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626806v1.0" data-responsePrompt="Wyoming" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-fillin="">Wyoming</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:4385757v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626858v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Reprocessor Zip
                     Code</label><p style="margin: 0;">
                     If Yes to Item No. 8,
                     Enter Zipcode of the reprocessor here 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#4626858v1.0" id="d1e16603" size="15" maxlength="15" data-question-prompt="Reprocessor Zip&#xA;                  Code" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626704v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#4626858v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385754v1.0</p></span></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h2 class="section-header"> F. OTHER (CONCOMITANT)
                  MEDICAL PRODUCTS
               </h2>
               <p style="margin-left: 3px"></p>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise1v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Product names and therapy
                     dates</label><p style="margin: 0;">
                     (exclude treatment of
                     event) 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise1v1.0" id="d1e16682" size="4000" maxlength="4000" data-question-prompt="Product names and therapy&#xA;                  dates" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626705v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise1v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2006128v2.0</p></span></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h2 class="section-header"> G. REPORTER </h2>
               <p style="margin-left: 3px">(See confidentiality section
                  on back)
               </p>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise2v1.0" class="question-prompt" style="display: block; font-weight: bold;">1. Name</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise2v1.0" id="d1e16764" size="60" maxlength="60" data-question-prompt="Name" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise2v1.0"><span class="form-cdeId">
                     <p>CDE NCI:2201323v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise3v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Address</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise3v1.0" id="d1e16808" size="200" maxlength="200" data-question-prompt="Address" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise3v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385855v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise4v1.0" class="question-prompt" style="display: block; font-weight: bold;"> City</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise4v1.0" id="d1e16850" size="30" maxlength="30" data-question-prompt="City" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise4v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385911v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;"> State</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" value="AK" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Alaska" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577227/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Alaska</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" value="AL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Alabama" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577226/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Alabama</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" value="AR" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Arkansas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577229/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Arkansas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" value="AZ" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Arizona" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577228/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Arizona</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" value="CA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="California" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577230/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">California</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" value="CO" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Colorado" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574185/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Colorado</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" value="CT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Connecticut" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577231/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Connecticut</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" value="DC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="District of Columbia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574186/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">District of Columbia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" value="DE" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Delaware" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2577232/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Delaware</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" value="FL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Florida" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574187/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Florida</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" value="GA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Georgia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2563969/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Georgia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" value="HI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Hawaii" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567778/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Hawaii</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" value="IA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Iowa" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574188/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Iowa</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" value="ID" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Idaho" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574189/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Idaho</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" value="IL" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Illinois" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567779/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Illinois</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" value="IN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Indiana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574190/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Indiana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" value="KS" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Kansas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567743/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Kansas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" value="KY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Kentucky" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574165/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Kentucky</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" value="LA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Louisiana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574166/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Louisiana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" value="MA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Massachusetts" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567723/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Massachusetts</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" value="MD" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Maryland" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567724/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Maryland</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" value="ME" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Maine" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574168/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Maine</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" value="MI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Michigan" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567725/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Michigan</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" value="MN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Minnesota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574169/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Minnesota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" value="MO" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Missouri" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574170/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Missouri</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" value="MS" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Mississippi" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567729/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Mississippi</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" value="MT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Montana" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574171/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Montana</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" value="NC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="North Carolina" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567732/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">North Carolina</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" value="ND" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="North Dakota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567733/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">North Dakota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" value="NE" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Nebraska" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567734/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Nebraska</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" value="NH" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="New Hampshire" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567736/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">New Hampshire</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" value="NJ" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="New Jersey" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567737/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">New Jersey</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" value="NM" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="New Mexico" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567739/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">New Mexico</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" value="NV" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Nevada" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567741/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Nevada</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" value="NY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="New York" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574174/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">New York</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" value="OH" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Ohio" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574175/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Ohio</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" value="OK" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Oklahoma" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574176/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Oklahoma</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" value="OR" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Oregon" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574177/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Oregon</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" value="PA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Pennsylvania" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567745/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Pennsylvania</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" value="RI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Rhode Island" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574179/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Rhode Island</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" value="SC" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="South Carolina" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567750/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">South Carolina</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" value="SD" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="South Dakota" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574180/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">South Dakota</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" value="TN" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Tennessee" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574181/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Tennessee</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" value="TX" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Texas" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567704/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Texas</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" value="UT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Utah" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574160/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Utah</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" value="VA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Virginia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574161/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Virginia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" value="VT" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Vermont" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567697/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Vermont</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" value="WA" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Washington" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574162/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Washington</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" value="WI" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Wisconsin" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567698/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Wisconsin</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" value="WV" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="West Virginia" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2574163/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">West Virginia</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise5v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" value="WY" data-question-prompt="State" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise5v1.0" data-responsePrompt="Wyoming" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/2567699/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Wyoming</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:4385912v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise6v1.0" class="question-prompt" style="display: block; font-weight: bold;"> ZIP</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise6v1.0" id="d1e19285" size="15" maxlength="15" data-question-prompt="ZIP" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise6v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385931v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise7v1.0" class="question-prompt" style="display: block; font-weight: bold;"> Phone #</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise7v1.0" id="d1e19327" size="25" maxlength="25" data-question-prompt="Phone #" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise7v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385953v1.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise8v1.0" class="question-prompt" style="display: block; font-weight: bold;"> E-mail</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise8v1.0" id="d1e19369" size="320" maxlength="320" data-question-prompt="E-mail" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise8v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385951v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">2. Health
                     Professional?
                  </h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise9v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" value="Yes" data-question-prompt="Health&#xA;                  Professional?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise9v1.0" data-responsePrompt="Yes" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197153/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Yes</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise9v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" value="No" data-question-prompt="Health&#xA;                  Professional?" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise9v1.0" data-responsePrompt="No" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/3197154/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">No</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:2179642v2.0</p></span></div>
               <div class="panel-question"><label for="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise10v1.0" class="question-prompt" style="display: block; font-weight: bold;">3. Occupation</label><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise10v1.0" id="d1e19566" size="40" maxlength="40" data-question-prompt="Occupation" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-pattern=" () " data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise10v1.0"><span class="form-cdeId">
                     <p>CDE NCI:4385976v1.0</p></span></div>
               <div class="panel-question">
                  <h4 class="question-prompt" style="font-weight: bold;">4. Also Reported
                     to:
                  </h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise11v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386108/1.0" value="Manufacturer" data-question-prompt="Also Reported&#xA;                  to:" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise11v1.0" data-responsePrompt="Manufacturer" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386108/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Manufacturer</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise11v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386107/1.0" value="User&#xA;                     Facility" data-question-prompt="Also Reported&#xA;                  to:" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise11v1.0" data-responsePrompt="User Facility" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386107/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">User Facility</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_4617751v1.0_question_identifier#Denise11v1.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386105/1.0" value="Distributor/Importer" data-question-prompt="Also Reported&#xA;                  to:" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/question_identifier#Denise11v1.0" data-responsePrompt="Distributor/Importer" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/#list_item_identifier/4386105/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/4617751v1.0/section_element-scoped_identifier#4626706v1.0" data-fillin="">Distributor/Importer</label></li>
                  </ul><span class="form-cdeId">
                     <p>CDE NCI:4386110v1.0</p></span></div>
            </div>
         </section>Form FDA 3500 Submission of a report does not constitute an admission that medical
         personnel or the product caused or contributed to the event.<input type="submit" value="Send Info"><input type="reset"></form>
   </body>
</html>
]]>
            </sdc:sdc_html_form>
         </sdc_html_package>
      </Structured>

      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID/>

   </form>

   <contentType>HTML</contentType>
   <responseCode>Request succeeded</responseCode>
</RetrieveFormResponse>
"""



HERF_html = """<RetrieveFormResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form"
   xmlns:mfi13="http://www.iso.org/19763/13/2013"
   xmlns:dex="urn:ihe:qrph:dex:2013"
   xmlns:mfi6="http://www.iso.org/19763/6/2013"
   xmlns:mdr3="http://www.iso.org/11179/3/2013"
   >
   <form>
       <Structured>
         <sdc_html_package>
            <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
            <sdc:supplemental_data>
               <anyXMLContentType></anyXMLContentType>          
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
             <sdc:sdc_html_form>
			 <![CDATA[
<!DOCTYPE html
  SYSTEM "about:legacy-compat">

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
                    }</style><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script><script type="text/javascript">//
$(function () {
	/*
	 * Process checkboxes and radio buttons so if a parent checkbox/radio button is unchecked, children are unchecked,
	 * if child checked then check parent, etc.
	 */
	var $parentCheckboxes = $('.guarded-element-question').parent().find('input[type=checkbox]:first');
	$parentCheckboxes.each(function () {
		var $parentCheckbox = $(this);
		var $childrenCheckboxes = $parentCheckbox.closest('li').find('ul li input[type=checkbox], input[type=radio]');

		if ($childrenCheckboxes.length > 0) {
			$childrenCheckboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=checkbox], input[type=radio]').is(':checked');
				$parentCheckbox.prop('checked', $anyChildrenChecked);
			});

			$parentCheckbox.click(function () {
				if (!($(this).is(':checked'))) {
					$(this).closest('li').find('ul li input[type=checkbox], input[type=radio]').prop('checked', $(this).prop('checked'));
				}
			})
		}
	});

	var $parentRadioboxes = $('.guarded-element-question').parent().find('input[type=radio]:first');
	$parentRadioboxes.each(function () {
		var $parentRadiobox = $(this);

		var $childrenRadioboxes = $parentRadiobox.closest('li').find('ul li input[type=radio]');
		if ($childrenRadioboxes.length > 0) {
			$childrenRadioboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=radio]').is(':checked');
				$parentRadiobox.prop('checked', $anyChildrenChecked);
			});

			$parentRadiobox.closest('li').siblings().find('input[type=radio]').change(function () {
				$childrenRadioboxes.each(function () {
					$(this).prop('checked', false);
				});
			});
		}
	})
});

var getXmlOutput = (function () {
	'use strict'
	function formatAttributes(attributes) {
		var
		SINGLE_QUOTE = "'",
		DOUBLE_QUOTE = '"',
		ESCAPED_QUOTE = {
			SINGLE_QUOTE : '&quot;',
			DOUBLE_QUOTE : '&apos;'
		};
		var
		att_value,
		single_quote_pos,
		double_quote_pos,
		use_quote,
		escape,
		quote_to_escape,
		att_str,
		re,
		result = '';
		for (var att in attributes) {
			att_value = '' + attributes[att];
			single_quote_pos = att_value.indexOf(SINGLE_QUOTE);
			double_quote_pos = att_value.indexOf(DOUBLE_QUOTE);
			if (single_quote_pos !=  - 1 && double_quote_pos !=  - 1) {
				att_str = ' ' + att + "='" + att_value + "'";
				result += att_str;
				continue;
			}
			if (double_quote_pos !=  - 1 && double_quote_pos < apos_pos) {
				use_quote = SINGLE_QUOTE;
			} else {
				use_quote = DOUBLE_QUOTE;
			}
			escape = ESCAPED_QUOTE[use_quote];
			re = new RegExp(use_quote, 'g');
			att_str = '\n' + '  ' + att + '=' + use_quote + att_value.replace(re, escape) + use_quote;
			result += att_str;
		}
		return result;
	}
	/*
	 *	Public functions
	 */
	function createElement(name, content, attributes) {
		var att_str = '';
		if (attributes) {
			att_str = formatAttributes(attributes);
		}
		var xml;
		if (!content) {
			xml = '<' + name + att_str + '>' + '</' + name + '>';
		} else {
			xml = '<' + name + att_str + '>' + content + '</' + name + '>';
		}
		return xml;
	}
	var repeat_master_list = {};
	function recordRepeatOfQuestion(questionId) {
		var count = repeat_master_list[questionId];
		if (count == null || count == undefined) {
			count = 0;
		}
		++count;
		repeat_master_list[questionId] = count;
		return count;
	}

	function createPayload() {
		var testSection = "";
		$('input').each(function (index, item) {
			var addQuestion = true;

			/* Skip the last two inputs - submit & reset */
			if ($(item).attr('type') != 'submit' && $(item).attr('type') != 'reset') {
				var attrs = [];
				attrs.section_identifier = $(item).attr('data-section-identifier');
				attrs.question_identifier = $(item).attr('data-question-identifier');
				attrs.question_prompt = $(item).attr('data-question-prompt');

				var dtype = $(item).attr('data-datatype');
				if (dtype != undefined && dtype != null && dtype != '') {
					attrs.datatype = $(item).attr('data-datatype');
				}
				var nestedElement = '';
				if ($(item).attr('type') == 'radio' || $(item).attr('type') == 'checkbox') {
					if ($(item).prop('checked')) {

						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						var responseAttrs = [];
						responseAttrs.itemPrompt = $(item).attr('data-responsePrompt');
						responseAttrs.itemIdentifier = $(item).attr('data-responseIdentifier');
						var fillInNum = parseInt($(item).attr('data-fillin'), 10);
						if (fillInNum != NaN && fillInNum > 0) {
							var fillInId = '#' + $(item).attr('id') + '-fillin';
							responseAttrs.fill_in = $(fillInId).val();
						}

						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					} else {
						addQuestion = false;
					}
				} else {
					// Regular text field
					// Skip the fill-in input element
					if ($(item).attr('id').indexOf('fillin') > 0) {
						addQuestion = false;
					}
					// Skip text fields if no text
					var text = $(item).val();
					if (addQuestion && (text == undefined || text == null || text == '')) {
						addQuestion = false;
					}
					if (addQuestion) {
						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					}
				}
				if ($(item).attr('data-pattern')) {
					nestedElement += '\n' + " <!--  " + getXmlOutput.createElement('pattern', $(item).attr('data-pattern')) + " --> ";
				}
				if (addQuestion) {
					testSection += getXmlOutput.createElement('question', nestedElement, attrs) + '\n';
				}
			}
		});

		return testSection;
	}

	return {
		createElement : createElement,
		createPayload : createPayload
	};
})();

function buildRequest(payload, endpoint) {
	var submitUrl = endpoint;
	var formDesignIdentifier = $('#sdc_form').attr('data-formDesignIdentifier');
	var formRepresentationIdentifier = $('#sdc_form').attr('data-formRepresentationIdentifier');
	var requestString =
		'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">\n' +
		'  <soap:Header>\n' +
		'    <Action xmlns="http://www.w3.org/2005/08/addressing">urn:ihe:iti:2007:SubmitForm</Action>\n' +
		'    <MessageID xmlns="http://www.w3.org/2005/08/addressing">urn:uuid:' + guid() + '</MessageID>\n' +
		'    <To xmlns="http://www.w3.org/2005/08/addressing">' + submitUrl + '</To>\n' +
		'    <ReplyTo xmlns="http://www.w3.org/2005/08/addressing">\n' +
		'      <Address>http://www.w3.org/2005/08/addressing/anonymous</Address>\n' +
		'    </ReplyTo>\n' +
		'  </soap:Header>\n' +
		'  <soap:Body>\n' +
		'<SubmitFormRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
		'    xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../Schemas/RFD.xsd" xmlns="urn:ihe:iti:rfd:2007"\n' +
		'    xmlns:sdc="http://nlm.nih.gov/sdc/form">\n' +
		'       <form_data xmlns="http://nlm.nih.gov/sdc/form" form_design_identifier="' + formDesignIdentifier + '"\n' +
		'            form_representation_identifier="' + formRepresentationIdentifier + '">\n' +
		'<body>\n' + payload + '\n' +
		'    </body>\n' +
		'    </form_data>\n' +
		' </SubmitFormRequest>\n' +
		'  </soap:Body>\n' +
		'</soap:Envelope>';

	//console.log(requestString);

	return requestString;
}
var statusMsg = '';
function buildStatusMsg(statusCode, endpoint) {
	if (statusCode === 200 || statusCode == 304) {
		statusMsg += 'SUCCESSFUL Sending status=: ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	
	} else {
		statusMsg += 'ERROR Sending status= ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	}
}

function sendRequest(request, endpoint, msg) {

	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open('POST', endpoint, true);
	xmlhttp.setRequestHeader('Content-Type', 'application/soap+xml');

	xmlhttp.onreadystatechange = function (event) {
		if (xmlhttp.readyState === 4) {
			buildStatusMsg(xmlhttp.status, endpoint);
		}
	};

	xmlhttp.send(request);
}

function submitForm(e, endpoint) {
	if (jQuery.support.opacity == false) {
		//  alert('OLD browser');
		event.returnValue = false;
	} else {
		//   alert('NEW browser');
		e.preventDefault();
		e.stopPropagation();
	}
	// endpoint may contain multiple url's separated by '|', last char will always be '|'
	endpoint = endpoint.replace(/\s+/g, '');
	endpoint = endpoint.substr(0, endpoint.length - 1);
	var endpointArray = endpoint.split('|');

	var payload = getXmlOutput.createPayload();

	for (var i = 0; i < endpointArray.length; i++) {
		var request = buildRequest(payload, endpointArray[i]);
		sendRequest(request, endpointArray[i]);
	}
	setTimeout(function () {
		alert(statusMsg);
	}, 2000);
	return false;
}

/**
 * Generates a GUID string.
 * @returns {String} The generated GUID.
 * @example af8a8416-6e18-a307-bd9c-f2c947bbb3aa
 * @author Slavik Meltser (slavik@meltser.info).
 * @link http://slavik.meltser.info/?p=142
 */
function guid() {
	function _p8(s) {
		var p = (Math.random().toString(16) + "000000000").substr(2, 8);
		return s ? "-" + p.substr(0, 4) + "-" + p.substr(4, 4) : p;
	}
	return _p8() + _p8(true) + _p8(true) + _p8();
}
//
</script></head>
   <body id="form">
      <form method="post" id="sdc_form" data-formDesignIdentifier="http://AHRQ.org/form_design_identifier#HERFv1_2" data-formRepresentationIdentifier="http://nci.nih.gov/xml/owl/cadsr#form_package/99999/1.0" action="#" onsubmit="submitForm(event,&#34;http://10.242.63.50:8080/RFD/Form/RFDSubmitForm_Service|https://10.242.63.50:8181/RFD/Form/RFDSubmitForm_Service|http://spojiti.crgmedical.com/connectSoap/SDCService_v3.asmx?WSDL|https://10.242.63.42:8080/SDCservice.asmx|http://10.242.63.42/SDCservice.asmx|https://10.242.63.41:7443/iheReceiver/services/receive|http://10.242.63.41:7080/iheReceiver/services/receive|https://10.242.63.36:8080/emarcreceiver|http://10.242.63.36/emarcreceiver|http://107.170.9.164:8080/SubmitFormTestService/SubmitForm_Service|&#34;)">
         <div id="form-heading-section">
            <h1 style="padding: 0 5px 0 5px"><span class="text-center"><strong>Healthcare Event Reporting Form (HERF) Hospital Version 1.2</strong></span><br></h1>
         </div>
         <div class="panel-question"><label for="d1e662" class="question-prompt" style="display: block; font-weight: bold;">Event ID</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE2" id="d1e681" size="9" maxlength="9" data-question-prompt="Event ID" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE2"></div>
         <div class="panel-question"><label for="d1e706" class="question-prompt" style="display: block; font-weight: bold;">Initial Report Date</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE30" id="d1e725" size="30" maxlength="30" data-question-prompt="Initial Report Date" data-datatype="string_date" data-section-identifier="" data-pattern="(MM/DD/YYYY)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE30"></div>
         <section>
            <div class="form-section panel-section">
               <div class="panel-question"><label for="d1e756" class="question-prompt" style="display: block; font-weight: bold;">Report Date</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE30" id="d1e783" size="30" maxlength="30" data-question-prompt="Report Date" data-datatype="string_date" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-pattern="(MM/DD/YYYY)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE30"></div>
               <div class="panel-question">
                  <h4 class="question-prompt">What is being reported?</h4>
                  <p style="margin: 0;">
                     CHECK ONE:
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE3" id="http://AHRQ.org/form/list_item_identifier#HERF/DE3/A3" value="A3" data-question-prompt="What is being reported?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE3" data-responsePrompt="Incident" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE3/A3" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Incident</label><div class="guarded-element">
                           <div class="panel-question"><label for="d1e1486" class="question-prompt" style="display: block; font-weight: bold;">Event Discovery Date</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE9a" id="d1e1511" size="30" maxlength="30" data-question-prompt="Event Discovery Date" data-datatype="string" data-section-identifier="" data-pattern="(MM/DD/YYYY)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE9a"></div>
                           <div class="panel-question"><label for="d1e1534" class="question-prompt" style="display: block; font-weight: bold;">Event Discovery Time</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE9b" id="d1e1559" size="30" maxlength="30" data-question-prompt="Event Discovery Time" data-datatype="string" data-section-identifier="" data-pattern="(HHMM)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE9b"><span style="margin-left: 1px">(MILITARY TIME)</span></div>
                        </div>
                        <div class="guarded-element">
                           <div class="panel-question"><label for="d1e1636" class="question-prompt" style="display: block; font-weight: bold;">Patient's Name</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE46" id="d1e1663" size="30" maxlength="30" data-question-prompt="Patient's Name" data-datatype="string" data-section-identifier="" data-pattern="(FIRST, MIDDLE, LAST)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE46"></div>
                           <div class="panel-question"><label for="d1e1687" class="question-prompt" style="display: block; font-weight: bold;">Patient's Date of Birth</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE47" id="d1e1714" size="30" maxlength="30" data-question-prompt="Patient's Date of Birth" data-datatype="string_date" data-section-identifier="" data-pattern="(MM/DD/YYYY)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE47"></div>
                           <div class="panel-question"><label for="d1e1737" class="question-prompt" style="display: block; font-weight: bold;">Patient's Medical Record #</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE49" id="d1e1764" size="30" maxlength="30" data-question-prompt="Patient's Medical Record #" data-datatype="string" data-section-identifier="" data-pattern="" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE49"></div>
                           <div class="panel-question">
                              <h4 class="question-prompt">Patient's Gender</h4>
                              <p style="margin: 0;">
                                 CHECK ONE:
                                 
                                 
                              </p>
                              <ul style="list-style-type: none; margin: 2px 0 0 0">
                                 <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE42" id="http://AHRQ.org/form/list_item_identifier#HERF/DE42/M" value="M" data-question-prompt="Patient's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE42" data-responsePrompt="Male" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE42/M" data-section-identifier="" data-fillin="">Male</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE42" id="http://AHRQ.org/form/list_item_identifier#HERF/DE42/F" value="F" data-question-prompt="Patient's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE42" data-responsePrompt="Female" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE42/F" data-section-identifier="" data-fillin="">Female</label></li>
                                 <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE42" id="http://AHRQ.org/form/list_item_identifier#HERF/DE42/UNK" value="UNK" data-question-prompt="Patient's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE42" data-responsePrompt="Unknown" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE42/UNK" data-section-identifier="" data-fillin="">Unknown</label></li>
                              </ul>
                           </div>
                        </div>
                     </li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE3" id="http://AHRQ.org/form/list_item_identifier#HERF/DE3/A6" value="A6" data-question-prompt="What is being reported?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE3" data-responsePrompt="Near Miss" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE3/A6" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Near Miss</label><div class="guarded-element">
                           <div class="panel-question"><label for="d1e1486" class="question-prompt" style="display: block; font-weight: bold;">Event Discovery Date</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE9a" id="d1e1511" size="30" maxlength="30" data-question-prompt="Event Discovery Date" data-datatype="string" data-section-identifier="" data-pattern="(MM/DD/YYYY)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE9a"></div>
                           <div class="panel-question"><label for="d1e1534" class="question-prompt" style="display: block; font-weight: bold;">Event Discovery Time</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE9b" id="d1e1559" size="30" maxlength="30" data-question-prompt="Event Discovery Time" data-datatype="string" data-section-identifier="" data-pattern="(HHMM)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE9b"><span style="margin-left: 1px">(MILITARY TIME)</span></div>
                        </div>
                     </li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE3" id="http://AHRQ.org/form/list_item_identifier#HERF/DE3/A9" value="A9" data-question-prompt="What is being reported?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE3" data-responsePrompt="Unsafe Condition" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE3/A9" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Unsafe Condition</label></li>
                  </ul>
               </div>
               <div class="panel-question"><label for="d1e1006" class="question-prompt" style="display: block; font-weight: bold;">Briefly describe the event that occurred or unsafe condition</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE15" id="d1e1033" size="30" maxlength="30" data-question-prompt="Briefly describe the event that occurred or unsafe condition" data-datatype="string" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-pattern="" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE15"></div>
               <div class="panel-question"><label for="d1e1052" class="question-prompt" style="display: block; font-weight: bold;">Briefly describe the location where the event occurred or where the unsafe condition
                     exists</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE18" id="d1e1075" size="30" maxlength="30" data-question-prompt="Briefly describe the location where the event occurred or where the unsafe condition exists" data-datatype="string" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-pattern="" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE18"></div>
               <div class="panel-question">
                  <h4 class="question-prompt">Which of the following categories are associated with the event or unsafe
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
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A42" value="A42" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Blood or Blood Product" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A42" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Blood or Blood Product</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A44" value="A44" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Device or Medical/Surgical Supply, including Health Information&#xA;                        Technology (HIT)" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A44" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Device or Medical/Surgical Supply, including Health Information
                           Technology (HIT)</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A48" value="A48" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Fall" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A48" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Fall</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A51" value="A51" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Healthcare-associated Infection" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A51" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Healthcare-associated Infection</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A54" value="A54" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Medication or Other Substance" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A54" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Medication or Other Substance</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A57" value="A57" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Perinatal" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A57" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Perinatal</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A460" value="A60" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Pressure Ulcer" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A460" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Pressure Ulcer</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A63" value="A63" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Surgery or Anesthesia (includes invasive procedure)" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A63" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Surgery or Anesthesia (includes invasive procedure)</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A64" value="A64" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Venous Thromboembolism" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A64" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="">Venous Thromboembolism</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE21" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A66" value="A66" data-question-prompt="Which of the following categories are associated with the event or unsafe&#xA;                  condition?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE21" data-responsePrompt="Other: PLEASE SPECIFY" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A66" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01" data-fillin="20">Other: PLEASE SPECIFY</label><input type="text" id="http://AHRQ.org/form/list_item_identifier#HERF/DE21/A66-fillin" size="20" style="margin-left: 4px; border: none; border-bottom: 1px solid black; text-decoration: underline;"></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> PATIENT INFORMATION (COMPLETE ONLY IF INCIDENT)</h1>
               <p style="margin-left: 3px">Please complete the patient identifiers below. Additional patient information is
                  captured on the Patient Information Form (PIF). (When reporting a perinatal incident
                  that affected a mother and a neonate, please complete the patient identifiers below
                  for the mother (Q8 – Q11) and the neonate (Q12 – Q15). Please also complete a
                  separate PIF for the neonate involved.)
               </p>
               <div class="panel-question"><label for="d1e1486" class="question-prompt" style="display: block; font-weight: bold;">Event Discovery Date</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE9a" id="d1e1511" size="30" maxlength="30" data-question-prompt="Event Discovery Date" data-datatype="string" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01.1" data-pattern="(MM/DD/YYYY)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE9a"></div>
               <div class="panel-question"><label for="d1e1534" class="question-prompt" style="display: block; font-weight: bold;">Event Discovery Time</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE9b" id="d1e1559" size="30" maxlength="30" data-question-prompt="Event Discovery Time" data-datatype="string" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC01.1" data-pattern="(HHMM)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE9b"><span style="margin-left: 1px">(MILITARY TIME)</span></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Patient Information (COMPLETE ONLY IF INCIDENT):</h1>
               <p style="margin-left: 3px">Please complete the patient identifiers below. Additional patient information is
                  captured on the Patient Information Form (PIF). (When reporting a perinatal incident
                  that affected a mother and a neonate, please complete the patient identifiers below
                  for the mother (Q8 – Q11) and the neonate (Q12 – Q15). Please also complete a
                  separate PIF for the neonate involved.)
               </p>
               <div class="panel-question"><label for="d1e1636" class="question-prompt" style="display: block; font-weight: bold;">Patient's Name</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE46" id="d1e1663" size="30" maxlength="30" data-question-prompt="Patient's Name" data-datatype="string" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC02" data-pattern="(FIRST, MIDDLE, LAST)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE46"></div>
               <div class="panel-question"><label for="d1e1687" class="question-prompt" style="display: block; font-weight: bold;">Patient's Date of Birth</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE47" id="d1e1714" size="30" maxlength="30" data-question-prompt="Patient's Date of Birth" data-datatype="string_date" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC02" data-pattern="(MM/DD/YYYY)" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE47"></div>
               <div class="panel-question"><label for="d1e1737" class="question-prompt" style="display: block; font-weight: bold;">Patient's Medical Record #</label><input type="text" name="http:__AHRQ.org_form_question_identifier#HERF_DE49" id="d1e1764" size="30" maxlength="30" data-question-prompt="Patient's Medical Record #" data-datatype="string" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC02" data-pattern="" data-question-repeat="1" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE49"></div>
               <div class="panel-question">
                  <h4 class="question-prompt">Patient's Gender</h4>
                  <p style="margin: 0;">
                     CHECK ONE:
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE42" id="http://AHRQ.org/form/list_item_identifier#HERF/DE42/M" value="M" data-question-prompt="Patient's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE42" data-responsePrompt="Male" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE42/M" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC02" data-fillin="">Male</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE42" id="http://AHRQ.org/form/list_item_identifier#HERF/DE42/F" value="F" data-question-prompt="Patient's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE42" data-responsePrompt="Female" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE42/F" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC02" data-fillin="">Female</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE42" id="http://AHRQ.org/form/list_item_identifier#HERF/DE42/UNK" value="UNK" data-question-prompt="Patient's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE42" data-responsePrompt="Unknown" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE42/UNK" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC02" data-fillin="">Unknown</label></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Neonatal Patient Information:</h1>
               <p style="margin-left: 3px">COMPLETE ONLY FOR NEONATE AFFECTED BY PERINATAL INCIDENT</p>
               <div class="panel-question">
                  <h4 class="question-prompt">Is this event a perinatal incident that affected a neonate?</h4>
                  <p style="margin: 0;">
                     CHECK ONE:
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_Hidden" id="http://AHRQ.org/form/list_item_identifier#HERF/DE34/A15" value="A15" data-question-prompt="Is this event a perinatal incident that affected a neonate?" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/Hidden" data-responsePrompt="Yes" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE34/A15" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC03" data-fillin="">Yes</label><div class="guarded-element-question"><b>Neonate's Name</b> (FIRST, MIDDLE, LAST) <input type="text" name="HERF_DE34" id="d1e2013" size="30" maxlength="30" data-question-prompt="Neonate's Name" data-datatype="string" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE34" data-pattern="(FIRST, MIDDLE, LAST)" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC03" data-question-repeat=""></div>
                        <div class="guarded-element-question"><b>Neonate's Date of Birth</b> (MM/DD/YYYY) <input type="text" name="HERF_DE37" id="d1e2053" size="30" maxlength="30" data-question-prompt="Neonate's Date of Birth" data-datatype="string_date" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE37" data-pattern="(MM/DD/YYYY)" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC03" data-question-repeat="1"></div>
                        <div class="guarded-element-question"><b>Neonate's Medical Record #</b><input type="text" name="HERF_DE40" id="d1e2103" size="30" maxlength="30" data-question-prompt="Neonate's Medical Record #" data-datatype="string" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE40" data-pattern="" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC03" data-question-repeat="1"></div>
                        <div class="guarded-element-question"><b>Neonate's Gender</b>
                           CHECK ONE:
                           
                           
                           <ul style="list-style-type: none; margin: 2px 0 0 0">
                              <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE43" id="http://AHRQ.org/form/list_item_identifier#HERF/DE43/M" value="M" data-question-prompt="Neonate's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE43" data-responsePrompt="Male" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE43/M" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC03" data-fillin="">Male</label></li>
                              <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE43" id="http://AHRQ.org/form/list_item_identifier#HERF/DE43/F" value="F" data-question-prompt="Neonate's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE43" data-responsePrompt="Female" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE43/F" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC03" data-fillin="">Female</label></li>
                              <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE43" id="http://AHRQ.org/form/list_item_identifier#HERF/DE43/UNK" value="UNK" data-question-prompt="Neonate's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE43" data-responsePrompt="Unknown" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE43/UNK" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC03" data-fillin="">Unknown</label></li>
                           </ul>
                        </div>
                     </li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_Hidden" id="http://AHRQ.org/form/list_item_identifier#HERF/DE34/A18" value="A18" data-question-prompt="Neonate's Gender" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/Hidden" data-responsePrompt="No" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE34/A18" data-section-identifier="http://AHRQ.org/form/section_identifier#HERF/SEC03" data-fillin="">No</label></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> REPORT AND EVENT REPORTER INFORMATION</h1>
               <div class="panel-question">
                  <h4 class="question-prompt">Anonymous Reporter</h4>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE33" id="http://AHRQ.org/form/list_item_identifier#HERF/DE33/A15" value="A15" data-question-prompt="Anonymous Reporter" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE33" data-responsePrompt="Yes" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE33/A15" data-section-identifier="http://AHRQ.org/form/list_item_identifier#HERF/SEC04" data-fillin="">Yes</label> (DONE)
                     </li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__AHRQ.org_form_question_identifier#HERF_DE33" id="http://AHRQ.org/form/list_item_identifier#HERF/DE33/A18" value="A18" data-question-prompt="Anonymous Reporter" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE33" data-responsePrompt="No" data-responseIdentifier="http://AHRQ.org/form/list_item_identifier#HERF/DE33/A18" data-section-identifier="http://AHRQ.org/form/list_item_identifier#HERF/SEC04" data-fillin="">No</label><div class="guarded-element-question"><b>Reporter's Name</b> (FIRST, MIDDLE, LAST) <input type="text" name="HERF_DE50" id="d1e2464" size="30" maxlength="30" data-question-prompt="Reporter's Name" data-datatype="string" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE50" data-pattern="(FIRST, MIDDLE, LAST)" data-section-identifier="http://AHRQ.org/form/list_item_identifier#HERF/SEC04" data-question-repeat="1"></div>
                        <div class="guarded-element-question"><b>Telephone Number</b><input type="text" name="HERF_DE52" id="d1e2510" size="30" maxlength="30" data-question-prompt="Telephone Number" data-datatype="integer" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE52" data-pattern="" data-section-identifier="http://AHRQ.org/form/list_item_identifier#HERF/SEC04" data-question-repeat="1"></div>
                        <div class="guarded-element-question"><b>Email Address</b><input type="text" name="HERF_DE53" id="d1e2552" size="30" maxlength="30" data-question-prompt="Email Address" data-datatype="string" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE53" data-pattern="" data-section-identifier="http://AHRQ.org/form/list_item_identifier#HERF/SEC04" data-question-repeat="1"></div>
                        <div class="guarded-element-question"><b>Reporter's Job or Position</b><input type="text" name="HERF_DE36" id="d1e2594" size="30" maxlength="30" data-question-prompt="Reporter's Job or Position" data-datatype="string" data-question-identifier="http://AHRQ.org/form/question_identifier#HERF/DE36" data-pattern="" data-section-identifier="http://AHRQ.org/form/list_item_identifier#HERF/SEC04" data-question-repeat=""></div>
                     </li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Thank you for completing these questions.</h1>
               <p style="margin-left: 3px">OMB No. 0935-0143 Exp. Date 10/31/2014 Public reporting burden for the collection
                  of information is estimated to average 10 minutes per response. An agency may not
                  conduct or sponsor, and a person is not required to respond to, a collection of
                  information unless it displays a currently valid OMB control number. Send comments
                  regarding this burden estimate or any other aspect of this collection of information,
                  including suggestions for reducing this burden, to: AHRQ Reports Clearance Officer,
                  Attention: PRA, Paperwork Reduction Project (0935-0143), AHRQ, 540 Gaither Road, Room
                  #5036, Rockville, MD 20850.
               </p>
            </div>
         </section>AHRQ Common Formats - Hospital Version 1.2 - 2012 Medication or Other Substance<input type="submit" value="Send Info"><input type="reset"></form>
   </body>
</html>
            ]]>
             </sdc:sdc_html_form>
         </sdc_html_package>
      </Structured>

      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID/>

   </form>

   <contentType>HTML</contentType>
   <responseCode>Request succeeded</responseCode>
</RetrieveFormResponse>
"""



NCI_Demographics_html = """<RetrieveFormResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns="urn:ihe:iti:rfd:2007"
   xmlns:sdc="http://nlm.nih.gov/sdc/form"
   xmlns:mfi13="http://www.iso.org/19763/13/2013"
   xmlns:dex="urn:ihe:qrph:dex:2013"
   xmlns:mfi6="http://www.iso.org/19763/6/2013"
   xmlns:mdr3="http://www.iso.org/11179/3/2013"
   >
   <form>
      <Structured>
         <sdc_html_package>
            <!-- Contains supplemental data related to the form instance e.g., generation date, pre-pop data, special instructions, etc. -->
            <sdc:supplemental_data>
               <anyXMLContentType></anyXMLContentType>          
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
<!DOCTYPE html
  SYSTEM "about:legacy-compat">

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
                    }</style><script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script><script type="text/javascript">//
$(function () {
	/*
	 * Process checkboxes and radio buttons so if a parent checkbox/radio button is unchecked, children are unchecked,
	 * if child checked then check parent, etc.
	 */
	var $parentCheckboxes = $('.guarded-element-question').parent().find('input[type=checkbox]:first');
	$parentCheckboxes.each(function () {
		var $parentCheckbox = $(this);
		var $childrenCheckboxes = $parentCheckbox.closest('li').find('ul li input[type=checkbox], input[type=radio]');

		if ($childrenCheckboxes.length > 0) {
			$childrenCheckboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=checkbox], input[type=radio]').is(':checked');
				$parentCheckbox.prop('checked', $anyChildrenChecked);
			});

			$parentCheckbox.click(function () {
				if (!($(this).is(':checked'))) {
					$(this).closest('li').find('ul li input[type=checkbox], input[type=radio]').prop('checked', $(this).prop('checked'));
				}
			})
		}
	});

	var $parentRadioboxes = $('.guarded-element-question').parent().find('input[type=radio]:first');
	$parentRadioboxes.each(function () {
		var $parentRadiobox = $(this);

		var $childrenRadioboxes = $parentRadiobox.closest('li').find('ul li input[type=radio]');
		if ($childrenRadioboxes.length > 0) {
			$childrenRadioboxes.click(function (event) {
				var $anyChildrenChecked = $(this).closest('ul').find('li input[type=radio]').is(':checked');
				$parentRadiobox.prop('checked', $anyChildrenChecked);
			});

			$parentRadiobox.closest('li').siblings().find('input[type=radio]').change(function () {
				$childrenRadioboxes.each(function () {
					$(this).prop('checked', false);
				});
			});
		}
	})
});

var getXmlOutput = (function () {
	'use strict'
	function formatAttributes(attributes) {
		var
		SINGLE_QUOTE = "'",
		DOUBLE_QUOTE = '"',
		ESCAPED_QUOTE = {
			SINGLE_QUOTE : '&quot;',
			DOUBLE_QUOTE : '&apos;'
		};
		var
		att_value,
		single_quote_pos,
		double_quote_pos,
		use_quote,
		escape,
		quote_to_escape,
		att_str,
		re,
		result = '';
		for (var att in attributes) {
			att_value = '' + attributes[att];
			single_quote_pos = att_value.indexOf(SINGLE_QUOTE);
			double_quote_pos = att_value.indexOf(DOUBLE_QUOTE);
			if (single_quote_pos !=  - 1 && double_quote_pos !=  - 1) {
				att_str = ' ' + att + "='" + att_value + "'";
				result += att_str;
				continue;
			}
			if (double_quote_pos !=  - 1 && double_quote_pos < apos_pos) {
				use_quote = SINGLE_QUOTE;
			} else {
				use_quote = DOUBLE_QUOTE;
			}
			escape = ESCAPED_QUOTE[use_quote];
			re = new RegExp(use_quote, 'g');
			att_str = '\n' + '  ' + att + '=' + use_quote + att_value.replace(re, escape) + use_quote;
			result += att_str;
		}
		return result;
	}
	/*
	 *	Public functions
	 */
	function createElement(name, content, attributes) {
		var att_str = '';
		if (attributes) {
			att_str = formatAttributes(attributes);
		}
		var xml;
		if (!content) {
			xml = '<' + name + att_str + '>' + '</' + name + '>';
		} else {
			xml = '<' + name + att_str + '>' + content + '</' + name + '>';
		}
		return xml;
	}
	var repeat_master_list = {};
	function recordRepeatOfQuestion(questionId) {
		var count = repeat_master_list[questionId];
		if (count == null || count == undefined) {
			count = 0;
		}
		++count;
		repeat_master_list[questionId] = count;
		return count;
	}

	function createPayload() {
		var testSection = "";
		$('input').each(function (index, item) {
			var addQuestion = true;

			/* Skip the last two inputs - submit & reset */
			if ($(item).attr('type') != 'submit' && $(item).attr('type') != 'reset') {
				var attrs = [];
				attrs.section_identifier = $(item).attr('data-section-identifier');
				attrs.question_identifier = $(item).attr('data-question-identifier');
				attrs.question_prompt = $(item).attr('data-question-prompt');

				var dtype = $(item).attr('data-datatype');
				if (dtype != undefined && dtype != null && dtype != '') {
					attrs.datatype = $(item).attr('data-datatype');
				}
				var nestedElement = '';
				if ($(item).attr('type') == 'radio' || $(item).attr('type') == 'checkbox') {
					if ($(item).prop('checked')) {

						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						var responseAttrs = [];
						responseAttrs.itemPrompt = $(item).attr('data-responsePrompt');
						responseAttrs.itemIdentifier = $(item).attr('data-responseIdentifier');
						var fillInNum = parseInt($(item).attr('data-fillin'), 10);
						if (fillInNum != NaN && fillInNum > 0) {
							var fillInId = '#' + $(item).attr('id') + '-fillin';
							responseAttrs.fill_in = $(fillInId).val();
						}

						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					} else {
						addQuestion = false;
					}
				} else {
					// Regular text field
					// Skip the fill-in input element
					if ($(item).attr('id').indexOf('fillin') > 0) {
						addQuestion = false;
					}
					// Skip text fields if no text
					var text = $(item).val();
					if (addQuestion && (text == undefined || text == null || text == '')) {
						addQuestion = false;
					}
					if (addQuestion) {
						attrs.question_repeat = recordRepeatOfQuestion($(item).attr('data-question-identifier'));
						nestedElement += '\n' + "   " + getXmlOutput.createElement('response', $(item).val(), responseAttrs);
					}
				}
				if ($(item).attr('data-pattern')) {
					nestedElement += '\n' + " <!--  " + getXmlOutput.createElement('pattern', $(item).attr('data-pattern')) + " --> ";
				}
				if (addQuestion) {
					testSection += getXmlOutput.createElement('question', nestedElement, attrs) + '\n';
				}
			}
		});

		return testSection;
	}

	return {
		createElement : createElement,
		createPayload : createPayload
	};
})();

function buildRequest(payload, endpoint) {
	var submitUrl = endpoint;
	var formDesignIdentifier = $('#sdc_form').attr('data-formDesignIdentifier');
	var formRepresentationIdentifier = $('#sdc_form').attr('data-formRepresentationIdentifier');
	var requestString =
		'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">\n' +
		'  <soap:Header>\n' +
		'    <Action xmlns="http://www.w3.org/2005/08/addressing">urn:ihe:iti:2007:SubmitForm</Action>\n' +
		'    <MessageID xmlns="http://www.w3.org/2005/08/addressing">urn:uuid:' + guid() + '</MessageID>\n' +
		'    <To xmlns="http://www.w3.org/2005/08/addressing">' + submitUrl + '</To>\n' +
		'    <ReplyTo xmlns="http://www.w3.org/2005/08/addressing">\n' +
		'      <Address>http://www.w3.org/2005/08/addressing/anonymous</Address>\n' +
		'    </ReplyTo>\n' +
		'  </soap:Header>\n' +
		'  <soap:Body>\n' +
		'<SubmitFormRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
		'    xsi:schemaLocation="urn:ihe:iti:rfd:2007 ../Schemas/RFD.xsd" xmlns="urn:ihe:iti:rfd:2007"\n' +
		'    xmlns:sdc="http://nlm.nih.gov/sdc/form">\n' +
		'       <form_data xmlns="http://nlm.nih.gov/sdc/form" form_design_identifier="' + formDesignIdentifier + '"\n' +
		'            form_representation_identifier="' + formRepresentationIdentifier + '">\n' +
		'<body>\n' + payload + '\n' +
		'    </body>\n' +
		'    </form_data>\n' +
		' </SubmitFormRequest>\n' +
		'  </soap:Body>\n' +
		'</soap:Envelope>';

	//console.log(requestString);

	return requestString;
}
var statusMsg = '';
function buildStatusMsg(statusCode, endpoint) {
	if (statusCode === 200 || statusCode == 304) {
		statusMsg += 'SUCCESSFUL Sending status=: ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	
	} else {
		statusMsg += 'ERROR Sending status= ' + statusCode + '\n'
		 + 'Endpoint: ' + endpoint + '\n' + '\n';
	}
}

function sendRequest(request, endpoint, msg) {

	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open('POST', endpoint, true);
	xmlhttp.setRequestHeader('Content-Type', 'application/soap+xml');

	xmlhttp.onreadystatechange = function (event) {
		if (xmlhttp.readyState === 4) {
			buildStatusMsg(xmlhttp.status, endpoint);
		}
	};

	xmlhttp.send(request);
}

function submitForm(e, endpoint) {
	if (jQuery.support.opacity == false) {
		//  alert('OLD browser');
		event.returnValue = false;
	} else {
		//   alert('NEW browser');
		e.preventDefault();
		e.stopPropagation();
	}
	// endpoint may contain multiple url's separated by '|', last char will always be '|'
	endpoint = endpoint.replace(/\s+/g, '');
	endpoint = endpoint.substr(0, endpoint.length - 1);
	var endpointArray = endpoint.split('|');

	var payload = getXmlOutput.createPayload();

	for (var i = 0; i < endpointArray.length; i++) {
		var request = buildRequest(payload, endpointArray[i]);
		sendRequest(request, endpointArray[i]);
	}
	setTimeout(function () {
		alert(statusMsg);
	}, 2000);
	return false;
}

/**
 * Generates a GUID string.
 * @returns {String} The generated GUID.
 * @example af8a8416-6e18-a307-bd9c-f2c947bbb3aa
 * @author Slavik Meltser (slavik@meltser.info).
 * @link http://slavik.meltser.info/?p=142
 */
function guid() {
	function _p8(s) {
		var p = (Math.random().toString(16) + "000000000").substr(2, 8);
		return s ? "-" + p.substr(0, 4) + "-" + p.substr(4, 4) : p;
	}
	return _p8() + _p8(true) + _p8(true) + _p8();
}
//
</script></head>
   <body id="form">
      <form method="post" id="sdc_form" data-formDesignIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier#2674812v4.0" data-formRepresentationIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/form_package_identifier#2674812v4.0/1" action="#" onsubmit="submitForm(event,&#34;http://10.242.63.50:8080/RFD/Form/RFDSubmitForm_Service|https://10.242.63.50:8181/RFD/Form/RFDSubmitForm_Service|http://spojiti.crgmedical.com/connectSoap/SDCService_v3.asmx?WSDL|https://10.242.63.42:8080/SDCservice.asmx|http://10.242.63.42/SDCservice.asmx|https://10.242.63.41:7443/iheReceiver/services/receive|http://10.242.63.41:7080/iheReceiver/services/receive|https://10.242.63.36:8080/emarcreceiver|http://10.242.63.36/emarcreceiver|http://107.170.9.164:8080/SubmitFormTestService/SubmitForm_Service|&#34;)">
         <div id="form-heading-section">
            <h1 style="padding: 0 5px 0 5px"><span class="text-center"><strong>Demography NCI Standard Template</strong></span><br></h1>
         </div>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Mandatory
                  Demography Questions
               </h1>
               <p style="margin-left: 3px">These items must
                  be included when this data is collected for reporting
               </p>
               <div class="panel-question">
                  <h4 class="question-prompt">Gender</h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575551/1.0" value="Female" data-question-prompt="Gender" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" data-responsePrompt="Female Gender" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575551/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Female Gender</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575550/1.0" value="Male" data-question-prompt="Gender" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" data-responsePrompt="Male Gender" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575550/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Male Gender</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575365/1.0" value="Unknown" data-question-prompt="Gender" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" data-responsePrompt="Unknown" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575365/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Unknown</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702892v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2573360/1.0" value="Unspecified" data-question-prompt="Gender" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702892v4.0" data-responsePrompt="Unspecified" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2573360/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Unspecified</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Race</h4>
                  <p style="margin: 0;">
                     Check all
                     that apply 
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572232/1.0" value="American&#xA;                                 Indian or Alaska Native" data-question-prompt="Race" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" data-responsePrompt="American Indian or Alaska Native" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572232/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">American Indian or Alaska Native</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572233/1.0" value="Asian" data-question-prompt="Race" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" data-responsePrompt="Asian" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572233/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Asian</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572313/1.0" value="Black or&#xA;                                 African American" data-question-prompt="Race" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" data-responsePrompt="Black or African American" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572313/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Black or African American</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572235/1.0" value="Native&#xA;                                 Hawaiian or other Pacific Islander" data-question-prompt="Race" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" data-responsePrompt="Native Hawaiian or Other Pacific&#xA;                                    Islander" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572235/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Native Hawaiian or Other Pacific
                           Islander</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572578/1.0" value="Not&#xA;                                 Reported" data-question-prompt="Race" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" data-responsePrompt="Not Reported" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572578/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Not Reported</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572577/1.0" value="Unknown" data-question-prompt="Race" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" data-responsePrompt="Unknown" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572577/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Unknown</label></li>
                     <li><label><input type="checkbox" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702904v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572236/1.0" value="White" data-question-prompt="Race" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702904v4.0" data-responsePrompt="White" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572236/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">White</label></li>
                  </ul>
               </div>
               <div class="panel-question"><label for="d1e1255" class="question-prompt" style="display: block; font-weight: bold;">Patient's
                     Date of Birth</label><p style="margin: 0;">
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702903v4.0" id="d1e1277" size="30" maxlength="30" data-question-prompt="Patient's&#xA;                              Date of Birth" data-datatype="string_date" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-pattern="(MM/DD/YYYY)" data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702903v4.0"></div>
               <div class="panel-question">
                  <h4 class="question-prompt">Ethnicity</h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702898v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581176/1.0" value="Hispanic&#xA;                                 or Latino" data-question-prompt="Ethnicity" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0" data-responsePrompt="Hispanic or Latino" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581176/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Hispanic or Latino</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702898v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2567110/1.0" value="Not&#xA;                                 Hispanic or Latino" data-question-prompt="Ethnicity" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0" data-responsePrompt="Not Hispanic or Latino" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2567110/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Not Hispanic or Latino</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702898v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572578/1.0" value="Not&#xA;                                 reported" data-question-prompt="Ethnicity" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0" data-responsePrompt="Not Reported" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572578/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Not Reported</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702898v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572577/1.0" value="Unknown" data-question-prompt="Ethnicity" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702898v4.0" data-responsePrompt="Unknown" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2572577/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702891v4.0" data-fillin="">Unknown</label></li>
                  </ul>
               </div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Conditional
                  Demography Questions
               </h1>
               <p style="margin-left: 3px">There are
                  business rules to indicate situations under which these elements should
                  be used on a case report form.
               </p>
               <div class="panel-question"><label for="d1e1586" class="question-prompt" style="display: block; font-weight: bold;">ZIP
                     Code</label><p style="margin: 0;">
                     
                     Conditionality Rule: Requirement for collection is imposed by the
                     trial sponsor. 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702914v4.0" id="d1e1609" size="15" maxlength="15" data-question-prompt="ZIP&#xA;                              Code" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-pattern="" data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702914v4.0"></div>
               <div class="panel-question">
                  <h4 class="question-prompt">Payment
                     Method
                  </h4>
                  <p style="margin: 0;">
                     
                     Conditionality Rule: Requirement for collection is imposed by the
                     trial sponsor. Sponsor now stipulates the use of codes with the
                     values. 
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936647/1.0" value="Managed&#xA;                                 Care/Medicare" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Managed Care/Medicare" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936647/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Managed Care/Medicare</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865123/1.0" value="Medicaid" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Medicaid" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865123/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Medicaid</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865124/1.0" value="Medicaid&#xA;                                 and Medicare" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Medicare And Medicaid" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865124/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Medicare And Medicaid</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932789/1.0" value="Medicare" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Medicare" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932789/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Medicare</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932791/1.0" value="Medicare&#xA;                                 and Private Insurance" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Medicare And Private Insurance" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932791/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Medicare And Private Insurance</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936649/1.0" value="Military&#xA;                                 or Veterans Sponsored, NOS" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Military Or Veterans Sponsored Insurance, Not&#xA;                                    Otherwise Specified" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936649/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Military Or Veterans Sponsored Insurance, Not
                           Otherwise Specified</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865126/1.0" value="Military&#xA;                                 Sponsored (Including CHAMPUS &amp; TriCare)" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Military Insurance" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865126/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Military Insurance</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865128/1.0" value="No Means&#xA;                                 of Payment (No Insurance)" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="No Insurance" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865128/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">No Insurance</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2559653/1.0" value="Other" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Other" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2559653/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Other</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865120/1.0" value="Private&#xA;                                 Insurance" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Private Insurance" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865120/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Private Insurance</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932793/1.0" value="Self-Pay&#xA;                                 (No Insurance)" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Self Payment" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2932793/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Self Payment</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936648/1.0" value="State&#xA;                                 Supplemental Health Insurance" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="State Supplemental Health Insurance" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936648/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">State Supplemental Health Insurance</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575365/1.0" value="Unknown" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Unknown" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2575365/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Unknown</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702916v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865127/1.0" value="Veterans&#xA;                                 Sponsored" data-question-prompt="Payment&#xA;                              Method" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702916v4.0" data-responsePrompt="Veterans Administration Sponsor&#xA;                                    Insurance" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2865127/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-fillin="">Veterans Administration Sponsor
                           Insurance</label></li>
                  </ul>
               </div>
               <div class="panel-question"><label for="d1e2387" class="question-prompt" style="display: block; font-weight: bold;">Country of
                     Residence</label><p style="margin: 0;">
                     
                     Conditionality Rule: Requirement for collection is imposed by the
                     trial sponsor. 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702932v4.0" id="d1e2410" size="75" maxlength="75" data-question-prompt="Country of&#xA;                              Residence" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-pattern="" data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702932v4.0"></div>
               <div class="panel-question"><label for="d1e2436" class="question-prompt" style="display: block; font-weight: bold;">Date
                     Completed</label><p style="margin: 0;">
                     
                     Conditionality Rule: Data Collection is done using paper Case Report
                     Forms (CRFs) instead of an Electronic Data Capture system.
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702934v4.0" id="d1e2459" size="30" maxlength="30" data-question-prompt="Date&#xA;                              Completed" data-datatype="string_date" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-pattern="(DD/MON/YYYY)" data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702934v4.0"></div>
               <div class="panel-question"><label for="d1e2485" class="question-prompt" style="display: block; font-weight: bold;">CDC Race
                     Code</label><p style="margin: 0;">
                     
                     Conditionality Rule: In the event the sponsor requires the data be
                     collected using the CDC codes, use this CDE instead of 2192199. Do NOT
                     collect both items. 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702936v4.0" id="d1e2508" size="6" maxlength="6" data-question-prompt="CDC Race&#xA;                              Code" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-pattern="" data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702936v4.0"></div>
               <div class="panel-question"><label for="d1e2534" class="question-prompt" style="display: block; font-weight: bold;">CDC Ethnicity
                     Code</label><p style="margin: 0;">
                     
                     Conditionality Rule: In the event the sponsor requires the data be
                     collected using the CDC codes, use this CDE instead of 2192217. Do NOT
                     collect both items. 
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702938v4.0" id="d1e2557" size="6" maxlength="6" data-question-prompt="CDC Ethnicity&#xA;                              Code" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702912v4.0" data-pattern="" data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702938v4.0"></div>
            </div>
         </section>
         <section>
            <div class="form-section panel-section">
               <h1 class="section-header"> Optional
                  Demography Questions
               </h1>
               <p style="margin-left: 3px">There is no
                  requirement for inclusion of these elements on the case report form. If
                  the design and scientific questions posed in the study dictate the need
                  to collect this type of data, these elements should be
                  included.
               </p>
               <div class="panel-question">
                  <h4 class="question-prompt">Highest
                     Education Level
                  </h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2671182/1.0" value="Bachelor's&#xA;                                 Degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="Bachelor's Degree" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2671182/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Bachelor's Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936654/1.0" value="Doctoral&#xA;                                 degree or professional degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="Professional Doctorate or Doctorate&#xA;                                    Degree" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936654/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Professional Doctorate or Doctorate
                           Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936655/1.0" value="Grade&#xA;                                 School" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="Grade School" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936655/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Grade School</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936656/1.0" value="Graduate&#xA;                                 or professional degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="Graduation Or Professional Degree" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936656/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Graduation Or Professional Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936657/1.0" value="High&#xA;                                 school graduate (including equivalency)" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="High School Completion or General Equivalency Diploma&#xA;                                    (GED) Completion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936657/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">High School Completion or General Equivalency Diploma
                           (GED) Completion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654055/1.0" value="Master's&#xA;                                 Degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="Master's Degree" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654055/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Master's Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936661/1.0" value="No formal&#xA;                                 education" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="No Formal Schooling" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936661/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">No Formal Schooling</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2947076/1.0" value="Not high&#xA;                                 school graduate" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="Not High School Graduate" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2947076/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Not High School Graduate</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702942v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936660/1.0" value="Some&#xA;                                 college or associate degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702942v4.0" data-responsePrompt="Some College or Associates Degree" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2936660/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Some College or Associates Degree</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Country of
                     Birth
                  </h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702952v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2571959/1.0" value="Other&#xA;                                 country" data-question-prompt="Country of&#xA;                              Birth" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0" data-responsePrompt="Other country" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2571959/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Other country</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702952v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561053/1.0" value="Other&#xA;                                 country, specify" data-question-prompt="Country of&#xA;                              Birth" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0" data-responsePrompt="OTHER COUNTRY, SPECIFY" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561053/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">OTHER COUNTRY, SPECIFY</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702952v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2564081/1.0" value="USA" data-question-prompt="Country of&#xA;                              Birth" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0" data-responsePrompt="USA" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2564081/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">USA</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702952v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561052/1.0" value="USA,&#xA;                                 specify the 2 letter State code, eg NY" data-question-prompt="Country of&#xA;                              Birth" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702952v4.0" data-responsePrompt="USA, SPECIFY THE 2 LETTER STATE CODE, EG&#xA;                                    NY" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561052/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">USA, SPECIFY THE 2 LETTER STATE CODE, EG
                           NY</label></li>
                  </ul>
               </div>
               <div class="panel-question">
                  <h4 class="question-prompt">Highest
                     Education Level
                  </h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581475/1.0" value="10th&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="10th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581475/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">10th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581476/1.0" value="11th&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="11th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581476/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">11th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654051/1.0" value="12th Grade&#xA;                                 No Diploma" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="12th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654051/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">12th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581466/1.0" value="1st&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="1st Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581466/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">1st Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581467/1.0" value="2nd&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="2nd Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581467/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">2nd Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581468/1.0" value="3rd&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="3rd Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581468/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">3rd Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581469/1.0" value="4th&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="4th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581469/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">4th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581470/1.0" value="5th&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="5th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581470/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">5th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581471/1.0" value="6th&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="6th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581471/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">6th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581472/1.0" value="7th&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="7th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581472/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">7th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581473/1.0" value="8th&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="8th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581473/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">8th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581474/1.0" value="9th&#xA;                                 Grade" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="9th Grade" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2581474/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">9th Grade</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688040/1.0" value="Academic&#xA;                                 Doctorate Degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Academic Doctorate Degree Completion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688040/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Academic Doctorate Degree Completion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654054/1.0" value="Associate&#xA;                                 Degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Associate Degree" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654054/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Associate Degree</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688041/1.0" value="Bachelor&#xA;                                 Degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Bachelor's Degree Completion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688041/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Bachelor's Degree Completion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654058/1.0" value="Don't&#xA;                                 Know" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Does Not Know" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654058/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Does Not Know</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654052/1.0" value="General&#xA;                                 Equivalency Diploma" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="General Equivalency Diploma" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654052/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">General Equivalency Diploma</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2681432/1.0" value="High&#xA;                                 School Graduate" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="High School Graduate" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2681432/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">High School Graduate</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2718906/1.0" value="Kindergarten" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Kindergarten Completion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2718906/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Kindergarten Completion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688039/1.0" value="Master's&#xA;                                 Degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Master's Degree Completion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688039/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Master's Degree Completion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654050/1.0" value="No Formal&#xA;                                 Schooling" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Never Attended" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654050/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Never Attended</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2718907/1.0" value="Preschool" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Preschool Completion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2718907/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Preschool Completion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688038/1.0" value="Professional Doctorate Degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Professional Doctorate Degree Completion" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2688038/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Professional Doctorate Degree Completion</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2579385/1.0" value="Refused" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Refuse" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2579385/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Refuse</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2569309/1.0" value="Some&#xA;                                 College, No Degree" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Some College" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2569309/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Some College</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702957v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654053/1.0" value="VoTech&#xA;                                 Program" data-question-prompt="Highest&#xA;                              Education Level" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702957v4.0" data-responsePrompt="Vocational Degree" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2654053/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Vocational Degree</label></li>
                  </ul>
               </div>
               <div class="panel-question"><label for="d1e4715" class="question-prompt" style="display: block; font-weight: bold;">Census Tract
                     Code at Enrollment</label><p style="margin: 0;">
                     
                     
                  </p><input type="text" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702984v4.0" id="d1e4737" size="6" maxlength="6" data-question-prompt="Census Tract&#xA;                              Code at Enrollment" data-datatype="string" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-pattern="(9999.99)" data-question-repeat="1" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702984v4.0"></div>
               <div class="panel-question">
                  <h4 class="question-prompt">Marital
                     Status
                  </h4>
                  <p style="margin: 0;">
                     
                     
                  </p>
                  <ul style="list-style-type: none; margin: 2px 0 0 0">
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578101/1.0" value="Divorced" data-question-prompt="Marital&#xA;                              Status" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" data-responsePrompt="Divorced: C51776" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578101/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Divorced: C51776</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578103/1.0" value="Domestic&#xA;                                 Partnership" data-question-prompt="Marital&#xA;                              Status" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" data-responsePrompt="Domestic Partner" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578103/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Domestic Partner</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578102/1.0" value="Married" data-question-prompt="Marital&#xA;                              Status" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" data-responsePrompt="Married: C51773" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2578102/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Married: C51773</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2576696/1.0" value="Never&#xA;                                 Married" data-question-prompt="Marital&#xA;                              Status" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" data-responsePrompt="Never married" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2576696/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">Never married</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561620/1.0" value="Separated" data-question-prompt="Marital&#xA;                              Status" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" data-responsePrompt="SEPARATED" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561620/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">SEPARATED</label></li>
                     <li><label><input type="radio" style="margin-right: 5px" name="http:__nci.nih.gov_xml_owl_cadsr_form_form_design_identifier_2674812v4.0_question_identifier#3702985v4.0" id="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561048/1.0" value="Widowed" data-question-prompt="Marital&#xA;                              Status" data-question-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/question_identifier#3702985v4.0" data-responsePrompt="WIDOWED" data-responseIdentifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/#list_item_identifier/2561048/1.0" data-section-identifier="http://nci.nih.gov/xml/owl/cadsr/form/form_design_identifier/2674812v4.0/section_element-scoped_identifier#3702940v4.0" data-fillin="">WIDOWED</label></li>
                  </ul>
               </div>
            </div>
         </section><input type="submit" value="Send Info"><input type="reset"></form>
   </body>
</html>
]]>
               
            </sdc:sdc_html_form>
         </sdc_html_package>
      </Structured>
      
      <!-- Comment: Optionally, insert GUID/UUID to track the RFD RetrieveFormResponse transaction -->
      <instanceID></instanceID>     
   </form>
<contentType>HTML</contentType>
<responseCode>Request succeeded</responseCode>
</RetrieveFormResponse>
"""


