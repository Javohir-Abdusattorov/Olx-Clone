
$(() => {

let url = `http://127.0.0.1:8000/filter/`
let pageCategory = $('.category-name').text().trim()
let prodData = JSON.parse($('.products-data').text().trim())
createProducts(prodData, $('.product-container'))

$('.products-data').remove()
$('.category-name').remove()
$('title').text(pageCategory)

if (pageCategory == 'Yengil mashinalar') $('.car-filter-form').removeClass('d-none')
if (pageCategory == 'Mobil telefon') $('.phone-filter-form').removeClass('d-none')
if (pageCategory == 'Xususiy uylar') $('.house-filter-form').removeClass('d-none')
if (pageCategory == 'Mebel') $('.furniture-filter-form').removeClass('d-none')
if (pageCategory == 'Qo\'l soatlari') $('.watch-filter-form').removeClass('d-none')
if (pageCategory == 'Kvartiralar') $('.apartment-filter-form').removeClass('d-none')

$('.mdb-select').materialSelect()
$('#select-options-house-in-house').find('.select-toggle-all label').text('Barchasini tanlash')
$('#select-options-house-around-house').find('.select-toggle-all label').text('Barchasini tanlash')

$('.filter-form').on('submit', evt => {
	evt.preventDefault()

	let filterParams = {
		q: $('#search').val() ? $('#search').val().trim() : null,
		category: pageCategory,
	}

	otherParams = createFilterParams(filterParams)
	filterParams = Object.assign(filterParams, otherParams)

	console.log(filterParams)
    $.ajax({
        type: 'POST',
        url: url,
        dataType: 'json',
        data: {
        	data: JSON.stringify(filterParams),
        	csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val().trim()
        },

        success: res => {
        	createProducts(res, $('.product-container'))
        }
    })
})

})

const createFilterParams = params => {
	if (params.category == 'Yengil mashinalar') return createCarFilterParams(params)
	else if (params.category == 'Mobil telefon') return createPhoneFilterParams(params)
	else if (params.category == 'Xususiy uylar') return createHouseFilterParams(params)
	else if (params.category == 'Mebel') return createFurnitureFilterParams(params)
	else if (params.category == 'Qo\'l soatlari') return createWatchFilterParams(params)
	else if (params.category == 'Kvartiralar') return createApartmentFilterParams(params)
}

const createParams = (name, typeParams, numberParams, specialParams) => {
	params = {}

	for (let i = 0; i < typeParams.length; i++) {
		let param = typeParams[i]
		let splitParam = param.split('_').join('-')
		let query = `#${name}-${splitParam}`
		params[param] = $(query).val() == 'null' ? null : $(query).val().trim()
	}
	for (let i = 0; i < numberParams.length; i++) {
		let param = `${numberParams[i]}_from`
		let splitParam = param.split('_').join('-')
		let query = `#${name}-${splitParam}`

		params[param] = $(query).val() == 'null' ? null : $(query).val().trim()
	}
	for (let i = 0; i < numberParams.length; i++) {
		let param = `${numberParams[i]}_to`
		let splitParam = param.split('_').join('-')
		let query = `#${name}-${splitParam}`

		params[param] = $(query).val() == 'null' ? null : $(query).val().trim()
	}
	for (let i = 0; i < specialParams.length; i++) {
		let obj = specialParams[i]

		if (obj.role == 'single') {
			let param = obj.name
			let splitParam = param.split('_').join('-')
			let query = `#${name}-${splitParam}`

			params[param] = $(query).val()
		}

		if (obj.role == 'boolean') {
			let param = obj.name
			let splitParam = param.split('_').join('-')
			let query = `#${name}-${splitParam}` 

			params[param] = $(query).val() == 'null' ? null : $(query).val() == '+' ? true : false
		}
	}

	return params
}

const createApartmentFilterParams = params => {
	let typeParams = ['plan', 'house_type', 'condition', 'building_type', 'sanuzel', 'seller']
	let numberParams = ['price', 'rooms_num', 'total_area', 'living_area', 'kitchen_area', 'floor', 'total_floor', 'ceil_height']
	let specialParams = [
		{ name: 'valute', role: 'single' },
		{ name: 'in_house', role: 'single' },
		{ name: 'around_house', role: 'single' },
		{ name: 'with_furniture', role: 'boolean' },
	]

	return createParams('apartment', typeParams, numberParams, specialParams)
}

const createWatchFilterParams = params => {
	let typeParams = ['model', 'condition', 'payment_method', 'seller']
	let numberParams = ['price']
	let specialParams = [{ name: 'valute', role: 'single' }]

	return createParams('watch', typeParams, numberParams, specialParams)
}

const createFurnitureFilterParams = params => {
	let typeParams = ['furniture_type', 'condition', 'payment_method', 'seller']
	let numberParams = ['price']
	let specialParams = [{ name: 'valute', role: 'single' }]

	return createParams('furniture', typeParams, numberParams, specialParams)
}

const createHouseFilterParams = params => {
	let typeParams = ['location', 'house_type', 'condition', 'building_type', 'water_support', 'seller', 'electricity_support', 'heating_support', 'gas_support']
	let numberParams = ['price', 'rooms_num', 'total_area', 'living_area', 'floors_num', 'ceil_height']
	let specialParams = [
		{ name: 'valute', role: 'single' },
		{ name: 'in_house', role: 'single' },
		{ name: 'around_house', role: 'single' },
		{ name: 'with_furniture', role: 'boolean' },
	]

	return createParams('house', typeParams, numberParams, specialParams)
}

const createPhoneFilterParams = params => {
	let typeParams = ['model', 'condition', 'payment_method', 'seller']
	let numberParams = ['price']
	let specialParams = [{ name: 'valute', role: 'single' }]

	return createParams('phone', typeParams, numberParams, specialParams)
}

const createCarFilterParams = params => {
	let typeParams = ['model', 'transmission', 'condition', 'fuel_type', 'payment_method', 'seller']
	let numberParams = ['price', 'engine_size', 'way_length', 'production_year']
	let specialParams = [{ name: 'valute', role: 'single' }]

	return createParams('car', typeParams, numberParams, specialParams)
}