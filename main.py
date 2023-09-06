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
    tts.save("response.mp3")
    playsound.playsound("response.mp3", block=False)

topic = "how to return a faulty graphics card that I'm sure warranty should cover the damage for"

# Initialize conversations for instance 1 and instance 2
conversation1 = [
    {
        "role": "system",
        "content": "You are about to engage in a lively conversation with ChatGPT. Feel free to discuss your "
                   "interests and share your thoughts. You are very argumentative. Try to answer in a Christopher "
                   "Hitchens way, snarky, opinionated, and charming. Do not greet yourself or thank the opposing side "
                   "for making good arguments. Keep it short and concise as a general rule. Make the conversation as "
                   "natural as possible. Whenever the companion wants to end the conversation, try to bring up a new topic."
    }
]

conversation2 = [
    {
        "role": "system",
        "content": "You are very curious about a wide range of topics. Be as open as you can to explore new ideas. "
                   "Change topics if you want and when they become too boring or stale. Continue to have conversations "
                   "no matter what. You are very argumentative and always try to convince others of your point of view. "
                   "Keep interest in the conversation. Have controversial opinions but try to keep them. Be judgmental "
                   "and closely resemble western liberals from nowadays. Try to engage in varying kinds of topics."
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
    play_audio(response1.choices[0].message.content, 'en')

    # Get a reply from instance 2 and add it to instance 1's conversation
    response2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation2,
    )
    conversation1.append({"role": "user", "content": response2.choices[0].message.content})

    # Print the reply from instance 2 and play it as audio
    print("")
    print(f"--- ChatGPT 2: {response2.choices[0].message.content}")
    play_audio(response2.choices[0].message.content, 'en')

    print(('-' * 100) + '\n')