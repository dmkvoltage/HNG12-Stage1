from fastapi import FastAPI, Query, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1): 
        if abs(n) % i == 0:
            return False
    return True

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(abs(n))] 
    return sum(d ** len(digits) for d in digits) == abs(n)

def is_perfect(n: int) -> bool:
    return sum(i for i in range(1, abs(n)) if abs(n) % i == 0) == abs(n)

def get_fun_fact(n: int) -> str:
    response = requests.get(f"http://numbersapi.com/{n}/math?json")
    if response.status_code == 200:
        return response.json().get("text", "No fact found.")
    return "No fact available."

def generate_reason(number: int) -> str:
    if is_armstrong(number):
        digits = [int(d) for d in str(abs(number))]
        armstrong_sum = " + ".join(f"{d}^{len(digits)}" for d in digits)
        return f"{number} is an Armstrong number because {armstrong_sum} = {abs(number)}"
    return get_fun_fact(number)

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="The number to classify")):
    if not number.lstrip('-').isdigit(): 
        raise HTTPException(
            status_code=400,
            detail={"number": number, "error": True}
        )
    
    number = int(number)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")
    
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(number))),
        "fun_fact": generate_reason(number)
    }
