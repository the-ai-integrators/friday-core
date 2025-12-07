# 🤝 Contributing to Friday

Thank you for your interest in contributing to **Friday — the multi-agent framework for enterprise AI workflows**.

We welcome contributions of all types:

- Bug fixes  
- Documentation improvements  
- New evaluators or observability hooks  
- New examples  
- Architectural proposals  

This document explains how to contribute effectively.

---

## 🧱 Code of Conduct

By participating in this project, you agree to follow our future:

```
CODE_OF_CONDUCT.md
```

(This file will be added soon.)

---

## 🛠 Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/theaiintegrators/friday-core.git
cd friday-core
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt   # when available
```

---

## 🧪 Running Tests

Tests are located in the `tests/` directory.

Run all tests:

```bash
pytest
```

Verbose mode:

```bash
pytest -vv
```

---

## 🧩 Contribution Types

### 1. Bug Fixes
- Open an issue describing the bug  
- Include reproduction steps  
- Submit a PR with a fix  

### 2. New Agents / Evaluators / Observability Providers
- Follow existing abstraction interfaces  
- Include examples  
- Add tests when appropriate  
- Document new additions in README or docs  

### 3. Documentation
- Fix typos, clarify explanations  
- Expand conceptual sections  
- Add diagrams or architecture notes  

### 4. Feature Requests
Open an issue with:

- Motivation  
- Proposed API  
- Example usage  

---

## 🔀 Pull Request Process

### 1. Fork the repository  
### 2. Create a feature branch  

```bash
git checkout -b feature/my-new-feature
```

### 3. Commit your changes  

```bash
git commit -m "Add new evaluator: JSONSchemaEvaluator"
```

### 4. Push your branch  

```bash
git push origin feature/my-new-feature
```

### 5. Open a Pull Request  
Include:

- Description of changes  
- Link to related issue  
- Before/after examples if behavior changed  

---

## 📦 Coding Standards

### ✔ Type hints required  
All public APIs must use Python typing.

### ✔ Docstrings encouraged  
Document:

- Purpose  
- Parameters  
- Return values  
- Edge cases  

### ✔ Tests for core features  
Changes affecting core logic must include tests.

---

## 🌿 Release Process (future)

When publishing to PyPI:

- Bump version (SemVer)  
- Update CHANGELOG  
- Tag release  
- Publish  

---

## ❤️ Thank You

Every contribution makes Friday stronger.  
We are building an ecosystem for **reliable, enterprise-grade AI workflows** — your help accelerates that mission.
