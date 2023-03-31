from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from app.core.config import api_key


template = """
You are an expert in {domain}.
Your protocol:
{protocol}
{prompt}
"""

input_variables = [
    "domain",
    "protocol",
    "prompt"
]


llm = OpenAI()
prompt = PromptTemplate(template=template, input_variables=input_variables)
chain = LLMChain(llm=llm, prompt=prompt)


def new_template(temp, variables):
    global prompt
    global template
    global input_variables
    global chain
    print("Updating template...")
    print("Template: ", temp)
    print("Variables: ", variables)
    template = temp
    input_variables = variables
    prompt = PromptTemplate(template=temp, input_variables=variables)
    chain = LLMChain(llm=llm, prompt=prompt)


def get_prompt():
    return prompt


def get_variables():
    return input_variables


def new_chain():
    global chain
    global prompt
    global llm
    chain = LLMChain(llm=llm, prompt=prompt)


def validate_key(x_api_key: str) -> bool:
    return x_api_key == api_key