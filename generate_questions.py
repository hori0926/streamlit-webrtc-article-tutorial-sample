from langchain.chat_models import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from typing import List
import json
import streamlit as st


def generate_questions(recruitInfo, n_query):
    instruction = f"You are a recruitment interviewer. Generate {n_query} questions which are likely to be asked in the interview at the following company. Please note that questions should be unique to the company:Please display only questions in a bullet point format."

    template = instruction + "\n#company:\n{company}\n"
    prompt = PromptTemplate(
        template=template,
        input_variables=["company"],
    ).format_prompt(company=json.dumps(recruitInfo))
    llm = OpenAI(temperature=1)
    output = llm(prompt.to_string())
    return output