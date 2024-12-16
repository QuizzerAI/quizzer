import json
from typing import Any, Dict
from model import AIResponse, AIQuestion

class AIDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj: Dict[str, Any]) -> Any:
        if "name" in obj:
            return AIResponse(**obj)
        if "answers" in obj:
            return AIQuestion(**obj)
        return obj
