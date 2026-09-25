import csv

from question import TOPICS
from analyzer import analyze_review
from aggregation import aggregate

INPUT_FILE = "dummy_reviews_51.csv"

with open(INPUT_FILE, encoding="utf-8") as f:
    reviews = list(csv.DictReader(f))
    
all_ratings = []

for review in reviews:
    ratings = analyze_review(review["review"])
    all_ratings.append(ratings)
    print(review["review_id"], ratings)
    
overall = sum(int(r["rating"]) for r in reviews)/len(reviews)
summary = aggregate(all_ratings)

print()
print(f"{overall:.1f} ★  based on {len(reviews)} ratings")
print("-" * 40)
for topic, info in summary.items():
    if info["average"] is None:
        print(f"{topic:<16} no ratings yet")
    else:
        print(f"{topic:<16} {info['average']:.1f} ★  ({info['count']} reviews)")