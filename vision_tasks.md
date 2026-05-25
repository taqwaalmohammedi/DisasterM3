# Computer Vision and Multi-Modal Tasks in DisasterM3 Analysis

In the context of remote sensing and disaster management, understanding environment changes requires shifting from traditional computer vision to Vision-Language multi-modal reasoning. This document maps foundational computer vision paradigms directly to the 9 benchmark tasks defined in the official DisasterM3 framework taxonomy.

---

## 1. Image Classification & Scenario Recognition

### A. Foundational Concept
Image classification assigns a global label or category to an entire scene based on macro visual patterns. It answers: *"What is the main event or land-use type?"*

### B. Direct Mapping to DisasterM3 Tasks
Our framework integrates global and patch-level classification through the following specific multi-modal reasoning tracks shown in the dataset taxonomy:
* **Disaster Type Recognition:** Identifying the core catastrophic event from post-disaster images (e.g., Question: *"What disaster has happened in this area?"* -> Answer: *"Explosion"*).
* **Disaster Scene Recognition:** Classifying background environment footprints (e.g., Question: *"What are land-use types in the pre-disaster scene?"* -> Answer: *"Harbor, industrial, and sea"*).
* **Disaster Bearing Bodies Recognition:** Identifying macro infrastructure systems under threat (e.g., Classifying presence of buildings, roads, or coastal elements).

---

## 2. Object Detection, Counting & Spatial Reasoning

### A. Foundational Concept
Object detection locates specific target structures using spatial bounding boxes or coordinates, moving from global understanding to region-level assessment (*"What objects are where, and how many?"*).

### B. Direct Mapping to DisasterM3 Tasks
The dataset expands localized spatial awareness into complex counting and relational evaluation tracks:
* **Damaged Building Counting:** Identifying and assessing the survival rate of localized structures (e.g., counting intact, major damaged, or total-destroyed buildings).
* **Damaged Object Relational Reasoning:** Evaluating geometric and contextual relationships between different localized bounding boxes (e.g., analyzing the spatial relation between an object in a `#pink box` and another in a `#blue box`).

---

## 3. Image Segmentation & Pixel-Level Estimation

### A. Foundational Concept
Segmentation provides the highest level of visual granularity by classifying every single pixel in the image, allowing for precise tracking of irregular boundaries and area ratios.

### B. Direct Mapping to DisasterM3 Tasks
DisasterM3 utilizes bi-temporal (pre and post-disaster) optical visuals combined with Synthetic Aperture Radar (SAR) to execute precise surface estimation:
* **Referring Segmentation:** Isolating pixel masks matching natural language prompts (e.g., Segmenting the specific paths of roads covered by debris or completely destroyed building clusters).
* **Damaged Road Area Estimation:** Calculating exact spatial ratios or damage percentages based on dense pixel analysis (e.g., estimating that exactly `1.99%` of roads are covered by debris).

---

## 4. Advanced Multi-Modal Visual Report Generation

Going beyond standard vision, the final layer combines classification, spatial reasoning, and segmentation insights into long-form linguistic tasks:
* **Disaster Description:** Generating descriptive paragraphs detailing the exact state of building collapses and road blockages.
* **Disaster Restoration Advice:** Providing structured immediate and long-term emergency response strategies based on the visual evidence parsed by the VLM.

---

### Framework Alignment Matrix

| Foundational Vision Task | DisasterM3 Taxonomy Level | Example Execution Metric |
| :---                       | :---                                     |                               :---    |
| **Image Classification**   | Recognition (Rec) & Damage Grading       | Classification Accuracy / F1-Score    |
| **Object Detection**       | Counting & Relational Reasoning          | Bounding Box IoU / Object Count Error |
| **Image Segmentation**     | Referring Segmentation & Area Estimation | Pixel-level mIoU / Ratio Calculations |
