#!/usr/bin/env python3
"""
Insert a document in Python
"""
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id if result.acknowledged else None
