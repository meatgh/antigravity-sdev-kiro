---
description: Comprehensive Standard Operating Procedure for remediating FAANG Interview Questions (Q41-Q100) to the Senior SDE Gold Standard.
---

# FAANG Question Remediation Workflow (Gold Standard)

This workflow is the **Single Source of Truth** for remediating interview questions. It mirrors the `FAANG_Interview_Question_Sol_Temp.md` structure exactly.
**Target Audience**: Senior/Staff SDE candidates (L5/L6).
**Minimum Length**: 2000 lines per question.

## Phase 1: Preparation (Critical First Step)
- [ ] **Context Loading**: Read the existing legacy content (usually 2-3 lines) to identify the core topic.
- [ ] **Topic Research**: Identify the "Big 5" languages implementation details (Java, Python, JS/TS, Go, C++).
- [ ] **Enterprise Context**: Identify *where* this specific pattern is used in AWS/Google/Netflix architecture.

## Phase 2: Execution - The 10 Mandatory Sections

### 1. Question Analysis & Understanding (200+ Lines)
*This is the MOST IMPORTANT section. You must prove you understand the problem before solving it.*
- [ ] **Interactive Visualization (Mermaid)**: 
    - [ ] Create a `mermaid` diagram illustrating the Problem Scope or Architecture.
    - [ ] **Example**: A Sequence Diagram showing a Race Condition, or a Class Diagram.
- [ ] **Question Statement**: Full problem description with constraints.
- [ ] **Question Explanation**: Break down the prompt sentence-by-sentence. What is implied? What is explicit?
- [ ] **Question Analysis**: "What this really tests" (Core concepts, Data structures).
- [ ] **Difficulty Breakdown**:
    - [ ] Algorithmic Constraints
    - [ ] Implementation Complexity
    - [ ] Optimization Challenges
    - [ ] Edge Case nuances
- [ ] **Company Context**: Specific examples from Google, Amazon, Meta, etc.
- [ ] **Real-World Applications**: Concrete production use cases (e.g., "Rate Limiter in API Gateway").

### 2. Solution Progression (Brute Force -> Optimal) (500+ Lines)
*For EACH Approach (Naive, Optimized, Optimal), you must include:*
- [ ] **Solution Discussion**: A detailed, text-based walkthrough of the logic **before** showing any code. Explain the trade-offs.
- [ ] **Code Implementation**: Fully commented code.
    -   *Crucial*: **Extensive Inline Comments**. Explain *why* a line exists, not just what it does.
- [ ] **Complexity Analysis**:
    - [ ] Time Complexity (Big O) with mathematical justification.
    - [ ] Space Complexity (Big O) with memory layout explanation.
    - [ ] **Performance Notes**: Why is this better/worse?

### 3. Multi-Language Implementations (400+ Lines)
*Implement the OPTIMAL solution in all 5 languages:*
- [ ] **Java**: Enterprise grade (Spring contexts, JavaDoc, Generics).
- [ ] **Python**: Pythonic (Context Managers, Decorators, Type Hints).
- [ ] **JavaScript/TypeScript**: Modern ESNext, Node.js patterns.
- [ ] **Go**: Idiomatic Go (Structs, Interfaces, Goroutines, `defer`).
- [ ] **C++**: Modern C++20 (Smart Pointers, RAII, Templates).
*Requirement*: **Extensive Inline Comments** in ALL languages demonstrating Senior SDE mastery of that language's specific idioms.

### 4. Edge Cases & Error Handling (200+ Lines)
- [ ] **Input Validation**: Nulls, Empty sets, Intl chars, Massive inputs.
- [ ] **Algorithmic Edge Cases**: Cycles, Negative weights, Overflows.
- [ ] **Security Analysis**:
    - [ ] ReDoS (Regex DoS)
    - [ ] Deserialization Gadgets
    - [ ] Buffer Overflows (C++)
    - [ ] Injection Risks
- [ ] **Error Handling**: Custom Exceptions vs Return Codes (Result Pattern).

### 5. Interview Simulation & Communication (200+ Lines)
- [ ] **Whiteboard Strategy**: Step-by-step generic guide (Clarify -> Design -> Code -> Test).
- [ ] **Communication Hooks**: "I'm thinking about trade-offs...", "In a distributed system...".
- [ ] **Handling Feedback**: How to pivot when the interviewer changes constraints.

### 6. Advanced Optimizations & Layout (250+ Lines)
- [ ] **Low-Level Enhancements**: Memory alignment, Cache locality, SIMD.
- [ ] **Distributed Context**: How this scales to 10k RPS (Sharding, Consistent Hashing).
- [ ] **Deep Dive**: Hardware sympathy (False Sharing, Branch Prediction).

### 7. Related Problems & Patterns (150+ Lines)
- [ ] **Code Reuse**: How this pattern solves other LeetCode/System Design problems.
- [ ] **Variations**: "What if the stream is infinite?", "What if disk is slow?".

### 8. Production System Integration (150+ Lines)
- [ ] **System Design**: Where does this class fit in a Microservices architecture?
- [ ] **Observability**: Metrics (Micrometer), Logging (MDC), Tracing (OpenTelemetry).
- [ ] **Database**: Schema implications, Indexes, ACID properties.

### 9. Behavioral & Leadership (100+ Lines)
- [ ] **Code Review Guide**: What would a Senior Engineer comment on this PR?
- [ ] **Mentorship**: How to explain this to a Junior Dev.
- [ ] **Business Value**: Translating O(N) to "$" savings.

### 10. Comprehensive Testing (100+ Lines)
- [ ] **Unit Tests**: JUnit/PyTest/Jest/GoTest/GoogleTest.
- [ ] **Integration Tests**: Dockerized environment setups.
- [ ] **Property-Based Testing**: Validating invariants (e.g., jqwik, Hypothesis).

## Phase 3: Final Verification (The "2000-Line Gate")
- [ ] **Line Count Check**: Is the total > 2000 lines?
    -   **CRITICAL RULE**: You are **FORBIDDEN** from marking this task as completed if the line count is < 2000.
    -   **NO UPPER LIMIT**: There is no maximum line count. More depth is always better.
- [ ] **Formatting Check**: Are all headers `###` or `####`?
- [ ] **Compile Check**: Do the code snippets look syntactically valid?

## Phase 4: Artifact Update (Definition of Done)
- [ ] **Update task.md**: 
    -   Only mark `[x]` IF AND ONLY IF the 2000-line check passed.
    -   If < 2000 lines, keep as `[/]` and add another section (e.g., "Deep Dive: JVM Internals") to reach the target.
- [ ] **Notify User**: summarize the depth and specific Enterprise topics covered.
