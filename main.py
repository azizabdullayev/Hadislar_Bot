import requests
import json
from config import *
from buttons import start_1, start_2, start_3, start_4


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    image = open('foto/rasm logo.png', 'rb')
    text = f"Assalomu alaykum va rohmatullohi va barakatuhu\nBizning bot hohlagan davlatdagi namoz vaqtini chiqarib bera oladi yoki hadislarni oqib yoki eshitishingiz mumkin!\nNamoz vohtini bilish uchun shahar nomini katta harf bilan kiriting👇 yoki hadislar haqida malumot oling."
    await msg.answer_photo(image, caption=text, reply_markup=start_1)


@dp.message_handler(commands=["help"])
async def help_1(msg: types.Message):
    await msg.answer(
        f"Agar sizda qandaydir muammolar paydo bo'lgan bo'lsa bizning admin bilan bog'lanib ularni hal etishingiz mumkin\nAmdin: https://t.me/aaaa_77_01",
        reply_markup=start_4)


@dp.message_handler(text="Namoz vaqtlarini bilish⏳")
async def bilish(msg: types.Message):
    text = f"Davlatni tanlang👇"
    await msg.answer(text, reply_markup=start_2)


@dp.message_handler(text="Afg'oniston")
async def next(msg: types.Message):
    await msg.answer('Bir daqiqa kuting.....')
    city = 'Афганистан'
    print(city)
    for i in range(1, 242):
        try:
            resul1 = requests.get(f'https://namaztimes.kz/ru/api/country?id={1}&type=json')
            ff = json.loads(resul1.text)
            print(ff)
            if ff['name'] == city:
                alt = ff['id']
                print(alt)
                form = requests.get(f'https://namaztimes.kz/api/praytimes?id={alt}').text
                form1 = json.loads(form)
                today = form1['date']
                form1 = form1['praytimes']
                bomdot = form1['bamdat']
                peshin = form1['besin']
                asr = form1['isfirar']
                shom = form1['ishtibaq']
                xufton = form1['ishaisani']
                await msg.answer(
                    f'Bugungi sana: {today}\nBomdot vaqti: {bomdot}\nPeshin vaqti: {peshin}\nAsr vaqti: {asr}\nShom vaqti: {shom}\nXufton vaqti: {xufton}',
                    reply_markup=start_3)
                return
            else:
                continue
        except:
            continue


@dp.message_handler(text="Qozog'iston")
async def next(msg: types.Message):
    await msg.answer('Bir daqiqa kuting.....')
    city = 'Казахстан'
    print(city)
    for i in range(1, 242):
        try:
            resul1 = requests.get(f'https://namaztimes.kz/ru/api/country?id={99}&type=json')
            ff = json.loads(resul1.text)
            print(ff)
            if ff['name'] == city:
                alt = ff['id']
                print(alt)
                form = requests.get(f'https://namaztimes.kz/api/praytimes?id={alt}').text
                form1 = json.loads(form)
                today = form1['date']
                form1 = form1['praytimes']
                bomdot = form1['bamdat']
                peshin = form1['besin']
                asr = form1['isfirar']
                shom = form1['ishtibaq']
                xufton = form1['ishaisani']
                await msg.answer(
                    f'Bugungi sana: {today}\nBomdot vaqti: {bomdot}\nPeshin vaqti: {peshin}\nAsr vaqti: {asr}\nShom vaqti: {shom}\nXufton vaqti: {xufton}',
                    reply_markup=start_3)
                return
            else:
                continue
        except:
            continue


@dp.message_handler(text="Qizg'iziston")
async def next(msg: types.Message):
    await msg.answer('Bir daqiqa kuting.....')
    city = 'Кыргызстан'
    print(city)
    for i in range(1, 242):
        try:
            resul1 = requests.get(f'https://namaztimes.kz/ru/api/country?id={104}&type=json')
            ff = json.loads(resul1.text)
            print(ff)
            if ff['name'] == city:
                alt = ff['id']
                print(alt)
                form = requests.get(f'https://namaztimes.kz/api/praytimes?id={alt}').text
                form1 = json.loads(form)
                today = form1['date']
                form1 = form1['praytimes']
                bomdot = form1['bamdat']
                peshin = form1['besin']
                asr = form1['isfirar']
                shom = form1['ishtibaq']
                xufton = form1['ishaisani']
                await msg.answer(
                    f'Bugungi sana: {today}\nBomdot vaqti: {bomdot}\nPeshin vaqti: {peshin}\nAsr vaqti: {asr}\nShom vaqti: {shom}\nXufton vaqti: {xufton}',
                    reply_markup=start_3)
                return
            else:
                continue
        except:
            continue


