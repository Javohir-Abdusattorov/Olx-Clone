
let carModelContainer = $('.transport-car-model')
let carPriceInput = carModelContainer.find('#car-price')
let carValuteInput = carModelContainer.find('.car-valute-select')
let carModelInput = carModelContainer.find('#car-model')
let carYearInput = carModelContainer.find('#car-year-production')
let carWayInput = carModelContainer.find('#car-way-length')
let carEngineSizeInput = carModelContainer.find('#car-engine-size')

let phoneModelContainer = $('.electrical-phone-model')
let phonePriceInput = phoneModelContainer.find('#phone-price')
let phoneValuteInput = phoneModelContainer.find('.phone-valute-select')
let phoneModelInput = phoneModelContainer.find('#phone-model')

let houseModelContainer = $('.realty-house-model')
let houseValuteInput = houseModelContainer.find('.house-valute-select')
let housePriceInput = houseModelContainer.find('#house-price')
let houseRoomNumInput = houseModelContainer.find('#house-rooms-num')
let houseTotalAreaInput = houseModelContainer.find('#house-total-area')
let houseLivingAreaInput = houseModelContainer.find('#house-living-area')
let houseFloorNumInput = houseModelContainer.find('#house-floor-num')
let houseCeilHeightInput = houseModelContainer.find('#house-ceil-height')

let furnitureModelContainer = $('.houseandgarden-furniture-model')
let furnitureValuteInput = furnitureModelContainer.find('.furniture-valute-select')
let furniturePriceInput = furnitureModelContainer.find('#furniture-price')

let watchModelContainer = $('.fashion-watch-model')
let watchPriceInput = watchModelContainer.find('#watch-price')
let watchValuteInput = watchModelContainer.find('.watch-valute-select')
let watchModelInput = watchModelContainer.find('#watch-model')

let apartmentModelContainer = $('.realty-apartment-model')
let apartmentValuteInput = apartmentModelContainer.find('.apartment-valute-select')
let apartmentPriceInput = apartmentModelContainer.find('#apartment-price')
let apartmentRoomsNumInput = apartmentModelContainer.find('#apartment-rooms-num')
let apartmentTotalAreaInput = apartmentModelContainer.find('#apartment-total-area')
let apartmentLivingAreaInput = apartmentModelContainer.find('#apartment-living-area')
let apartmentKitchenAreaInput = apartmentModelContainer.find('#apartment-kitchen-area')
let apartmentFloorInput = apartmentModelContainer.find('#apartment-floor')
let apartmentTotalFloorInput = apartmentModelContainer.find('#apartment-total-floor')
let apartmentConstructionYearInput = apartmentModelContainer.find('#apartment-construction-year')
let apartmentCeilHeightInput = apartmentModelContainer.find('#apartment-ceil-height')

let url = window.location.href
let subcategories = []
let productImageDeleteUrl = ''

$(() => {
	let data = $('.subcategories-data').text().trim()
	subcategories = JSON.parse(data)
	$('.subcategories-data').remove()
})

const createProductCAR = prod => {
	let paymentMethod = carModelContainer.find('input#car-payment-method:checked')
	let transmission = carModelContainer.find('input#car-transmission:checked')
	let fuelType = carModelContainer.find('input#car-fuel-type:checked')
	let condition = carModelContainer.find('input#car-condition:checked')
	let otherOptions = getCheckboxData( carModelContainer.find('.car-other-options') )
	let seller = carModelContainer.find('input#car-seller:checked')
	prod.error = true

	if (!paymentMethod.length) return showError()
	if (paymentMethod == 'Narx') {
		if (!carPriceInput.val().trim() || parseInt(carPriceInput.val().trim()) < 0 ) return showError()
	}			
	if (carModelInput.val() == '!=!') return showError()
	if (!carYearInput.val().trim()) return showError()
	if (!carWayInput.val().trim()) return showError()
	if (!transmission.length) return showError()
	if (!carEngineSizeInput.val().trim()) return showError()
	if (!fuelType.length) return showError()
	if (!condition.length) return showError()
	if (!otherOptions) return showError()
	if (!seller.length) return showError()

	prod.error = false
	prod.payment_method = paymentMethod.val().trim()
	prod.price = parseInt(carPriceInput.val().trim())
	prod.valute = carValuteInput.val().trim()
	prod.model = carModelInput.val().trim()
	prod.production_year = parseInt(carYearInput.val().trim())
	prod.way_length = parseInt(carWayInput.val().trim())
	prod.transmission = transmission.val().trim()
	prod.engine_size = parseFloat(carEngineSizeInput.val().trim())
	prod.fuel_type = fuelType.val().trim()
	prod.condition = condition.val().trim()
	prod.other_options = otherOptions
	prod.seller = seller.val().trim()

	if (prod.payment_method == 'Ayirboshlash') prod.price == 0

	return prod
}

