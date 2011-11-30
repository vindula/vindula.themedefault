$j = jQuery.noConflict();

$j(document).ready(function(){	
	$j('#cancel-coment').live('click',function(){
		$j(this).parent().parent().parent().parent().find('#new-comments').css('display','none');
	});
	$j('input[name="url_context"]').attr('value',location);
	
	var user = $j('#user-igual').val();
	if (user == 'True'){
		$j('div#howareu').hide();
		$j('div#recados').hide();
		$j('div#perfil').show();
	} else{
		$j('div#perfil').hide();
		$j('div#howareu').show();
		$j('div#recados').hide();
	};
	
	
	$j('a#howareu').click(function(){
		$j('div#howareu').show();
		$j('div#recados').hide();
		$j('div#perfil').hide();
		
		$j('li#howareu').addClass('selected');
		$j('li#scraps').removeClass('selected');
		$j('li#perfil').removeClass('selected');
	});
	
	
	$j('a#scraps').click(function(){
		$j('div#howareu').hide();
		$j('div#recados').show();
		$j('div#perfil').hide();
		
		$j('li#howareu').removeClass('selected');
		$j('li#scraps').addClass('selected');
		$j('li#perfil').removeClass('selected');
	});
	
	
	$j('a#perfil').click(function(){
		$j('div#howareu').hide();
		$j('div#recados').hide();
		$j('div#perfil').show();
		
		$j('li#howareu').removeClass('selected');
		$j('li#scraps').removeClass('selected');
		$j('li#perfil').addClass('selected');
	});

	
	$j('div.geral_lista_comentarios span#number-comments').click(function() {
		var comments = $j(this).parent().parent().find('.comments-cont');
		var text = $j('div.geral_lista_comentarios span#show-hide');
		
		if (comments.css('display') == 'none') {
			comments.show();
			text.text(' Ocultar');
		}
		else {
			comments.hide();
			text.text(' Ver');
		}
	})
				
});	