/* FONTE: popupforms.js - */
$j = jQuery.noConflict();

function mostraFoto(){
    var user = $j('#username').val();
    var html = '';
    html +='<img src="/user-image?username='+user+'"/> ';
    if (user != 'undefined') {
        $j('div#preview-user').html(html);
     }
 };


$j(document).ready(function(){
	
    var common_content_filter = '#content>*:not(div.configlet),dl.portalMessage.error,dl.portalMessage.info';
    var common_jqt_config = {fixed:false,speed:'fast',mask:{color:'#000',opacity: 0.4,loadSpeed:0,closeSpeed:0}, height:'400px'};

    // Visual dialog
   
   $j('a.crop-foto').prepOverlay({
        subtype: 'iframe',
        config: common_jqt_config,
        width:'50%'
   });
        
   $j('a.crop-foto').click(function(){
       var height = (window.innerHeight - 22 )*0.7 +'px';
       $j('div.overlay iframe').css('height', height);
       
   });
});