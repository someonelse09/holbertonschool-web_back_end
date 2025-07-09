#!/usr/bin/env python3
""" This is a Python function that returns 
the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ topic (string) will be topic searched,
    considering that mongo_collection
    will be the pymongo collection object """

    return list(mongo_collection.find({ "topics": topic }))
