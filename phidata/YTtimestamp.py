from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
import os
from phi.llm.mistral import MistralChat
from phi.model.groq import Groq
from dotenv import load_dotenv
load_dotenv()
os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")

agent = Agent(
    name="YouTube Timestamps Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    instructions=[
        "You are a YouTube agent. First check the length of the video. Then get the detailed timestamps for a YouTube video corresponding to correct timestamps.",
        "Don't hallucinate timestamps.",
        #"It has a collection of songs. Identify tiemstamps for each song in the list.",
        "Make sure to return the timestamps in the format of `[start_time, end_time, Song name]`.",
    ],
)
agent.print_response(
    "Get the detailed timestamps for this video https://www.youtube.com/watch?v=M5tx7VI-LFA", markdown=True
)
#https://www.youtube.com/watch?v=M5tx7VI-LFA
#https://www.youtube.com/watch?v=aWdK_4eZYBk