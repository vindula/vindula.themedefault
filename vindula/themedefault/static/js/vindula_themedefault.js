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
	
	
	/* ADJUSTMENTS */

	$j('select option').text( function(index, text) {
	 	if ($j(this).text() == 'no value') $j(this).text('--');
	} )
	
	$j('div.autocompleteInputWidget span.option label span').text( function(index, text) {
	 	if ($j(this).text() == '(nothing)') $j(this).text('Nenhum');
	} )
	
	$j('dd.actionMenuContent a.contenttype-collection').attr("class", "contenttype-topic");
	$j('dd.actionMenuContent a.contenttype-link img').hide();
	
	
	/* LINK THEME EDIT */
	$j('div.logo').hover(function(){
		$j('div.logo a.theme-edit').css("display", "inline");
	},function() {
		$j('div.logo a.theme-edit').css("display", "none");
	});
	
	$j('div#informacao').hover(function(){
		$j('div#informacao a.theme-edit').css("display", "inline");
	},function() {
		$j('div#informacao a.theme-edit').css("display", "none");
	});

	
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
	
	/* CORRECTING PROBLEMS WITH FLOAT LEFT */
	
	$j('div.userlist').height($j('div#geral_colunas').height());
	$j('div.food-control-panel').height($j('div#geral_colunas').height());
	 
});