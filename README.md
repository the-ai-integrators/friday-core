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