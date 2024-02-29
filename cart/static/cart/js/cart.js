
  
  var buttons = $('.amount-container')
  
  $(buttons).each(function(){
    var btn = $(this).children()
    var plus = $(btn).last()
    var minus = $(btn).first()
    
    $(plus).click(function(){
      var input = $(plus).parent().children().filter('input')
      var current_val = parseInt($(input).val())
      
      $(input).val(current_val+1);
      $(input).trigger('change')
    });
    $(minus).click(function(){
      
      var input = $(this).parent().children().filter('input')
      var current_val =parseInt($(input).val())
      
      if(current_val>=2){
        $(input).val(current_val-1)
        $(input).trigger('change')
      }
      
    });
  });
  
  
  var total_tag = $('footer').find('.total-price')
  var overall_total = 0
  
  
  function calculateTotal(){
    $('.cart-product').each(function(){
      
      let productId = $(this).attr('id')
      
      let checkbox = $(this).find('input[type="checkbox"]')
   
      var price = parseInt($(this).find('.product-price').text().split('$')[1])
      var amount = parseInt($(this).find('.amount-container input').val())
      
      if($(checkbox).is(':checked')){
        overall_total = (overall_total+(price*amount))
        toCheckOut.push({
          product_id:productId,
          amount:amount
        })
      }
      
    });
  }
  
  function resetTotal(){
    overall_total = 0
    toCheckOut = []
  }
  
  function updateTotal(){
    $(total_tag).text(overall_total)
  }
  
  
  $('input[type="checkbox"]').each(function(){
    $(this).change(function(){
      resetTotal()
      calculateTotal()
      updateTotal()
    });
  });
  
  $('.amount-container input').each(function(){
    $(this).change(function(){
      resetTotal()
      calculateTotal()
      updateTotal()
    });
  });
  
 