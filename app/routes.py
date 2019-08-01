from app import app
from flask import render_template, request
from app.models import model, formopener
import random

pickupDict = {"animal":["Are you a cat because you're purrrrrrfect.", "Are you a unicorn cause you are my fantasy.", "Your like a bright light and im like a bug, because im so darn attracted to you.", "Are you a sheep cause your body is unbaaaaalievable", "Girl, if you were a dinosaur, you'd be a Gorgeousaurus", "Are you the energizer bunny cause you just keep going and going through my mind.", "Do you have some bug spray? Because I have butterflies in my tummy", "Kiss me if I'm wrong, but dinosaurs still exist, right?", "Wanna go on a picnic? Alpaca lunch.", "Im placing you on the endangered species list. Because baby your one of a kind."], 
"food":["Baby, if you were a fruit you'd be a fineapple.","Anyone can sit here and buy you drinks. I want to buy you dinner!","We should get coffee sometime because I like you a latte!","If you were a vegetable you'd be a Cute-Cumber","You must be a banana because I find you very a-peeling.","Are you a doughnut, because I find you a-dough-rable.","I think we'd make a cute pear","Do you have raisins? How about a date?","Your the macaroni to my cheese.","You make my heart skip a beet.","I'd love to see you s'more.","You've stolen a pizza my heart.","I cannoli have eyes for you.","I think your barbecute.","I think we're mint to be.","This might be cheesy but I think we're grate.", "I’d take you to a candy shop, but you’re already so sweet.", "Hershey factories make millions of kisses a day, but I’m only asking for one.", "Have you been eating Lucky Charms? Because you’re looking magically delicious!", "You must be peanut butter because you’re making my legs feel like jelly."], 
"nerdy": ["Is your name Google? Because you have everything I've been searching for.", "Is your name Wi-fi? Because I'm really feeling a connection.", "You had me at Hello World.", "You've stolen the ASCII to my heart.", "Are you a computer keyboard? Because you're my type.", "If Internet Explorer is brave enough to ask you to be your default browser, I’m brave enough to ask you out!","Girl, you are hotter than the bottom of my laptop.","WebMD says your love is contagious.","Where's the 'like' button for that smile?","You are the Apple of my i-Mac.","You must be Windows 95 because you've got me feeling so unstable."], 
"random":["Are you from korea? Cause you could be my seoul mate.", "I thought Happiness starts with H. But why does mine starts with U.", "Do believe in love at first sight? Or should I walk by you again?","Are you religious? Cause you’re the answer to all my prayers.","Hey, tie your shoes! I don’t want you falling for anyone else.","You must be Jamaican, because Jamaican me crazy.","Somebody call the cops, because it’s got to be illegal to look that good!", "I must be a snowflake, because I've fallen for you.","Hello, I'm a thief, and I'm here to steal your heart.","There is something wrong with my cell phone. It doesn't have your number in it.","You spend so much time in my mind, I should charge you rent.","I must be in a museum, because you truly are a work of art.","I'm new in town. Could you give me directions to your apartment?","Well, here I am. What were your other two wishes?", "Is it hot in here or is it just you?", "Feel my t-shirt, it’s made of boyfriend material.", "You're like a dictionary... you add meaning to my life.", "Can I take a picture of you so santa knows what I want for christmas?", "What does it feel like to be the most beautiful girl in the room?", "Would you grab my arm so I can tell my friends I've been touched by an angel?"]
}


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template("index.html")
@app.route('/')
@app.route('/results', methods = ['GET', 'POST'])
@app.route('/results.html', methods = ['GET', 'POST'])
def results():
    if request.method == 'GET':
        return "Unrecognized key word"
    else:
        userdata=request.form.to_dict()
        category = userdata["x"]
        generated = random.choice(pickupDict[category])
    return render_template("results.html", category=category,generated=generated)
    
    
    
    
