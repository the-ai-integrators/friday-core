# 🔐 Security Policy

## 1. Supported Versions
Security updates apply to the latest version of each Friday component:

| Component             | Status  |
|-----------------------|---------|
| friday-core           | Active  |
| friday-evaluation     | Active  |
| friday-observability  | Active  |

Older versions may not receive security fixes.

---

## 2. Reporting a Vulnerability
If you discover a security vulnerability, please report it **privately**:

```
theaiintegrators@gmail.com
```

We request that you:

- Do **not** open a public GitHub issue  
- Provide a clear description of the vulnerability  
- Include steps to reproduce (if possible)  
- Indicate potential impact  

We aim to acknowledge all reports within **72 hours**.

---

## 3. Responsible Disclosure
We follow responsible disclosure principles:

- We will investigate the issue promptly  
- We will work with you on a coordinated fix  
- We will credit you unless anonymity is requested  
- We will not pursue legal action for good‑faith reporting  

---

## 4. Security Best Practices for Contributors
When contributing to Friday components:

- Do not commit secrets or API keys  
- Use environment variables for credentials  
- Validate all external inputs  
- Follow Python best practices  
- Do not rely on LLM outputs for security‑critical routing  
- Avoid exposing sensitive data through logs or evaluators  

---

## 5. Scope
This policy covers all Friday repositories:

- friday-core  
- friday-evaluation  
- friday-observability  
- Documentation and examples  

It does **not** cover commercial deployments outside the open‑source codebase.

---

## 6. Data Handling Guidance
Friday does not store user data itself, but developers should:

- Mask sensitive values in logs and traces  
- Ensure observability providers comply with governance rules  
- Avoid sending PII to external APIs unless approved  

---

## 7. Contact
For any security concerns, please contact:

📧 **theaiintegrators@gmail.com**
