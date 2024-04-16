#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #3
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with
# standard arrays

#importing some Python libraries
from pymongo import MongoClient
import datetime

def connectDataBase():

    # Creating a database connection object using pymongo

    DB_NAME = "Docs"
    DB_HOST = "localhost"
    DB_PORT = 27017

    try:

        client = MongoClient(host=DB_HOST, port=DB_PORT)
        db = client[DB_NAME]
        print("Successful Connection")
        return db

    except:
        print("Database not connected successfully")

def createDocument(col, docId, docText, docTitle, docDate, docCat):

    # create a dictionary indexed by term to count how many times each term appears in the document.
    # Use space " " as the delimiter character for terms and remember to lowercase them.
    docText = docText.lower()
    word_list = docText.split(" ")  
    dict = {}
    for word in word_list:
        # If the word is already in the dictionary, increment its count
        if word in dict:
            dict[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            dict[word] = 1

    # create a list of objects to include full term objects. [{"term", count, num_char}]
    # --> add your Python code here
    terms = []
    
    for word in dict:
        terms.append({
                "term": word,
                "count": dict.get(word),
                "num_char" : len(word),
            })

    # produce a final document as a dictionary including all the required document fields
    doc = {
            "docID": docId,
            "docText": docText,
            "docTitle": docTitle,
            "docDate": docDate,
            "docCat": docCat, 
            "terms": terms,     
    }

    # insert the document
    col.insert_one(doc)

def deleteDocument(col, docId):

    # Delete the document from the database
    # --> add your Python code here
    col.delete_one({"_id": id})

def updateDocument(col, docId, docText, docTitle, docDate, docCat):

    # Delete the document
    # --> add your Python code here
    col.delete_one({"_id": id})

    # Create the document with the same id
    # --> add your Python code here
    doc = {"_id": id,
            "docID": docId,
            "docText": docText,
            "docTitle": docTitle,
            "docDate": docDate,
            "docCat": docCat,      
    }
    col.insert_one({"_id": id}, doc)
    

def getIndex(col):

    # Query the database to return the documents where each term occurs with their corresponding count. Output example:
    # {'baseball':'Exercise:1','summer':'Exercise:1,California:1,Arizona:1','months':'Exercise:1,Discovery:3'}
    # ...
    # --> add your Python code here
    
    # Dictionary to store term counts
    term_counts = {}

    # Iterate over each document in the collection
    for doc in col.find():
        # Extract terms and their counts from the document
        terms = doc.get("terms", [])
        for term_info in terms:
            term = term_info["term"]
            count = term_info["count"]
            # Add the term and its count to the term_counts dictionary
            if term in term_counts:
                term_counts[term].append((doc["docTitle"], count))
            else:
                term_counts[term] = [(doc["docTitle"], count)]

    return term_counts
    
    
    