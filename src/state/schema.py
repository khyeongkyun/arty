# src/state/schema.py
from typing import Annotated, TypedDict, List
from pydantic import BaseModel, Field
import operator

class Section(BaseModel):
    name: str = Field(
        description="Name for this section of the report."
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section."
    )

class Sections(BaseModel):
    sections: List[Section] = Field(
        description="Sections of the report."
    )

class State(TypedDict):
    topic: str
    sections: List[Section]
    completed_sections: Annotated[List[str], operator.add]
    final_report: str

class WorkerState(TypedDict):
    section: Section
    completed_sections: Annotated[List[str], operator.add]