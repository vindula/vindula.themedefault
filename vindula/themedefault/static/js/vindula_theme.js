$j = jQuery.noConflict();

$j(document).ready(function(){
	
	
	/* PERSONAL TOOLS */
	setTextPortalPersonaltools();

	function setTextPortalPersonaltools(){
		var time = new Date();
		time = time.getHours();
		if (time > 17)  var msg = 'Boa noite, ';
		else if (time > 12) var msg = 'Boa tarde, ';
		else var msg = 'Bom dia, ';
		$j('a#user-name').text(msg + $j('a#user-name').text());
	}
	
	/* GALLERY CYCLE NEWS */
	var cycle_timeout = $j('input#cycle-timeout').attr('value');
	
	$j('.gallery-cycle').cycle({
	    fx:     'scrollLeft',
	    speed:   800,
	    timeout: parseInt(cycle_timeout),
	    next:   '#cycle-next',
	    prev:   '#cycle-prev',
		pager:  '#cycle-nav'
	});
	
	$j('div#cycle-nav a').html('<img src="/++theme++vindula.themedefault/images/cyclenav.png" />');
	
	
	/* FILD NAME */
	 $j('div#form-widgets-local_othernews-input-fields span.label').text( function(index, text) {
	 	if ($j(this).text() == '(nothing)') $j(this).text('Em todo o portal');
	 } )
	 
	 $j('div#form-widgets-local_medianews-input-fields span.label').text( function(index, text) {
	 	if ($j(this).text() == '(nothing)') $j(this).text('Em todo o portal');
	 } )
	 
	 $j('div#form-widgets-image-input-fields span.label').text( function(index, text) {
	 	if ($j(this).text() == '(nothing)') $j(this).text('Nenhuma imagem');
	 } )
	 
});