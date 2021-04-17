port = "COM3"
leftport = "COM5"
#servodriver = Runtime.createAndStart("Adafruit16CServoDriver","Adafruit16CServoDriver")
right = Runtime.createAndStart("right","Arduino")
right.connect(port)
left = Runtime.start("left", "Arduino")
left.connect(leftport)
#servodriver.setController("left","0","0x40")
##########################################################################################
Voice="dfki-ot-hsmm" 
voiceType = Voice
mouth = Runtime.createAndStart("mouth", "MarySpeech")
mouth.setVoice(voiceType)
cenekontrol = Runtime.createAndStart("cenekontrol", "MouthControl")

WebGui = Runtime.create("WebGui","WebGui")
WebGui.autoStartBrowser(False)
WebGui.startService()
WebGui.startBrowser("http://localhost:8888/#/service")
#webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
#webkitspeechrecognition.setLanguage("tr")
ear = Runtime.createAndStart("ear", "WebkitSpeechRecognition")
ear.addListener("publishText", python.name, "heard");
ear.setLanguage("tr")
ear.addMouth(mouth)
##########################################################################################
gozx = Runtime.createAndStart("gozx","Servo")
gozy = Runtime.createAndStart("gozy","Servo")
boyun = Runtime.createAndStart("boyun","Servo")
cene = Runtime.createAndStart("cene","Servo")
boyunsag = Runtime.createAndStart("boyunsag","Servo")
boyunsol = Runtime.createAndStart("boyunsol","Servo") 
gozx.attach(left, 2)
gozy.attach(left, 3)
boyun.attach(left, 4)
cene.attach(left, 6)
boyunsag.attach(left, 7)
boyunsol.attach(left, 5)
cenekontrol.setJaw(cene)
cenekontrol.setMouth(mouth)
cenekontrol.setmouth(77,180)
cenekontrol.setdelays(60,60,70)
cenekontrol.startService()
##########################################################################################
boyunsag.map(0,180,20,170)
boyunsol.map(0,180,20,170)
boyun.map(0,180,20,170)
gozx.map(0,180,50,170)
gozy.map(0,180,20,180)
cene.map(0,180,0,170)
cene.setVelocity(-1)
gozx.setVelocity(-1)
gozy.setVelocity(-1)
boyun.setVelocity(-1)
boyunsag.setVelocity(-1)
boyunsol.setVelocity(-1)
gozx.setRest(130)
gozy.setRest(145)
boyun.setRest(50)
cene.setRest(40)
boyun.rest()
gozy.rest()
gozx.rest()
cene.rest()
#########################################################################################
def heard(data):
  print "Speech Recognition Data:"+str(data)
#########################################################################################
ear.addCommand("merhaba", "python", "merhaba")

#########################################################################################
def merhaba():
  mouth.speakBlocking("merhaba merve")