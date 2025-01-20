from pathlib import Path

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


config_list = [
    {
        # Let's choose the Mixtral 8x22B model
        "model": "llama3-8b-8192",
        # Provide your Mistral AI API key here or put it into the MISTRAL_API_KEY environment variable.
        "api_key": os.environ.get("GROQ_API_KEY"),
        # We specify the API Type as 'mistral' so it uses the Mistral AI client class
        "api_type": "groq",
    }
]



from autogen import ConversableAgent

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message="You are playing a game of guess-my-number. You have the "
    "number 53 in your mind, and I will try to guess it. "
    "If I guess too high, say 'too high', if I guess too low, say 'too low'. ",
    llm_config={"config_list": config_list},
    is_termination_msg=lambda msg: "53" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="NEVER",  # never ask for human input
)

# agent_guess_number = ConversableAgent(
#     "agent_guess_number",
#     system_message="I have a number in my mind, and you will try to guess it. "
#     "If I say 'too high', you should guess a lower number. If I say 'too low', "
#     "you should guess a higher number. ",
#     llm_config={"config_list": config_list},
#     human_input_mode="NEVER",
# )

# result = agent_with_number.initiate_chat(
#     agent_guess_number,
#     message="I have a number between 1 and 100. Guess it!",
# )

human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)

# Start a chat with the agent with number with an initial guess.
result = human_proxy.initiate_chat(
    agent_with_number,  # this is the same agent with the number as before
    message="10",
)