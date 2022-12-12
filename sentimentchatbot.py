import pandas as pd
import pickle
import numpy as np
import random
#import pyttsx3
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP
import datetime
#import speech_recognition as sr

count_vect = pickle.load(open(r'sentiment\count_vect.p', 'rb'))
model=pickle.load(open(r'sentiment\naive_bayes.p','rb'))
#engine = pyttsx3.init()


def predict_emotion(sample_text,cv,model):
    myvect=cv.transform(sample_text).toarray()
    prediction=model.predict(myvect)
    pred_proba=model.predict_proba(myvect)
    pred_percentage_for_all=dict(zip(model.classes_,pred_proba[0]))
    # print("prediction: {}, prediction Score {}".format(prediction[0],np.max(pred_proba)))
    # return pred_percentage_for_all
    return (prediction[0],np.max(pred_proba))


#engine=pyttsx3.init('sapi5')
#voices=engine.getProperty("voices")
#engine.setProperty('voices','voices[1].id')
#def speak(text):
    #engine.say(text)
    #engine.runAndWait()


#def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello Thank you for signing M-Friend,Good Morning,How can I help you?")
        print("Hello Thank you for signing M-Friend,Good Morning,How can I help you?")
 
    elif hour>=12 and hour<=18:
        speak("Hello Thank you for signing M-Friend,Good Afternoon,How can I help you?,")
        print("Hello Thank you for signing M-Friend,Good Afternoon,How can I help you?")

    elif hour >=21 and hour<24:
        speak("Good night,it's time for bed,sleep well")
        print("Good night,it's time for bed sleep well")

    else:
        speak("Hello F_name,Good Evening")
        print("Hello F_name,Good Evening")

#def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        print("message")
        #audio=r.listen(source, phrase_time_limit=5)
    try:
        statement=r.recognize_google(audio,language="en-in")
        print(f"user said:{statement}\n")

    except Exception as e:
        #speak("Pardon me,please say that again")
        return "None"
    return statement
    
#print("Loading your AI personal assistant M-Friend")
#speak("Loading your AI personal assistant M-Friend")
#takeCommand()
#wishMe()
#if "time in statement":
#    strTime=datetime.datetime.now().strftime("%H:%M:%S")
#    speak(f"the time is {strTime}")
#    print(f"the time is {strTime}")

