# Created by yassin sanad

# 🤖 Secure Embodied AI Controller

A production-style AI Agent that safely controls a robotic arm using:
- 🧠 OpenAI LLM (GPT-4o-mini)
- 🛡️ Security Guardrails (Prompt Injection Protection)
- 🗂️ Vector Memory (Chroma DB)
- 🔧 ROS2 Simulation Interface
- 🌐 FastAPI Backend

---

## 🚀 Project Overview

This project demonstrates a secure autonomous AI agent capable of:

- Understanding natural language commands
- Executing robotic arm movements via ROS2 simulation
- Storing long-term memory using vector embeddings (Chroma)
- Preventing prompt injection and malicious commands
- Running as a public API service

---

## 🏗️ Architecture

User → FastAPI → Security Layer → AI Agent → Tool (ROS2 Sim) → Memory (Chroma) → Safe Response

---

## 🔐 Security Features

- Pattern-based prompt injection detection
- Query length protection (anti-DoS)
- Output sanitization (API key redaction)
- Controlled tool execution

---

## 🧠 AI Agent

Built using:
- LangChain AgentExecutor
- OpenAI Functions Agent
- Custom prompt template
- Tool-based execution system

---

## 🗂️ Memory System

- Vector-based long-term memory
- Powered by Chroma DB
- OpenAI Embeddings
- Persistent local storage

---

## 🛠️ Technologies Used

- Python
- FastAPI
- LangChain
- OpenAI API
- ChromaDB
- ROS2 (Simulated)
- Uvicorn

---
