$(document).ready( function() {

    $('.paywithRazorpay').click(function (e){
        
        e.preventDefault();

        var fname = $("[ name='fname' ]").val()
        var lname = $("[ name='fname' ]").val()
        var email = $("[ name='fname' ]").val()
        var phone = $("[ name='fname' ]").val()
        var city = $("[ name='fname' ]").val()
        var state = $("[ name='fname' ]").val()

        if(fname == "" || lname == "" ) {

            alert("All fields are mandatory")
            swal("All fields are mandatory", "error");
            return false;
        }

        else{



        }

        $.ajax({
            method: "method",
            url: "/proeed-to-pay/",
            dataType: "dataType",
            success: function (response) {
                
            }
        });

        var options = {
            "key": "YOUR_KEY_ID", // Enter the Key ID generated from the Dashboard
            "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            "currency": "INR",
            "name": "Acme Corp",
            "description": "Test Transaction",
            "image": "https://example.com/your_logo",
            "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
            "handler": function (response){
                alert(response.razorpay_payment_id);
                alert(response.razorpay_order_id);
                alert(response.razorpay_signature)
            },
            "prefill": {
                "name": "Gaurav Kumar",
                "email": "gaurav.kumar@example.com",
                "contact": "9999999999"
            },
            "notes": {
                "address": "Razorpay Corporate Office"
            },
            "theme": {
                "color": "#3399cc"
            }
        };
        var rzp1 = new Razorpay(options);
       
        rzp1.open();

    });

});