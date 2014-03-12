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
	});
});