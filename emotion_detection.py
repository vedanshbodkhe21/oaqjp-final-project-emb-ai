"""
Detect emotion of a text
"""

import json
import requests

# Timeout for requets.post
TIMEOUT = 0.5

def emotion_detector(text_to_analyse):
    """Detect emotion of input"""

    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    # Make the request
    r = requests.post(
        url,
        headers=header,
        json=payload,
        timeout=TIMEOUT
        )

    # Load in json
    js = json.loads(r.text)
    emotion_dict = js['emotionPredictions'][0]['emotion']

    # Find the dominant emotion and add it to result
    max_emo = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = max_emo

    return emotion_dict
