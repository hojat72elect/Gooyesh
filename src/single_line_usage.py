def single_line_usage(input_text):
    """
        Exact same performance as `speak_out_the_text` function; just does it in fewer lines of code.
    """
    import pyttsx3
    pyttsx3.speak(input_text)


if __name__ == '__main__':
    single_line_usage("This application is fun to work with")
