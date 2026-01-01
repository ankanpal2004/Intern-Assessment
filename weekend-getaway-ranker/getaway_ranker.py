# Weekend Getaway Ranker

destinations = [
    {"name": "Jaipur", "distance": 280, "rating": 4.6, "popularity": 85},
    {"name": "Agra", "distance": 230, "rating": 4.4, "popularity": 90},
    {"name": "Rishikesh", "distance": 240, "rating": 4.7, "popularity": 88},
    {"name": "Manali", "distance": 540, "rating": 4.8, "popularity": 92}
]

def calculate_score(distance, rating, popularity):
    return (rating * 0.5) + (popularity * 0.3) - (distance * 0.01)

def rank_destinations(destinations):
    return sorted(
        destinations,
        key=lambda d: calculate_score(
            d["distance"], d["rating"], d["popularity"]
        ),
        reverse=True
    )

ranked = rank_destinations(destinations)

print("Top Weekend Destinations:\n")
for place in ranked:
    print(
        place["name"],
        "- Score:",
        round(calculate_score(
            place["distance"],
            place["rating"],
            place["popularity"]
        ), 2)
    )
