package com.mongodb;

import org.bson.Document;
import org.bson.conversions.Bson;
import org.eclipse.jetty.util.Fields;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.lang.Object;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Field;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Projections;
import com.mongodb.client.model.Sorts;
import com.mongodb.client.model.UpdateOptions;
import com.mongodb.client.model.Updates;
import com.mongodb.Helpers;

public class MongoDbFinalQ8 {

    public static void main(String[] args) 
    {
// --------------------------------------------------------------------------------------------------------------
// Setting up MongoDB Java Driver
// --------------------------------------------------------------------------------------------------------------               
        // NOTE 1. Creating MongoClient and setting it up
        // MongoClient is the entry point for Mongo db
        // We can give the server address and port in the mongoClient constructor
        // We can also pass Connection string
        // We also have MongoClientOptions where you can build your client options
        
        MongoClient client = new MongoClient();
        
        // Both the database name and collection name is movies
        MongoDatabase db = client.getDatabase("finalQ8");
        MongoCollection<Document> animals = db.getCollection("animals");
        
        Document animal = new Document("animal", "monkey");

        animals.insertOne(animal);
        animal.remove("animal");
        animal.append("animal", "cat");
        animals.insertOne(animal);
        animal.remove("animal");
        animal.append("animal", "lion");
        animals.insertOne(animal);        
    }
}
