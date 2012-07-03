$j = jQuery.noConflict();

$j(document).ready(function(){
	
	/* Modificar portlet Navegação */ 
	var html = '<dd class="portletFooter"></dd>';
	$j.find(['div.portletWrapper .portletNavigationTree, #portlet-prefs']).each(function(){
		$j(this).append(html);	
	});
	
});