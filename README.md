# 🛡️ SafeSphere AI - Industrial Safety Intelligence Platform

## 🚀 Overview

SafeSphere AI is an AI-powered Industrial Safety Intelligence Platform designed to prevent workplace accidents before they occur. The platform combines IoT sensor data, SCADA systems, CCTV analytics, permit-to-work records, maintenance logs, worker tracking, and regulatory knowledge into a unified intelligence layer that detects compound risk conditions and recommends preventive actions in real time.

Unlike traditional monitoring systems that generate isolated alerts, SafeSphere AI correlates multiple risk factors simultaneously to identify hidden hazards that individual systems cannot detect on their own.

---

# 🎯 Problem Statement

Industrial facilities generate massive amounts of operational and safety data. However, these data streams often exist in silos, making it difficult to identify dangerous combinations of events before an incident occurs.

Examples include:

* Hot work activities near elevated gas concentrations
* Maintenance operations during abnormal process conditions
* Worker entry into hazardous zones without proper permits
* PPE violations in critical operational areas
* Simultaneous operations creating unforeseen risks

SafeSphere AI addresses these challenges through predictive intelligence, explainable AI, and automated safety orchestration.

---

# ✨ Key Features

## 🔥 Compound Risk Detection Engine

Detects dangerous combinations of:

* Gas accumulation
* Temperature anomalies
* Active permits
* Maintenance activities
* Worker density
* Equipment health status

Provides real-time risk scores and predictive alerts.

---

## 🗺️ Geospatial Safety Heatmap

Visualizes:

* Live risk zones
* Worker locations
* Hazardous areas
* Permit overlap regions
* Equipment health status

Provides plant-wide situational awareness.

---

## 🤖 AI Safety Copilot

Allows safety officers to ask questions such as:

> Why is Zone C marked high risk?

The AI provides explainable responses using:

* Sensor evidence
* Permit data
* Historical incidents
* Regulatory guidelines

---

## 📚 RAG-Powered Incident Intelligence

Retrieves insights from:

* OISD Standards
* Factory Act Guidelines
* DGMS Regulations
* Near-Miss Reports
* Historical Incident Records

Identifies recurring patterns and recommends preventive actions.

---

## 🎥 CCTV Safety Analytics

Computer Vision modules detect:

* Missing helmets
* Missing safety vests
* Restricted area violations
* Worker crowding
* Unsafe behavior
* Unauthorized access

---

## 📋 Digital Permit Intelligence

Analyzes permit activities against live plant conditions.

Examples:

* Hot Work + Gas Leak
* Confined Space Entry + Oxygen Deficiency
* Maintenance + Equipment Instability

Automatically flags unsafe permit combinations.

---

## 🚨 Emergency Response Orchestrator

On critical events:

* Generates alerts
* Notifies response teams
* Triggers evacuation workflows
* Preserves evidence
* Creates incident reports

Reducing response time during emergencies.

---

# 🏗️ System Architecture

```text
IoT Sensors
      │
      ▼
SCADA Systems
      │
      ▼
Permit Records
      │
      ▼
Maintenance Logs
      │
      ▼
CCTV Analytics
      │
      ▼
Data Fusion Layer
      │
      ▼
Knowledge Graph
      │
      ▼
Multi-Agent AI System
      │
      ▼
Risk Prediction Engine
      │
      ▼
Safety Dashboard
      │
      ▼
Emergency Response System
```

# 🧠 AI Agents

## Risk Agent

Evaluates:

* Environmental conditions
* Sensor anomalies
* Operational risks

## Permit Agent

Analyzes permit conflicts and simultaneous operations.

## Compliance Agent

Checks compliance against:

* OISD
* Factory Act
* DGMS Guidelines

## Emergency Agent

Coordinates incident response workflows.

## Incident Intelligence Agent

Performs historical incident analysis using RAG.

---

# 🛠️ Technology Stack

## Frontend

* Next.js
* TypeScript
* Tailwind CSS
* Mapbox
* Recharts

## Backend

* FastAPI
* Python
* PostgreSQL
* Redis

## Artificial Intelligence

* Gemini API
* LangGraph
* CrewAI

## Computer Vision

* YOLO
* OpenCV

## Knowledge Graph

* Neo4j

## RAG Pipeline

* ChromaDB
* Sentence Transformers

## Deployment

* Docker
* AWS

---

# 📂 Project Structure

```text
SafeSphereAI/
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── services/
│
├── backend/
│   ├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── database/
│
├── ai_agents/
│   ├── risk_agent.py
│   ├── permit_agent.py
│   ├── compliance_agent.py
│   └── emergency_agent.py
│
├── rag/
│   ├── vector_store/
│   ├── embeddings/
│   └── rag_pipeline.py
│
├── cv/
│   ├── ppe_detection.py
│   └── hazard_detection.py
│
├── knowledge_graph/
│   └── neo4j_schema.cypher
│
├── infra/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
│
└── docs/
```

# ⚡ Installation

## Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Docker

```bash
docker-compose up --build
```

# 🎬 Demo Scenario

1. Gas concentration begins rising.
2. Maintenance permit becomes active.
3. Worker enters affected zone.
4. AI detects compound hazard.
5. Risk score exceeds threshold.
6. Heatmap updates to critical status.
7. Emergency alerts are triggered.
8. AI generates explainable recommendations.
9. Safety officer takes preventive action.

Accident prevented before escalation.

# 📈 Future Enhancements

* Digital Twin Integration
* Drone-Based Safety Inspection
* Predictive Equipment Failure Detection
* AR-Based Worker Safety Guidance
* Multilingual Voice Safety Assistant
* Autonomous Incident Investigation

# 🏆 Impact

SafeSphere AI transforms industrial safety from reactive incident management to proactive accident prevention.

Our mission is simple:

**Predict Risks. Prevent Accidents. Protect Lives.**
