$j = jQuery.noConflict();

$j(document).ready(function(){
	$j(".user-vision").click(function(ev){
        ev.preventDefault();
        ev.stopPropagation();
        $j('a span i',this).toggleClass('vindula-icon-eye-4');
        $j('a span i',this).toggleClass('vindula-icon-eye');
        
		$j(".adm-vision").each(function(){
			$j(this).toggleClass('hide');
		});
		setcookie_vision();

	});
	setup_vision();
});

function setup_vision(){
	var vision = $j.cookie("user_vision");
	if (vision=='show'){
        $j('.user-vision a span i').removeClass('vindula-icon-eye-4');
        $j('.user-vision a span i').addClass('vindula-icon-eye');
        
		$j(".adm-vision").each(function(){
			$j(this).removeClass('hide');
		});
	};
};

function setcookie_vision(){
	var vision = $j.cookie("user_vision");
	if (vision=='show'){
		$j.cookie("user_vision",'hide');		
	}else{
		$j.cookie("user_vision",'show');		
	};
};
