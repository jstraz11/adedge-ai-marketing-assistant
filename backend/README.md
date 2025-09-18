# Backend (FastAPI)

Run locally (Windows + Git Bash):
```bash
cd /c/Users/jakes/adedge-ai-marketing-assistant
python -m venv .venv
source .venv/Scripts/activate
# NOTE: Installing all deps may fail on Windows because of lightgbm.
# If it fails, use the minimal install shown below.
pip install -r backend/requirements.txt || true

# Minimal install (skip lightgbm) if the line above fails:
pip install fastapi==0.115.2 pydantic==2.8.2 "uvicorn[standard]==0.30.6" pandas==2.2.2 SQLAlchemy==2.0.34 psycopg2-binary==2.9.9 python-dotenv==1.0.1 python-multipart==0.0.9 numpy==1.26.4

# Use SQLite locally so Postgres is not required:
export DATABASE_URL=sqlite:///./local.db

# Start the API
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

Key endpoints:
- GET /health
- POST /upload/csv
- GET /best
- GET /recommendations/budget
- GET /report
- POST /train/audience
- POST /connectors/harvest
- POST /creative/generate
- POST /apply
