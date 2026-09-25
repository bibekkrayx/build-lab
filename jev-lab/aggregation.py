from question import TOPICS

def aggregate(all_ratings):
  summary = {}
  
  for topic in TOPICS:
    scores = [ratings[topic] for ratings in all_ratings if topic in ratings]
    
    if scores:
      average = round(sum(scores)/len(scores), 1)
    else:
      average = None
      
    summary[topic] = {"average": average, "count": len(scores)}
    
  return summary