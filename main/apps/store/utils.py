
import json

def get_list_from_touple(touple):
    arr = []
    for item in touple:
        arr.append(item[1])

    return arr


ADDRESS = (
    ('Toshkent', 'Toshkent'),
    ('Sirdaryo', 'Sirdaryo'),
    ('Jizzax', 'Jizzax'),
    ('Samarqand', 'Samarqand'),
    ('Buxoro', 'Buxoro'),
    ('Qashqadaryo', 'Qashqadaryo'),
    ('Navoiy', 'Navoiy'),
    ('Surxondaryo', 'Surxondaryo'),
    ('Namangan', 'Namangan'),
    ('Andijon', 'Andijon'),
    ('Farg\'ona', 'Farg\'ona'),
    ('Xorazm', 'Xorazm'),
    ('Qoraqalpog\'iston Res.', 'Qoraqalpog\'iston Res.'),
)

PAYMENT_METHOD = (
    ('Ayirboshlash', 'Ayirboshlash'),
    ('Bepul', 'Bepul'),
    ('Narx', 'Narx'),
)

VALUTE = (
    ('sum', 'sum'),
    ('y.e.', 'y.e.'),
)

SELLER = (
    ('Jismoniy shaxs', 'Jismoniy shaxs'),
    ('Yuridik shaxs', 'Yuridik shaxs'),
)


PHONE_MODEL = (
    ('Artel', 'Artel'),
    ('Alcatel-Lucent', 'Alcatel-Lucent'),
    ('Apple', 'Apple'),
    ('ASUS', 'ASUS'),
    ('BlackBerry', 'BlackBerry'),
    ('Fly', 'Fly'),
    ('Google', 'Google'),
    ('HTC', 'HTC'),
    ('Huawei', 'Huawei'),
    ('Lenovo', 'Lenovo'),
    ('LG', 'LG'),
    ('Meizu', 'Meizu'),
    ('Mio', 'Mio'),
    ('Motorola', 'Motorola'),
    ('Nokia', 'Nokia'),
    ('Pantech', 'Pantech'),
    ('Samsung', 'Samsung'),
    ('Sony', 'Sony'),
    ('Sony Ericsson', 'Sony Ericsson'),
    ('Vertu', 'Vertu'),
    ('Xiaomi', 'Xiaomi'),
    ('Boshqa marka', 'Boshqa marka'),
)

PHONE_CONDITION = (
    ('Ishlatilgan', 'Ishlatilgan'),
    ('Yangi', 'Yangi'),
)


CAR_MODEL = (
    ('Chevrolet', 'Chevrolet'),
    ('Daewoo', 'Daewoo'),
    ('Mercedes', 'Mercedes'),
    ('Bmw', 'Bmw'),
    ('Vaz', 'Vaz'),
    ('Toyota', 'Toyota'),
    ('Hyudai', 'Hyudai'),
    ('Opel', 'Opel'),
    ('Ford', 'Ford'),
    ('Nissan', 'Nissan'),
    ('Audi', 'Audi'),
    ('Kia', 'Kia'),
    ('Fiat', 'Fiat'),
    ('Mazda', 'Mazda'),
    ('Lexus', 'Lexus'),
    ('Volkswagen', 'Volkswagen'),
    ('Mitsubishi', 'Mitsubishi'),
    ('Gaz', 'Gaz'),
    ('Moskvich', 'Moskvich'),
    ('Uaz', 'Uaz'),
    ('Zaz', 'Zaz'),
    ('Izh', 'Izh'),
    ('Boshqalar', 'Boshqalar'),
)

CAR_PAYMENT_METHOD = (
    ('Ayirboshlash', 'Ayirboshlash'),
    ('Narx', 'Narx'),
)

CAR_CONDITION = (
    ('Ideal', 'Ideal'),
    ('Yaxshi', 'Yaxshi'),
    ('O\'rta', 'O\'rta'),
    ('Ta\'mir talab', 'Ta\'mir talab'),
)

CAR_TRANSMISSION = (
    ('Mexanik', 'Mexanik'),
    ('Avtomatik', 'Avtomatik'),
    ('Boshqa', 'Boshqa'),
)

CAR_FUEL_TYPE = (
    ('Benzin', 'Benzin'),
    ('Dizel', 'Dizel'),
    ('Boshqa', 'Boshqa'),
)

CAR_OTHER_OPTIONS = (
    ('Bojxonada rasmiylashtirilgan', 'Bojxonada rasmiylashtirilgan'),
    ('Elektr ko‘zgular', 'Elektr ko‘zgular'),
    ('El. oyna ko‘targichlar', 'El. oyna ko‘targichlar'), 
    ('Konditsioner', 'Konditsioner'), 
    ('Xavfsizlik tizimi', 'Xavfsizlik tizimi'), 
    ('Parktronik', 'Parktronik'), 
)


