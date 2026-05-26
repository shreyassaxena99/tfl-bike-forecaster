import requests
from datetime import datetime
from typing import Any, Dict

ENDPOINT_URL = "https://api.tfl.gov.uk/BikePoint/"

def convert_str_datetime_to_epoch(str_datetime: str) -> int:
    dt = datetime.fromisoformat(str_datetime.replace('Z', '+00:00'))
    timestamp = dt.timestamp()
    return int(timestamp)

def filter_additional_attributes(raw_additional_attributes: dict, refined_dict: dict) -> None:
    for attribute in raw_additional_attributes:
        raw_attribute_key = attribute['key']
        refined_key = raw_attribute_key[0].lower() + raw_attribute_key[1:]
        refined_dict[refined_key] = attribute["value"] if len(attribute["value"]) > 0 else None

        if "timestamp" not in refined_dict:
            refined_dict["timestamp"] = convert_str_datetime_to_epoch(attribute["modified"])

def convert_raw_to_refined(raw_data: dict) -> dict:
    refined_data_point = dict()
    refined_data_point["bikePointId"] = raw_data['id']
    refined_data_point["name"] = raw_data['commonName']
    refined_data_point["lat"] = raw_data["lat"]
    refined_data_point["long"] = raw_data["lon"]
    
    additional_attributes = raw_data['additionalProperties']

    filter_additional_attributes(additional_attributes, refined_data_point)

    return refined_data_point

def get_bikepoint_data() -> list[Dict[str, Any]]:
    response = requests.get(ENDPOINT_URL)

    if response.status_code == 200:
        data = response.json()
    else:
        raise Exception(f"Error: {response.status_code}")

    return [convert_raw_to_refined(data_point) for data_point in data]
