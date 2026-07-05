from app.workflow import workflow
from app.doc_generator import generate_doc

state = {
    "request": "Create a proposal for an AI Resume Screening System.",
    "tasks": [],
    "proposal": "",
    "document": ""
}

# Run LangGraph
state = workflow.invoke(state)

# Generate Word document
state = generate_doc(state)

print("\n========== TASKS ==========\n")
for task in state["tasks"]:
    print("-", task)

print("\n========== DOCUMENT ==========\n")
print(state["document"])