from pathlib import Path

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY1"]=os.getenv("GROQ_API_KEY1")

# os.environ['KMP_DUPLICATE_LIB_OK']='True'


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

import tempfile

import fitz  # PyMuPDF
import requests

from autogen.agentchat.contrib.capabilities.text_compressors import LLMLingua
from autogen.agentchat.contrib.capabilities.transforms import TextMessageCompressor

AUTOGEN_PAPER = "https://arxiv.org/pdf/2308.08155"


def extract_text_from_pdf():
    # Download the PDF
    response = requests.get(AUTOGEN_PAPER)
    response.raise_for_status()  # Ensure the download was successful

    text = ""
    # Save the PDF to a temporary file
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(temp_dir + "temp.pdf", "wb") as f:
            f.write(response.content)

        # Open the PDF
        with fitz.open(temp_dir + "temp.pdf") as doc:
            # Read and extract text from each page
            for page in doc:
                text += page.get_text()

    return text


# Example usage
pdf_text = extract_text_from_pdf()

llm_lingua = LLMLingua()
text_compressor = TextMessageCompressor(text_compressor=llm_lingua)
compressed_text = text_compressor.apply_transform([{"content": pdf_text}])

print(text_compressor.get_logs([], []))



import os

import autogen
from autogen.agentchat.contrib.capabilities import transform_messages

system_message = "You are a world class researcher."
#config_list = [{"model": "gpt-4-turbo", "api_key": os.getenv("OPENAI_API_KEY")}]

# Define your agent; the user proxy and an assistant
researcher = autogen.ConversableAgent(
    "assistant",
    llm_config={"config_list": config_list},
    max_consecutive_auto_reply=1,
    system_message=system_message,
    human_input_mode="NEVER",
)
user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
    max_consecutive_auto_reply=1,
)
context_handling = transform_messages.TransformMessages(transforms=[text_compressor])
context_handling.add_to_agent(researcher)

message = "Summarize this research paper for me, include the important information" + pdf_text
result = user_proxy.initiate_chat(recipient=researcher, clear_history=True, message=message, silent=True)

print(result.chat_history[1]["content"])