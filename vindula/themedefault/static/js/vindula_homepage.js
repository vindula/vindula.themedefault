$j = jQuery.noConflict();

function onAfter(curr, next, opts, fwd) {
    var index = opts.currSlide;
    $j('#prev')[index == 0 ? 'hide' : 'show']();
    $j('#next')[index == opts.slideCount - 1 ? 'hide' : 'show']();
    //get the height of the current slide
    var $ht = $j(this).height();
    //set the container's height to that of the current slide
    $j(this).parent().css("height", $ht);
}

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
		//height:	441,
		after: onAfter,
		width: 940
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
	
	$j('div#cycle-nav-banner a').html('');
	$j('div#cycle-nav a').html('');
	
});