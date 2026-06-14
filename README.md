# SIEM Platform — Security Event Simulation, Detection & AI-Powered Investigation Pipeline

A modular SIEM-style security analytics platform built using Python, FastAPI, Redis Streams, OCSF normalization, Sigma rules, stateful correlation, and local AI models.

This project simulates how enterprise SIEM/XDR/MDR platforms ingest, normalize, correlate, detect, investigate, and enrich suspicious security activity from multiple telemetry sources.

---

# Features

* Security Event Simulator API
* 100,000+ Generated Security Events
* Vendor-Style REST Endpoints
* Rate-Limited API Polling
* Redis Streams Integration
* OCSF Normalization Layer
* Sigma Rule Detection Engine
* Custom Detection Rules
* Stateless Detections
* Stateful Correlation Detections
* Findings / Alert Generation
* Incident Aggregation
* MITRE ATT&CK Mapping
* Executive Security Reporting
* Local LLM Integration (Ollama)
* GPT-OSS Support
* AI Incident Analysis
* AI Generated Sigma Rules
* Modular Microservice Architecture

---

# Architecture

```text
                ┌─────────────────────┐
                │ Event Generator     │
                │ Generate Events     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ FastAPI Simulator   │
                │ Vendor APIs         │
                └──────────┬──────────┘
                           │
                    REST Polling
                           │
                           ▼
                ┌─────────────────────┐
                │ Collector Service   │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Raw Log Storage     │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Redis Streams       │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ OCSF Mapper         │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Sigma Engine        │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Stateless Rules     │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Stateful Rules      │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Findings            │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Incident Builder    │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ MITRE Mapper        │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ AI Incident         │
                │ Analyzer            │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Executive Report    │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ AI Sigma Generator  │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Generated Rules     │
                └─────────────────────┘
```

---

# Project Structure

```text
siem-platform/
│
├── simulator/
│   ├── api.py
│   ├── generator.py
│   └── events.json
│
├── collector/
│   ├── collector.py
│   └── raw_logs/
│
├── queue/
│   └── redis_producer.py
│
├── parser/
│   └── ocsf_mapper.py
│
├── detections/
│   ├── sigma_engine.py
│   ├── stateless.py
│   ├── stateful.py
│   │
│   ├── sigma_rules/
│   ├── custom/
│   └── generated/
│
├── findings/
│   └── writer.py
│
├── pipeline/
│   └── run_pipeline.py
│
├── ai/
│   ├── __init__.py
│   ├── ollama_client.py
│   ├── incident_builder.py
│   ├── mitre_mapper.py
│   ├── ai_incident_analyzer.py
│   └── sigma_generator.py
│
├── alerts/
│   ├── findings.json
│   ├── incidents.json
│   ├── enriched_incidents.json
│   └── executive_report.json
│
├── docker-compose.yml
├── requirements.txt
├── LICENSE
└── README.md
```

---

# Technologies Used

* Python
* FastAPI
* Redis Streams
* OCSF
* REST APIs
* YAML
* Sigma Rules
* Stateful Correlation
* MITRE ATT&CK
* Ollama
* GPT-OSS
* Security Event Processing

---

# Event Categories

The simulator exposes multiple vendor-style endpoints.

| Endpoint        | Purpose             |
| --------------- | ------------------- |
| `/events`       | All events          |
| `/api/auth`     | Authentication logs |
| `/api/firewall` | Firewall logs       |
| `/api/edr`      | EDR / Process logs  |
| `/api/cloud`    | Cloud / VPN logs    |

---

# Sample Event

```json
{
  "event_id": "uuid",
  "timestamp": "2026-06-01T12:00:00",
  "event_type": "login_failed",
  "user": "admin",
  "source_ip": "10.1.1.10",
  "destination_ip": "172.16.1.20",
  "risk_score": 95,
  "country": "Germany"
}
```

---

# Linux Setup (Linux Mint / Ubuntu)

## Install Python

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

Verify:

```bash
python3 --version
```

---

## Install Redis

```bash
sudo apt install redis-server -y

sudo systemctl enable redis-server
sudo systemctl start redis-server
```

Verify:

```bash
redis-cli ping
```

Expected:

```text
PONG
```