HOUSE_LOCATION = (
    ('Shaharda', 'Shaharda'),
    ('Shahar atrofida', 'Shahar atrofida'),
    ('Qishloq joylarida', 'Qishloq joylarida'),
    ('Trassa chetida', 'Trassa chetida'),
    ('Suv havzasi, daryo yaqinida', 'Suv havzasi, daryo yaqinida'),
    ('Tog\' etagida', 'Tog\' etagida'),
    ('Dalahovli hududida', 'Dalahovli hududida'),
    ('Yopiq hududda', 'Yopiq hududda'),
)

HOUSE_PAYMENT_METHOD = (
    ('Narx', 'Narx')
)

HOUSE_CONDITION = (
    ('Mualliflik loyihasi', 'Mualliflik loyihasi'),
    ('Evrotaʼmir', 'Evrotaʼmir'),
    ('Oʻrtacha', 'Oʻrtacha'),
    ('Taʼmir talab', 'Taʼmir talab'),
    ('Qora suvoq', 'Qora suvoq'),
    ('Tozalashdan avvalgi pardoz', 'Tozalashdan avvalgi pardoz'),
    ('Buziladigan', 'Buziladigan'),
)

HOUSE_TYPE = (
    ('Uy', 'Uy'),
    ('Fligel', 'Fligel'),
    ('Kottej', 'Kottej'),
    ('Uyning bir qismi', 'Uyning bir qismi'),
    ('Dala hovli', 'Dala hovli'),
    ('Tounxaus', 'Tounxaus'),
)

HOUSE_BUILDING_TYPE = (
    ('G\'ishtli', 'G\'ishtli'),
    ('Panelli', 'Panelli'),
    ('Monolitli', 'Monolitli'),
    ('Blokli', 'Blokli'),
    ('Yog\'och', 'Yog\'och'),
)

HOUSE_WATER = (
    ('Uyda', 'Uyda'),
    ('Markazlashgan suv taʼminoti', 'Markazlashgan suv taʼminoti'),
    ('Oʻtkazish imkoniyati', 'Oʻtkazish imkoniyati'),
    ('Uchastkada quduq', 'Uchastkada quduq'),
    ('Chekkasida', 'Chekkasida'),
    ('Quduq', 'Quduq'),
    ('Yoʻq', 'Yoʻq'),
)

HOUSE_ELECTRICITY = (
    ('Bor', 'Bor'),
    ('Ulanish imkoniyati bor', 'Ulanish imkoniyati bor'),
    ('Yoʻq', 'Yoʻq'),
)

HOUSE_HEATING = (
    ('Markazlashgan', 'Markazlashgan'),
    ('Gazda', 'Gazda'),
    ('Qattiq yoqilgʻida', 'Qattiq yoqilgʻida'),
    ('Suyuq yoqilgʻida', 'Suyuq yoqilgʻida'),
    ('Elektrda', 'Elektrda'),
    ('Aralash', 'Aralash'),
    ('Isitkichsiz', 'Isitkichsiz'),
)

HOUSE_GAS = (
    ('Magistral', 'Magistral'),
    ('Alohida', 'Alohida'),
    ('Ulanish imkoniyati bor', 'Ulanish imkoniyati bor'),
    ('Yoʻq', 'Yoʻq'),
)

HOUSE_IN = ['Internet', 'Telefon', 'Suzish havzasi', 'Garaj', 'Konditsioner', 'Maishiy texnika', 'Kanalizatsiya', 'Tomorqa', 'Qoʻriqchi', 'Yertoʻla, omborcha', 'Sauna, hammom', 'Sportzal', 'Yoʻldosh televideniye']

HOUSE_AROUND = ['Kasalxona, poliklinika', 'Bolalar maydonchasi', 'Bolalar bogʻchasi', 'Bekatlar', 'Park, yashil zona', 'Koʻngilochar muassasalar', 'Restoran, kafelar', 'Turargoh', 'Supermarket, doʻkonlar', 'Maktab']


FURNITURE_TYPE = (
    ('Mehmonxona uchun mebel', 'Mehmonxona uchun mebel'),
    ('Yotoqxona uchun mebel', 'Yotoqxona uchun mebel'),
    ('Dahliz uchun mebel', 'Dahliz uchun mebel'),
    ('Oshxona mebeli', 'Oshxona mebeli'),
    ('Ofis mebeli', 'Ofis mebeli'),
    ('Bog\' mebeli', 'Bog\' mebeli'),
    ('Maxsus mebel', 'Maxsus mebel'),
)

WATCH_MODEL = (
    ('Tissot', 'Tissot'),
    ('Adriatica', 'Adriatica'),
    ('Aigner', 'Aigner'),
    ('Alfex', 'Alfex'),
    ('AndyWatch', 'AndyWatch'),
    ('Anne Klein', 'Anne Klein'),
    ('Appella', 'Appella'),
    ('Appetime', 'Appetime'),
    ('Aristo', 'Aristo'),
    ('Armand Basi', 'Armand Basi'),
    ('Armand Nicolet', 'Armand Nicolet'),
    ('Armani', 'Armani'),
    ('Atlantic', 'Atlantic'),
    ('Auguste Reymond', 'Auguste Reymond'),
    ('Axcent', 'Axcent'),
    ('Balmain', 'Balmain'),
    ('Baume', 'Baume'),
    ('Benetton', 'Benetton'),
    # ('Adriatica', 'Adriatica'),
    # ('Adriatica', 'Adriatica'),
    # ('Adriatica', 'Adriatica'),
    # ('Adriatica', 'Adriatica'),
    # ('Adriatica', 'Adriatica'),
)


