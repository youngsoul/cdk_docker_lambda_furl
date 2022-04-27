import requests
import logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


def handler(event, context):
    logger.debug("Running Dockerized Lambda")
    chi_time_response = requests.get("http://worldtimeapi.org/api/timezone/America/Chicago")
    json_response = chi_time_response.json()

    chi_time = json_response['unixtime']

    try:
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps(f"Lambda Complete: {chi_time}")
        }
    except Exception as exc:
        logger.error(f"Error: {exc}")

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps(f"ERROR: {exc}")
        }
