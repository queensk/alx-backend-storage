#!/usr/bin/env python3
"""
Top students
"""
def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {"_id": "$_id", "name": {"$first": "$name"}, "averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(pipeline)
