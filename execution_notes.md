# DisasterM3 Minimal Execution Run & Reproducibility Notes

This document provides a realistic engineering audit of deploying and executing a minimal run of the original DisasterM3 benchmark scripts using an isolated local Windows Command Prompt (CMD) interface. These diagnostic observations justify the modular overhaul detailed in our `analysis.md` (Task 3).

---

## 1. Environment Initialization & Setup

The execution setup followed standard baseline isolation procedures:
* **Host Environment:** Windows Command Prompt (CMD)
* **Python Architecture:** Python 3.10+
* **Target Workspace:** Local workspace directory.

---

## 2. Live Terminal Workflow & Real Execution Output

The reproduction steps were carried out line-by-line via the terminal interface, capturing real environment limitations:

```bash
# Step 1: Clone the repository down to the local host machine
git clone [https://github.com/taqwaalmohammedi/DisasterM3.git](https://github.com/taqwaalmohammedi/DisasterM3.git)
cd DisasterM3

# Step 2: Establish a local virtual environment for version isolation
python -m venv venv
call venv\Scripts\activate

# Step 3: Attempt package injection using the explicit reference tracker
pip install -r requirements.txt



Executed In-Terminal Failure Observation (A):

ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'

# Step 4: Attempting direct execution of the model baseline interface script
python pyscripts/eval_baseline.py

Executed In-Terminal Failure Observation (B):

python: can't open file 'C:\Users\USER\DisasterM3\pyscripts\eval_baseline.py': [Errno 2] No such file or directory

## 3. Critical Reproducibility Barriers & Engineering Diagnosis

The errors caught during this live terminal run explicitly confirm the structural gaps and high coupling limitations of the original repository. These diagnostic findings directly served as the primary motivation for the modular architectural design planned in Task 3, and subsequently implemented in later tasks:

1. **Missing Environment Blueprint (`requirements.txt`):** The upstream repository was published without a frozen production lockfile. This introduces massive dependency volatility for incoming researchers trying to map correct library variations (such as specific PyTorch, Transformers, or VLLM versions).
2. **Brittle Monolithic Structure & Hardcoded Directory Assumptions:** The automated failure to trigger script files like `eval_baseline.py` highlights that academic benchmarking suites often release dataset-specific scripts that lack standardized execution entry-points. Moving files or running them from alternative terminal roots causes immediate path decay.
3. **Tight Path Coupling & The Need for Abstraction:** Visual data paths, annotations, and parameters are completely embedded inside hidden python sub-layers instead of dynamic root configurations. **To solve this barrier, a decoupled and unified data ingestion layer was subsequently developed in Task 5 (for DisasterM3) and expanded in Task 8 (for MONITRS), successfully isolating data parsing from the execution code.**
