
let savedProducts = JSON.parse(localStorage.getItem('SavedProducts')) || []

$('.add-to-saved-btn').on('click', evt => {
	addToSavedProducts(evt)
})

$('.product-container').on('click', evt => {
	if ( !evt.target.matches('.add-to-saved-btn') ) return

	addToSavedProducts(evt)	
})

const addToSavedProducts = evt=> {
	let productID = $(evt.target).parent().parent().parent().data('productId')
	$(evt.target).parent().parent().parent().attr('data-saved-product', true)

	if (savedProducts.indexOf(productID) > -1) {
		let index = savedProducts.findIndex(prod => prod === productID)
		savedProducts.splice(index, 1)
	} else {
		savedProducts.push(productID)
	}

	updateSavedProducts(savedProducts)
	localStorage.setItem('SavedProducts', JSON.stringify(savedProducts))
}

const updateSavedProducts = savedProducts => {
	for (let i = 0; i < $('.ad').length; i++) {
		let product = $(`.ad:eq(${i})`)
		let productID = product.data('productId')
		product.find('.add-to-saved-btn').removeClass('text-danger').addClass('text-muted').html(`<i class="far fa-heart"></i>`)
		
		if (savedProducts.indexOf(productID) > -1) {
			product.find('.add-to-saved-btn').removeClass('text-muted').addClass('text-danger').html(`<i class="fas fa-heart"></i>`)
		}
	}
}
updateSavedProducts(savedProducts)

$('.saved-ads-btn').on('click', evt => {
	$('.saved-ads-btn').attr('href', `http://127.0.0.1:8000/user-saved-ads?products=${JSON.stringify(savedProducts)}`)
})

const openSubCategories = (self, isTop) => {
	let id = parseInt(self.data('categoryId'))
	let data = categoryData.filter(category => category.id === id)[0]
	let parent = isTop ? $('.subcategory-wrapper-top') : $('.subcategory-wrapper-bottom')
	let container = parent.find('div.d-flex')
	container.html('')

	if ( container.data('currentSub') == id ) {
		return parent.addClass('d-none')
	}

	for (let i = 0; i < data.sub.length; i++) {
		let linkHtml = `<a href="http://127.0.0.1:8000/category/${data.sub[i].id}" class="city-link subcategory-link d-flex align-items-center"><i class="fas fa-chevron-right mr-2"></i> <p class="m-0">${data.sub[i].name}</p></a>`
		container.append(linkHtml)
	}
	container.data('current-sub', id)
	parent.removeClass('d-none')
	isTop ? $('.subcategory-wrapper-bottom').addClass('d-none') : $('.subcategory-wrapper-top').addClass('d-none')
}