from app.rag import retrieve_context, generate_response

def extraction_agent(document):
    return generate_response(f"Extract underwriting data: {document}")

def validation_agent(data):
    return generate_response(f"Validate data: {data}")

def enrichment_agent(document):
    return retrieve_context(document)

def risk_agent(data, context):
    prompt = f"""
    DATA: {data}
    CONTEXT: {context}

    Provide risk score and recommendation.
    """
    return generate_response(prompt)

def orchestrate(document):
    extracted = extraction_agent(document)
    validation = validation_agent(extracted)
    context = enrichment_agent(document)
    risk = risk_agent(extracted, context)

    return {
        "extracted": extracted,
        "validation": validation,
        "risk_assessment": risk
    }