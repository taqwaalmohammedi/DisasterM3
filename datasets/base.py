from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BaseDataset(ABC):
    """
    Abstract Base Class acting as a strict structural contract for all 
    disaster-related benchmarks within the modular evaluation framework.
    """
    
    def __init__(self, data_path: str, split: str = "val", configs: Dict[str, Any] = None):
        self.data_path = data_path
        self.split = split
        self.configs = configs or {}
        
    @abstractmethod
    def load(self) -> List[Dict[str, Any]]:
        """
        Loads and parses the raw dataset annotations into a unified 
        standardized multi-modal format.
        
        Returns:
            List[Dict[str, Any]]: A list of standardized samples containing 
                                  image paths, text queries, and ground truths.
        """
        raise NotImplementedError("Subclasses must implement the load method.")
