function submitFormData(){
    console.log('Payment button clicked')

    var userFormData = {
        'name':null,
        'email':null,
        'total':total,
    }

    var shippingInfo = {
        'address':null,
        'city':null,
        'state':null,
        'zipcode':null,
    }

    if (shipping != 'False'){
        shippingInfo.address = form.address.value
        shippingInfo.city = form.city.value
        shippingInfo.state = form.state.value
        shippingInfo.zipcode = form.zipcode.value
    }

    if (user == 'AnonymousUser'){
        userFormData.name = form.name.value
        userFormData.email = form.email.value
    }

    console.log('Shipping Info:', shippingInfo)
    console.log('User Info:', userFormData)

    var url = "/process_order/"
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'applicaiton/json',
            'X-CSRFToken':csrftoken,
        }, 
        body:JSON.stringify({'form':userFormData, 'shipping':shippingInfo}),
        
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data);
        alert('Transaction completed');  

        cart = {}
        document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

        window.location.href = "{% url 'index' %}"

        })
}

if (shipping == 'False' && user != 'AnonymousUser'){
    //Hide entire form if user is logged in and shipping is false
        document.getElementById('form-wrapper').classList.add("hidden");
        //Show payment if logged in user wants to buy an item that does not require shipping
        document.getElementById('payment-info').classList.remove("hidden");
}
if (shipping == 'False' && user != 'AnonymousUser'){
    //Hide entire form if user is logged in and shipping is false
        document.getElementById('form-wrapper').classList.add("hidden");
        //Show payment if logged in user wants to buy an item that does not require shipping
        document.getElementById('payment-info').classList.remove("hidden");
}