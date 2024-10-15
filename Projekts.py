from collections import Counter

def analyze_text(text):
    words = text.split() # Sadala tekstu, izmantojot atstarpes kā vārdu atdalītāju.
    word_count = len(words) #Pievieno vārdus sarakstā
    
    sentence_count = text.count('.') + text.count('!') + text.count('?') #Saskaita teikumus izmantojot punktu, izsaukum zīmi un jautājum zīmi.
    
    most_common_word = find_most_common_word(words)
    
    return word_count, sentence_count, most_common_word

def find_most_common_word(words):
    if len(words) > 0: #Pārbauda vai ir kādi vārdi
        most_common_word = Counter(words).most_common(1)[0][0] #Atrod visbiežāko vārdu
    else:
        most_common_word = "Nav vārdu" #Ja vārdu nav atgriež paziņojumu ka vārdu nav
    return most_common_word #atgriež paziņojumu ar visbiežāk lietoto vārdu

while True:
    text = input("Ievadiet tekstu (vai ierakstiet 'iziet', lai beigtu): ") #Cikls turpināsies kamēr neievadīs ''iziet''
    
    if text.lower() == 'iziet': #Kad ievada ''iziet'' cikls tiek pārtraukts
        print("Programma beidzas.")
        break 
    
    word_count, sentence_count, most_common_word = analyze_text(text) #Izsauc funkciju, lai analizētu tekstu
    
    print(f"Vārdu skaits: {word_count}")
    print(f"Teikumu skaits: {sentence_count}")
    print(f"Visbiežāk lietotais vārds: '{most_common_word}'")
