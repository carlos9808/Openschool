$('#forma-chat').on('submit', function(event){
	event.preventDefault();

	$.ajax({
	url: '/post/',
	type: 'POST',
	data: { mensaje: $('#chat-msj').val() },

	succes: function(json){
	  $('#chat-msj').val('');
	  $('#lista').append('<li class="text-right list-group-item"' + json.msj + '</li>');
	  var chatlist= document.getElementById('lista-msj');
	  chatlist.scrollTop= chatlist.scrollHeight;
	}
	});
});
 function getMessages(){
 if(!scrolling){
  $.get('/mensaje/', function(mensajes){
  $.('#lista').html(mensajes);
  var chatlist= document.getElementById('lista-msj');
  chatlist.scrollTop= chatlist.scrollHeight;
  });
 }
 scrolling=false;
 }

 var scrolling=false;
 $(function(){
   $('#lista-msj').on('scroll',function(){
   scrolling=true;
   });
   refreshTimer=setInterval(getMessages,2500);
 });

 $(document).ready(function(){
  $('#Enviar').attr('disabled','disabled');
  $('#chat-msj').keyup(function(){
    if($(this).val() != ''){
    $('#Enviar').removeAttr('disabled');
    }
    else{
     $('#Enviar').attr('disabled','disabled');
    }
  });
 });

 function getCookie(name){
 	var cookieValue=null;
 	if(document.cookie && document.cookie !=''){
 		var cookies=document.cookie.split(';');
 		for(var i=0;i<cookies.length;i++){
 			var cookie=jQuery.trim(cookies[i]);
 			if(cookie.substring(0,name.length+1)==(name+'=')){
 				cookieValue=decodeURIComponent(cookie.substring(name.length+1));
 				break;
 			}
 		}
 	}
 	return cookieValue;
 }
 var csrftoken = getCookie('csrftoken');

 function csrfSafeMethod(method){
 	return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
 }

 $.ajaxSetup({
 	beforeSend: function(xhr,settings) {
 		if(!csrfSafeMethod(settings.type) && !this.crossDomain)
 		{
 			xhr.setRequestHeader("X-CSRFToken",csrftoken);
 		}
 	}
 });