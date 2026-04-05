from fastapi import FastAPI
from pydantic import BaseModel
from app.agents import orchestrate
from app.security import sanitize_input
from app.evaluation import evaluate_response

import logging
import os

# Logging setup (App Insights compatible)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-underwriting")

app = FastAPI(title="AI Underwriting Platform")

# Request model
class Request(BaseModel):
    document_text: str


# Health check (for AKS readiness/liveness)
@app.get("/")
def health():
    logger.info("Health check called")
    return {"status": "ok"}


# Main API
@app.post("/underwrite")
def underwrite(req: Request):
    try:
        logger.info("Received underwriting request")

        # Step 1: Security validation
        clean_input = sanitize_input(req.document_text)

        # Step 2: Agent orchestration
        result = orchestrate(clean_input)

        # Step 3: AI evaluation
        evaluation = evaluate_response(result["risk_assessment"])

        logger.info("Underwriting completed successfully")

        return {
            "status": "success",
            "result": result,
            "evaluation": evaluation
        }

    except Exception as e:
        logger.error(f"Error during underwriting: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }