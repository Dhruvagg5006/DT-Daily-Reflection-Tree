# 🌳 DT Fellowship Assignment — Daily Reflection Tree

## 👤 Candidate: Dhruv Aggarwal

**Role Applied:** Business Analyst / Data Scientist (Knowledge Engineer)

---

## 🧠 Overview

This project implements a **deterministic reflection system** that guides an employee through a structured end-of-day conversation.

Unlike traditional AI chatbots, this system:

* ❌ Does NOT use any LLM at runtime
* ✅ Produces **fully deterministic outputs**
* ✅ Encodes psychological frameworks into a **navigable decision tree**

The goal is to transform **human reflection (subjective)** into a **structured, auditable process (objective)**.

---

## 🎯 Core Idea

> The tree is the product. AI is only a tool used during development.

This system behaves like a **"choose-your-path" reflection engine**:

* Each question has fixed options
* Each option leads to a predefined path
* Same inputs → same outputs every time

---

## 🔍 Psychological Framework

The tree is built on three sequential axes:

### 1️⃣ Locus (Victim → Victor)

* Measures **perceived control**
* Internal vs External locus of control

### 2️⃣ Orientation (Entitlement → Contribution)

* Measures **value mindset**
* What I *gave* vs what I *deserve*

### 3️⃣ Radius (Self → Others)

* Measures **scope of concern**
* Self-centric vs team/customer-centric thinking

These axes are **connected and progressive**, forming a natural reflection flow.

---

## 🏗️ System Design

### 📌 Deterministic Tree Structure

* Nodes represent conversation steps
* Each node has:

  * `type` (question, decision, reflection, etc.)
  * `options` (fixed choices)
  * `target` (next node)
  * `signal` (state update)

---

### 🔁 Node Types

| Type         | Purpose                  |
| ------------ | ------------------------ |
| `start`      | Begin session            |
| `question`   | User selects option      |
| `decision`   | Internal branching logic |
| `reflection` | Insight / reframe        |
| `bridge`     | Axis transition          |
| `summary`    | Final synthesis          |
| `end`        | Close session            |

---

### 📊 State Management (Signals)

The system tracks behavior using simple counters:

```json
axis1: internal vs external  
axis2: contribution vs entitlement  
axis3: wide vs narrow
```

These signals determine:

* Branching decisions
* Final summary output

---

### 🔤 Personalization (Without AI)

The system uses **string interpolation**:

```
"You said '{A1_Q1.answer}'..."
```

This creates a personalized experience **without using LLMs**.

---

## 📁 Project Structure

```
DT-Daily-Reflection-Tree/
│
├── tree/
│   ├── reflection-tree.json
│   └── tree-diagram.md
│
├── agent/ (optional)
│   └── main.py
│
├── transcripts/
│   ├── persona1.md
│   └── persona2.md
│
├── write-up.md
├── README.md
```

---

## 🧪 Sample Execution Paths

### 👤 Persona 1

* External locus
* Entitlement mindset
* Self-centric

➡️ Reflection emphasizes awareness of agency and contribution gaps

---

### 👤 Persona 2

* Internal locus
* Contribution mindset
* Altrocentric

➡️ Reflection reinforces ownership and outward impact

---

## ⚙️ Optional Agent (CLI)

A simple CLI agent (Python) can:

* Load the JSON tree
* Traverse nodes
* Capture user inputs
* Track signals
* Generate final summary

No APIs. No randomness. Fully deterministic.

---

## 🚫 Guardrails Against AI Hallucination

* No AI calls in runtime system
* All logic explicitly defined in JSON
* Psychological concepts verified manually
* Reflection text is static (no generation)

AI was used only for:

* Brainstorming questions
* Refining tone
* Validating clarity

---

## 💡 Design Decisions

* Limited options (3–4 per question) → reduces fatigue
* Non-moralizing tone → "wise colleague", not judge
* Axis sequencing → builds cognitive progression
* Signal-based branching → simple yet powerful

---

## 🚀 Future Improvements

* Add deeper branching for edge cases
* Introduce scoring visualization dashboard
* Build web UI for better user experience
* Expand psychological depth (e.g., habits, feedback loops)

---

## 🧾 How to Run (Optional Agent)

```bash
python agent/main.py
```

---

## 🎤 Submission Includes

* ✅ Reflection Tree (JSON)
* ✅ Tree Diagram (Mermaid)
* ✅ Write-up
* ✅ Transcripts (2 personas)
* 🎤 Voice Note (shared separately)

---

## 🏁 Final Thought

This project demonstrates how **human psychology can be encoded into deterministic systems** — enabling consistent, scalable reflection without relying on AI at runtime.

> The challenge is not building software — it is structuring thought.

---
"# DT-Daily-Reflection-Tree" 
