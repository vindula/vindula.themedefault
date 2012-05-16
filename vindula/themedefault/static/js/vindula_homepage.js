$j = jQuery.noConflict();

$j(document).ready(function(){
	
	
	/* GALLERY CYCLE BANNER */
	var cycle_timeout_banner = $j('input#cycle-timeout-banner').attr('value');
	
	$j('#cont_banner').cycle({
	    fx:     'scrollHorz',
	    speed:   800,
	    timeout: parseInt(cycle_timeout_banner),
	    next:   '#cycle-next-banner',
	    prev:   '#cycle-prev-banner',
		pager:  '#cycle-nav-banner',
		height:	395
	});
	

	/* GALLERY CYCLE NEWS */
	var cycle_timeout = $j('input#cycle-timeout').attr('value');
	
	$j('.gallery-cycle').cycle({
	    fx:     'scrollHorz',
	    speed:   800,
	    timeout: parseInt(cycle_timeout),
	    next:   '#cycle-next',
	    prev:   '#cycle-prev',
		pager:  '#cycle-nav',
		height:	240
	});
	
	$j('div#cycle-nav a').html('<img src="/++theme++vindula.themedefault/images/buttons/cyclenav.png" />');
	
});