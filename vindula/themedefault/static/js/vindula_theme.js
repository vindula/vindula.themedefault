$j = jQuery.noConflict();

$j(document).ready(function(){
	
setTextPortalPersonaltools();

function setTextPortalPersonaltools(){
	var time = new Date();
	time = time.getHours();
	if (time > 17)  var msg = 'Boa noite, ';
	else if (time > 12) var msg = 'Boa tarde, ';
	else var msg = 'Bom dia, ';
	$j('a#user-name').text(msg + $j('a#user-name').text());
}
		
});