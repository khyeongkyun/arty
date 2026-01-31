from langchain.messages import SystemMessage, HumanMessage
from llms.factory import get_llm
from state.schema import State, Sections

llm = get_llm(role="planner")
planner = llm.with_structured_output(Sections)

def director(state: State):
    report_sections = planner.invoke(
        [
            SystemMessage(content="Generate a plan for the report."),
            HumanMessage(content=f"Here is the report topic: {state['topic']}"),
        ]
    )
    return {"sections": report_sections.sections}