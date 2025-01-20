import json
import httpx
import os
from phi.agent import Agent
from typing import List
from phi.llm.mistral import MistralChat
from dotenv import load_dotenv
from phi.model.groq import Groq
load_dotenv()
os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")
from phi.model.groq import Groq

def get_top_hackernews_stories(num_stories: int = 10) :
    
    #Fetch top story IDs
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)

myagent = Agent(model=Groq(id="llama-3.3-70b-versatile"), tools=[get_top_hackernews_stories],
show_tool_calls=True, markdown=True
    )
myagent.print_response("Summarize the top 5 stories on hackernews?", stream=True)


