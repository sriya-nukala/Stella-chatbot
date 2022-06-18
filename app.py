from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app=Flask(__name__)

chatbot=ChatBot('Stella_chatbot')

trainer= ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

@app.route("/") 
def home():
    return render_template("stella.html")

@app.get("/get")
def get__stellaresponse():
    ques=request.args.get('msg')
    return str(chatbot.get_response(ques))

if __name__=="__main__":
    app.run() 