import threading
import itertools
import time
import random as r
rightport = "COM5"
leftport = "COM4"
rservodriver = Runtime.createAndStart("rservodriver","Adafruit16CServoDriver")
lservodriver = Runtime.createAndStart("lservodriver","Adafruit16CServoDriver")
right = Runtime.start("right","Arduino")
right.connect(rightport)
left = Runtime.start("left","Arduino")
left.connect(leftport)
rservodriver.setController("right","0","0x40")
lservodriver.setController("left","0","0x40")
##########################################################################################
mouth = Runtime.start("MarySpeech", "MarySpeech")
mouth.setVoice("dfki-ot-hsmm")
mouthcontrol = Runtime.start("mouthcontrol","MouthControl")
htmlFilter = Runtime.start("htmlfilter","HtmlFilter")
WebGui = Runtime.create("WebGui","WebGui")
WebGui.autoStartBrowser(False)
WebGui.startService()
WebGui.startBrowser("http://localhost:8888/#/service")
ear = Runtime.createAndStart("ear", "WebkitSpeechRecognition")
ear.setAutoListen(False) 
ear.setContinuous(False)
ear.setLanguage("tr")
ear.addMouth(mouth)
##########################################################################################
romuzyan = Runtime.createAndStart("romuzyan","Servo") 
romuzon = Runtime.createAndStart("romuzon","Servo") 
rbicep = Runtime.createAndStart("rbicep","Servo") 
rdonme = Runtime.createAndStart("rdonme","Servo") 
rbas = Runtime.createAndStart("rbas","Servo") 
risaret = Runtime.createAndStart("risaret","Servo") 
rorta = Runtime.createAndStart("rorta","Servo") 
ryuzuk = Runtime.createAndStart("ryuzuk","Servo") 
rserce = Runtime.createAndStart("rserce","Servo")
lomuzyan = Runtime.createAndStart("lomuzyan","Servo") 
lomuzon = Runtime.createAndStart("lomuzon","Servo") 
lbicep = Runtime.createAndStart("lbicep","Servo") 
ldonme = Runtime.createAndStart("ldonme","Servo") 
lbas = Runtime.createAndStart("lbas","Servo") 
lisaret = Runtime.createAndStart("lisaret","Servo") 
lorta = Runtime.createAndStart("lorta","Servo") 
lyuzuk = Runtime.createAndStart("lyuzuk","Servo") 
lserce = Runtime.createAndStart("lserce","Servo")
lbilek = Runtime.createAndStart("lbilek","Servo")
basdonme = Runtime.createAndStart("basdonme","Servo")
cene = Runtime.createAndStart("cene","Servo") 
boyun = Runtime.createAndStart("boyun","Servo") 
boyunr = Runtime.createAndStart("boyunr","Servo") 
boyunl = Runtime.createAndStart("boyunl","Servo") 
gozx = Runtime.createAndStart("gozx","Servo") 
gozy = Runtime.createAndStart("gozy","Servo") 
##########################################################################################
mouthcontrol.setJaw(cene)
mouthcontrol.jaw.setMinMax(80,180)
mouthcontrol.jaw.map(0,180,80,180)
mouthcontrol.jaw.setRest(20)
mouthcontrol.setmouth(80,180)
mouthcontrol.setMouth(mouth)
######################################################################################
romuzyan.attach(rservodriver, 9)
romuzon.attach(rservodriver, 8)
rbicep.attach(rservodriver, 5) 
rdonme.attach(rservodriver, 10)
rbas.attach(rservodriver, 3)
risaret.attach(rservodriver, 1)
rorta.attach(rservodriver, 4)
ryuzuk.attach(rservodriver, 2)
rserce.attach(rservodriver, 0)
lbilek.attach(lservodriver,6)  #120 baÅŸlangÄ±Ã§ map(0-180)
lomuzyan.attach(lservodriver, 9) #map(130-65) baÅŸlangÄ±Ã§ 180
lomuzon.attach(lservodriver, 10) #map(90-170) baÅŸlangÄ±Ã§ 180
lbicep.attach(lservodriver, 5)  #bicep  180 baÅŸlangÄ±Ã§ map(65,145)
ldonme.attach(lservodriver, 8)  #map(60-130) 130 baÅŸlangÄ±Ã§
lbas.attach(lservodriver, 4)
lisaret.attach(lservodriver, 3)
lorta.attach(lservodriver, 2)
lyuzuk.attach(lservodriver, 1)
lserce.attach(lservodriver, 0)
cene.attach(rservodriver, 11)
boyun.attach(lservodriver, 12)
boyunr.attach(lservodriver, 14)
boyunl.attach(lservodriver, 13)
basdonme.attach(rservodriver, 13)
gozx.attach(rservodriver, 15) #(120-180) 120 baÅŸlangÄ±Ã§
gozy.attach(rservodriver, 14) #(30-180) 130b
##########################################################################################
romuzyan.map(0,180,50,105)
romuzon.map(0,180,0,180)
rbicep.map(0,180,0,76)
rdonme.map(0,180,60,180)
rbas.map(0,180,0,150)
risaret.map(0,180,0,150)
rorta.map(0,180,0,170)
ryuzuk.map(0,180,0,170)
rserce.map(0,180,0,180)
lomuzyan.map(0,180,65,130)
lomuzon.map(0,180,90,170)
lbicep.map(0,180,65,145)
ldonme.map(0,180,60,130)
lbas.map(0,180,0,140)
lisaret.map(0,180,0,140)
lorta.map(0,180,0,140)
lyuzuk.map(0,180,0,140)
lserce.map(0,180,0,170)
cene.map(0,180,70,140)
boyun.map(0,180,0,180)
basdonme.map(0,180,0,180)
gozx.map(0,180,120,180)
gozy.map(0,180,30,180)
romuzon.moveTo(180)
romuzyan.moveTo(180)
rbicep.moveTo(180)
rdonme.moveTo(100)
rbas.moveTo(180)
risaret.moveTo(180)
rorta.moveTo(180)
ryuzuk.moveTo(180)
rserce.moveTo(180)
lomuzon.moveTo(180)
lomuzyan.moveTo(180)
lbicep.moveTo(180)
ldonme.moveTo(130)
lbas.moveTo(0)
lisaret.moveTo(0)
lorta.moveTo(0)
lyuzuk.moveTo(0)
lserce.moveTo(0)
cene.moveTo(0)
gozx.moveTo(150)
gozy.moveTo(170)
rbicep.setVelocity(20)
romuzon.setVelocity(20)
lbicep.setVelocity(20)
lomuzon.setVelocity(20)
boyun.setVelocity(30)
boyunr.setVelocity(30)
boyunl.setVelocity(30)
basdonme.setVelocity(30)
boyun.moveTo(90)
boyunr.moveTo(40)
boyunl.moveTo(140)
basdonme.moveTo(100)

