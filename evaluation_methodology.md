# Evaluation Methodology for Vision-Language Models (VLMs)

Evaluating Multimodal Vision-Language Models (VLMs) differs significantly from assessing traditional single-modality models (such as pure language or pure vision models). Because VLMs process both visual context (images) and textual context (prompts/questions) simultaneously to produce text-based responses, their evaluation requires specialized frameworks and metrics.

---

### 1. Nature of Evaluation Data
Evaluation datasets for VLMs in disaster analysis typically consist of triplets or structured pairs that test the model's cross-modal reasoning capability:
* **Visual Inputs:** High-resolution remote sensing imagery, including satellite data (e.g., pre- and post-disaster patches) or drone/UAV aerial captures.
* **Textual Prompts / Questions:** Ground-truth text inputs that can range from simple open-ended questions (*"What is the damage level of the building in the center?"*) to multiple-choice questions (MCQs) or direct instructions for damage grading.
* **Ground-Truth Answers:** The expected correct responses, often verified and annotated by human domain experts or GIS professionals.

### 2. Evaluation Frameworks & Paradigms
VLM evaluation generally follows two main paradigms based on the task structure:

#### A. Discriminative / Closed-Ended Evaluation
The model is constrained to select from a fixed set of options (e.g., Multiple Choice Questions) or provide binary answers (Yes/No). 
* **Advantage:** Evaluation is completely objective, deterministic, and easy to automate.

#### B. Generative / Open-Ended Evaluation
The model generates free-form text responses to describe a scene, assess damage, or answer complex situational questions.
* **Advantage:** Captures the full reasoning capabilities of the model.
* **Challenge:** Parsing natural language outputs to match structural truth requires flexible text-matching or LLM-as-a-judge approaches.

---

### 3. Key Evaluation Metrics

Depending on the specific disaster task, VLMs are evaluated using a combination of the following metrics:

#### A. Classification & Discriminative Metrics
Used when the VLM performs tasks like multiple-choice Visual Question Answering (VQA) or macro damage classification:
* **Accuracy:** The percentage of correctly answered questions or correctly assigned damage classes.
* **F1-Score / Precision / Recall:** Crucial for disaster analysis because data is often highly imbalanced (e.g., far fewer "destroyed" buildings compared to "undamaged" ones). F1-score ensures the model genuinely performs well across all damage categories.

#### B. Open-Ended Text Generation Metrics
Used to evaluate free-form text generation by comparing the model's generated text against the expert-annotated ground truth text:
* **BLEU (Bilingual Evaluation Understudy) & ROUGE:** Measure n-gram overlap between the generated text and the reference answer. Commonly used in open-ended VQA.
* **METEOR & CIDEr:** Advanced translation and image captioning evaluation metrics that account for synonyms, stemming, and term-frequency weighting, offering a closer match to human judgment.

#### C. Remote Sensing & Spatial-Aware Metrics
In specialized disaster benchmarks, evaluation occasionally measures the model’s adherence to spatial constraints:
* **IoU (Intersection over Union) / Grounding Accuracy:** When a VLM is asked to locate or "ground" a specific disaster element textually, metrics evaluate how precisely the model’s predicted spatial coordinates or region bounding boxes align with the actual disaster footprint.
