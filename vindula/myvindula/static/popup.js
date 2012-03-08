/* FONTE: popupforms.js - */
$j = jQuery.noConflict();

$j(document).ready(function(){
	
    var common_content_filter = '#content>*:not(div.configlet),dl.portalMessage.error,dl.portalMessage.info';
    var common_jqt_config = {fixed:false,speed:'fast',mask:{color:'#000',opacity: 0.4,loadSpeed:0,closeSpeed:0}};

 
 
    // Visual dialog
    $j("a.visualiza").prepOverlay({
		subtype: 'ajax',
        filter: common_content_filter,
        formselector: 'addForm',
        closeselector: '[name=form.fechar]',
        width:'50%',
        config: common_jqt_config,
		});
   
});