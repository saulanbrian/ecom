$(document).ready(function(){
  var addToCart = $('.button-container');
  
  $(addToCart).each(function(){
    var button =  $(this).children().filter('.add-button').first();
    
    $(button).one('click',function(){
      var p = $(this).closest('.product');
      var product_id = $(p).attr('id');
      
      $.ajax({
        url:addToCartUrl,
        method:'POST',
        headers:{
          'X-CSRFToken':csrfToken
        },
        data:{
          id_:product_id
        },
        success:function(response){
          alert(response.message)
          $(button).text('Go to Cart')
          $(button).removeClass('add-button')
          $(button).attr({
            'onclick':"location.href='" + cartUrl + "'",
          })
        },
        error:function(xhr,status){
          var response = xhr.responseJSON;
          
          alert(response.message)
        }
      });
      
    });
  });
  
  
});