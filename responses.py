from datetime import datetime

def sampleresponses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hey", "Wassap"):
        return "Hey dude/girl! How is it going?"

    if user_message in ("who are you", "who are you?", "your name",):
        return "I'm Nuriddin's bot. I can do not much things ))) Coz I was created for testing. Maybe will turn into real worth project in the future;))"

    if user_message in ("time", "time?", "what time is it?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return date_time

    return "I don't understad that you've requested. Please try again. Or wait to expand my abilities by admins ;)"

