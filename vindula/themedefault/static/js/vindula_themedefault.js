$j = jQuery.noConflict();

	/* PERSONAL TOOLS */
	function setTextPortalPersonaltools(){
		var time = new Date();
		time = time.getHours();
		if (time > 17)  var msg = 'Boa noite, ';
		else if (time > 12) var msg = 'Boa tarde, ';
		else var msg = 'Bom dia, ';
		$j('a#user-name').text(msg + $j('a#user-name').text());
	};

$j(document).ready(function(){
	
	setTextPortalPersonaltools();

	/* ADJUSTMENTS */ 
	$j('select option').text(function(index, text){
	 	if ($j(this).text() == 'no value') $j(this).text('--');
	});
	
	/* Modificar portlet Navegação */ 
	var html = '<dd class="portletFooter"></dd>';
	$j('div.portletWrapper .portletNavigationTree').each(function(){
		$j(this).append(html);	
	});
	
	/* Modificar links adicionais dos usuarios */ 
	var links = $j('div#links-adcionais').html();
	$j('div#links-adcionais').insertBefore('dl#portal-personaltools #personaltools-logout');


	/*
	$j('div.autocompleteInputWidget span.option label span').text(function(index, text){
	 	if ($j(this).text() == '(nothing)') $j(this).text('Nenhum');
	});*/
	
	/*
	$j('dd.actionMenuContent a.contenttype-collection').attr("class", "contenttype-topic");
	$j('dd.actionMenuContent a.contenttype-link img').hide();*/
	
	
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
	
	
	/* COMMENT BUTTON 
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
	});*/ 
	
	/* CORRECTING PROBLEMS WITH FLOAT LEFT */ 
	//$j('div.userlist').height($j('div#geral_colunas').height());
	//$j('div.food-control-panel').height($j('div#geral_colunas').height());
	
	
	var common_content_filter = '#content>*:not(div.configlet),dl.portalMessage.error,dl.portalMessage.info';
    var common_jqt_config = {fixed:false,speed:'fast',mask:{color:'#000',opacity: 0.4,loadSpeed:0,closeSpeed:0}};

    // Exemplo dialog
    $j('a.visualizacao').prepOverlay({
        subtype: 'image',
        filter: common_content_filter,
        closeselector: '[name=form.cancelar]',
        width: '25%',
        config: common_jqt_config,
        });
	
	 
});