# Evaluation Methodology for Vision-Language Models (VLMs) in DisasterM3

Evaluating Multimodal Vision-Language Models (VLMs) differs significantly from assessing traditional single-modality models. Because VLMs process both visual context (multi-sensor imagery) and textual context (prompts/instructions) simultaneously to produce responses, their evaluation requires specialized multi-tier frameworks. This document outlines general VLM evaluation and maps it directly to the DisasterM3 benchmark infrastructure.

---

## 1. Nature of Evaluation Data & Instruction Pairs

Evaluation datasets in disaster analysis test cross-modal reasoning using structured tokens or multi-modal triplets:
* **Visual Inputs:** Multi-sensor imagery combining **Bi-temporal Optical satellite data** (Pre-disaster vs. Post-disaster patches) and **Post-disaster Synthetic Aperture Radar (SAR)** imagery to bypass weather or cloud obstructions.
* **Textual Instructions / Questions:** Ground-truth text prompts ranging from closed questions to long-form generative requests (e.g., *"How many major damaged buildings are in this disaster?"* or *"Segment the total-destroyed building?"*).
* **Ground-Truth Targets:** Expected accurate responses, consisting of target classes, exact entity counts, spatial bounding box coordinates, pixel mask identifiers, or expert-annotated text reports.

---

## 2. Evaluation Frameworks & Paradigms in DisasterM3

The DisasterM3 framework evaluates model performance across a progressive taxonomy divided into distinct analytical layers:

### A. Recognition (Rec) Layer [Closed-Ended / Discriminative]
* **Mechanism:** The model answers focused text prompts evaluating macro environmental features (Disaster Type, Scene Recognition, and Bearing Bodies Recognition).
* **Evaluation Paradigm:** Objective and deterministic mapping where responses are checked against exact nominal categorical strings (e.g., Target: `"Explosion"`).

### B. Counting & Ratio Estimation Layer [Quantitative Deterministic]
* **Mechanism:** Tasks like **Damaged Building Counting** and **Damaged Road Area Estimation** require the VLM to extract numerical density values from visual frames.
* **Evaluation Paradigm:** Evaluates exact mathematical proximity to ground truth values (e.g., extracting exact percentages like `"1.99%"` or absolute counts).

### C. Localization & Relational Reasoning Layer [Spatial-Aware Paradigm]
* **Mechanism:** Includes **Referring Segmentation** and **Damaged Object Relational Reasoning**. The model must understand positional tokens or direct bounding box links (e.g., spatial relations between `#pink box` and `#blue box`).
* **Evaluation Paradigm:** Measures spatial grounding, ensuring linguistic outputs correctly correlate with physical positions on the map coordinates.

### D. Report Generation Layer [Open-Ended Generative]
* **Mechanism:** Deep contextual generation tasks including dense **Disaster Description** paragraphs and actionable, long-form **Disaster Restoration Advice** (Immediate vs. Long-term strategies).
* **Evaluation Paradigm:** Open-ended string parsing to verify logical consistency and linguistic coverage.

---

## 3. Key Evaluation Metrics

Depending on the specific layer of the taxonomy being tested, models in the repository are evaluated using a combination of the following metrics:

### A. Classification & Counting Metrics (Rec & Counting Layers)
* **Accuracy:** The basic percentage of correctly identified disaster types or land-use categories across the benchmark subsets (e.g., `bearing_body` or `report`).
* **F1-Score / Precision / Recall:** Critical due to severe data imbalance in disaster areas (e.g., instances of "destroyed buildings" are far rarer than "intact buildings"). F1-score guarantees that the VLM genuinely recognizes heavy damage without being biased by dominant majority classes.
* **Mean Absolute Error (MAE) / RMSE:** Used specifically to track counting accuracy for isolated structural assets or collapsed building metrics.

### B. Open-Ended Text Generation Metrics (Report Layer)
* **BLEU & ROUGE:** Measures exact n-gram token overlap between the VLM's generated summary reports and the reference expert-annotated texts.
* **METEOR & CIDEr:** Advanced translation and image captioning evaluation metrics that leverage synonyms, stemming, and TF-IDF term weighting. This provides a closer match to a human inspector's judgment when evaluating complex paragraphs like "Restoration Advice."

### C. Spatial-Aware & Grounding Metrics (Localization Layer)
* **Intersection over Union (IoU) / mIoU:** Measures the pixel-level overlap accuracy when evaluating **Referring Segmentation** targets (e.g., tracking the exact shape of a landslide footprint or a flooded road section).
* **Bounding Box Grounding Accuracy:** Measures how accurately the VLM isolates bounding box coordinate predictions against ground truth spatial grids.