const creataProductPHONE = prod => {
	let paymentMethod = phoneModelContainer.find('input#phone-payment-method:checked').val().trim()
	let condition = phoneModelContainer.find('input#phone-condition:checked')
	let seller = phoneModelContainer.find('input#phone-seller:checked')
	prod.error = true

	if (!paymentMethod.length) return showError()
	if (paymentMethod == 'Narx') {
		if (!phonePriceInput.val().trim() || parseInt(phonePriceInput.val().trim()) < 0) return showError()
	}
	if (phoneModelInput.val() == '!=!') return showError()
	if (!condition.length) return showError()
	if (!seller.length) return showError()

	prod.error = false
	prod.payment_method = paymentMethod
	prod.price = parseInt(phonePriceInput.val().trim())
	prod.valute = phoneValuteInput.val().trim()
	prod.model = phoneModelInput.val().trim()
	prod.condition = condition.val().trim()
	prod.seller = seller.val().trim()

	if (prod.payment_method == 'Narx') prod.price = parseInt(phonePriceInput.val().trim())
		else prod.price = 0

	return prod
}

const createProductHOUSE = prod => {
	let houseLocation = $('input.house-location:checked')
	let houseWithFurniture = $('.house-with-furniture:checked')
	let houseCondition = $('.house-condition:checked')
	let houseType = $('#house-type')
	let houseBuildingType = $('#house-building-type')
	let houseWaterSupport = $('.house-water:checked')
	let houseElectricitySupport = $('.house-electricity-support:checked')
	let houseHeatingSupport = $('.house-heating:checked')
	let houseGasSupport = $('.house-gas-support:checked')
	let houseSeller = $('.house-seller:checked')
	let inHouse = getCheckboxData( houseModelContainer.find('.in-house-container') )
	let aroundHouse = getCheckboxData( houseModelContainer.find('.around-house-container') )
	prod.error = 0

	if (!houseRoomNumInput.val().trim()) return showError()
	if (!housePriceInput.val().trim() || housePriceInput.val().trim() < 0) return showError()
	if (!houseTotalAreaInput.val().trim()) return showError()
	if (!houseLivingAreaInput.val().trim()) return showError()
	if (!houseFloorNumInput.val().trim()) return showError()
	if (!houseCeilHeightInput.val().trim()) return showError()
	if (!houseLocation.length) return showError()
	if (!houseWithFurniture.length) return showError()
	if (!houseCondition.length) return showError()
	if (!houseWaterSupport.length) return showError()
	if (!houseElectricitySupport.length) return showError()
	if (!houseHeatingSupport.length) return showError()
	if (!houseGasSupport.length) return showError()
	if (!houseSeller.length) return showError()		
	if (!inHouse) return showError()
	if (!aroundHouse) return showError()
	if (houseType.val() == '!=!') return showError()
	if (houseBuildingType.val() == '!=!') return showError()

	prod.error = false
	prod.price = parseInt(housePriceInput.val().trim())
	prod.valute = houseValuteInput.val().trim()
	prod.payment_method = 'Narx'
	prod.rooms_num = houseRoomNumInput.val().trim()
	prod.total_area = houseTotalAreaInput.val().trim()
	prod.living_area = houseLivingAreaInput.val().trim()
	prod.location = houseLocation.val().trim()
	prod.floors_num = houseFloorNumInput.val().trim()
	prod.ceil_height = houseCeilHeightInput.val().trim()
	prod.with_furniture = houseWithFurniture.val().trim() == 'true' ? true : false
	prod.condition = houseCondition.val().trim()
	prod.house_type = houseType.val().trim()
	prod.building_type = houseBuildingType.val().trim()
	prod.water_support = houseWaterSupport.val().trim()
	prod.electricity_support = houseElectricitySupport.val().trim()
	prod.heating_support = houseHeatingSupport.val().trim()
	prod.gas_support = houseGasSupport.val().trim()
	prod.seller = houseSeller.val().trim()
	prod.in_house = inHouse
	prod.around_house = aroundHouse

	return prod
}

