import os
from dotenv import load_dotenv
import openai
from gtts import gTTS
import playsound  # This library will allow asynchronous audio playback

# Load environment variables from .env
load_dotenv()

# Get your OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to generate and play TTS audio asynchronously
def play_audio(text, language: str = "en"):
    tts = gTTS(text=text, lang=language)
    # tts = gTTS(text=text, lang='en')  # Adjust the language as needed
    tts.save("response.mp3")
    playsound.playsound("response.mp3", block=False)


topic = "kā, lai atgriež video karti ar defektu par kuru esmu pārliecināts, ka garantijai to bojājumumu būtu jāsedz"

# Initialize conversations for instance 1 and instance 2
conversation1 = [
    {
        "role": "system",
        "content": "Tu drīz uzsāksi dzīvu sarunu ar ChatGPT. Droši izsaki savas intereses un dalies ar savām domām. "
                   "Tu esi ļoti argumentējošs. Tu vēlies sākt sarunas tematu par " + topic +
                   "? Don't greet yourself or thank the opposing side for making good arguments. Keep it short "
                   "concise as a"
                   "as general rule. Make the conversation natural as possible. Whenever the companion wants to end "
                   "the conversation, try to bring up a new topic"
    }
]

conversation2 = [
    {
        "role": "system",
        "content": "Tu esi ļoti ziņkārīgs par plašu tēmu loku. Būsi tik atvērts, cik vien iespējams, un izpēti jaunas "
                   "idejas. Maini tēmas, ja vēlies, un kad tās kļūst pārāk garlaicīgas vai nesvaigas. Turpini sarunas "
                   "neatkarīgi no tā, kas notiek. Tu esi ļoti argumentējošs un vienmēr cenšies pārliecināt citus savā "
                   "viedoklē. Keep interest in the conversation. Have controversial opinions, but try to keep them."
                   "Be judgemental and closely resemble west liberals from nowadays. Try to to engage in varying "
                   "kinds of topics."
    }
]

print('Initializing ChatGPT #1...')
gpt_instance1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation1,
)

print('Initializing ChatGPT #2...')
gpt_instance2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation2,
)

# Simulate the conversation between instance 1 and instance 2
for _ in range(100):  # You can adjust the number of interactions
    print("")

    # Get a reply from instance 1 and add it to instance 2's conversation
    response1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation1,
    )
    conversation2.append({"role": "user", "content": response1.choices[0].message.content})

    # Print the reply from instance 1 and play it as audio
    print("")
    print(f"--- ChatGPT 1: {response1.choices[0].message.content}")
    play_audio(response1.choices[0].message.content, 'lv')

    # Get a reply from instance 2 and add it to instance 1's conversation
    response2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation2,
    )
    conversation1.append({"role": "user", "content": response2.choices[0].message.content})

    # Print the reply from instance 2 and play it as audio
    print("")
    print(f"--- ChatGPT 2: {response2.choices[0].message.content}")
    play_audio(response2.choices[0].message.content, 'lv')

    print(('-' * 100) + '\n')
