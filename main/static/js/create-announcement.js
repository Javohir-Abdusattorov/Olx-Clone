
$('.payment-method[value="Narx"]').attr('checked', true)

$(() => {
	$('.mdb-select').materialSelect()
})

$('.create-form').on('submit', evt => {
	evt.preventDefault()

	if (!$('#category').val() || $('#category').val() == '!=!') return showError()
	if (!$('#subcategory').val() || $('#subcategory').val() == '!=!') return showError()
	if (!$('#title').val()) return showError()
	if (!$('#info').val()) return showError()
	if (!$('#city').val() || $('#city').val() == '!=!') return showError()
	if (!$('#email').val()) return showError()

	let product = {
		title: $('#title').val().trim(),
		category: $('#category').val().trim(),
		subcategory: $('#subcategory').val().trim(),
		description: $('#info').val().trim(),
		image_url: $('.image-link').attr('href'),
		city: $('#city').val().trim(),
		contact_phone: $('#phone').val().trim(),
		contact_email: $('#email').val().trim(),
		csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val().trim(),
	}

	if (!product.image_url) product.image_url = 'https://i.ibb.co/Kx9Y0ht/700x400.png'

	createSubProduct(product)	
	if (product.error) return showError()
		
    $.ajax({
        type: 'POST',
        url: url,
        dataType: 'json',
        data: product,

        success: res => {
        	console.log(res)
        	$('.validation-errors').html('')
        	if (res.error) {
        		for (let i = 0; i < res.message.length; i++) {
        			showErrorText(`${res.message[i].key}: ${res.message[i].value}`)
        		}
        		return;
        	}
        	showSuccess()
        	setTimeout(() => window.location.href = 'http://127.0.0.1:8000/', 3000)
        },
        error: () => responseError()
    })
})