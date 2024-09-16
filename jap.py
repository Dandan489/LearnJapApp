import random, time, os
from gtts import gTTS
from playsound import playsound
hiragana = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", \
    "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん"]
romaji = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so", "ta", "chi", "tsu", "te", "to", \
    "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho", "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "wo", "n"]
vocabs = ["わたし", "ほん", "がくせい", "ちゅうごく", "かいしゃいん", "かんこく", "あなた", "せんせい", "にほん", "にっぽん", "たいわん", "はたち", "おくに", "どちら", "おしごと"]


print("1. kana rush")
print("2. vocab quiz")
type = int(input())

if(type == 1):
    right = 0
    total = 0
    startTime = time.time()
    while True:
        ind = random.randrange(0, len(romaji))
        print(hiragana[ind])
        inn = input()
        if(inn == "exit"):
            break
        elif(inn == romaji[ind]):
            print("correct!")
            right+=1
        else:
            print("wrong!, it's " + romaji[ind])
        total+=1
        endTime = time.time()
    print("Result:")
    print("Correctness: " + str(round(right/total*100, 2)) + "%")
    print("Average Time: " + str(round((endTime-startTime)/total, 2)) + " second")
elif(type == 2):
    while True:
        ind = random.randrange(0, len(vocabs))
        tts = gTTS(text=vocabs[ind], lang='ja')
        tts.save("output.mp3")
        audio_file = os.path.dirname(__file__) + '\\output.mp3'
        playsound(audio_file)
        next = input()
        print(vocabs[ind])
        if(next == "exit"):
            break
else:
    print("exited")
