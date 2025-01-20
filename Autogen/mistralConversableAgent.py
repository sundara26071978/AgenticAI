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

agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": config_list},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)
reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)