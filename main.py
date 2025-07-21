from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow frontend requests (change to your frontend domain in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/pdus_per_second")
async def get_pdu_rate():
    """
    Simulates PDUs per second value.
    Returns a random number (0-50).
    """
    pdu_rate = random.randint(0, 50)
    return {"pdus_per_second": pdu_rate}
