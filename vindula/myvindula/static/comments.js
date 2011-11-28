$j = jQuery.noConflict();

$j(document).ready(function(){	
	$j('#cancel-coment').live('click',function(){
		$j(this).parent().parent().parent().parent().find('#new-comments').css('display','none');
	});
	$j('input[name="url_context"]').attr('value',location);
	
	var user = $j('#user-igual').val();
	if (user == 'True'){
		$j('div#howareu').addClass('display-none');
		$j('div#perfil').removeClass('display-none');
	} else{
		$j('div#perfil').addClass('display-none');
		$j('div#howareu').removeClass('display-none');
	};
	
	
	$j('div#perfil').add
	
	$j('a#howareu').click(function(){
		$j('div#howareu').removeClass('display-none');
		$j('div#perfil').addClass('display-none');
		
		
		$j('li#howareu').addClass('selected');
		$j('li#perfil').removeClass('selected');
		
	});
	
	$j('a#perfil').click(function(){
		$j('div#howareu').addClass('display-none');
		$j('div#perfil').removeClass('display-none');
		
		$j('li#perfil').addClass('selected');
		$j('li#howareu').removeClass('selected');
	});


					
});	