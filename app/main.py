from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional
import httpx

app = FastAPI(title="Interactive API Website")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

class ProxyRequest(BaseModel):
    method: str
    url: str
    headers: Optional[Dict[str, str]] = {}
    body: Optional[Any] = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/proxy")
async def proxy(request: ProxyRequest):
    async with httpx.AsyncClient() as client:
        try:
            # Filter out restricted headers if necessary
            headers = request.headers.copy() if request.headers else {}
            
            response = await client.request(
                method=request.method,
                url=request.url,
                headers=headers,
                json=request.body
            )
            
            content = None
            try:
                content = response.json()
            except:
                content = response.text

            return {
                "status": response.status_code,
                "headers": dict(response.headers),
                "data": content
            }
        except Exception as e:
            return {"error": str(e), "status_code": 500}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
