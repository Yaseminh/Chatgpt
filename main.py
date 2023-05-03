import openai
import json

with open("anket.json", "r") as f:
 anket = json.load(f)

 anket_alani = anket["anket_alani"]
 anket_suresi = anket["anket_suresi"]
 soru_sayisi = anket["soru_sayisi"]
 cevap_sayisi = anket["cevap_sayisi"]


print("Anket alani:", anket_alani)
print("Anket süresi:", anket_suresi)
print("Soru sayısı:", soru_sayisi)
print("Cevap sayısı:", cevap_sayisi)

# html sayfa hazırlatma

openai.api_key=""


#bir apiye istek atılacak ve o istek ile veriler gelecek..


#content="Sadece bir html sayfa hazırla. <!DOCTYPE html> ile başlasın. Paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstünde ad soyad girilen bir alan olsun. Devamında ise bu html sayfanın içinde finans alanında 3  tane soru olsun. Her sorunun 5 şıkkı olsun. Bir tane şık seçilebilsin. Form action adı submit-survey.py  ve form action methodu post olsun."
#content=f'Sadece bir html kodu hazırla. <!DOCTYPE html> ile başlasın. Cevabına paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstünde ad soyad girilen bir alan olsun. Devamında ise bu html sayfanın içinde {anket_alani} alanında {soru_sayisi}  tane soru olsun. Her sorunun {cevap_sayisi} şıkkı olsun. Bir tane şık seçilebilsin. Form action adı http://127.0.0.1:8080/anketverisi  ve form action methodu post olsun.';
#content=f'Sadece bir html kodu hazırla. <!DOCTYPE html> ile başlasın. Cevabına paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstünde ad soyad girilen bir alan olsun. Devamında ise bu html sayfanın içinde {anket_alani} alanında {soru_sayisi}  tane soru olsun  ve value değeri soru texti ile aynı olsun. Her sorunun {cevap_sayisi} şıkkı olsun. Bir tane şık seçilebilsin. Form action adı http://127.0.0.1:8080/anketverisi  ve form action methodu post olsun.';
#content=f'Sadece bir html kodu hazırla. <!DOCTYPE html> ile başlasın. Cevabına paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstünde ad soyad girilen bir alan olsun. Devamında ise bu html sayfanın içinde {anket_alani} alanında {soru_sayisi}  tane soru olsun  ve value değeri soru texti ile aynı olsun. Her sorunun {cevap_sayisi} şıkkı olsun. Bir tane şık seçilebilsin. Form action adı http://127.0.0.1:8080/anketverisi  ve form action methodu post olsun.';
#content=f'Sadece bir html kodu hazırla. <!DOCTYPE html> ile başlasın ve   <body id="sayfa"> tagi içersin. Cevabına paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstünde ad soyad girilen bir alan olsun. Devamında ise bu html sayfanın içinde finans alanında 3  tane soru olsun  ve value değeri soru texti ile aynı olsun. Her sorunun 3 şıkkı olsun. Bir tane şık seçilebilsin. </body> üstüne <script src="script.js"></script> ekle. Form action adı http://127.0.0.1:8080/anketverisi  ve form action methodu post olsun.';
#content=f'Sadece bir html kodu hazırla. <!DOCTYPE html> ile başlasın ve   <body id="sayfa"> tagi içersin. Cevabına paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstüne ya da en altına hiçbir şey ekleme. Bütün şimdi bahsedeceğim alanlar formun içinde olsun. Sayfanın en üstünde ad soyad girilen bir alan olsun. Devamında ise bu html sayfanın içinde {anket_alani} alanında {soru_sayisi}   tane soru olsun  ve value değeri soru texti ile aynı olsun. Her sorunun {cevap_sayisi} şıkkı olsun. Bir tane şık seçilebilsin. </body> üstüne <script src="script.js"></script> ekle. Form action adı http://127.0.0.1:8080/anketverisi  ve form action methodu post olsun.';
#content=f'Sadece bir html kodu hazırla. <!DOCTYPE html> ile başlasın ve <head> altına bu değeri <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> eklesin  ve bootstrap kullansın ve oluşturulan sayfada renkli butonlar, güzel görünümlü inputlar yer alsın. <body id="sayfa"> tagi içersin. Cevabına paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstüne ya da en altına hiçbir şey ekleme. Bütün şimdi bahsedeceğim alanlar formun içinde olsun. Sayfanın en üstünde ad soyad girilen bir alan olsun. Devamında ise bu html sayfanın içinde {anket_alani} alanında {soru_sayisi} tane soru olsun  ve value değeri soru texti ile aynı olsun. Her sorunun {cevap_sayisi} şıkkı olsun. Bir tane şık seçilebilsin. </body> üstüne <script src="script.js"></script> ekle. Form action adı http://127.0.0.1:8080/anketverisi  ve form action methodu post olsun.';
#content=f'Sadece bir html kodu hazırla. <!DOCTYPE html> ile başlasın </html> ile bitsin. <head> altına bu değeri <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> eklesin. Bootstrap kullansın ve oluşturulan sayfada renkli butonlar, güzel görünümlü inputlar yer alsın. <body id="sayfa"> tagi içersin. Cevabına paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstüne ya da en altına hiçbir şey ekleme. Bütün şimdi bahsedeceğim alanlar formun içinde olsun. Sayfanın en üstünde ad soyad girilen bir alan olsun. Devamında ise bu html sayfanın içinde {anket_alani} alanında {soru_sayisi} tane soru olsun  ve value değeri soru texti ile aynı olsun. Her sorunun {cevap_sayisi} şıkkı olsun. Bir tane şık seçilebilsin. </body> üstüne <script src="script.js"></script> ekle. Form action adı http://127.0.0.1:8080/anketverisi  ve form action methodu post olsun.';
content=f'Sadece bir html kodu hazırla. <!DOCTYPE html> ile başlasın ve <head> altına bu değeri <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> eklesin  ve bootstrap kullansın ve oluşturulan sayfada renkli butonlar, güzel görünümlü inputlar yer alsın. <body id="sayfa"> tagi içersin. type="checkbox" kullanma. Cevabına paragraf, cümle, yazı, açıklama, bilgi yazma. Sayfanın en üstüne ya da en altına hiçbir şey ekleme. Bütün şimdi bahsedeceğim alanlar formun içinde olsun. Bu html sayfanın içinde {anket_alani} alanında {soru_sayisi} tane soru olsun  ve value değeri soru texti ile aynı olsun. Her sorunun {cevap_sayisi} şıkkı olsun. Bir tane şık seçilebilsin. </body> üstüne <script src="script.js"></script> ekle. Form action adı http://127.0.0.1:8080/anketverisi  ve form action methodu post olsun.';
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": content},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)

with open("survey.html", "w", encoding="utf-8") as f:
    f.write(result)

#python backend kodunu hazırlatma ve kaydetme
'''content2="Flask modülünü kullanarak yukarıdaki html'in form verilerini al ve seçilen şıkları bir json dosyası oluşturup kaydeden bir python kodu yaz."
response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": content2},
        ]
)

result2 = ''
for choice2 in response2.choices:
    result2 += choice2.message.content

print(result2)

with open("getanswer.py", "w") as f:
    f.write(result2)'''





