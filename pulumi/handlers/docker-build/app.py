import json
import base64
import os
from dotenv import load_dotenv

load_dotenv()

def handler(event, context):
    body = event.get('body')

    if body is None or body == "":
        return "Body is empty. Expected JSON object.", 422

    body = json.loads(base64.b64decode(body))

    # Extract request information
    input_text = body.get('text')
    text_id = body.get('textId')
    voice_id = body.get('voiceId')

    # Imports
    from boto3 import Session
    from boto3 import resource
    session = Session(region_name="us-east-1")

    # Define polly and s3 resources
    polly = session.client("polly")

    s3 = resource('s3')
    bucket_name = os.getenv("BUCKET_NAME")
    bucket = s3.Bucket(bucket_name)

    # File can be found with text id as the name
    filename = f"{text_id}.mp3"

    response = polly.synthesize_speech(
    Text=input_text,
    OutputFormat="mp3",
    VoiceId=voice_id
    )
    stream = response["AudioStream"]

    bucket.put_object(Key=filename, Body=stream.read())