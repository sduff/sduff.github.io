document.addEventListener('DOMContentLoaded', function() {
	console.log('Ready');
	submit();
});

function submit() {
	var xmlhttp;
	if (window.XMLHttpRequest) {
		xmlhttp = new XMLHttpRequest();
	} else {
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}

	xmlhttp.onreadystatechange = function () {
		if (xmlhttp.readyState = 4 && xmlhttp.status==200)
		{
			alert("great");
		}
	}
	xmlhttp.open("GET","https://docs.google.com/forms/d/e/1FAIpQLSfHNc1IwugcY_GB2o983NWupttP6ez6ppTSL8LW0xpYMkcQDA/formResponse?ifq&entry.1977584514="+"asdwoasda@asd.com"+"&submit=Submit", true);
	xmlhttp.send();
}

/* https://eureka.ykyuen.info/2014/07/30/submit-google-forms-by-curl-command/
 * https://stackoverflow.com/questions/8567114/how-to-make-an-ajax-call-without-jquery
 * http://www.javascriptkit.com/dhtmltutors/ajaxgetpost.shtml
 * http://www.javascriptkit.com/dhtmltutors/ajaxgetpost2.shtml
 */
