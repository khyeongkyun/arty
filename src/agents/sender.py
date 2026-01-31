from state.schema import State

def sender(state: State):
    completed_report_sections = "\n\n---\n\n".join(
        state["completed_sections"]
    )
    return {"final_report": completed_report_sections}