import azure.functions as func
from fastapi import FastAPI
from app import app as fastapi_app

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.WsgiMiddleware(fastapi_app).handle(req)
