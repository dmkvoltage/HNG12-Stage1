from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utility functions
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(abs(n))]  # Use absolute value for Armstrong check
    return sum(d ** len(digits) for d in digits) == abs(n)

def is_perfect(n: int) -> bool:
    if n < 1:
        return False  # Negative numbers are not considered perfect
    return sum(i for i in range(1, n) if n % i == 0) == n

def get_fun_fact(n: int) -> str:
    response = requests.get(f"http://numbersapi.com/{n}/math?json")
    if response.status_code == 200:
        return response.json().get("text", "No fact found.")
    return "No fact available."

def generate_reason(number: int) -> str:
    if is_armstrong(number):
        digits = [int(d) for d in str(abs(number))]  # Use absolute value
        armstrong_sum = " + ".join(f"{d}^{len(digits)}" for d in digits)
        return f"{number} is an Armstrong number because {armstrong_sum} = {abs(number)}"
    return get_fun_fact(number)

# 🟢 **1️⃣ Path Parameter Version**
@app.get("/api/classify-number/{number}")
def classify_number_path(number: str = Path(..., description="The number to classify")):
    if not number.lstrip("-").isdigit():  # Allow negative numbers
        raise HTTPException(status_code=400, detail={"number": number, "error": True})
    return classify_helper(int(number))

# 🟢 **2️⃣ POST Request Version**
class NumberInput(BaseModel):
    number: str  # Accept string to validate first

@app.post("/api/classify-number")
def classify_number_post(data: NumberInput):
    if not data.number.lstrip("-").isdigit():  # Allow negative numbers
        raise HTTPException(status_code=400, detail={"number": data.number, "error": True})
    return classify_helper(int(data.number))

# Common function to classify numbers
def classify_helper(number: int):
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")
    
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(number))),  # Use absolute value
        "fun_fact": generate_reason(number)
    }
