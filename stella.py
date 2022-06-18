from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
 
chatbot=ChatBot('Stella_chatbot')

trainer= ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

print("Hello, I am a Stella")

while True:
    ques= input(">>>")
    print(chatbot.get_response(Statement(text=ques,search_text=ques)))