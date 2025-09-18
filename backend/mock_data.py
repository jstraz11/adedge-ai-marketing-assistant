def mock_audiences():
    return [
        {"id": 1, "segment": "Pet Owners - Dogs", "score": 0.78},
        {"id": 2, "segment": "Pet Owners - Cats", "score": 0.74},
        {"id": 3, "segment": "Vet Shoppers - High Intent", "score": 0.82},
    ]

def mock_creatives():
    return [
        {"id": 1, "name": "Ad A - Hero Vet", "ctr": 0.032, "cvr": 0.041},
        {"id": 2, "name": "Ad B - Dental Month", "ctr": 0.028, "cvr": 0.053},
        {"id": 3, "name": "Ad C - Puppy Pack", "ctr": 0.025, "cvr": 0.033},
    ]
