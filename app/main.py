from fastapi import FastAPI, HTTPException

from app.request import AgentRequest
from app.response import AgentResponse

from app.config import (
    APP_NAME,
    APP_VERSION,
    validate_config,
)

from app.workflow import workflow
from app.doc_generator import generate_doc


# Validate configuration at startup
validate_config()

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="AI Business Proposal Generator using LangGraph",
)


@app.get("/")
def health_check():
    return {
        "status": "success",
        "message": "API is running."
    }


@app.post("/agent", response_model=AgentResponse)
def run_agent(request: AgentRequest):

    try:

        state = {
            "request": request.request,
            "tasks": [],
            "proposal": "",
            "document": ""
        }

        # Execute LangGraph workflow
        state = workflow.invoke(state)

        # Generate Word document
        state = generate_doc(state)

        return AgentResponse(
            status="success",
            message="Business proposal generated successfully.",
            request=state["request"],
            tasks=state["tasks"],
            proposal=state["proposal"],
            document=state["document"],
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )