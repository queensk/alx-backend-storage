#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_stats():
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient()
    collect_nginx = client.logs.nginx

    doc_number = collect_nginx.count_documents({})
    print("{} logs".format(doc_number))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collect_nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    status = collect_nginx.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status} status check")

    print("IPs:")
    pipeline = [
        {"$group":
         {
             "_id": "$ip",
             "count": {"$sum": 1}
         }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ]
    for ip in collect_nginx.aggregate(pipeline):
        print(f"\t{ip['ip']}: {ip['count']}")


if __name__ == "__main__":
    nginx_stats()
