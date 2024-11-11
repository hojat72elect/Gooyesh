def change_voice_rate_volume(input_text):
    import pyttsx3
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate', 125)

    volume = engine.getProperty('volume')
    print(volume)
    engine.setProperty('volume', 1.0)

    # voices[0] is male and voices[1] is a female.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # engine.say(input_text)
    engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()



if __name__ == '__main__':
    change_voice_rate_volume("This application is fun to work with")
