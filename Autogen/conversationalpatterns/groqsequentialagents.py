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

# The Number Agent always returns the same numbers.
number_agent = ConversableAgent(
    name="Number_Agent",
    system_message="You return me the numbers I give you, one number each line.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",
)

# The Adder Agent adds 1 to each number it receives.
adder_agent = ConversableAgent(
    name="Adder_Agent",
    system_message="You add 1 to each number I give you and return me the new numbers, one number each line.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",
)

# The Multiplier Agent multiplies each number it receives by 2.
multiplier_agent = ConversableAgent(
    name="Multiplier_Agent",
    system_message="You multiply each number I give you by 2 and return me the new numbers, one number each line.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",
)

# The Subtracter Agent subtracts 1 from each number it receives.
subtracter_agent = ConversableAgent(
    name="Subtracter_Agent",
    system_message="You subtract 1 from each number I give you and return me the new numbers, one number each line.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",
)

# The Divider Agent divides each number it receives by 2.
divider_agent = ConversableAgent(
    name="Divider_Agent",
    system_message="You divide each number I give you by 2 and return me the new numbers, one number each line.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",
)

# Start a sequence of two-agent chats.
# Each element in the list is a dictionary that specifies the arguments
# for the initiate_chat method.
chat_results = number_agent.initiate_chats(
    [
        {
            "recipient": adder_agent,
            "message": "14",
            "max_turns": 1,
            "summary_method": "last_msg",
        },
        {
            "recipient": multiplier_agent,
            "message": "These are my numbers",
            "max_turns": 1,
            "summary_method": "last_msg",
        },
        {
            "recipient": subtracter_agent,
            "message": "These are my numbers",
            "max_turns": 1,
            "summary_method": "last_msg",
        },
        {
            "recipient": divider_agent,
            "message": "These are my numbers",
            "max_turns": 1,
            "summary_method": "last_msg",
        },
    ]
)