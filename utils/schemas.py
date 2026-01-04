from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class FeedbackRecord:
    source_id: str
    source_type: str   # app_store | support_email
    raw_text: str
    metadata: Dict[str, Any]
@dataclass
class ClassificationResult:
    category: str        # Bug | Feature Request | Praise | Complaint | Spam
    confidence: float    # 0.0 - 1.0
@dataclass
class FeatureAnalysisResult:
    feature_summary: str
    user_intent: str
    demand_level: str   # Low | Medium | High
    suggested_priority: str  # Low | Medium | High
