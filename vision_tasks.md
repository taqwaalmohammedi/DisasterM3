# Computer Vision Tasks in Natural Disaster Analysis

In the context of computer vision and remote sensing, understanding the environment from satellite or drone imagery requires different levels of visual granularity. The three foundational tasks are Image Classification, Object Detection, and Semantic/Instance Segmentation.

---

### 1. Image Classification
* **Definition:** Image classification assigns a single label or category to an entire image based on its overall visual content. It answers the question: *"What is in this image?"*
* **Application in Natural Disasters:**
  * **Disaster Detection:** Classifying a satellite scene as either "Flooded" or "Non-Flooded".
  * **Damage Grading:** Assigning a macro-level tag to an area image, such as "Severe Damage", "Moderate Damage", or "No Damage" after an earthquake.

### 2. Object Detection
* **Definition:** Object detection goes a step further by identifying the presence of specific objects and locating them within the image using bounding boxes (defined by coordinate points). It answers: *"What objects are where?"*
* **Application in Natural Disasters:**
  * **Infrastructure Monitoring:** Detecting and drawing bounding boxes around collapsed bridges, blocked roads, or damaged buildings to help rescue teams map accessible routes.
  * **Asset Counting:** Counting affected structures, isolated vehicles, or deployed rescue boats in a disaster zone.

### 3. Image Segmentation
* **Definition:** Segmentation provides pixel-level analysis. Instead of drawing a rough box, it classifies every single pixel in the image into a specific category. 
  * *Semantic Segmentation:* Groups all pixels belonging to the same class (e.g., all water pixels).
  * *Instance Segmentation:* Separates individual objects of the same class (e.g., distinguishing Building A from Building B).
* **Application in Natural Disasters:**
  * **Flood Extent Mapping:** Precisely delineating the boundary of water bodies to measure the exact square mileage of flooded land.
  * **Landslide and Wildfire Footprints:** Tracking the exact boundaries of a wildfire burn scar or a landslide path, which is crucial for environmental impact assessment and future risk modeling.

---

### Summary of Differences in Disaster Context

| Feature | Image Classification | Object Detection | Image Segmentation |
| :--- | :--- | :--- | :--- |
| **Granularity** | Image-level (Global) | Region-level (Bounding Box) | Pixel-level (Exact Shape) |
| **Output Example** | "This entire satellite image shows a flooded region." | "There are 5 damaged buildings detected in this grid." | "These specific 14,500 pixels represent the exact path of the lava flow." |
| **Computational Complexity** | Low | Medium | High |
