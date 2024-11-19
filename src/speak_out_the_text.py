def speak_out_the_text(input_text):
    """
        Just speaks out the text with the default voice over you have on your machine.
        Nothing else.
    """
    import pyttsx3
    engine = pyttsx3.init()

    # For Mac, If you face error related to "pyobjc" when running the `init()` method :
    # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

    rate = engine.getProperty('rate')
    print(f"The rate of the voice engine is : {rate}")
    # engine.setProperty('rate', 125) # this is for changing the rate of the engine

    volume = engine.getProperty('volume')
    print(f"The volume of the voice engine is :{volume}")
    # engine.setProperty('volume', 1.0) # This is for changing the volume of the engine

    # voices[0] is male and voices[1] is a female.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(input_text)
    engine.runAndWait()


if __name__ == '__main__':
    import tkinter as tk

    root = tk.Tk()
    root.title("Gooyesh text to Speech Engine")

    text_label = tk.Label(root, text="Enter text here:")
    text_label.grid(row=0, column=0, sticky="w")

    text_entry = tk.Text(root, height=10, width=40)
    text_entry.grid(row=1, column=0, columnspan=2, sticky="nsew")

    play_button = tk.Button(root, text="Play", command=lambda: speak_out_the_text(text_entry.get("1.0", tk.END)))
    play_button.grid(row=2, column=0, sticky="w")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    root.mainloop()
