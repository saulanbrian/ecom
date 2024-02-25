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
      var total_tag = $('.price-container .total-price')
      var total = parseInt($(total_tag).text())
      
      if ($(this).is(':checked')){
        var product_price = parseInt($(this).closest('.right-container').siblings('.details').find('.price').text().split('$')[1]);
       
        var amount = parseInt($(this).parent('.checkbox-container').siblings('.amount-container').children().filter('input').val());
        
        $(total_tag).text(total+(product_price*amount))
      }else{
        $(total_tag).text(total-1)
      }
      
    });
  });
  

});