
meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "SIGMA": "ktoś sigma",
            "RIZZLER": "ktoś kto rizzuje osoby",
            "SHEESH": "lekka dezaprobata",
            "AGGRO": "stać się agresywnym/zły",
            }
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
    # Co powinniśmy zrobić, jeśli słowo zostało znalezione?
else:
    # Co powinniśmy zrobić, jeśli słowo nie zostało znalezione?
    print("womp womp nie znam tego")
