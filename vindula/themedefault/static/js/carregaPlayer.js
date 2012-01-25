$j = jQuery.noConflict();

$j(document).ready(function(){
	$j('a.autoFlowPlayer').each(function(){
		var img = $j(this).parent().find('img');
		var style = "display:block;width:"+img.width()+"px;height:"+img.height()+"px;cursor:pointer;"
		$j(this).attr('style',style);
		
		var href = img.attr('title');
		var id = this.id;
		id = id.replace('_','');
		id = id.replace('.flv','');
		
	});
});