const createProductFURNITURE = prod => {
	let paymentMethod = furnitureModelContainer.find('input#furniture-payment-method:checked')
	let condition = furnitureModelContainer.find('input#furniture-condition:checked')
	let furnitureType = furnitureModelContainer.find('#furniture-type')
	let seller = furnitureModelContainer.find('input#furniture-seller:checked')
	prod.error = true

	if (!paymentMethod.length) return
	if (paymentMethod == 'Narx') {
		if (!furniturePriceInput.val().trim() || furniturePriceInput.val().trim() < 0) return
	}
	if (furnitureType.val() == '!=!') return
	if (!condition.length) return
	if (!seller.length) return

	prod.error = false
	prod.payment_method = paymentMethod.val().trim()
	prod.valute = furnitureValuteInput.val().trim()
	prod.furniture_type = furnitureType.val().trim()
	prod.condition = condition.val().trim()
	prod.seller = seller.val().trim()

	if (prod.payment_method == 'Narx') prod.price = parseInt(furniturePriceInput.val().trim())
		else prod.price = 0

	return prod
}

const createProductWATCH = prod => {
	let paymentMethod = watchModelContainer.find('input#watch-payment-method:checked').val().trim()
	let condition = watchModelContainer.find('input#watch-condition:checked')
	let seller = watchModelContainer.find('input#watch-seller:checked')
	prod.error = true

	if (!paymentMethod.length) return showError()
	if (paymentMethod == 'Narx') {
		if (!watchPriceInput.val().trim() || parseInt(watchPriceInput.val().trim()) < 0) return showError()
	}
	if (watchModelInput.val() == '!=!') return showError()
	if (!condition.length) return showError()
	if (!seller.length) return showError()

	prod.error = false
	prod.payment_method = paymentMethod
	prod.price = parseInt(watchPriceInput.val().trim())
	prod.valute = watchValuteInput.val().trim()
	prod.model = watchModelInput.val().trim()
	prod.condition = condition.val().trim()
	prod.seller = seller.val().trim()

	if (prod.payment_method == 'Narx') prod.price = parseInt(watchPriceInput.val().trim())
		else prod.price = 0

	return prod
}

const createProductAPARTMENT = prod => {
	let houseType = apartmentModelContainer.find('.apartment-type:checked')
	let buildingType = apartmentModelContainer.find('#apartment-building-type')
	let plan = apartmentModelContainer.find('#apartment-plan')
	let sanuzel = apartmentModelContainer.find('.apartment-sanuzel:checked')
	let withFurniture = apartmentModelContainer.find('.apartment-with-furniture:checked')
	let inHouse = getCheckboxData( apartmentModelContainer.find('.in-apartment-container') )
	let aroundHouse = getCheckboxData( apartmentModelContainer.find('.around-apartment-container') )
	let condition = apartmentModelContainer.find('#apartment-condition')
	let seller = apartmentModelContainer.find('.apartment-seller:checked')
	prod.error = true

	if (!apartmentPriceInput.val().trim()) return showError()
	if (!houseType.length) return showError()
	if (!apartmentRoomsNumInput.val().trim()) return showError()
	if (!apartmentTotalAreaInput.val().trim()) return showError()
	if (!apartmentLivingAreaInput.val().trim()) return showError()
	if (!apartmentKitchenAreaInput.val().trim()) return showError()
	if (!apartmentFloorInput.val().trim()) return showError()
	if (!apartmentTotalFloorInput.val().trim()) return showError()
	if (!buildingType.val().trim() == '!=!') return showError()
	if (!plan.val().trim() == '!=!') return showError()
	if (!apartmentConstructionYearInput.val().trim()) return showError()
	if (!sanuzel.length) return showError()
	if (!withFurniture.length) return showError()
	if (!apartmentCeilHeightInput.val().trim()) return showError()
	if (!condition.val().trim() == '!=!') return showError()
	if (!seller.length) return showError()

	prod.error = false
	prod.payment_method = 'Narx'
	prod.valute = apartmentValuteInput.val().trim()
	prod.price = apartmentPriceInput.val().trim()
	prod.house_type = houseType.val().trim()
	prod.rooms_num = apartmentRoomsNumInput.val().trim()
	prod.total_area = apartmentTotalAreaInput.val().trim()
	prod.living_area = apartmentLivingAreaInput.val().trim()
	prod.kitchen_area = apartmentKitchenAreaInput.val().trim()
	prod.floor = apartmentFloorInput.val().trim()
	prod.total_floor = apartmentTotalFloorInput.val().trim()
	prod.building_type = buildingType.val().trim()
	prod.plan = plan.val().trim()
	prod.construction_year = apartmentConstructionYearInput.val().trim()
	prod.sanuzel = sanuzel.val().trim()
	prod.with_furniture = withFurniture.val().trim() == 'true' ? true : false
	prod.ceil_height = apartmentCeilHeightInput.val().trim()
	prod.in_house = inHouse
	prod.around_house = aroundHouse
	prod.condition = condition.val().trim()
	prod.seller = seller.val().trim()

	return prod
}

