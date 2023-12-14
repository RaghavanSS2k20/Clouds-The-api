def map_emotion_to_sentiment(emotion_label):
    if emotion_label == 'positive':
        return 'good'
    elif emotion_label == 'neutral':
        return 'neutral'
    elif emotion_label == 'negative':
        return 'bad'
    else:
        return 'unknown'  # Handle unknown labels if needed
def get_dominant_emotion(emotions):
    if not emotion:
        return None
    dominant_emotion = max(emotions, key=lambda x: x['score'])
    return map_emotion_to_sentiment(dominant_emotion['label'])