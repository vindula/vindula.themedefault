$j = jQuery.noConflict();

$j(document).ready(function(){		
	
	var user = $j('#user-igual').val();
	if (user == 'True'){
		$j('div#howareu').hide();
		$j('div#scraps').hide();
		$j('div#perfil').show();
	} else{
		$j('div#perfil').hide();
		$j('div#howareu').show();
		$j('div#scraps').hide();
	};
	
	var variaveis = location.search.split("?");
	var scraps = variaveis[1].lastIndexOf("scraps");
	if (scraps != -1){
		$j('div#howareu').hide();
		$j('div#scraps').show();
		$j('div#perfil').hide();
		
		$j('li#howareu').removeClass('selected');
		$j('li#scraps').addClass('selected');
		$j('li#perfil').removeClass('selected');
		
	};
	  
	
	$j('a#howareu').click(function(){
		$j('div#howareu').show();
		$j('div#scraps').hide();
		$j('div#perfil').hide();
		
		$j('li#howareu').addClass('selected');
		$j('li#scraps').removeClass('selected');
		$j('li#perfil').removeClass('selected');
	});
	
	
	$j('a#scraps').click(function(){
		$j('div#howareu').hide();
		$j('div#scraps').show();
		$j('div#perfil').hide();
		
		$j('li#howareu').removeClass('selected');
		$j('li#scraps').addClass('selected');
		$j('li#perfil').removeClass('selected');
	});
	
	
	$j('a#perfil').click(function(){
		$j('div#howareu').hide();
		$j('div#scraps').hide();
		$j('div#perfil').show();
		
		$j('li#howareu').removeClass('selected');
		$j('li#scraps').removeClass('selected');
		$j('li#perfil').addClass('selected');
	});
	
});