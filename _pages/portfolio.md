---
permalink: /portfolio/
title: "AI Engineering Portfolio"
author_profile: true
---

# AI Engineering & Human-Centered AI Portfolio

I build research prototypes and engineering systems at the intersection of **Human-AI Interaction, Machine Learning, LLM Systems, Data Engineering, and Agentic Workflows**.

My research background is in human-AI interaction and quantitative evaluation. This portfolio documents the engineering side of that work: turning research questions into runnable systems, APIs, pipelines, tests, and reproducible demos.

---

## 1. ReflectAI
### Adaptive reflection for Human-LLM collaboration

**Focus:** HCI · Human-Centered AI · LLM integration · adaptive interfaces · experiment logging

ReflectAI is an interactive research prototype for studying whether an interface can detect possible over-reliance on LLM output and introduce reflection without taking agency away from the user.

**Engineering highlights**
- Streamlit application with three experimental conditions: Baseline, Static Reflection, and Adaptive Reflection
- OpenAI-compatible LLM adapter with local fallback
- transparent reliance-risk logic using response latency, revision behavior, and user action
- adaptive reflection trigger
- structured interaction logging and condition-level dashboard
- unit tests and GitHub Actions CI
- browser-based live demo

[Live Demo](https://lujiehuang.github.io/ReflectAI/) · [GitHub](https://github.com/lujiehuang/ReflectAI)

---

## 2. RelianceML
### Behavioral over-reliance prediction pipeline

**Focus:** Machine Learning · feature engineering · model evaluation · FastAPI

RelianceML extends the ReflectAI idea from a hand-crafted heuristic toward a trainable prediction pipeline.

**Engineering highlights**
- reproducible synthetic interaction-data generator for controlled prototyping
- feature engineering from behavioral traces
- Logistic Regression and Random Forest baselines
- ROC-AUC, F1, precision, recall, and accuracy evaluation
- serialized model artifacts
- typed FastAPI inference endpoint
- CI pipeline covering training and API smoke tests

The current dataset is explicitly synthetic and is used only to demonstrate the engineering workflow; it is not presented as empirical evidence about human behavior.

[GitHub](https://github.com/lujiehuang/RelianceML)

---

## 3. ScholarFlow
### Literature ETL, semantic retrieval, and RAG pipeline

**Focus:** Data Engineering · ETL · SQLite · semantic search · RAG · APIs

ScholarFlow demonstrates an end-to-end scholarly-data workflow from normalized literature records to semantic retrieval and RAG-ready context generation.

**Engineering highlights**
- schema normalization and deterministic deduplication
- SQLite persistence layer
- local semantic retrieval backend
- RAG context builder
- FastAPI search service
- modular separation of ingestion, storage, retrieval, and serving
- unit tests and CI-ready structure

[GitHub](https://github.com/lujiehuang/ScholarFlow)

---

## 4. AgentLab
### Tool-using research agent with retry and state management

**Focus:** LLM agents · tool calling · workflow orchestration · reliability · observability

AgentLab is a deterministic research-agent prototype designed to make orchestration logic inspectable and testable.

**Engineering highlights**
- explicit PLAN / ACT / OBSERVE / RETRY / DONE state model
- tool registry and structured tool calls
- transient-failure injection and automatic retry
- structured step logs
- reproducible offline tool layer
- FastAPI serving
- unit tests and CI smoke testing

[GitHub](https://github.com/lujiehuang/AgentLab)

---

## Engineering capability map

| Capability | Evidence |
|---|---|
| Human-centered interactive systems | ReflectAI |
| LLM integration and adaptive behavior | ReflectAI |
| ML training and evaluation | RelianceML |
| Prediction API design | RelianceML |
| ETL and persistent storage | ScholarFlow |
| Semantic retrieval and RAG context construction | ScholarFlow |
| Tool calling and state management | AgentLab |
| Retry and failure recovery | AgentLab |
| Testing and CI | All four projects |

---

## Technical stack

**Languages & analysis:** Python, SQL, quantitative research workflows  
**ML & data:** pandas, scikit-learn, feature engineering, model evaluation, SQLite  
**AI systems:** LLM APIs, semantic retrieval, RAG pipelines, tool-using agents  
**Applications & APIs:** Streamlit, FastAPI  
**Engineering practice:** modular architecture, structured logging, unit testing, CI, reproducible workflows  
**Research evaluation:** controlled experimental design, behavioral logging, SEM, fsQCA, NCA

---

## Research direction

I am particularly interested in building and evaluating AI systems that support **calibrated reliance, user control, reflective interaction, trustworthy human-AI collaboration, and adaptive intervention**.

My longer-term goal is to connect technical system design with rigorous user evaluation: not only asking whether an AI system works, but also **how people rely on it, when intervention is useful, and how interfaces can preserve human agency**.
