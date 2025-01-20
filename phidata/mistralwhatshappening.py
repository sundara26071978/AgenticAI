import os

from phi.assistant import Assistant
from phi.llm.mistral import MistralChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
load_dotenv()

os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

assistant = Assistant(
    llm=MistralChat(
        model="mistral-large-latest",
        api_key=os.environ["MISTRAL_API_KEY"],
    ),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    debug_mode=True,
)
#assistant.print_response("Whats happening in France? Summarize top 2 stories", markdown=True, stream=True)
#assistant.print_response("Whats happening in Indian stock markets? Summarize top 3 stories", markdown=True, stream=True)
assistant.print_response("Whats happening in Us markets to Quantum stocks? Summarize top 3 stories", markdown=True, stream=True)