import json
import difflib
##############get close matches gives similar words
from difflib import get_close_matches
##############gTTS converts text to speech
from gtts import gTTS
##############playsound plays the sound
from playsound import playsound


##############load the dataset
dataset = json.load(open("English thesauras\data.json",'r'))



###############Input the word
voice_obj = gTTS("Enter the word : ")
voice_obj.save("English thesauras\Start.mp3")
###play mp3 file
playsound("English thesauras\Start.mp3")
word = input("Enter the word : ").lower()



###############function to provide values for keys
def translate(word):
    try:
        return dataset[word]
    except:
        return False


################function to print and voice the meaning
def meaning(w):
    my_text= ""
    for i,d in enumerate(translate(w)):
        print("{}. {}.".format(i+1,d))
        my_text += "{}. {}.".format(i+1,d)
    
    voice_obj_2 = gTTS(my_text)
    voice_obj_2.save("English thesauras\Meaning.mp3")
    ###play mp3 file
    playsound("English thesauras\Meaning.mp3")





#################if not translated
if not translate(word):
    word_found = False
    for i in get_close_matches(word,dataset.keys()):
        print("\nDo you mean {} instead? ".format(i))


        ##voice for similar texts
        similar_word_text =  "\nDo you mean {} instead? ".format(i)
        voice_obj_3 = gTTS(similar_word_text)
        voice_obj_3.save("English thesauras\Conf_{}.mp3".format(i))
        ###play mp3 file
        playsound("English thesauras\Conf_{}.mp3".format(i))
    
        ##confirmation
        conf = input("Type Y for Yes and N for No : ").lower()

        
        if conf == 'y':
            word_found = True
            word = i
            meaning(word)
            break
        else:
            pass
    if not word_found:
        print("\nNo such word available, kindly double check.\n")
        voice_obj_4 = gTTS("No such word available, kindly double check")
        voice_obj_4.save("English thesauras\Conf.mp3")
        ###play mp3 file
        playsound("English thesauras\Conf.mp3")
else:
    meaning(word)
