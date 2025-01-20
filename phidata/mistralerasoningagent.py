from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.mistral import MistralChat
from phi.model.groq import Groq

from dotenv import load_dotenv
import os
load_dotenv()

os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

task = (
    "Three missionaries and three cannibals need to cross a river. "
    "They have a boat that can carry up to two people at a time. "
    "If, at any time, the cannibals outnumber the missionaries on either side of the river, the cannibals will eat the missionaries. "
    "How can all six people get across the river safely? Provide a step-by-step solution and show the solutions as an ascii diagram"
)

reasoning_agent = Agent(model=MistralChat(id="mistral-large-latest", api_key=os.environ["MISTRAL_API_KEY"],), reasoning=True, markdown=True, structured_outputs=True)
#reasoning_agent = Agent(model=Groq(id="llama-3.3-70b-versatile"), reasoning=True, markdown=True, structured_outputs=True)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)