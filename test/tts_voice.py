import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[-2].id) #-1 voz em ingles -2 voz em portugues

engine.say("Como vai meu criador")
engine.runAndWait()
