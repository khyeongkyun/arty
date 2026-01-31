from langchain_openai import ChatOpenAI
from llms.config import CONFIG

def get_llm(role: str):

    if role == "planner":
        return ChatOpenAI(
            model="gpt-4o",
            api_key=CONFIG["openai"]["api_key"],
            base_url=CONFIG["openai"]["base_url"],
            temperature=0
        )

    if role == "writer":
        return ChatOpenAI(
            model="gpt-4o-mini",
            api_key=CONFIG["openai"]["api_key"],
            base_url=CONFIG["openai"]["base_url"],
            temperature=0
        )