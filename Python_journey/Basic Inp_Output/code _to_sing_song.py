import pyttsx3
import time

# Initialize engine once (not inside loop)
engine = pyttsx3.init()

while True:
    engine.say("Oee Sandhya, khana pakyo ki nai? Malai bhok lagyo!")
    engine.runAndWait()
    time.sleep(3)  # wait 3 seconds before repeating (you can change this)
    # To stop the loop, you can use a break condition or interrupt the program manually