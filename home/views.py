# from django.shortcuts import render

# # Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import openai,os
import webbrowser

from dotenv import load_dotenv

load_dotenv()
openaiapikey=os.getenv('openaiapikey')

def Main_Interface(request):
   return render(request,"mainPage.html")


def ImageGenerator(request):
   imagename=request.GET['imagetext']
   print("Name:::::::::::::",imagename)
   openai.api_key=openaiapikey
   response = openai.Image.create(
      prompt=imagename,
      n=1,
      size="1024x1024"
      )
   image_url = response['data'][0]['url']
   chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
   webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
   webbrowser.get('chrome').open_new_tab(image_url)
   return JsonResponse({'result':True},safe=False)

def AskAnything(request):
   openai.api_key=openaiapikey
   asktext=request.GET['asktext']
   response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=asktext,
        max_tokens=1000,
        temperature=0.7
   )
   chatbot_response = response["choices"][0]["text"]
   print(chatbot_response)
   return JsonResponse({'asktext': chatbot_response }, safe=False)

def AddComment(request):
   openai.api_key=openaiapikey
   addcomment="add comment in this code line by line "+request.GET['addcomment']
   print(addcomment)
   response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=addcomment,
        max_tokens=1000,
        temperature=0.7
   )
   chatbot_response = response["choices"][0]["text"]
   print(chatbot_response)
   return JsonResponse({'outputcode': chatbot_response }, safe=False)


