import os
from phi.agent import Agent
from phi.model.mistral import MistralChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from dotenv import load_dotenv
from phi.model.groq import Groq
load_dotenv()
os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

agent = Agent(
     model=MistralChat(id="mistral-large-latest", api_key=os.environ["MISTRAL_API_KEY"],),
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are a senior NYT researcher writing an article on a topic.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare an NYT worthy article based on the information.",
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    # debug_mode=True,
)
agent.print_response("QAOA", stream=True)