@dp.message_handler(text="Tojikiston")
async def next(msg: types.Message):
    await msg.answer('Bir daqiqa kuting.....')
    city = 'Таджикистан'
    print(city)
    for i in range(1, 242):
        try:
            resul1 = requests.get(f'https://namaztimes.kz/ru/api/country?id={191}&type=json')
            ff = json.loads(resul1.text)
            print(ff)
            if ff['name'] == city:
                alt = ff['id']
                print(alt)
                form = requests.get(f'https://namaztimes.kz/api/praytimes?id={alt}').text
                form1 = json.loads(form)
                today = form1['date']
                form1 = form1['praytimes']
                bomdot = form1['bamdat']
                peshin = form1['besin']
                asr = form1['isfirar']
                shom = form1['ishtibaq']
                xufton = form1['ishaisani']
                await msg.answer(
                    f'Bugungi sana: {today}\nBomdot vaqti: {bomdot}\nPeshin vaqti: {peshin}\nAsr vaqti: {asr}\nShom vaqti: {shom}\nXufton vaqti: {xufton}',
                    reply_markup=start_3)
                return
            else:
                continue
        except:
            continue


@dp.message_handler(text="Turkmaniston")
async def next(msg: types.Message):
    await msg.answer('Bir daqiqa kuting.....')
    city = 'Туркмения'
    print(city)
    for i in range(1, 242):
        try:
            resul1 = requests.get(f'https://namaztimes.kz/ru/api/country?id={201}&type=json')
            ff = json.loads(resul1.text)
            print(ff)
            if ff['name'] == city:
                alt = ff['id']
                print(alt)
                form = requests.get(f'https://namaztimes.kz/api/praytimes?id={alt}').text
                form1 = json.loads(form)
                today = form1['date']
                form1 = form1['praytimes']
                bomdot = form1['bamdat']
                peshin = form1['besin']
                asr = form1['isfirar']
                shom = form1['ishtibaq']
                xufton = form1['ishaisani']
                await msg.answer(
                    f'Bugungi sana: {today}\nBomdot vaqti: {bomdot}\nPeshin vaqti: {peshin}\nAsr vaqti: {asr}\nShom vaqti: {shom}\nXufton vaqti: {xufton}',
                    reply_markup=start_3)
                return
            else:
                continue
        except:
            continue


@dp.message_handler(text="O'zbekiston")
async def next(msg: types.Message):
    await msg.answer('Bir daqiqa kuting.....')
    city = 'Узбекистан'
    print(city)
    for i in range(1, 242):
        try:
            resul1 = requests.get(f'https://namaztimes.kz/ru/api/country?id={209}&type=json')
            ff = json.loads(resul1.text)
            print(ff)
            if ff['name'] == city:
                alt = ff['id']
                print(alt)
                form = requests.get(f'https://namaztimes.kz/api/praytimes?id={alt}').text
                form1 = json.loads(form)
                today = form1['date']
                form1 = form1['praytimes']
                bomdot = form1['bamdat']
                peshin = form1['besin']
                asr = form1['isfirar']
                shom = form1['ishtibaq']
                xufton = form1['ishaisani']
                await msg.answer(
                    f'Bugungi sana: {today}\nBomdot vaqti: {bomdot}\nPeshin vaqti: {peshin}\nAsr vaqti: {asr}\nShom vaqti: {shom}\nXufton vaqti: {xufton}',
                    reply_markup=start_3)
                return
            else:
                continue
        except:
            continue


@dp.message_handler(text="Ortga  qaytish")
async def ortga(msg: types.Message):
    text = f"Ortga qayttingiz"
    await msg.answer(text, reply_markup=start_1)


@dp.message_handler(text="Ortga qaytish")
async def ortga(msg: types.Message):
    text = f"Ortga qayttingiz"
    await msg.answer(text, reply_markup=start_2)


@dp.message_handler(text="Bosh sahifaga qaytish")
async def ortga(msg: types.Message):
    text = f"Bosh sahifaga qayttingiz"
    await msg.answer(text, reply_markup=start_1)


@dp.message_handler(text="Hadislar📖")
async def hadislar(msg: types.Message):
    image_1 = open('video/videoplayback.mp4', 'rb')
    image_2 = open('video/vodeoplayback 2.mp4', 'rb')
    text_1 = open('hadislar/hadislarda-oila-tarbiyasi.pdf', 'rb')
    text_2 = open("hadislar/Imom al-Buxoriy. Al-Jome' as-sahih. 1-jild.pdf", 'rb')
    await msg.answer_video(image_1)
    await msg.answer_video(image_2)
    await msg.answer_document(text_1)
    await msg.answer_document(text_2, reply_markup=start_4)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
