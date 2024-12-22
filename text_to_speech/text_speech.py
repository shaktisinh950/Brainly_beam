import os
from gtts import gTTS

def text_to_speech(text, username):
    user_folder = os.path.join(os.getcwd()+'/text_to_speech', username)
    os.makedirs(user_folder, exist_ok=True)

    mp3_filename = os.path.join(user_folder, "speech.mp3")

    tts = gTTS(text=text, lang='en')
    tts.save(mp3_filename)

    print(f"Speech saved to: {mp3_filename}")
    return mp3_filename

# Example usage
user_text = "my name is Shakti parmar , i am studying in LJ UNIVERSITY"
user_name = "shakti"

text_to_speech(user_text, user_name)

