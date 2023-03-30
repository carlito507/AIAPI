import pytest
from utils import (
    new_template,
    new_chain,
    get_prompt,
    get_variables,
    validate_key,
    api_key,
    PromptTemplate,
    OpenAI,
    LLMChain,
)


pytest.main()


def test_prompt_template_init():
    template = "Test template: {variable}"
    input_variables = ["variable"]
    prompt = PromptTemplate(template=template, input_variables=input_variables)

    assert prompt.template == template
    assert prompt.input_variables == input_variables


def test_openai_init():
    llm = OpenAI()
    assert llm is not None


def test_llmchain_init():
    template = "Test template: {variable}"
    input_variables = ["variable"]
    prompt = PromptTemplate(template=template, input_variables=input_variables)
    llm = OpenAI()
    chain = LLMChain(llm=llm, prompt=prompt)

    assert chain.llm == llm
    assert chain.prompt == prompt


def test_new_template():
    new_template("New template: {new_var}", ["new_var"])

    prompt = get_prompt()
    variables = get_variables()

    assert prompt.template == "New template: {new_var}"
    assert variables == ["new_var"]


def test_new_chain():
    new_chain()

    # You may need to adjust this part according to the actual behavior and requirements
    assert isinstance(get_prompt(), PromptTemplate)


def test_validate_key():
    assert validate_key(api_key) is True
    assert validate_key("invalid_key") is False