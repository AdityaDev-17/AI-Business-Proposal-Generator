from typing import TypedDict, List


class AgentState(TypedDict):
    # User input
    request: str

    # Planner output
    tasks: List[str]

    # Executor output
    proposal: str

    # Generated document path
    document: str