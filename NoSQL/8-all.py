#!/usr/bin/env python3
""" This is a Python function
that lists all documents in a collection """


def list_all(mongo_collection):
    """ This function returns an empty list
    if no document in the collection, assuming that
    mongo_collection will be the pymongo collection object """

    documents = list(mongo_collection.find())
    return documents
