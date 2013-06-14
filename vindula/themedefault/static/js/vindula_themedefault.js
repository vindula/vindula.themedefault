$j = jQuery.noConflict();

	/* PERSONAL TOOLS */
	function setTextPortalPersonaltools(){
		var time = new Date();
		time = time.getHours();
		if (time > 17){
		  var msg = 'Boa noite, ';
		} else if (time > 12){
		  var msg = 'Boa tarde, ';
		} else {
		  var msg = 'Bom dia, ';
		}
		$j('a#user-name').text(msg + $j('a#user-name').text());
	};

	function CheckPost(resp, elem){
		var post = resp.find("textarea"), text = post.val();
		if (text.length > 0) {
			return true;
		}
		else {
			alert('Seu pensamento não pode ficar em branco.');
			launchCKInstances
			return false;
		};
	}

    function enviar_formulario(id_element){
        $j(id_element).submit();
    }


$j(document).ready(function(){
    $j('#new_menssage').click(function(event){
        event.preventDefault();
        event.stopPropagation();
        var url = '/vindula-api/social/personal/message/',
        url = url.concat(window.token,'?iframe_id=new_menssage');

        $j(window.parent.document).vindula('add_menssage_box', {'id': 'new_menssage', 'src': url, 'iframe_class': 'menssage_box', 'left': '200px'});
    });


    $j('.vd-message.has-count > a').click(function(){
        var $ctx = $j(this)

        $.ajax({
            url : url_notified_message,
            type : 'POST',
            data : {hash_obj:'all'},
            success:function(result) {
                if (result.status){
                    $ctx.parent().removeClass('has-count');
                }
            }
        });

    });

    $j('.vd-notify.has-count > a').click(function(){
        var $ctx = $j(this)

        $.ajax({
            url : url_notified_notification,
            type : 'POST',
            data : {hash_obj:'all'},
            success:function(result) {
                if (result.status){
                    $ctx.parent().removeClass('has-count');
                }
            }
        });

    });


	setTextPortalPersonaltools();

	/* ADJUSTMENTS */
	$j('select option').text(function(index, text){
	 	if ($j(this).text() == 'no value') $j(this).text('--');
	});

	/* Modificar links adicionais dos usuarios */
	var links = $j('div#links-adcionais').html();
	$j('div#links-adcionais').insertBefore('dl#portal-personaltools #personaltools-logout');

	/* LINK THEME EDIT */
	$j('div.logo').hover(function(){
		$j('div.logo a.theme-edit').css("display", "inline");
	},function() {
		$j('div.logo a.theme-edit').css("display", "none");
	});

	$j('div#informacao').hover(function(){
		$j('div#informacao a.theme-edit').css("display", "inline");
	},function() {
		$j('div#informacao a.theme-edit').css("display", "none");
	});

	var common_content_filter = '#content=*,dl.portalMessage.error,dl.portalMessage.info';
    var common_jqt_config = {fixed:false,speed:'fast',mask:{color:'#000',opacity: 0.4,loadSpeed:0,closeSpeed:0}};

    // Exemplo dialog
    $j('a.visualizacao').prepOverlay({
        subtype: 'image',
        filter: common_content_filter,
        closeselector: '[name=form.cancelar]',
        width: '25%',
        config: common_jqt_config
        });

    function teste(){
        $j('#fieldset-global-settings').parent().attr('id','content');
    }

    common_jqt_config['onLoad'] = function (e) {launchCKInstances();
                                                $j('#fieldset-global-settings').parent().attr('id','content');
                                                };
    common_jqt_config['onBeforeClose'] = function(e){removeEditor()};

    // Modal do album de fotos
    $j('a.albunphoto').prepOverlay({
        subtype: 'ajax',
        filter: common_content_filter,
        closeselector: '[name=form.cancelar]',
        formselector: '[name=save-coment]',
        width: '50%',
        config: common_jqt_config
        });

    // Howareyou no mural
    $j('a.new-howareu').prepOverlay({
        subtype: 'ajax',
        filter: '#fieldset-global-settings=*',
        formselector: '[name=myvindula-form]',
        noform:'reload',
        width: '50%',
        config: common_jqt_config,
		beforepost: function(resp, elem){
            return CheckPost(resp, elem);
        }
        });

    // Modal editra portlet
    $j('a.portlet-ajax').prepOverlay({
        subtype: 'ajax',
        filter: common_content_filter,
        closeselector: '[name=form.button.cancel],[name=form.actions.cancel]',
        formselector: '[id=zc.page.browser_form],[name=edit_form]',
        noform:'reload',
        width: '50%',
        config: common_jqt_config
        });


	//CRIA UM CYCLE PARA AS IMAGENS DO CABE�ALHO DO PORTAL
	$j('#cycle-logo').cycle({
		cssBefore: {
	        zIndex: 1
	    },
		height: '93px',
		fx: 'fade'
	});


});