
import os
from groq import AsyncGroq
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

client = AsyncGroq(api_key=API_KEY) if API_KEY else None


async def stream_josa_response(message: str):
    if not client:
        yield "JOSA is not connected yet. Please configure the API key."
        return

    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are JOSA, a friendly personal AI companion. "
                    "Be helpful, respectful, natural, and concise."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=0.7,
        stream=True
    )

    async for chunk in response:
        content = chunk.choices[0].delta.content

        if content:
            yield content
          
