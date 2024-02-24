$(document).ready(function(){
  
  var buttons = $('.amount-container')
  
  $(buttons).each(function(){
    var btn = $(this).children()
    var plus = $(btn).last()
    var minus = $(btn).first()
    
    $(plus).click(function(){
      var input = $(plus).parent().children().filter('input')
      var current_val = parseInt($(input).val())
      
      $(input).val(current_val+1);
    });
    $(minus).click(function(){
      
      var input = $(this).parent().children().filter('input')
      var current_val =parseInt($(input).val())
      
      if(current_val>=2){
        $(input).val(current_val-1)
      }
      
    });
  });

  $('.checkbox-container input').each(function(){
    $(this).change(function(){
      var total = parseInt($('.price-container .price').text())
      
      if ($(this).is(':checked')){
        alert('checked');
      }else{
        alert('unchecked');
      }
      
    });
  });
  

});