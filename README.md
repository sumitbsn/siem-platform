# SIEM Platform — Security Event Simulation & Detection Pipeline

A modular SIEM-style security analytics platform built using Python, FastAPI, Redis Streams, OCSF normalization, and detection pipelines.

This project simulates how enterprise SIEM/XDR/MDR systems ingest, normalize, correlate, and detect suspicious security activity from multiple vendor-like event sources.

---

# Features

* Security event simulator API
* 10,000+ generated security events
* Vendor-style REST endpoints
* Rate-limited API polling
* Redis Streams integration
* OCSF normalization layer
* Stateless detections
* Stateful correlation detections
* Findings/alerts generation
* Modular microservice architecture

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
                │ Detection Engine    │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Findings / Alerts   │
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
│   ├── events.json
│
├── collector/
│   ├── collector.py
│   ├── raw_logs/
│
├── queue/
│   ├── redis_producer.py
│
├── parser/
│   ├── ocsf_mapper.py
│
├── detections/
│   ├── sigma_engine.py
│   ├── stateless.py
│   ├── stateful.py
│
├── findings/
│   ├── writer.py
│
├── pipeline/
│   ├── run_pipeline.py
│
├── alerts/
│   ├── findings.json
│
├── docker-compose.yml
├── requirements.txt
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
* Security Event Processing

---

# Event Categories

The simulator exposes multiple vendor-style endpoints.

| Endpoint        | Purpose             |
| --------------- | ------------------- |
| `/events`       | All events          |
| `/api/auth`     | Authentication logs |
| `/api/firewall` | Firewall logs       |
| `/api/edr`      | EDR/process logs    |
| `/api/cloud`    | Cloud/VPN logs      |

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

Verify installation:

```bash
python3 --version
```

---

## Install Redis

```bash
sudo apt install redis-server -y
```

Enable and start Redis:

```bash
sudo systemctl enable redis-server
sudo systemctl start redis-server
```

Verify Redis:

```bash
redis-cli ping
```

Expected output:

```text
PONG
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repo-url>
cd siem-platform
```

---

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

---

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

The homepage displays all available API endpoints.

---

## Step 3 — Run Collector

Open another terminal:

```bash
cd collector
python collector.py
```

Logs will be stored in:

```text
collector/raw_logs/
```

---

## Step 4 — Push Events to Redis Streams

```bash
cd queue
python redis_producer.py
```

Redis stream name:

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

# Detection Results

Alerts are written to:

```text
alerts/findings.json
```

Example alert:

```json
{
  "alert": "Possible Brute Force Attack",
  "source_ip": "10.1.1.5",
  "count": 5
}
```

---

# Detection Types

## Sigma Rules

YAML-based portable detections.

Example:

```yaml
title: Failed Login Detection

detection:
  keywords:
    - login_failed
```

---

## Stateless Detections

Single-event analysis.

Example:

```python
if event["risk_score"] > 80:
    alert()
```

---

## Stateful Detections

Correlation across multiple events.

Example:

```text
5 failed logins from same IP
```

---

# OCSF Mapping

The parser normalizes events into OCSF-like schema.

Example:

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

# Current Detection Examples

## Stateless

* High risk activity
* Suspicious VPN login

## Stateful

* Brute-force detection
* Port scan detection

---

# Future Improvements

* Kafka integration
* Elasticsearch indexing
* Kibana dashboards
* Real-time streaming detections
* MITRE ATT&CK mapping
* Threat intelligence enrichment
* UEBA analytics
* Async collectors
* Multi-tenant support
* Detection API dashboard

---

# Learning Objectives

This project demonstrates:

* SIEM architecture
* Security event pipelines
* Detection engineering
* Stateful correlation
* OCSF normalization
* Streaming security analytics
* API-based telemetry ingestion
* Redis-based event streaming

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
