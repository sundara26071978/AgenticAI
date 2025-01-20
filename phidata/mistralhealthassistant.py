import os
from phi.assistant import Assistant
from phi.llm.mistral import MistralChat
from dotenv import load_dotenv
load_dotenv()

os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

assistant = Assistant(
    llm=MistralChat(
        model="open-mixtral-8x22b",
        api_key=os.environ["MISTRAL_API_KEY"],
    ),
    description="You help people with their health and fitness goals.",
    debug_mode=True,
)
assistant.print_response("Share a quick healthy breakfast recipe.", markdown=True, stream=False)