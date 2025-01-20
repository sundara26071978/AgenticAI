from pathlib import Path

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")


config_list = [
    {
        # Let's choose the Mixtral 8x22B model
        "model": "open-mixtral-8x22b",
        # Provide your Mistral AI API key here or put it into the MISTRAL_API_KEY environment variable.
        "api_key": os.environ.get("MISTRAL_API_KEY"),
        # We specify the API Type as 'mistral' so it uses the Mistral AI client class
        "api_type": "mistral",
    }
]


#print(config_list)


from autogen import ConversableAgent

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=2)