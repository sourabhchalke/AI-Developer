import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Rutika  Madam lavvkar chai baanvaa")

# Get current rate
rate = engine.getProperty('rate')
print(f"Current rate: {rate}")

# Set a slower rate (default is around 200)
# Lower number = slower speech
engine.setProperty('rate', 180)  # Try values between 100-180

engine.runAndWait()