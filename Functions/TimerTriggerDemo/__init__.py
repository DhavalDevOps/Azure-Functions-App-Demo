import azure.functions as func
import datetime
import logging

def main(mytimer: func.TimerRequest) -> None:
    utc_time = datetime.datetime.utcnow().isoformat()
    logging.info(f"Timer trigger executed at {utc_time}")
