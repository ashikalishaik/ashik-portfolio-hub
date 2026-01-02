from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="Ashik Portfolio Hub")


class Project(BaseModel):
    id: int
    slug: str
    name: str
    description: str
    github_url: str
    live_url: Optional[str] = None
    tags: List[str] = []


# In-memory "DB" for now
PROJECTS: List[Project] = [
    Project(
        id=1,
        slug="gnn-node-classification",
        name="GNN Node Classification & Visualizer",
        description="Graph Neural Network node classification and visualization project with PyTorch Geometric.",
        github_url="https://github.com/ashikalishaik/gnn-node-classification",
        tags=["gnn", "deep-learning", "research"],
    ),
    Project(
        id=2,
        slug="time-series-forecasting",
        name="Time Series Forecasting Pipeline",
        description="End-to-end time series forecasting with decomposition, baselines, and SARIMA.",
        github_url="https://github.com/ashikalishaik/I-am-a-Junior-Man/tree/main/project_02_time_series_forecasting",
        tags=["time-series", "forecasting", "sarima"],
    ),
    Project(
        id=3,
        slug="ai-call-agent",
        name="AI Call Agent",
        description="Backend for AI-driven call handling and call summary generation.",
        github_url="https://github.com/ashikalishaik/ai-call-agent",
        tags=["ai", "backend", "automation"],
    ),
    Project(
        id=4,
        slug="vision-we-all-can-see",
        name="VISION – Assistive Vision App",
        description="Android app for real-time object detection with audio feedback for visually impaired users.",
        github_url="https://github.com/ASHIKalip/VISION-we-all-can-see",
        tags=["android", "cv", "accessibility"],
    ),
    Project(
        id=5,
        slug="studentmarket",
        name="StudentMarket – Campus Marketplace",
        description="FastAPI + PostgreSQL full-stack marketplace for students.",
        github_url="https://github.com/ashikalishaik/intl_student_marketplace_repo",
        tags=["fastapi", "postgresql", "web-app"],
    ),
]


@app.get("/")
def root():
    return {"message": "Ashik Portfolio Hub API is running"}


@app.get("/projects", response_model=List[Project])
def list_projects():
    return PROJECTS


@app.get("/projects/{slug}", response_model=Project)
def get_project(slug: str):
    for p in PROJECTS:
        if p.slug == slug:
            return p
    # simple error for now
    return {"detail": "Project not found"}