---

# Local AI Setup (Optional)

## Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify:

```bash
ollama --version
```

---

## Start Ollama

```bash
ollama serve
```

---

## Pull GPT-OSS

```bash
ollama pull gpt-oss:20b
```

Alternative models:

```bash
ollama pull qwen3:8b
ollama pull llama3.1:8b
ollama pull gemma3:12b
```

Verify:

```bash
ollama list
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/sumitbsn/siem-platform.git
cd siem-platform
```

## 2. Create Virtual Environment

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the SIEM Platform

## Step 1 — Generate Events

```bash
cd simulator
python generator.py
```

---

## Step 2 — Start Simulator API

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

Open:

```text
http://localhost:8000/
```

---

## Step 3 — Run Collector

```bash
cd collector
python collector.py
```

Logs stored in:

```text
collector/raw_logs/
```

---

## Step 4 — Push Events to Redis Streams

```bash
cd queue
python redis_producer.py
```

Redis stream:

```text
security_events
```

---

## Step 5 — Run Detection Pipeline

From project root:

```bash
python -m pipeline.run_pipeline
```

---

# Optional AI Commands

## Build Incidents

```bash
python -m ai.incident_builder
```

Output:

```text
alerts/incidents.json
```

---

## AI Incident Analysis

```bash
python -m ai.ai_incident_analyzer
```

Output:

```text
alerts/executive_report.json
```

---

## Generate Sigma Rules

```bash
python -m ai.sigma_generator
```

Output:

```text
detections/generated/generated_sigma_rules.yml
```

---

# Full End-to-End Execution

```bash
python -m pipeline.run_pipeline
```

Performs:

1. OCSF Normalization
2. Sigma Detection
3. Stateless Detection
4. Stateful Detection
5. Findings Generation
6. Incident Building
7. MITRE Mapping
8. AI Incident Analysis
9. Executive Report Generation
10. AI Sigma Rule Generation

---

# Detection Results

Primary outputs:

```text
alerts/findings.json
alerts/incidents.json
alerts/enriched_incidents.json
alerts/executive_report.json
detections/generated/generated_sigma_rules.yml
```

---

# Detection Engine

## Community Sigma Rules

```text
detections/sigma_rules/
```

## Organization Custom Rules

```text
detections/custom/
```

## AI Generated Rules

```text
detections/generated/
```

Generated rules should be reviewed before production use.

---

# Detection Types

## Sigma Rules

```yaml
title: Failed Login Detection

detection:
  keywords:
    - login_failed
```

## Stateless Detections

```python
if event["risk_score"] > 80:
    alert()
```

## Stateful Detections

```text
5 failed logins from same IP
```

---

# OCSF Mapping

```json
{
  "class_uid": 1001,
  "category_name": "Security",
  "activity_name": "login_failed",
  "src_endpoint": {
    "ip": "10.1.1.1"
  },
  "dst_endpoint": {
    "ip": "172.16.1.1"
  },
  "user": {
    "name": "admin"
  },
  "severity_id": 80
}
```

---

# AI Investigation Pipeline

```text
findings.json
      ↓
incident_builder.py
      ↓
incidents.json
      ↓
mitre_mapper.py
      ↓
enriched_incidents.json
      ↓
ai_incident_analyzer.py
      ↓
executive_report.json
      ↓
sigma_generator.py
      ↓
generated_sigma_rules.yml
```

---

# Current Detection Examples

## Stateless

* High Risk Activity
* Suspicious VPN Login

## Stateful

* Brute Force Detection
* Port Scan Detection

---

# Learning Objectives

This project demonstrates:

* SIEM Architecture
* Security Event Pipelines
* Detection Engineering
* Sigma Rule Development
* Stateful Correlation
* OCSF Normalization
* MITRE ATT&CK Mapping
* AI-Powered Security Analysis
* Local LLM Integration
* Streaming Security Analytics
* API-Based Telemetry Ingestion
* Redis-Based Event Streaming

---

# Inspired By

Enterprise SIEM/XDR/MDR platforms such as:

* Splunk
* Elastic Security
* Microsoft Sentinel
* CrowdStrike Falcon
* Arctic Wolf
* Google Chronicle

---

# License

MIT License
