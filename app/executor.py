from app.openai_client import llm
from app.proposal_prompt import PROPOSAL_PROMPT
from app.state import AgentState


def executor(state: AgentState) -> AgentState:
    """
    Executor Node

    Generates the complete business proposal
    using the user's request and planner tasks.
    """

    prompt = PROPOSAL_PROMPT.format(
        request=state["request"],
        tasks="\n".join(state["tasks"])
    )

    proposal = llm.generate(prompt)

    state["proposal"] = proposal

    return state