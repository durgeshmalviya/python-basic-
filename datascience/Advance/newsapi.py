
from turtle import left
import requests
import tkinter as tk
from gtts import gTTS
import os

def getNews():
    api_key = "ef0c5520221348b1889838c5acc6e198"
    url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey="+api_key
    news = requests.get(url).json()
    
    articles = news ["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])
        
    for i in range(20):
        my_news=my_news+str(i+1)+ "," + my_articles[i]+ "\n"


    label.config(text = my_news)

canvas = tk.Tk()
canvas.geometry("720x480")
canvas.title("News Top 10")


button = tk.Button(canvas, font = 10,bg= "Grey",fg = "Black",text = "Close",command = quit, height= 2,width = 10,bd = 7)
button.pack(side = "right")

button = tk.Button(canvas, font = 20,bg= "Grey",fg = "Black",text = "Refresh",command = getNews,height = 2,width = 10,bd = 7)
button.pack(side = "left")

canvas.configure(bg ="Black")


label = tk.Label(canvas,bg ="Black",font = 10 , justify = "left", fg = "green")
label.pack(pady = 20)


getNews()

language = 'en'
mytext = 'getNews()'
myobj = gTTS(text=mytext, lang=language, slow=False)

canvas.mainloop()