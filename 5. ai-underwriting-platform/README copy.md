# 🧠 AI Underwriting Platform (GenAI + Agentic AI)

## 📌 Overview

This project demonstrates a **cloud-native AI underwriting platform** leveraging **Generative AI (RAG)** and **Agentic AI workflows** to automate insurance underwriting processes.

It simulates real-world enterprise use cases such as:

* Document ingestion (emails, PDFs)
* AI-based data extraction and validation
* Risk assessment and recommendation
* Workflow automation using AI agents

---

## 🏗️ Architecture Highlights

* **GenAI (LLM + RAG)** for document understanding and recommendations
* **Agentic AI** for autonomous workflow orchestration
* **API-first microservices architecture**
* **Cloud-ready deployment (Azure / AWS)**

---

## ⚙️ Key Features

✔ Multi-format document ingestion (PDF, email)
✔ AI-based underwriting data extraction
✔ RAG-based contextual decision making
✔ Risk scoring and policy recommendation
✔ Human-in-the-loop validation
✔ Secure prompt handling (basic guardrails)

---

## 🤖 AI Components

### GenAI (RAG)

* Embeddings + vector search
* Context-aware LLM responses

### Agentic AI

* Extraction Agent
* Validation Agent
* Enrichment Agent
* Risk Assessment Agent

---

## ☁️ Cloud & DevOps Ready

* Designed for Azure / AWS deployment
* Terraform-based infrastructure
* API-first integration

---

## 🚀 How to Run

```bash
git clone https://github.com/<your-username>/ai-underwriting-genai-agentic
cd ai-underwriting-genai-agentic

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📊 Sample API

POST `/underwrite`

```json
{
  "document_text": "Sample insurance policy document..."
}
```

---

## 🔐 Security Considerations

* Prompt injection detection (basic)
* Input sanitization
* Extendable for enterprise security (Zero Trust, RBAC, etc.)

---

## 📈 Future Enhancements

* Azure OpenAI / AWS Bedrock integration
* Production-grade vector DB (Azure AI Search)
* CI/CD pipelines (GitHub Actions)
* Kubernetes deployment (AKS/EKS)

---

## 👨‍💻 Author

Ashok R
Cloud & AI Solutions Architect
