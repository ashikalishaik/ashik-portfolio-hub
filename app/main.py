from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="Ashik Portfolio Hub")


class Project(BaseModel):
    slug: str
    name: str
    category: str  # e.g. "ML", "Time Series", "Vision", "Web"
    short_summary: str
    github_url: str
    tags: List[str]
    tech_stack: List[str]
    highlight: Optional[str] = None  # e.g. "GNN visualizer", "SARIMA pipeline"


# ---- In-memory project catalog ----
PROJECTS: List[Project] = [
    Project(
        slug="gnn-node-classification",
        name="GNN Node Classification & Visualizer",
        category="Graph ML",
        short_summary="Node classification and GNN behavior visualizer built for ECE 655.",
        github_url="https://github.com/ashikalishaik/gnn-node-classification",
        tags=["GNN", "PyTorch", "Visualization"],
        tech_stack=["Python", "PyTorch", "torch-geometric", "Matplotlib"],
        highlight="Visualizes message passing and node embedding evolution."
    ),
    Project(
        slug="time-series-forecasting",
        name="Time Series Forecasting Pipeline",
        category="Time Series",
        short_summary="End-to-end forecasting with decomposition, baselines, and SARIMA.",
        github_url="https://github.com/ashikalishaik/I-am-a-Junior-Man/tree/main/project_02_time_series_forecasting",
        tags=["Forecasting", "SARIMA", "MAE/RMSE"],
        tech_stack=["Python", "pandas", "statsmodels", "Matplotlib"],
        highlight="Includes naive, seasonal naive, and SARIMA with proper evaluation."
    ),
    Project(
        slug="ai-call-agent",
        name="AI Call Agent",
        category="Backend / AI",
        short_summary="Backend to handle unanswered calls and generate AI-driven summaries.",
        github_url="https://github.com/ashikalishaik/ai-call-agent",
        tags=["Backend", "AI"],
        tech_stack=["Python", "FastAPI", "External APIs"],
        highlight="Automates call handling and structured summary generation."
    ),
    Project(
        slug="vision-we-all-can-see",
        name="VISION – Assistive App for Visually Impaired",
        category="Mobile / Vision",
        short_summary="Android app with object detection and audio feedback.",
        github_url="https://github.com/ASHIKalip/VISION-we-all-can-see",
        tags=["Android", "Computer Vision"],
        tech_stack=["Android", "Java/Kotlin", "SSD MobileNetV2"],
        highlight="Real-time detection with TTS feedback."
    ),
    Project(
        slug="studentmarket",
        name="StudentMarket – Campus Marketplace",
        category="Web / Backend",
        short_summary="Full-stack marketplace for campus item listings.",
        github_url="https://github.com/ashikalishaik/intl_student_marketplace_repo",
        tags=["Web", "Backend", "Database"],
        tech_stack=["FastAPI", "PostgreSQL", "HTML", "CSS", "JavaScript"],
        highlight="REST APIs, auth, PostgreSQL data model."
    ),
]


@app.get("/")
def root():
    return {"message": "Ashik Portfolio Hub API is running"}


@app.get("/api/projects", response_model=List[Project])
def list_projects() -> List[Project]:
    return PROJECTS


@app.get("/api/projects/{slug}", response_model=Project)
def get_project(slug: str) -> Project:
    for proj in PROJECTS:
        if proj.slug == slug:
            return proj
    # If not found, FastAPI will convert this to a 404
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Project not found")
