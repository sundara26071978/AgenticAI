# %% [markdown]
# # Lesson 3: Reflection and Blogpost Writing

# %% [markdown]
# ## Setup

# %%
from pathlib import Path

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY1"]=os.getenv("GROQ_API_KEY1")


config_list = [
    {
        # Let's choose the Mixtral 8x22B model
        #"model": "llama3-8b-8192",
        "model": "llama-3.3-70b-versatile",
        #"model": "deepseek-r1-distill-llama-70b",
        # Provide your Mistral AI API key here or put it into the MISTRAL_API_KEY environment variable.
        "api_key": os.environ.get("GROQ_API_KEY1"),
        # We specify the API Type as 'mistral' so it uses the Mistral AI client class
        "api_type": "groq",
    }
]

llm_config={"config_list": config_list}
print(llm_config)

# %% [markdown]
# ## The task!

# %%
task = '''
        Write a concise but engaging blogpost about
       DeepLearning.AI. Make sure the blogpost is
       within 100 words.
       '''


# %% [markdown]
# ## Create a writer agent

# %%
import autogen

writer = autogen.AssistantAgent(
    name="Writer",
    system_message="You are a writer. You write engaging and concise " 
        "blogpost (with title) on given topics. You must polish your "
        "writing based on the feedback you receive and give a refined "
        "version. Only return your final work without additional comments.",
    llm_config=llm_config,
)

# %%
reply = writer.generate_reply(messages=[{"content": task, "role": "user"}])
from pprint import pprint
pprint(reply)


# %% [markdown]
# ## Adding reflection 
# 
# Create a critic agent to reflect on the work of the writer agent.

# %%
critic = autogen.AssistantAgent(
    name="Critic",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    llm_config=llm_config,
    system_message="You are a critic. You review the work of "
                "the writer and provide constructive "
                "feedback to help improve the quality of the content.",
)

# %%
res = critic.initiate_chat(
    recipient=writer,
    message=task,
    max_turns=2,
    summary_method="last_msg"
)

# %% [markdown]
# ## Nested chat

# %%
SEO_reviewer = autogen.AssistantAgent(
    name="SEO Reviewer",
    llm_config=llm_config,
    system_message="You are an SEO reviewer, known for "
        "your ability to optimize content for search engines, "
        "ensuring that it ranks well and attracts organic traffic. " 
        "Make sure your suggestion is concise (within 3 bullet points), "
        "concrete and to the point. "
        "Begin the review by stating your role.",
)


# %%
legal_reviewer = autogen.AssistantAgent(
    name="Legal Reviewer",
    llm_config=llm_config,
    system_message="You are a legal reviewer, known for "
        "your ability to ensure that content is legally compliant "
        "and free from any potential legal issues. "
        "Make sure your suggestion is concise (within 3 bullet points), "
        "concrete and to the point. "
        "Begin the review by stating your role.",
)

# %%
ethics_reviewer = autogen.AssistantAgent(
    name="Ethics Reviewer",
    llm_config=llm_config,
    system_message="You are an ethics reviewer, known for "
        "your ability to ensure that content is ethically sound "
        "and free from any potential ethical issues. " 
        "Make sure your suggestion is concise (within 3 bullet points), "
        "concrete and to the point. "
        "Begin the review by stating your role. ",
)

# %%
meta_reviewer = autogen.AssistantAgent(
    name="Meta Reviewer",
    llm_config=llm_config,
    system_message="You are a meta reviewer, you aggragate and review "
    "the work of other reviewers and give a final suggestion on the content.",
)

# %% [markdown]
# ## Orchestrate the nested chats to solve the task

# %%
def reflection_message(recipient, messages, sender, config):
    return f'''Review the following content. 
            \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}'''

review_chats = [
    {
     "recipient": SEO_reviewer, 
     "message": reflection_message, 
     "summary_method": "reflection_with_llm",
     "summary_args": {"summary_prompt" : 
        "Return review into as JSON object only:"
        "{'Reviewer': '', 'Review': ''}. Here Reviewer should be your role",},
     "max_turns": 1},
    {
    "recipient": legal_reviewer, "message": reflection_message, 
     "summary_method": "reflection_with_llm",
     "summary_args": {"summary_prompt" : 
        "Return review into as JSON object only:"
        "{'Reviewer': '', 'Review': ''}.",},
     "max_turns": 1},
    {"recipient": ethics_reviewer, "message": reflection_message, 
     "summary_method": "reflection_with_llm",
     "summary_args": {"summary_prompt" : 
        "Return review into as JSON object only:"
        "{'reviewer': '', 'review': ''}",},
     "max_turns": 1},
     {"recipient": meta_reviewer, 
      "message": "Aggregrate feedback from all reviewers and give final suggestions on the writing.", 
     "max_turns": 1},
]


# %%
critic.register_nested_chats(
    review_chats,
    trigger=writer,
)

# %% [markdown]
# **Note**: You might get a slightly different response than what's shown in the video. Feel free to try different task.

# %%
res = critic.initiate_chat(
    recipient=writer,
    message=task,
    max_turns=2,
    summary_method="last_msg"
)

# %% [markdown]
# ## Get the summary

# %%
print(res.summary)


