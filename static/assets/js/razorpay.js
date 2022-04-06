
$(document).ready(function () {

  $('#rzp-button1').click(function () {
    var address = $('input[name="address"]:checked').val();


    $.ajax({
      method: 'GET',
      url: '/razorpay',
      data: {
        address: address
      },
      success: function (response) {
        console.log(response)

        
        var options = {
          "key": "rzp_test_3N7o3ki2CcSEKS", // Enter the Key ID generated from the Dashboard
          "amount": response.total * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
          "currency": "INR",
          "name": "Hrishi S Vijayan",
          "description": "Thank you for buying from us",
          "image": "https://example.com/your_logo",
          "handler": function (response) {
            order_place();
          },
          "prefill": {
            "name": response.name,
            "email": response.email,
            "contact": response.phone
          },
          "theme": {
            "color": "#3399cc"
          }
        };
        var rzp1 = new Razorpay(options);
        rzp1.open();

      }
    })

  })

})