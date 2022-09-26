import speech_recognition as sr
import webbrowser as wb
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
array = []

with sr.Microphone() as source:
    print ('Speak Now')
    audio = r2.listen(source)
    result = r2.recognize_google(audio)
    print (result)


if 'list' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        print ('What do you wanna add?')
        audio = r2.listen(source)
        try:
            output = r2.recognize_google(audio)
            print (output)
            array.append(output)
            print(array)
        except sr.UnknownValueError:
            print ('error')
        except sr.RequestError as e:
            print ('failed' . format (e))


if 'search' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    try:
        get = r2.recognize_google(audio).replace('search', '').replace('online', '')
        print (get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print ('error')
    except sr.RequestError as e:
        print ('failed' . format (e))

if 'search Google' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    with sr.Microphone() as source:
        print ('Search your query')
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print (get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print ('error')
        except sr.RequestError as e:
            print ('failed' . format (e))

if 'search YouTube' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print ('Search your query')
        audio = r1.listen(source)
        try:
            get = r1.recognize_google(audio)
            print (get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print ('error')
        except sr.RequestError as e:
            print ('failed' . format (e))