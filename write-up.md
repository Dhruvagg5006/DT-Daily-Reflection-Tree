# 🧾 Write-up — Daily Reflection Tree Design

## 👤 Candidate: Dhruv Aggarwal

---

##  1. Design Approach

I approached this assignment as a **knowledge engineering problem**, not a chatbot design task.

The core challenge was to convert **abstract psychological frameworks** into a **deterministic, structured decision tree** that a user can navigate without ambiguity. The goal was to design a system where:

* Every input leads to a predictable output
* Every reflection is pre-encoded (not generated)
* The experience feels like a **guided conversation**, not a survey

I focused on making the tree:

* **Deterministic** → no randomness or AI dependency
* **Traceable** → every path can be followed in the data
* **Psychologically meaningful** → grounded in real behavioral patterns

---

##  2. Psychological Foundations

The design is based on three core psychological axes:

### Axis 1: Locus (Victim → Victor)

Based on **Locus of Control (Julian Rotter)** and **Growth Mindset (Carol Dweck)**.

* Internal locus: “I influence outcomes”
* External locus: “Outcomes happen to me”

The questions were designed to surface **perceived agency**, especially in difficult situations.
Instead of blaming the user, reflections gently highlight moments of **choice and control**.

---

### Axis 2: Orientation (Entitlement → Contribution)

Based on **Psychological Entitlement** and **Organizational Citizenship Behavior**.

* Contribution: Focus on effort, helping, value creation
* Entitlement: Focus on recognition, expectations, fairness

The challenge here was that entitlement is often **invisible to the individual**.
So I designed options that make this visible without sounding accusatory.

---

### Axis 3: Radius (Self → Others)

Based on **Self-Transcendence (Maslow)** and **Perspective-Taking**.

* Narrow radius: Self-focused thinking
* Wide radius: Team, colleague, or customer awareness

This axis expands the user's perspective from “me” to “we”, helping contextualize their experience within a larger system.

---

##  3. Tree Structure & Flow

The tree follows a strict sequence:

**Axis 1 → Axis 2 → Axis 3**

This ordering is intentional:

* Agency (Axis 1) is foundational
* Contribution (Axis 2) builds on agency
* Perspective (Axis 3) expands contribution

Each axis contains:

* 3 question nodes
* 1 decision node
* 1 reflection node

Bridge nodes connect the axes to maintain conversational flow.

---

##  4. Branching Logic Design

Branching is handled using **decision nodes** based on accumulated signals.

Example:

* If `axis1.internal > axis1.external` → internal reflection
* Else → external reflection

This allows the system to:

* Adapt to user patterns
* Remain fully deterministic
* Avoid complex scoring models

Each option contributes a **signal** such as:

* `axis1:internal`
* `axis2:contribution`
* `axis3:wide`

These signals are tallied and used for both:

* Branching decisions
* Final summary generation

---

##  5. Question Design Strategy

I spent the majority of time refining questions and options.

Key principles:

* **Clarity over cleverness** → easy to answer when tired
* **Mutually exclusive options** → avoid confusion
* **Realistic language** → reflect actual workplace thoughts
* **Balanced framing** → no “obviously correct” answer

Each question was tested mentally against different personas to ensure:

* It captures a meaningful distinction
* It doesn’t feel like a test or evaluation

---

##  6. Reflection Design

Reflections are designed to:

* Reframe behavior, not judge it
* Encourage awareness, not guilt
* Sound like a **thoughtful colleague**, not a manager

For example:

* Instead of saying “You lacked ownership”
* I wrote: “There were moments shaped by external factors… but you still made choices.”

This maintains psychological safety while still guiding insight.

---

##  7. Trade-offs

### Simplicity vs Depth

I limited:

* Questions to 3 per axis
* Options to 3–4 per question

This reduces cognitive load but limits depth.

---

### Determinism vs Personalization

Without LLMs:

* Personalization is limited to interpolation
* But ensures consistency and auditability

---

### Breadth vs Completeness

The tree captures key behaviors but does not:

* Handle all edge cases
* Adapt dynamically beyond predefined paths

---

##  8. Use of AI (and Guardrails)

AI tools were used as:

* A **brainstorming assistant**
* A **language refinement tool**
* A **simulation partner** for testing personas

However, I ensured:

* No AI-generated content was used without review
* Psychological concepts were cross-checked
* Final structure and logic were **manually designed**

### Guardrails applied:

* No runtime AI usage
* No free-text interpretation
* All outputs predefined in the tree

---

##  9. What I Would Improve

With more time, I would:

* Add deeper branching within each axis
* Introduce multi-day tracking of behavior patterns
* Build a web interface for improved usability
* Expand reflections with more nuanced scenarios

---

##  10. Conclusion

This project demonstrates how **human reflection can be encoded into a deterministic system**.

The key insight is that:

> Structure can guide self-awareness without relying on AI.

Designing this system required balancing:

* Psychology and logic
* Simplicity and depth
* Determinism and empathy

This aligns closely with the role of a **Knowledge Engineer** — translating human behavior into structured, navigable systems.

---
