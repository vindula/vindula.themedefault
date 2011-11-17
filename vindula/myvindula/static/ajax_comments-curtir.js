$j = jQuery.noConflict();

$j(document).ready(function(){
	
	$j("div.bt_comentar #comentar").click(function(){
		$j('#comment-geral').css('display','block')
		
	});
	$j("#comment-geral #cancel").click(function(){
		$j('#comment-geral').css('display','none')
		
	});
	
	
	$j('input.comments').click(function(){
		var url = $j('#portal_url').val() + "/myvindula-comments";
		var ctx = $j(this);
		var username = $j('#username').val();
		var id_obj = $j(this).attr('id');
		var type = $j(this).parent().find('#'+id_obj).find('#type').val();
		var isPlone = $j(this).parent().find('#'+id_obj).find('#isPlone').val();
		
		$j.get(url,{username:username,
 				    id_obj:id_obj,
					type:type,
					isPlone:isPlone}, function(data){

				ctx.parent().find('#new-comments').html(data);
				ctx.parent().find('#new-comments').css('display','block');
				//$j('#spinner').addClass('display-none');
				
			});
		
	});
	
	$j('span.link').click(function(){
		var url = $j('#portal_url').val() + "/myvindula-like";
		var url_sucess = $j('#context_url').val();
		var ctx = $j(this);
		
		var username = $j('#username').val();
		var id_obj = $j(this).attr('id');
		var type = $j(this).parent().find('#'+id_obj).find('#type').val();
		var isPlone = $j(this).parent().find('#'+id_obj).find('#isPlone').val();
		
		var dislike = $j(this).attr('src');
		$j.get(url,{username:username,
 				    id_obj:id_obj,
					type:type,
					isPlone:isPlone,
					dislike:dislike}, function(){
				window.location=url_sucess;						
			});
	
	});

});
