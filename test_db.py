import pyodbc

# I am testing if Python can connect to my PipelineAutomation database
try:
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=(local)\\SQLEXPRESS;'
        'DATABASE=PipelineAutomation;'
        'Trusted_Connection=yes;'
    )
    print("Successfully connected to PipelineAutomation database!")
    connection.close()
    
except Exception as e:
    print(f"Failed to connect: {e}")