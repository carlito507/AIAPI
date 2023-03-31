from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.utils.utils import get_variables, get_prompt, new_template, new_chain

import logging

logger = logging.getLogger(__name__)


class NewTemplateInput(BaseModel):
    template: str
    variables: list[str]


# Create a router
llm_chain_router = APIRouter()


# API endpoints
@llm_chain_router.get("/llm_chain")
async def get_llm_chain():
    print("Getting prompt...")
    prompt = get_prompt()
    print("Prompt: ", prompt)
    return {"prompt": prompt}, 200


@llm_chain_router.post("/llm_chain")
async def llm_chain(request: Request):
    data = await request.json()
    print(data)
    print(get_variables())
    print(get_prompt())
    response = new_chain()
    return {"response": response}, 200


@llm_chain_router.get("/llm_chain/new_template")
async def get_new_template():
    temp = """
    You are an expert in {bitch}.
    Your protocol:
    {protocol}
    {prompt}
    """
    variables = [
        "bitch",
        "protocol",
        "prompt"
    ]
    new_template(temp, variables)
    prompt = get_prompt()
    return {"prompt": prompt}, 200


@llm_chain_router.post("/llm_chain/new_template")
async def post_new_template(input_data: NewTemplateInput):
    new_template(input_data.template, input_data.variables)
    return {"status": "Template updated successfully"}, 200
