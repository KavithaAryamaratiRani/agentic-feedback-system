from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class FeedbackRecord:
    source_id: str
    source_type: str   # app_store | support_email
    raw_text: str
    metadata: Dict[str, Any]
