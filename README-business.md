# AdEdge AI Marketing Assistant — Client Quick Start

This lets you run the assistant locally with **Docker** (no coding).

- Frontend: http://localhost:8080
- Backend (API): http://localhost:8000

## 1) Prerequisites
- Install **Docker Desktop** (Windows/Mac): https://www.docker.com/products/docker-desktop
- Download this project (ZIP) or receive it from us.

## 2) Start the app
Open a terminal in the project folder and run:
```bash
docker compose up -d --build
```
Then open **http://localhost:8080**.

## 3) Upload your CSV
Click **Upload CSV**. Use this header format:
```
Platform,Impressions,Clicks,Conversions,Cost,Date
```
Example:
```
Google,12000,600,90,450.00,2025-09-19
```

## 4) Stop / Update
- Stop: `docker compose down`
- Update after file changes: `docker compose up -d --build`

## 5) Troubleshooting
- Page loads but no data: make sure both containers are running (`docker ps`).
- CSV errors: check the header names exactly; Date must be `YYYY-MM-DD`.
- Port in use: edit `docker-compose.yml` and change the left ports (e.g., `8081:80`).

## Notes
- Uses local SQLite database (persists in Docker volume).
- For production hosting, we can deploy the API to a public HTTPS URL and point the frontend at it.
