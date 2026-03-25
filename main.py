from fastapi import FastAPI
from pydantic import BaseModel
import pyodbc
from datetime import datetime

# I am creating a FastAPI application
app = FastAPI()

# This defines what a test result looks like
class TestResult(BaseModel):
    test_name: str
    passed: bool
    duration_ms: int
    error_message: str = None

# This function connects to my database
def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=(local)\\SQLEXPRESS;'
        'DATABASE=PipelineAutomation;'
        'Trusted_Connection=yes;'
    )
    return connection

# This is the endpoint that receives test results
@app.post("/results")
def save_test_result(result: TestResult):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # I am inserting the test result into my database
        cursor.execute("""
            INSERT INTO TestResults (TestName, Passed, DurationMs, RunAt, ErrorMessage)
            VALUES (?, ?, ?, ?, ?)
        """, result.test_name, result.passed, result.duration_ms, datetime.now(), result.error_message)
        
        conn.commit()
        conn.close()
        
        return {"status": "success", "message": "Test result saved"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

# This is a simple check to see if the API is running
@app.get("/health")
def health_check():
    return {"status": "API is running"}