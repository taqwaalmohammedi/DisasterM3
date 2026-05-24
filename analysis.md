# Comprehensive Architectural Analysis and Modular Redesign of DisasterM3

## 1. Code Organization & Structural Analysis
After auditing the initial `DisasterM3` repository, the current codebase serves as a solid research baseline but exhibits typical characteristics of an early-stage academic project. The core functionalities are split into standard directory structures:
* `models/`: Manages deep learning architectures and transformer interfaces.
* `pyscripts/`: Contains various ad-hoc execution scripts for training, evaluation, and data preprocessing.

### Core Architectural Bottlenecks:
* **The Monolithic Script Problem:** The primary issue is that data parsing, input pipeline transformations, and inference execution loops are compiled inside single files (like the baseline evaluation scripts). There is no isolation of concerns.
* **Lack of Formal Polymorphism:** The repository does not utilize abstract base classes or strict interfaces. Methods accept loose dictionary outputs, making it highly error-prone if data shapes change.

---

## 2. Dataset and Model Coupling (The Generalization Barrier)
The most critical limitation of the current design is its rigid coupling with the `DisasterM3` dataset schema. 

### Why the current framework cannot ingest external benchmarks (e.g., MONITRS, EarthVQA) out-of-the-box:
1. **Hardcoded Data Paradigms:** The parsing logic explicitly searches for fixed JSON keys unique to DisasterM3 (such as exact text prompt keys and image naming syntax).
2. **Inflexible Pipelines:** Because image loading, resizing, and text tokenization happen inside the model execution loop, adding a dataset with a different format (like EarthVQA's question-answer structure) requires rewriting the core evaluation logic itself.
3. **Absence of a Config Layer:** Model parameters, dataset split paths, and evaluation modes are passed via brittle CLI arguments or hardcoded strings at the top of python files, preventing configuration-driven benchmarking.

---

## 3. Proposed Target Modular Architecture
To transform this codebase into an enterprise-grade evaluation ecosystem, I propose a decoupled, object-oriented framework that completely separates data ingestion from model inference.

### Pipeline Flow:
`Raw Ingestion (Dataset Adapter)` ➔ `Unified Payload` ➔ `Model Inference (Runner)` ➔ `Task Metrics (Evaluator)`

### Proposed Directory Blueprint:
```text
framework/
├── configs/               # Centralized YAML files for plug-and-play experimentation
├── datasets/              # Isolated data layer
│   ├── base.py            # BaseDataset abstract class enforcing a strict contract
│   ├── disasterm3.py      # Adapter converting DisasterM3 to unified format
│   └── monitrs.py         # Adapter for future external dataset integration
├── models/                # Pluggable model wrappers
│   ├── base.py            # Abstract Base Model Runner
│   └── qwen_runner.py     # Implementation for specific VLMs
├── evaluation/            # Standalone mathematical metric computation
│   ├── base.py            # Base Evaluator layer
│   └── vqa.py             # Specific metrics (Accuracy, BLEU, ROUGE)
└── experiments/           # Execution and experiment tracking management
    ├── runner.py          # Framework orchestrator driven completely by configuration
    └── tracker.py         # Third-party integration (MLflow / Weights & Biases)
