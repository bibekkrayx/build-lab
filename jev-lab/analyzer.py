from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient
from question import QUESTIONS, TOPICS

load_dotenv()

client = TypeSafeClient()

MENTION_THRESHOLD = 0.6

def analyze_review(review_text):
  response = client.system_one(
    model="jev-latest",
    state=review_text,
    questions=QUESTIONS
  )
  
  answers = response.answers
  
  print('ANALYZER: ',answers)
  
  ratings = {}
  
  for topic_name, topic_id in TOPICS.items():
    mentioned = answers[topic_id+"_mentioned"].noul
    
    if mentioned >= MENTION_THRESHOLD:
      level = answers[topic_id+"_rating"].score
      stars = level+1
      ratings[topic_name] = round(stars, 1)
  
  return ratings