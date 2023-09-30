from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import openai
import json
import os


f = open(f'{os.path.dirname(os.getcwd())}/config.json')
config = json.load(f)

openai.api_key = config['api_keys']['openai_api_key']


# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample.json
#config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
assistant = AssistantAgent("assistant")#, llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(assistant, message=input('state input here'))