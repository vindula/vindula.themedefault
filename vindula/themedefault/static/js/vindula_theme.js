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
	    fx:     'scrollHorz',
	    speed:   800,
	    timeout: parseInt(cycle_timeout),
	    next:   '#cycle-next',
	    prev:   '#cycle-prev',
		pager:  '#cycle-nav',
		height:	240
	});
	
	$j('div#cycle-nav a').html('<img src="/++theme++vindula.themedefault/images/buttons/cyclenav.png" />');
	
	
	/* FILD NAME */

	$j('select option').text( function(index, text) {
	 	if ($j(this).text() == 'no value') $j(this).text('--');
	} )
	
	$j('div.autocompleteInputWidget span.option label span').text( function(index, text) {
	 	if ($j(this).text() == '(nothing)') $j(this).text('Nenhum');
	} )

	
	/* COMMENT BUTTON */
	
	var flag = 0;
	$j('div#comentar').hide();
	$j('input#comentar').click(function(){
		if (flag == 0){
			$j('div#comentar').slideDown('slow');
			flag = 1;	
		}else{
			$j('div#comentar').slideUp('slow');
			flag = 0;
		};
		
	});
	 
});