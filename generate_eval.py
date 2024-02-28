from langchain.chat_models import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from typing import List
import json
import streamlit as st


def generate_eval(recruitInfo: dict):
    template = """You are a recruitment interviewer. Generate 3 evaluation criteria which are the most important in the following company.:
    {company}
    #examples;
    Clarity: Whether the opinion is expressed concisely,
    Comprehension: Am I understanding the intent of the question correctly?
    """
    prompt = PromptTemplate(
        template=template,
        input_variables=["company"],
    ).format_prompt(company=json.dumps(recruitInfo))
    llm = OpenAI(temperature=1)
    output = llm(prompt.to_string())
    return output