#Sad – Drama
#Disgust – Musical
#Anger – Family
#Anticipation – Thriller
#Fear – Sport
#Enjoyment – Thriller
#Trust – Western
#Surprise – Film-Noir
#happy_movies = ['https://www.imdb.com/list/ls050539170/']
#Family_movies=['https://www.imdb.com/search/title/?genres=family&title_type=feature&sort=moviemeter']
#Drama_movies=["https://www.imdb.com/search/title/?genres=drama&title_type=feature&sort=moviemeter"]
#Sport_movies=['https://www.imdb.com/search/title/?genres=sport&title_type=feature&sort=moviemeter']
#Romantic_movies=['https://www.imdb.com/search/title/?genres=romance&title_type=feature&sort=moviemeter']
#Film_Noir=['https://www.imdb.com/search/title/?genres=film_noir&title_type=feature&sort=moviemeter']
#chatlog = []
#print( 'how are you today?')
def sentiment(inserting_text):
    happy_movies = ["https://www.imdb.com/title/tt0386588/?ref_=ttls_li_tt","https://www.imdb.com/title/tt1306980/?ref_=ttls_li_tt","https://www.imdb.com/title/tt0035423/?ref_=ttls_li_tt","https://www.imdb.com/title/tt1022603/?ref_=ttls_li_tt","https://www.imdb.com/title/tt1605783/?ref_=ttls_li_tt","https://www.imdb.com/title/tt1570728/?ref_=ttls_li_tt"]
    Family_movies=["https://www.imdb.com/title/tt10999120/?ref_=adv_li_tt","https://www.imdb.com/title/tt1596342/?ref_=adv_li_tt","https://www.imdb.com/title/tt17220704/?ref_=adv_li_tt","https://www.imdb.com/title/tt13320662/?ref_=adv_li_tt","https://www.imdb.com/title/tt15824322/?ref_=adv_li_tt","https://www.imdb.com/title/tt3447590/?ref_=adv_li_tt","https://www.imdb.com/title/tt0113820/?ref_=adv_li_tt"]
    Drama_movies=["https://www.imdb.com/title/tt9114286/?ref_=adv_li_tt","https://www.imdb.com/title/tt9288822/?ref_=adv_li_tt","https://www.imdb.com/title/tt11564570/?ref_=adv_li_tt","https://www.imdb.com/title/tt9411972/?ref_=adv_li_tt","https://www.imdb.com/title/tt14208870/?ref_=adv_li_tt","https://www.imdb.com/title/tt15501640/?ref_=adv_li_tt","https://www.imdb.com/title/tt13833688/?ref_=adv_li_tt"]
    Sport_movies=["https://www.imdb.com/title/tt5533370/?ref_=adv_li_tt","https://www.imdb.com/title/tt8745676/?ref_=adv_li_tt","https://www.imdb.com/title/tt1950186/?ref_=adv_li_tt","https://www.imdb.com/title/tt8009428/?ref_=adv_li_tt","https://www.imdb.com/title/tt3076658/?ref_=adv_li_tt","https://www.imdb.com/title/tt6343314/?ref_=adv_li_tt","https://www.imdb.com/title/tt1291584/?ref_=adv_li_tt"]
    Romantic_movies=["https://www.imdb.com/title/tt14715170/?ref_=adv_li_tt","https://www.imdb.com/title/tt13007592/?ref_=adv_li_tt","https://www.imdb.com/title/tt14109724/?ref_=adv_li_tt","https://www.imdb.com/title/tt13139228/?ref_=adv_li_tt","https://www.imdb.com/title/tt0314331/?ref_=adv_li_tt","https://www.imdb.com/title/tt20850406/?ref_=adv_li_tt","https://www.imdb.com/title/tt3774694/?ref_=adv_li_tt"]
    Film_Noir=['https://www.imdb.com/title/tt0038669/?ref_=adv_li_tt','https://www.imdb.com/title/tt0048394/?ref_=adv_li_tt','https://www.imdb.com/title/tt0043338/?ref_=adv_li_tt','https://www.imdb.com/title/tt0050241/?ref_=adv_li_tt','https://www.imdb.com/title/tt0050249/?ref_=adv_li_tt','https://www.imdb.com/title/tt0050439/?ref_=adv_li_tt']
    chatlog = []
    message = inserting_text
    sentiment = predict_emotion([message], count_vect, model)
    print(sentiment)

    if message.lower() == 'thank you':
        print('glad to help,bye see you soon')
        #speak('glad to help you,bye see you soon')
        chatlogdf = pd.DataFrame(chatlog, columns=['message', 'sentiment', 'recommendation'])
        chatlogdf.to_csv('chatlog.csv', index= False)
        
    else:
        if sentiment[0] == 'joy':
            recommendation = random.choice(happy_movies)
            response = 'Did you know ?,Happiness is the meaning and the purpose of life, the whole aim and end of human existence,SO to make your day better here I have presented movie: '
            #engine.say(response)
            #print=(response)
            #engine.runAndWait()
            #print(recommendation)

        elif sentiment[0] == 'anger':
            recommendation = random.choice(Family_movies)
            response = ' Did you know ? Anger has been linked to health issues such as high blood pressure, heart problems, headaches, skin disorders, and digestive problems but do not worry here I have the list of family movies that can can cheer you up: '
            #engine.say(response)
            #engine.runAndWait()
            #return(recommendation)
            #print('angry')

        elif sentiment[0] == 'sadness':
             recommendation = random.choice(Drama_movies)
             response = ' Did you know?, sadness can cause distinctive physical sensations in the chest: tight muscles, a pounding heart, rapid breathing, and even a churning stomach.I am sorry that you feel sad and I do not want to know why but I can help you recommending some drama movies,which will help you comeover: '
             #engine.say(response)
            #print=('i am sorry that you feel sad and i do not want to know why but i can help you recommending some drama movies,which will help you comeover: ')
             #engine.runAndWait()
            # return(recommendation)
            #print('sad')
        
        elif sentiment[0] == 'fear':
             recommendation = random.choice(Sport_movies)
             response = 'I am sorry that you feel fear and I do not want to know why are you feeling fear but here is the list of sports movies that can build your confidence up: '
             #engine.say(response)
             #engine.runAndWait()
            # return(recommendation)
            #print('fear')
        
        elif sentiment[0] == 'love':
             recommendation = random.choice(Romantic_movies)
             response = 'Did you know? Fun fact  men fall in love faster than women, and here is my recoomendation to watch movies with your betterhalf: '
             #engine.say(response)
             #engine.runAndWait()
             #return(recommendation)
             #print('love')
        
        elif sentiment[0] == 'surprise':
             recommendation = random.choice(Film_Noir)
             response = 'Did you know ?When we experience a surprise, the level of serotonin and dopamine in our body increases amazingly.This makes experiences more enjoyable so I suggest you to sit down and watch this movie: '
             #engine.say(response)
             #engine.runAndWait()
             #return(recommendation)
             #print('surprise')
        
        chatlog.append([message, sentiment, recommendation])
        return (response, recommendation)

    
    