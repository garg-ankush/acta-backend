import json
import base64
import os
from dotenv import load_dotenv

load_dotenv()

REGION = "us-east-1"

def handler(event, context):
    body = event.get('body')

    if body is None or body == "":
        return "Body is empty", 422

    body = json.loads(base64.b64decode(body))

    # Extract request information from body
    input_text = body.get('text') # Input text
    text_id = body.get('textId') # Id of the input text
    voice_id = body.get('voiceId') # Voice id for the speaker

    # Imports
    from boto3 import Session
    from boto3 import resource
    session = Session(region_name=REGION)

    # Define polly and s3 resources
    polly = session.client("polly")

    s3 = resource('s3')
    bucket_name = os.getenv("BUCKET_NAME")
    bucket = s3.Bucket(bucket_name)

    # File can be found with text id as the name
    filename = f"{text_id}.mp3"

    # Synthesize audio from text
    response = polly.synthesize_speech(
        Text=input_text,
        OutputFormat="mp3",
        VoiceId=voice_id
    )
    stream = response["AudioStream"]

    # Upload audio to S3
    # Use the text ID as the file name
    bucket.put_object(Key=filename, Body=stream.read())