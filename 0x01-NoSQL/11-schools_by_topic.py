#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    schools = []
    query = mongo_collection.find({"topics": {"$in": [topic]}})
    for school in query:
        schools.append(school)
    return schools
