$j = jQuery.noConflict();

$j(document).ready(function(){	
	$j('#cancel-coment').live('click',function(){
		$j(this).parent().parent().parent().parent().find('#new-comments').css('display','none');
	});
	$j('input[name="url_context"]').attr('value',location);
	
					
});	