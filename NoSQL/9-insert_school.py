#!/usr/bin/env python3
""" This is a Python function that inserts
a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ The functioin Returns the new _id
    assuming mongo_collection will be
    the pymongo collection object """
    
    document_to_insert = kwargs
    resulting_collection = mongo_collection.insert_one(document_to_insert)
    return resulting_collection
