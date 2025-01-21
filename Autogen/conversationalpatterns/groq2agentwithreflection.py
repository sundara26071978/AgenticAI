from pathlib import Path

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY1"]=os.getenv("GROQ_API_KEY1")


config_list = [
    {
        # Let's choose the Mixtral 8x22B model
        "model": "llama3-8b-8192",
        # Provide your Mistral AI API key here or put it into the MISTRAL_API_KEY environment variable.
        "api_key": os.environ.get("GROQ_API_KEY1"),
        # We specify the API Type as 'mistral' so it uses the Mistral AI client class
        "api_type": "groq",
    }
]



from autogen import ConversableAgent

student_agent = ConversableAgent(
    name="Student_Agent",
    system_message="You are a student willing to learn.",
    llm_config={"config_list": config_list},
)
teacher_agent = ConversableAgent(
    name="Teacher_Agent",
    system_message="You are a Autogen framework teacher.",
    llm_config={"config_list": config_list},
)

chat_result = student_agent.initiate_chat(
    teacher_agent,
    #message="What is two agent chat with reflection?",
    #message="What is sequential chat pattern in agentic AI?",
    #message="What is demographic parity vs equalized odds?",
    message="why do we compare implied volatility to historical volatility?",
    summary_method="reflection_with_llm",
    max_turns=2,    
)


# print(chat_result.chat_history)
      
# print(ConversableAgent.DEFAULT_SUMMARY_PROMPT)


# import pprint

# # pprint.pprint(chat_result.chat_history)

# # Get the cost of the chat.
# pprint.pprint(chat_result.cost)