$j = jQuery.noConflict();

$j(document).ready(function(){
	
	function reloadPortlet(){

		$j('#reload-data-protlet').addClass('display-none');
		$j('#spinner').removeClass('display-none');
		
		var url = $j('#url').val() + '/reload-aniversariantes'
		var quantidade = $j('#quantidade').val();
		var tipo_busca = $j('#tipo_busca').val();
		var show_picture = $j('#show_picture').val();
		var details_user = $j('#details_user').val();
		var search_random = $j('#search_random').val();
		
		var max_result = $j('#max_result').val();
		
		if (parseInt(max_result) > parseInt(quantidade)) {
			$j('#b_start').val(sequencia(quantidade,$j('#b_start').val(), max_result));
		};

		var b_start = $j('#b_start').val();

		$j.get(url,{quantidade:quantidade,
 				    type_search:tipo_busca,
					show_picture:show_picture,
					details_user:details_user,
					search_random:search_random,
					b_start:b_start,}, function(data){

				$j('#reload-data-protlet').html(data);
				$j('#reload-data-protlet').removeClass('display-none');
				$j('#spinner').addClass('display-none');
				
			});
	};
	
	function sequencia(quant, b_start, max_result){
		if (max_result != null){
			var x = parseInt(b_start) + parseInt(quant)
			if(parseInt(x) < parseInt(max_result)){
				return x;
			}else{
				return 0
			}
			
		}else{
			return 0; 
		}
		
	};
	/*
	$j('body').click(function(){
		reloadPortlet();	
	});*/
	
	reloadPortlet();
	
	window.setInterval(function(){
		reloadPortlet();
	},300000);//5 minutos

});