APARTMENT_TYPE = (
    ('Yangi qurilgan uylar', 'Yangi qurilgan uylar'),
    ('Ikkilamchi bozor', 'Ikkilamchi bozor'),
)

APARTMENT_PLAN = (
    ('Aralash', 'Aralash'),
    ('Alohida ajratilgan', 'Alohida ajratilgan'),
    ('Aralash-alohida', 'Aralash-alohida'),
    ('Studiya', 'Studiya'),
    ('Pentxaus', 'Pentxaus'),
    ('Ko\'p darajali', 'Ko\'p darajali'),
    ('Kichik oilalar uchun', 'Kichik oilalar uchun'),
)

APARTMENT_SANUZEL = (
    ('Alohida', 'Alohida'),
    ('Aralash', 'Aralash'),
    ('2 va undan ko\'p', '2 va undan ko\'p'),
)

APARTMENT_CONDITION = (
    ('Mualliflik loyihasi', 'Mualliflik loyihasi'),
    ('Evrotaʼmir', 'Evrotaʼmir'),
    ('Oʻrtacha', 'Oʻrtacha'),
    ('Taʼmir talab', 'Taʼmir talab'),
    ('Qora suvoq', 'Qora suvoq'),
    ('Tozalashdan avvalgi pardoz', 'Tozalashdan avvalgi pardoz'),
)

APARTMENT_IN = ['Internet', 'Telefon', 'Muzlatkich', 'Televizor', 'Konditsioner', 'Kabelli TV', 'Kir yuvish mashinasi', 'Oshxona', 'Balkon']

APARTMENT_AROUND = ['Kasalxona, poliklinika', 'Bolalar maydonchasi', 'Bolalar bogʻchasi', 'Bekatlar', 'Park, yashil zona', 'Koʻngilochar muassasalar', 'Restoran, kafelar', 'Turargoh', 'Supermarket, doʻkonlar', 'Maktab']


address = get_list_from_touple(ADDRESS)
payment_method = get_list_from_touple(PAYMENT_METHOD)
valute = get_list_from_touple(VALUTE)
seller = get_list_from_touple(SELLER)

phone_model = get_list_from_touple(PHONE_MODEL)
phone_condition = get_list_from_touple(PHONE_CONDITION)

car_model = get_list_from_touple(CAR_MODEL)
car_payment_method = get_list_from_touple(CAR_PAYMENT_METHOD)
car_condition = get_list_from_touple(CAR_CONDITION)
car_transmission = get_list_from_touple(CAR_TRANSMISSION)
car_fuel_type = get_list_from_touple(CAR_FUEL_TYPE)
car_other_options = get_list_from_touple(CAR_OTHER_OPTIONS)

house_location = get_list_from_touple(HOUSE_LOCATION)
house_condition = get_list_from_touple(HOUSE_CONDITION)
house_type = get_list_from_touple(HOUSE_TYPE)
house_building_type = get_list_from_touple(HOUSE_BUILDING_TYPE)
house_water = get_list_from_touple(HOUSE_WATER)
house_electricity = get_list_from_touple(HOUSE_ELECTRICITY)
house_heating = get_list_from_touple(HOUSE_HEATING)
house_gas = get_list_from_touple(HOUSE_GAS)

furniture_type = get_list_from_touple(FURNITURE_TYPE)
watch_model = get_list_from_touple(WATCH_MODEL)

apartment_type = get_list_from_touple(APARTMENT_TYPE)
apartment_plan = get_list_from_touple(APARTMENT_PLAN)
apartment_sanuzel = get_list_from_touple(APARTMENT_SANUZEL)
apartment_condition = get_list_from_touple(APARTMENT_CONDITION)

context = {
    'transport': {
        'car': {
            'models': car_model,
            'payment_method': car_payment_method,
            'transmission': car_transmission,
            'fuel_type': car_fuel_type,
            'condition': car_condition,
            'other_options': car_other_options,
        },
    },
    'electrical': {
        'mobile_phone': {
            'models': phone_model,
            'condition': phone_condition,
        },
    },
    'realty': {
        'house': {
            'location': house_location,
            'condition': house_condition,
            'type': house_type,
            'building_type': house_building_type,
            'water': house_water,
            'electricity': house_electricity,
            'heating': house_heating,
            'gas': house_gas,
            'in_house': HOUSE_IN,
            'around_house': HOUSE_AROUND,
        },
        'apartment': {
            'type': apartment_type,
            'plan': apartment_plan,
            'sanuzel': apartment_sanuzel,
            'condition': apartment_condition,
            'in_house': APARTMENT_IN,
            'around_house': APARTMENT_AROUND,
        }
    },
    'house_and_garden': {
        'furniture': {
            'type': furniture_type,
        },
    },
    'fashion': {
        'watch': {
            'model': watch_model,
        },
    },
}