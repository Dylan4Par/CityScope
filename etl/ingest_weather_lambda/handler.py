# Example AWS Lambda handler (Python 3.11)
# Purpose: fetch latest weather sample for Denver (KDEN) from an API and write JSON to S3.
# Note: In public repo, keep this as a stub — no credentials or real endpoints.

import json
from datetime import datetime, timezone

def handler(event, context):
    # Synthetic payload for demo — replace with real API call in private repo.
    payload = {
        "station": "KDEN",
        "ts": datetime.now(timezone.utc).isoformat(),
        "temp_c": 5.0,
        "wind_kts": 12,
        "precip_mm": 0.0,
        "conditions": "Clear"
    }
    # Normally: put to S3 with boto3. Omitted here.
    return {
        "statusCode": 200,
        "body": json.dumps(payload)
    }
