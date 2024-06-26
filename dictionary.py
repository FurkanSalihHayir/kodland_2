import time
ad = input("Merhaba! Adınız nedir?")
time.sleep(1)
print("Pekala " + ad + ". Sözlüğe giriş yapmak istiyorsan Y, istemiyorsan Y'den başka herhangi bir tuşa basabilirsin." )
cevap = input().upper()
time.sleep(1)
if cevap == "Y":
    meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bulduğunuz herhangi bir şey için kullanılan kısaltma. (Laughing out loud)",
            "RIZZ": "Karizmanın Alfa kuşak hali :/",
            "AGGRO": "Agresifleşmek/sinirlenmek",
            "LMAO": "Lol'ün argolu hali"
            }
    asked_questions = 0
    while asked_questions < 5:
        word = input("Anlamadığınız bir kelime yazın: ").upper()
        asked_questions += 1
        if word in meme_dict.keys():
            print(meme_dict[word])
        else:
            print("...")
    time.sleep(1)
    print("İstediğin şeyleri cevapladım. Bedava denemeniz bitmiştir :D")
else:
    print("O zaman görüşmek üzere!")
