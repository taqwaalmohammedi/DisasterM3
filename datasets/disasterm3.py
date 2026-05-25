import os
import json
from typing import Dict, Any, List
from datasets.base import BaseDataset

class DisasterM3Dataset(BaseDataset):
    """
    Adapter dataset class specifically built to ingest, clean, and map 
    the DisasterM3 benchmark data into the framework's unified ecosystem.
    """
    
    def load(self) -> List[Dict[str, Any]]:
        """
        Parses DisasterM3 JSON manifests and constructs standardized data payloads.
        """
        manifest_file = os.path.join(self.data_path, f"{self.split}.json")
        
        if not os.path.exists(manifest_file):
            raise FileNotFoundError(f"DisasterM3 manifest not detected at: {manifest_file}")
            
        with open(manifest_file, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            
        standardized_samples = []
        
        for sample in raw_data:
            standardized_payload = {
                "id": sample.get("id") or sample.get("sample_id"),
                "image_path": os.path.join(self.data_path, "images", sample.get("image")),
                "question": sample.get("question"),
                "task_type": sample.get("task_type", "vqa"),
                "ground_truth": sample.get("answer") or sample.get("label")
            }
            standardized_samples.append(standardized_payload)
            
        return standardized_samples
