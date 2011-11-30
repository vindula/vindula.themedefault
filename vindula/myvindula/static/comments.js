$j = jQuery.noConflict();

$j(document).ready(function(){	
	$j('#cancel-coment').live('click',function(){
		$j(this).parent().parent().parent().parent().find('#new-comments').css('display','none');
	});
	$j('input[name="url_context"]').attr('value',location);
	
	var user = $j('#user-igual').val();
	if (user == 'True'){
		$j('div#howareu').addClass('display-none');
		$j('div#recados').addClass('display-none');
		$j('div#perfil').removeClass('display-none');
	} else{
		$j('div#perfil').addClass('display-none');
		$j('div#howareu').removeClass('display-none');
		$j('div#recadosu').removeClass('display-none');
	};
	
	
	$j('a#howareu').click(function(){
		$j('div#howareu').removeClass('display-none');
		$j('div#recados').removeClass('display-none');
		$j('div#perfil').addClass('display-none');
		
		
		$j('li#howareu').addClass('selected');
		$j('li#perfil').removeClass('selected');
		
	});
	
	$j('a#perfil').click(function(){
		$j('div#howareu').addClass('display-none');
		$j('div#recados').addClass('display-none');
		$j('div#perfil').removeClass('display-none');
		
		$j('li#perfil').addClass('selected');
		$j('li#howareu').removeClass('selected');
	});
	
	
	$j('div.geral_lista_comentarios span#number-comments').click(function() {
		var comments = $j(this).parent().parent().find('.comments-cont');
		
		if (comments.css('display') == 'none') 
			comments.show();
		else 
			comments.hide();
	})
				
});	