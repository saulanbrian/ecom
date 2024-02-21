$(document).ready(function(){
  var buttons = $('.button-container').children()
  $(buttons).each(function(){
    $(this).first().click(function(){
      
      $(this).text('clicked')
      
      var id = $(this).parent().attr('class');
      
      $.ajax({
        url:'{% url "add-to-cart" %}',
        method:'POST',
        data:{
          product_id:id
        },
        success:function(){
          alert('success')
        },
        error:function(){
          alert('failed')
        }
        }
      })
    })
  })
})