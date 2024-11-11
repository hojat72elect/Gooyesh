def speak_out_the_text(input_text):
    """
        Just speaks out the text with the default voice over you have on your machine.
        Nothing else.
    """
    import pyttsx3
    engine = pyttsx3.init()

    # For Mac, If you face error related to "pyobjc" when running the `init()` method :
    # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

    engine.say(input_text)
    engine.runAndWait()



if __name__ == '__main__':
    speak_out_the_text("My name is Jonathan blow.")
    speak_out_the_text("How are you doing today?")
    speak_out_the_text("Yes it's a pleasant day.")
