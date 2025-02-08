# Number Classification API 🔢

A robust FastAPI-powered REST API that analyzes numbers, providing mathematical properties and interesting facts. Built with performance and scalability in mind, this API offers comprehensive number analysis including primality tests, perfect number verification, and Armstrong number detection.

## 🌟 Features

- **Number Properties Analysis**
  - Prime number detection
  - Perfect number verification
  - Armstrong number identification
  - Odd/Even classification
  - Digit sum calculation

- **Fun Facts Integration**
  - Retrieves interesting mathematical facts from Numbers API
  - Custom explanations for Armstrong numbers

## 🚀 Live Demo

API is accessible at: [Your Render URL here]

## 📚 API Documentation

### Main Endpoint

```
GET /api/classify-number?number={number}
```

### Example Request

```bash
curl "http://127.0.0.1:8000/api/classify-number?number=371"
```

### Sample Response

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response

```json
{
    "number": "abc",
    "error": true
}
```

## 🛠️ Technical Stack

- **FastAPI**: High-performance web framework
- **Python 3.7+**: Modern Python runtime
- **Numbers API**: External API integration for mathematical facts
- **Uvicorn**: ASGI server implementation

## ⚙️ Local Development

1. **Clone the Repository**
   ```bash
   git clone [your-repo-url]
   cd [repository-name]
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Development Server**
   ```bash
   uvicorn main:app --reload
   ```

   Access the API at `http://localhost:8000`

## 📈 Performance Features

- Optimized algorithmic implementations for number property checks
- Asynchronous request handling with FastAPI
- Efficient caching for external API calls
- Sub-500ms response times
- CORS enabled for cross-origin requests

## 🚀 Deployment

This API is deployed on Render for reliable and scalable hosting. The deployment process is automated through GitHub integration.

### Environment Requirements

Create a `requirements.txt` file with:
```
fastapi
uvicorn
requests
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Numbers API](http://numbersapi.com/)
- [Render Documentation](https://render.com/docs)