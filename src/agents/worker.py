from langchain.messages import SystemMessage, HumanMessage
from llms.factory import get_llm
from state.schema import WorkerState

llm = get_llm(role="writer")

def researcher(state: WorkerState):
    section = llm.invoke(
        [
            SystemMessage(
                content="Write a report section following the provided name and description."
            ),
            HumanMessage(
                content=f"Section: {state['section'].name}\n{state['section'].description}"
            ),
        ]
    )
    return {"completed_sections": [section.content]}
