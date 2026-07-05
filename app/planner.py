from app.openai_client import llm
from app.planner_prompt import PLANNER_PROMPT
from app.state import AgentState


def planner(state: AgentState) -> AgentState:
    """
    Planner Node

    Generates a task list from the user's request.
    """

    prompt = PLANNER_PROMPT.format(request=state["request"])

    response = llm.generate(prompt)

    # Convert numbered list into Python list
    tasks = []

    for line in response.split("\n"):
        line = line.strip()

        if not line:
            continue

        # Remove numbering like:
        # 1.
        # 2)
        # -
        line = line.lstrip("0123456789.-) ").strip()

        if line:
            tasks.append(line)

    state["tasks"] = tasks

    return state