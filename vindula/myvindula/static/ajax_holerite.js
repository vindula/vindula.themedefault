$j = jQuery.noConflict();

$j(document).ready(function(){
	

	$j('select#select-holerite').change(function(){
		var url = $j('#portal_url').val() + "/myvindula-find-holerite";
		var competencia = $j(this).val();
		var matricula = $j('#matricula').val();
		$j('#spinner').removeClass('display-none');
		$j('#holerite').addClass('display-none');
		
		$j.get(url,{competencia:competencia,
					matricula:matricula}, function(data){

				$j('#holerite').html(data);
				$j('#holerite').removeClass('display-none');
				$j('#spinner').addClass('display-none');
				
			});
		
	});
});
