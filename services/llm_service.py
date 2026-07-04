import os

from groq import Groq
from dotenv import load_dotenv


class LLMService:

    def __init__(self):

        load_dotenv()

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = "llama-3.3-70b-versatile"

    def ask_llm(self, prompt):

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced Business Intelligence Analyst. "
                        "Provide concise, professional business insights and recommendations."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,
            max_tokens=500

        )

        return response.choices[0].message.content