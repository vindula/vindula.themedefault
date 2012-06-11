$j = jQuery.noConflict();

$j(document).ready(function(){
	$j('select#select-holerite').change(function(){
		var url = $j('#portal_url').val() + "/myvindula-find-holerite";
		var competencia = $j(this).val();
		var cpf = $j('#cpf').val();
		$j('#spinner').removeClass('display-none');
		$j('#holerite').addClass('display-none');
		
		$j.get(url,{competencia:competencia,
					cpf:cpf}, function(data){

				$j('#holerite-cont').html(data);
				$j('#holerite-cont').removeClass('display-none');
				$j('#spinner').addClass('display-none');
			});
	});
});