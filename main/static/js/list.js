
let allProducts = []
let staticData = []
let productsData = []
let pagesNum = 0
let perPage = 10
let usdValute = 10339
let getValuteUrl = `https://nbu.uz/uz/exchange-rates/json/`
let mainContainer

$.ajax({
    type: 'GET',
    url: getValuteUrl,

    success: res => {
    	let obj = res.filter(val => val.title === 'AQSh dollari')
    	usdValute = parseInt(obj[0].cb_price)
    },
    error: (error) => console.error(error)
})

const createProducts = (products, container, isForUserAds=false) => {
	if (products.length < 1) return container.find('.ads-wrapper').html('')

	allProducts = products
	productsData = []
	pagesNum = Math.ceil( products.length / perPage )
	mainContainer = container
	
	for (let i = 0; i < pagesNum; i++) {
		let j = i * 10
		pageList = products.slice(j, j + perPage)
		productsData.push(pageList)
	}

	createProductsHtml(productsData[0], container.find('.ads-wrapper'), isForUserAds)
	createPagination(products, container.find('.btns-wrapper'))
}

const createProductsHtml = (data, container, isForUserAds) => {
	container.html('')
	data.forEach(product => {
		let date = new Date(product.parent_product.created_at)
 		let fullDate = `${date.getDate()}-${date.getMonth()+1}-${date.getFullYear()}, ${date.getHours()}:${date.getMinutes()}`		           
		let adHtml = $(`
			<div class="d-flex my-4 p-3 text-left bg-white shadow ad block-ad" data-product-id="${product.parent_product.id}" data-saved-product="">
	            <a href="/ad/${product.parent_product.id} class="js-qwynlraxz"><img src="${product.parent_product.image_url}" class="ad-photo" alt="image"></a>
	            <div class="d-flex px-3 ad-info-wrap">
	                <div class="d-flex justify-content-between">
	                    <a href="/ad/${product.parent_product.id}" class="text-dark js-qwynlraxz">
	                    <h4 class="text-b">${product.parent_product.title}</h4></a>                    
	                    <h5><strong></strong></h5>
	                </div>
	                <div class="d-flex justify-content-between align-items-center ad-title-info">
	                    <p class="ad-info-text mb-0">${product.parent_product.address} - ${fullDate}</p>
	                    <button class="btn p-0 text-muted add-to-saved-btn waves-effect waves-light">
	                        <i class="far fa-heart" aria-hidden="true"></i>
	                    </button>
	                </div>
	            </div>
	        </div>
		`)

		if (isForUserAds) {
			adHtml.find('.add-to-saved-btn').remove()
			adHtml.find('.ad-title-info').append(`
				<button class="btn btn-danger m-0 px-3 py-2 delete-ad-btn" data-toggle="modal" data-target="#delete-ad-modal">Olib tashlash <i class="fas fa-times ml-1"></i></button>
			`)
		}

		if (product.payment_method == 'Narx') adHtml.find('h5 strong').text(`${product.price} ${product.valute}`)
		else if (product.payment_method == 'Bepul') adHtml.find('h5 strong').text('Hadya qilaman')
		else adHtml.find('h5 strong').text(product.payment_method)

		if (product.parent_product.category_id == 5) {
			if (product.payment_method == 'Narx') adHtml.find('h5 strong').text(`${product.price_from} - ${product.price_to} ${product.valute}`)
			else adHtml.find('h5 strong').text(product.payment_method)
		}

		container.append(adHtml)
	})
	updateSavedProducts(savedProducts)
}

const createPagination = (data, container) => {
	container.html('')

	for (let i = 0; i < pagesNum; i++) {
		let buttonHtml = $(`
			<button onclick="gotoPage($(this))" class="btn btn-primary mx-2 mb-2 py-2 page-btn" data-page-number="${i}">${i + 1}</button>
		`)
		container.append(buttonHtml)
	}
}

const gotoPage = (self) => {
	$('.page-btn').removeClass('active')
	self.addClass('active')
	let pageNum = parseInt(self.data('pageNumber'))
	let page = productsData[pageNum]
	createProductsHtml(page, mainContainer.find('.ads-wrapper'))
}

const sortList = (self, container) => {
	let val = self.val().trim()
	let func

	if (val == 'null') return createProducts(staticData, container)

	if (val == 'price-') {
		allProducts.sort((a, b) => {
			let a_price = a.valute == 'y.e.' ? a.price * usdValute : a.price
			let b_price = b.valute == 'y.e.' ? b.price * usdValute : b.price

			return a_price - b_price
		})
	}

	if (val == 'price+') {
		allProducts.sort((a, b) => {
			let a_price = a.valute == 'y.e.' ? a.price * usdValute : a.price
			let b_price = b.valute == 'y.e.' ? b.price * usdValute : b.price

			return b_price - a_price
		})
	}

	if (val == 'date+') {
		allProducts.sort((a, b) => {
			let a_date = new Date(a.parent_product.created_at)
			let b_date = new Date(b.parent_product.created_at)

			return b_date - a_date
		})
	}

	if (val == 'date-') {
		allProducts.sort((a, b) => {
			let a_date = new Date(a.parent_product.created_at)
			let b_date = new Date(b.parent_product.created_at)

			return a_date - b_date
		})
	}

	createProducts(allProducts, container)
}