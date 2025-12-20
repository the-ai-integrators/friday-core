# ⚙️ Friday Core

*Modular orchestration engine for enterprise-grade multi-agent AI
workflows*

<p align="left">
  <a href="https://github.com/theaiintegrators"><img src="https://img.shields.io/badge/Friday--Ecosystem-4B8BF5" /></a>
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/badge/python-3.9_3.10_3.11-blue" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" />
</p>

> **Note**  
> Friday is a personal open-source project built for learning and experimentation with multi-agent orchestration patterns.  
> It is not affiliated with any employer, customer, or commercial offering.

------------------------------------------------------------------------

## 🌟 Overview

**Friday Core** provides the foundation for constructing
**deterministic, evaluable, observable** multi-agent systems.

This open-core edition includes:

-   LangGraph-based example workflow
-   Simple agent abstractions
-   Deterministic state transitions
-   Clean orchestration
-   No private logic

------------------------------------------------------------------------

## 📘 Friday Core Architecture

![Friday Core Architecture](./docs/01-public-friday-core.png)

------------------------------------------------------------------------

## 🎥 Architecture Walkthrough (Video)

A short demo showcasing how **Friday Core** performs multi-agent orchestration
in a real enterprise-style interface (Microsoft Teams), including:

- Intent-based agent routing
- Deterministic state transitions
- Tool / MCP-based execution
- Execution-level observability via LangSmith

▶️ Watch: https://www.youtube.com/watch?v=ddowg61Qt80

> This video corresponds to **FRIDAY CORE EP01 — Core Orchestration**.

------------------------------------------------------------------------

## ✨ Features (Public Edition)

-   Lightweight LangGraph workflow
-   Example agents (`SearchAgent`, `MathAgent`)
-   Deterministic state updates
-   Extensible architecture
-   Demo runner

------------------------------------------------------------------------

## 🏛 Architecture

    User Input → SearchAgent → MathAgent → Final Output (state)

------------------------------------------------------------------------

## 📚 Repository Structure

    friday-core/
      ├── friday/
      │   ├── agents/
      │   ├── graphs/
      │   └── utils/
      ├── examples/
      ├── requirements.txt
      ├── LICENSE
      └── README.md

------------------------------------------------------------------------

## 🚀 Quick Start

``` bash
git clone https://github.com/theaiintegrators/friday-core
cd friday-core

python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows PowerShell

pip install -r requirements.txt
python -m examples.run_demo
```

------------------------------------------------------------------------

## 🧭 Roadmap

-   MCP tool integration
-   Parallel execution patterns
-   Workflow visualizer
-   LangFuse auto-enrichment
-   Built‑in safety evaluators
-   Friday CLI
-   Deployment templates

------------------------------------------------------------------------

## 🔭 Vision

Friday aims to make AI systems:

-   **Predictable**
-   **Testable**
-   **Observable**
-   **Enterprise-ready**

With a code-first, extensible design that scales from prototypes to full
production platforms.

------------------------------------------------------------------------

## 📄 License

MIT License
Copyright © 2025
The AI Integrators

------------------------------------------------------------------------

## 💬 Contact & Contributions

-   Open an Issue or Discussion
-   PRs welcome
-   https://github.com/theaiintegrators