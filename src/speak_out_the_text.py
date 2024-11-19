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
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.title("Gooyesh text to Speech Engine")

    text_label = tk.Label(root, text="Enter text here:")
    text_label.pack()

    text_entry = tk.Text(root, height=10, width=40)
    text_entry.pack()

    play_button = tk.Button(root, text="Play", command=lambda: speak_out_the_text(text_entry.get("1.0", tk.END)))
    play_button.pack()

    root.mainloop()