const createSubProduct = (prod) => {
	let mainCategory = prod.category
	let subCategory = prod.subcategory

	if (mainCategory == 'Transport') {
		if (subCategory == 'Yengil mashinalar') {
			prod = createProductCAR(prod)
		}
	}
	if (mainCategory == 'Elektr jihozlari') {
		if (subCategory == 'Mobil telefon') {
			prod = creataProductPHONE(prod)
		}
 	}
	if (mainCategory == 'Ko\'chmas mulk') {
		if (subCategory == 'Xususiy uylar') {
			prod = createProductHOUSE(prod)
		}
		if (subCategory == 'Kvartiralar') {
			prod = createProductAPARTMENT(prod)
		}
 	}
	if (mainCategory == `Uy va bog'`) {
		if (subCategory == 'Mebel') {
			prod = createProductFURNITURE(prod)
		}
 	}
	if (mainCategory == `Moda va stil`) {
		if (subCategory == 'Qo\'l soatlari') {
			prod = createProductWATCH(prod)
		}
 	}
}

const createOtherOptions = () => {
	let val = $('#subcategory').val().trim()
	if (val == 'Yengil mashinalar') $('.transport-car-model').removeClass('d-none')
	if (val == 'Mobil telefon') $('.electrical-phone-model').removeClass('d-none')
	if (val == 'Xususiy uylar') $('.realty-house-model').removeClass('d-none')
	if (val == 'Mebel') $('.houseandgarden-furniture-model').removeClass('d-none')
	if (val == 'Qo\'l soatlari') $('.fashion-watch-model').removeClass('d-none')
	if (val == 'Kvartiralar') $('.realty-apartment-model').removeClass('d-none')
}

// ==================================================================================================================

const changeMethod = input => {
	let subcategory = $('#subcategory').val().trim()
	let target = input.parent().parent().next()
	let val = input.val().trim()
	
	target.removeClass('d-flex').addClass('d-none')
	if (val == 'Narx') target.addClass('d-flex').removeClass('d-none')
}

const createSubCategory = () => {
	let val = $('#category').val().trim()
	let subcategory = subcategories.filter(category => category.parent_category === val)

	$('#subcategory').html('<option disabled selected>Rukn</option>')
	if (!subcategory.length) $('#subcategory').append(`<option disabled selected>Bu bo'lim uchun rukn yo'q</option>`)

	for (let i = 0; i < subcategory.length; i++) {
		$('#subcategory').append(`<option value="${subcategory[i].name}">${subcategory[i].name}</option>`)
	}
}

const changeProgrammingAdType = self => {
	let val = self.val().trim()

	if (val == 'Izlayapman') $('.programming-resume-wrapper').removeClass('d-none')
	else $('.programming-resume-wrapper').addClass('d-none')
}

const getCheckboxData = container => {
	let arr = []
	let inputs = container.find('input[type="checkbox"]:checked')

	for (let i = 0; i < inputs.length; i++) {
		arr.push(container.find(`input[type="checkbox"]:checked:eq(${i})`).val().trim())
	}

	return JSON.stringify(arr)
}

const fileChange = () => {
	let file = document.getElementById('product-image')
	let form = new FormData()
	form.append("image", file.files[0])

	let settings = {
	  "url": "https://api.imgbb.com/1/upload?key=a2bd17fcdc0d49be220966602a794fa2",
	  "method": "POST",
	  "timeout": 0,
	  "processData": false,
	  "mimeType": "multipart/form-data",
	  "contentType": false,
	  "data": form
	}

	$.ajax(settings).done(response => {
	 	let res = JSON.parse(response)
	 	if (!res.success)  return showErrorText('E\'lon rasmi muvaffaqtiyatli yuklanmadi, iltimos yana urinib koring!')
	 	$('.image-link').removeClass('d-none').attr('href', res.data.display_url)
	 	productImageDeleteUrl = res.data.delete_url
	})
}

const showError = () => {
	let errHtml = `<p class="text-danger text-center text-b">Xato ketdi! Iltimos, har bir inputni tekshiring!</p>`
	$('.validation-errors').append(errHtml)
}

const showErrorText = txt => {
	let errHtml = `<p class="text-danger text-center text-b">${txt}</p>`
	$('.validation-errors').append(errHtml)
}

const showSuccess = () => {
	let errHtml = `<p class="text-success text-center text-b">E'lon muvaffaqtiyatli yaratildi!</p>`
	$('.validation-errors').append(errHtml)
}

const responseError = (request, errorType, errorMessage) => 'Xato ketdi: ' + errorType + errorMessage