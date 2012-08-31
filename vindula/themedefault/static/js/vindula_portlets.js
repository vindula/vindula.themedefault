$j = jQuery.noConflict();

$j(document).ready(function(){
	
	/* Modificar portlet Navegação */ 
	var html = '<dd class="portletFooter"></dd>';
	$j('div.portletWrapper .portletNavigationTree').each(function(){
		$j(this).append(html);	
	});
	
});