###############################################
htmlFilter.addListener("publishText",python.name,"say");
ear.setAutoListen(True)
ear.startListening()
############################################################
ear.addListener("publishText","python","replacer")
def replacer(data):
    data = data.replace(chr(214),"O")#Ö
    data = data.replace(chr(246),"o")#ö
    data = data.replace(chr(252),"u")#ü
    data = data.replace(unichr(220),"U")#Ü
    data = data.replace(unichr(305),"i")#ı   
    data = data.replace(chr(231),"c")#ç
    data = data.replace(unichr(199),"C")#Ç
    data = data.replace(unichr(351),"s")#ş
    data = data.replace(unichr(350),"s")#Ş
    data = data.replace(unichr(287),"g")#ğ   
    data = data.replace(unichr(286),"g")#Ğ        
    print data
    ear.setStripAccents(True)
    if data == "ellerini kapat":
        rel(180,180,180,180,180)
        lel(180,180,180,180,180)
    elif data == "ellerini ac":
        rel(0,0,0,0,0)
        lel(0,0,0,0,0) 
    elif data == "saga bak":
        basdonme.moveTo(180) 
    elif data == "sola bak":
        basdonme.moveTo(0) 
    elif data == "ortaya bak":
        basdonme.moveTo(100) 
    elif data == "asagi bak":
        boyun.moveTo(10) 
    elif data == "yukari bak":
        boyun.moveTo(160) 
    elif data == "onune bak":
        boyun.moveTo(90)         
    elif data == "merhaba":
        merhaba() 
    elif data == "kendinden bahset":
        tanit()  
    elif data == "arkadasin var mi":
        arkadas()  
    elif data == "gorusuruz":
        bay()  
 
        
def rel(bas,isaret,orta,yuzuk,serce):
	rbas.moveTo(bas)
	risaret.moveTo(isaret)
	rorta.moveTo(orta)
	ryuzuk.moveTo(yuzuk)
	rserce.moveTo(serce)

def lel(bas,isaret,orta,yuzuk,serce):
	lbas.moveTo(bas)
	lisaret.moveTo(isaret)
	lorta.moveTo(orta)
	lyuzuk.moveTo(yuzuk)
	lserce.moveTo(serce)


def gozler(x,y):
	gozx.moveTo(x)
	gozy.moveTo(y)

def boyunlar(on,r,l):
	boyun.moveTo(on)
	boyunr.moveTo(r)
	boyunl.moveTo(l)

def merhaba():
	x= r.randint(1,2)
	if x == 1:
	  mouth.speak("merhaba")
	elif x == 2:
	  mouth.speak("selam")

def bay():
	x= r.randint(1,3)
	if x == 1:
	  mouth.speak(u'bay bay')
	elif x == 2:
	  mouth.speak(u'görüşmek üzere')
	elif x == 3:
	  mouth.speak(u'görüşürüz kendine iyi bak')

def tanit():
	mouth.speakBlocking(u'benim adım sirius')
	mouth.speakBlocking(u'meykırlan kodlama atölyesinde doğdum')
	mouth.speakBlocking(u'yeni  bilgiler öğrenmeyi heyecan verici buluyorum')

def arkadas():
	mouth.speak(u'şuanda tek arkadaşım mira')

