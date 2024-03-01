$(document).ready(function(){
  var currentRoute = $('div.nav-bar').attr('id')
  $('div.nav-bar').children('.nav-btn').each(function(){
    var btnId = $(this).attr('id')
    if(currentRoute==btnId){
      $(this).attr('id','current-route')
    }
  });
});