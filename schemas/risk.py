from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

# CAMBRIDGE RISK Taxo catergories
class RiskCategory(str, Enum):
    FINANCIAL = "Financial"
    OPERATIONAL = "Operational"
    HAZARD = "Hazard"
    STRATEGIC = "Strategic"
    REPUTATIONAL = "Reputational"
    COMPLIANCE = "Compliance"
    ENVIRONMENTAL = "Environmental"

class DetectedRisk(BaseModel):
    risk_label: str = Field(description="Short name of the detected risk")
    risk_description: str = Field(description="What the risk is, based on the article")
    evidence: str = Field(description="Direct quote or paraphrase from the article that supports the risk detection")
    tx_category: RiskCategory = Field(description="Cambridge Risk Taxonomy category that the detected risk falls under")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score of the risk detection, between 0.0 and 1.0")


class RiskAssessment(BaseModel):
        company: str = Field(description="Name of the company being assessed for risks")
        article_title: str
        article_summary: str
        detected_risks: List[DetectedRisk] = Field(description="List of detected risks in the article")
        overall_risks: str = Field(description="LOW, MEDIUM, HIGH, or CRITICAL based on the detected risks and their confidence scores")
        analyst_notes: Optional[str] = None
        