# TicketFlow AI

A sanitized portfolio project inspired by a real operational problem: technicians had to repeatedly check a ticketing system for new work, then manually read and reorganize the relevant details.

The goal is not to reproduce any employer system or data. This repository uses **fabricated data only** and demonstrates the engineering ideas behind the workflow.

## Problem

Repeated manual checking creates more than a small time cost. It creates a continuous **monitoring burden**: someone has to remember to interrupt their real work just to see whether anything changed.

The design principle is therefore:

> **human pull -> system push**

Let software monitor deterministic state changes, then involve a person only when attention or judgement is needed.

## Target architecture

```text
Mock Ticket Source
        |
        v
Python Monitor / Extractor
        |
        v
State + Change Detection
        |
        v
HTTP Webhook
        |
        v
n8n Orchestration
        |
        +--> AI Structured Extraction
        +--> Schema Validation
        +--> Data / State Handling
        +--> Email / WhatsApp Notification
```

n8n is an intentional part of the architecture. Python is used where code ownership, parsing, testing and reliability are valuable; n8n is used where workflow orchestration, AI steps and connectors are a better fit.

## Build plan

### Phase 1 — regain code ownership
- hand-code ticket state comparison
- write and run unit tests
- explain every line without relying on an AI-generated implementation

### Phase 2 — HTTP and mock ticket source
- retrieve fabricated tickets over HTTP
- parse JSON
- persist local state
- detect changes between polling cycles

### Phase 3 — n8n integration
- POST detected changes to an n8n webhook
- structured AI extraction
- schema validation
- human notification

### Phase 4 — reliability
- retry / timeout handling
- logging
- duplicate-event protection
- safer closed-ticket semantics

### Phase 5 — production-style improvements
- database persistence
- Docker
- environment-based secrets/configuration
- CI tests
- architecture documentation

## Current status

**Phase 1 in progress.** See [`FIRST_TASK.md`](FIRST_TASK.md).

## Privacy and security

This repository must never contain real employer credentials, session cookies, internal URLs, customer information, ticket contents, confidential screenshots or system configuration. All examples must be fabricated or sanitized.

## Author

Ng Man Kit (Gary) — building this project as part of a transition from IT/AV systems work into Technical Solutions and Workflow / AI Automation engineering.
