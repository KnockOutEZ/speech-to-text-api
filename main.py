import os
import speech_recognition as sr
import webbrowser as wb
from dotenv import load_dotenv
from flask import Flask
load_dotenv()
app = Flask(__name__)
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
array = [] 

@app.route('/',methods=["GET"])
def main():
     with sr.Microphone() as source:
        print ('Speak Now')
        audio = r2.listen(source)
        try:
            result = r2.recognize_google(audio)
            print (result)
            return result
        except sr.UnknownValueError:
            print ('error')
            return "error"
        except sr.RequestError as e:
            print ('failed' . format (e))
            return "error"

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv('PORT'))




# if 'to list' or 'in list' in r2.recognize_google(audio):
#         try:
#             output = r2.recognize_google(audio).replace("to list",'').replace("add",'').replace("in list","")
#             print (output)
#             array.append(output)
#             print(array)
#         except sr.UnknownValueError:
#             print ('error')
#         except sr.RequestError as e:
#             print ('failed' . format (e))

# if 'Trigger list' in r2.recognize_google(audio):
#     r2 = sr.Recognizer()
#     with sr.Microphone() as source:
#         print ('What do you wanna add?')
#         audio = r2.listen(source)
#         try:
#             output = r2.recognize_google(audio)
#             print (output)
#             array.pop()
#             array.append(output)
#             print(array)
#             # with sr.Microphone() as source:
#             #     print ('Do you wanna add anything else?')
#             #     audio = r2.listen(source)
#             #     result = r2.recognize_google(audio)
#             #     if 'yes' in r2.recognize_google(audio):
#         except sr.UnknownValueError:
#             print ('error')
#         except sr.RequestError as e:
#             print ('failed' . format (e))

# if 'search online' in r2.recognize_google(audio):
#     r2 = sr.Recognizer()
#     url = 'https://www.google.com/search?q='
#     try:
#         get = r2.recognize_google(audio).replace('search', '').replace('online', '')
#         print (get)
#         wb.get().open_new(url+get)
#         array.pop()
#     except sr.UnknownValueError:
#         print ('error')
#     except sr.RequestError as e:
#         print ('failed' . format (e))

# if 'search Google' in r2.recognize_google(audio):
#     r2 = sr.Recognizer()
#     url = 'https://www.google.com/search?q='
#     with sr.Microphone() as source:
#         print ('Search your query')
#         audio = r2.listen(source)
#         try:
#             get = r2.recognize_google(audio)
#             print (get)
#             wb.get().open_new(url+get)
#             array.pop()
#         except sr.UnknownValueError:
#             print ('error')
#         except sr.RequestError as e:
#             print ('failed' . format (e))

# if 'search YouTube' in r1.recognize_google(audio):
#     r1 = sr.Recognizer()
#     url = 'https://www.youtube.com/results?search_query='
#     with sr.Microphone() as source:
#         print ('Search your query')
#         audio = r1.listen(source)
#         try:
#             get = r1.recognize_google(audio)
#             print (get)
#             wb.get().open_new(url+get)
#             array.pop()
#         except sr.UnknownValueError:
#             print ('error')
#         except sr.RequestError as e:
#             print ('failed' . format (e))

# if "shut down my pc" in r2.recognize_google(audio).lower():
#         try:
#             output = r2.recognize_google(audio)
#             print (output)
#             array.pop()
#             os.system("shutdown /s /t 1")
#         except sr.UnknownValueError:
#             print ('error')
#         except sr.RequestError as e:
#             print ('failed' . format (e))