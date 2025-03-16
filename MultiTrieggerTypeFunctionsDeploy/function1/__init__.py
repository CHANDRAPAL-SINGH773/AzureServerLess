import os
import psycopg2
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port="5432"
        )
        return func.HttpResponse("PostgreSQL private endpoint is accessible!", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error connecting to PostgreSQL: {str(e)}", status_code=500)
