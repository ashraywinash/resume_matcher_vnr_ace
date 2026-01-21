import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# for model in genai.list_models():
#     print(model.name)
#     print("  Supported methods:", model.supported_generation_methods)
#     print()

MODEL_NAME = "models/gemini-2.5-flash"

def call_gemini(messages: list) -> str:
    """
    messages = [
      {"role": "system", "content": "..."},
      {"role": "user", "content": "..."}
    ]
    """

    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=messages[0]["content"]
    )

    chat = model.start_chat(history=[])

    response = chat.send_message(
        messages[1]["content"],
        generation_config=genai.types.GenerationConfig(
            temperature=0.2
        )
    )


    return response.text
    