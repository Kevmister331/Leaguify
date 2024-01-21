from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(
    api_key = os.environ.get('API_KEY')
)

def get_recommendations(traits):
    prompt1 = "Generate 10 different, popular songs that actually exist, based on these traits:"
    prompt2 = ". Please choose more popular songs for the first 5, and choose less popular (more indie or niche) songs for the last 5. Return the result as an array of json objects, with each object representing a song in the following format: {artist: <artist name>, song: <song title>}"
    for trait in traits:
        prompt1 = prompt1 + " " + trait
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":prompt1 + prompt2
            }
        ],
        model="gpt-3.5-turbo"
    )

    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content