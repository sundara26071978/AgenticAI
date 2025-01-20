from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
import os
from phi.llm.mistral import MistralChat
from phi.model.groq import Groq
from dotenv import load_dotenv
load_dotenv()
os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")



reasoning_agent = Agent(model=Groq(id="llama-3.3-70b-versatile"), tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",)
reasoning_agent.print_response("Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True)
