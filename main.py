from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Route trả về version
@app.get("/get_version")
def get_version():
    return {"version": "1.0.0"}

# Route kiểm tra số nguyên tố
@app.get("/check_prime/{number}")
def check_prime(number: int):
    if number < 2:
        return {"number": number, "is_prime": False}
    for i in range(2, number):
        if number % i == 0:
            return {"number": number, "is_prime": False}
    return {"number": number, "is_prime": True}

# Chạy ứng dụng bằng uvicorn:
# uvicorn main:app --reload
