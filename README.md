# Flask API Assignment

A self-contained Flask REST API demonstrating python fundamentals including function structures, control loops, custom typecast validations, and pytest assertions.

## Setup Instructions

1. **Create and open the project directory:**
   ```bash
   mkdir flask_api_assignment && cd flask_api_assignment
   ```

2. **Initialize your isolated python virtual environment:**
   ```bash
   python -m venv venv
   # Activation Command (Windows):
   venv\Scripts\activate
   ```

3. **Install project dependencies:**
   ```bash
   pip install Flask pytest
   ```

## How to Run the Server

Start the endpoint backend engine using your system terminal prompt:
```bash
python app.py
```
The application will listen live locally on **http://127.0.0.1:5000**.

## Executing Automated Tests

Run your structural diagnostic verification suite using pytest:
```bash
pytest test_app.py
```

### Execution Verification Outcomes
* **Test Case 1:** GET `/hello` (Default Parameters) ➡️ **PASSED** (HTTP 200)
* **Test Case 2:** POST `/sum` (Valid Mathematical List) ➡️ **PASSED** (HTTP 200)
* **Test Case 3:** POST `/sum` (Malformed Text Payload Error Check) ➡️ **PASSED** (HTTP 400 Validation Block)

**Diagnostic Suite Status Summary:** `3 passed in 0.10s`

## Assumptions and References
* **AI transparency. I did not write this source code independently. I received extensive help from Google Gemini AI. Gemini also helped with formatting and site navigation.
* **Current Understanding: I am still unsure about writing and formatting the code, but I do somewhat understand that JSON parses data to be read by other systems and that API is the messenger that carries it.
References: Sourced code endpoint designs  guidelines from class video tutorials ("Install basic flask with GET and POST Endpoints,Interoperability-Python Turorial_Working with JSON Data)
