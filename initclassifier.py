from transformers import pipeline
def init_classifer():

    distilled_student_sentiment_classifier = pipeline(
        model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
        return_all_scores=True
    )
    return distilled_student_sentiment_classifier