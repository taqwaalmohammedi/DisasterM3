import os
import json
from typing import Dict, Any, List
from datasets.base import BaseDataset

class MONITRSDataset(BaseDataset):
    """
    Task 8 Implementation: Concrete dataset adapter built to ingest 
    and normalize the external MONITRS benchmark into our unified ecosystem.
    """
    
    def load(self) -> List[Dict[str, Any]]:
        """
        Parses MONITRS structured JSON annotations and adapts geospatial paths
        into the framework's standardized dictionary contract.
        """
        manifest_file = os.path.join(self.data_path, f"monitrs_{self.split}.json")
        
        if not os.path.exists(manifest_file):
            raise FileNotFoundError(f"MONITRS target manifest missing at: {manifest_file}")
            
        with open(manifest_file, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            
        standardized_samples = []
        
        for sample in raw_data:
            # Structuring dynamic multi-sensor fields into our framework's standard format
            standardized_payload = {
                "id": sample.get("mission_id") or sample.get("id"),
                "image_path": os.path.join(self.data_path, "patches", sample.get("image_name")),
                "question": sample.get("text_prompt") or sample.get("question"),
                "task_type": "remote_sensing_vqa",
                "ground_truth": sample.get("expert_label") or sample.get("answer")
            }
            standardized_samples.append(standardized_payload)
            
        return standardized_samples
