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

public class MongoDbCrudOperations {

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
        MongoDatabase db = client.getDatabase("movies");
        MongoCollection<Document> coll = db.getCollection("movies");
        
        // NOTE 2. Delete the existing collection
        coll.drop();
        
        // NOTE 3. Create a document
        Document movie1 = new Document("title", "Usual Suspects")
                          .append("year", 1999)
                          .append("imdb", "tty1999");
        
// --------------------------------------------------------------------------------------------------------------
// Insert and InsertMany()
// --------------------------------------------------------------------------------------------------------------               
        
        // NOTE 4. Using insertOne()
        coll.insertOne(movie1);

        Document movie2 = new Document("title", "Titanic")
                          .append("year", 2010)
                          .append("imdb", "tty2010");
        
        Document movie3 = new Document("title", "Snow Day")
                          .append("year", 1990)
                          .append("imdb", "tty1990");

        Document movie4 = new Document("title", "No Country for Old Men")
                          .append("imdb", "tty1996");
        
        movie4.append("year", 1996);

        // NOTE 5. Using insertMany() and asList()
        coll.insertMany(Arrays.asList(movie2, movie3, movie4));
        
        // NOTE 6. Print Json document using Utility function
        //Helpers.printJson(movie2);
        
// --------------------------------------------------------------------------------------------------------------
// Find and Count
// --------------------------------------------------------------------------------------------------------------               
        // NOTE 7. Get one document and print it
        Document firstMovie = coll.find().first();
        //Helpers.printJson(firstMovie);
        
        // NOTE 8. Get all documents as list and print them
        List<Document> movieDocs = coll.find().into(new ArrayList<Document>());
        for (Document movieDoc : movieDocs)
        {
            //Helpers.printJson(movieDoc);
        }
        
        // NOTE 9. Iterating through Cursor
        // MongoCursor is used to iterate if the number of collection is large
        MongoCursor<Document> cur = coll.find().iterator();
        try
        {
            while (cur.hasNext())
            {
                Document nextDoc = cur.next();
                //Helpers.printJson(nextDoc);
            }
        }
        finally {
            cur.close();
        }
        
        // NOTE 10. Count the number of collections
        System.out.println("Collection Count: " + coll.count());
        
// --------------------------------------------------------------------------------------------------------------
// QUERYING with Filters
// --------------------------------------------------------------------------------------------------------------
        // NOTE 11. Filters to find and count
        Bson filter = new Document("title", "Titanic");
        //List<Document> movieDocs = coll.find(filter).into(new ArrayList<Document>());
        System.out.println("Collection Count: " + coll.count(filter));
        
        Bson filter2 = new Document("title", "Titanic")
                       .append("year", new Document("$gt", 2000)
                                       .append("$lt", 2015));
        System.out.println("Collection Count: " + coll.count(filter2));
        
        // NOTE 12. Builder for Filters
        Bson filter6 = Filters.eq("year", 2000);
        Bson filter7 = Filters.and(Filters.eq("title", "Titanic"), 
                                   Filters.gt("year", 2000),
                                   Filters.lt("year", 2015));
        
        // NOTE 13. Exclude certain field from displaying it
        // Say we don't want imdb field
        //Bson projection = new Document("imdb", 0); // 0 means DON'T include "imdb"
        Bson projection2 = new Document("imdb", 0)
                           .append("_id", 0); 
        
// --------------------------------------------------------------------------------------------------------------
// QUERYING with Projections
// --------------------------------------------------------------------------------------------------------------       
        // NOTE 14. Making use of Project class
        // Same as (13) but using Projection class
        Bson projection3 = Projections.exclude("imdb", "_id");
        
        // NOTE 15. By default "_id" gets INCLUDED if it is not excluded
        Bson projection4 = Projections.include("imdb", "title");
        
        // NOTE 16. Using both exclude and include
        // Use "fields" to have both include and exclude
        Bson projection5 = Projections.fields(Projections.include("imdb", "title"), 
                                              Projections.exclude("_id"));
        
        // NOTE 17. Using "excludeId" to exclude id
        Bson projection6 = Projections.fields(Projections.include("imdb", "title", "year"), 
                                              Projections.excludeId());

        
        List<Document> movieDocs2 = coll.find()
                                        .projection(projection6)
                                        .into(new ArrayList<Document>());
        for (Document movieDoc : movieDocs2)
        {
        //  Helpers.printJson(movieDoc);
        }
        
        
// --------------------------------------------------------------------------------------------------------------
// Sort Skip and Limit
// --------------------------------------------------------------------------------------------------------------               
        // NOTE 18. Sorting using a criteria
        Bson criteria7= new Document("year", 1);
        // Bson criteria7= new Document("year", 1).append("title", -1);
        
        // NOTE 19. Using Builder to Sort
        Bson criteria8 = Sorts.ascending("year");
        Bson criteria9 = Sorts.orderBy(Sorts.ascending("year"), Sorts.descending("title"));
        
        // NOTE 20. Using "limit" to limit the number of results
        // NOTE 21. Using "skip" to limit the number of results

        List<Document> movieDocs3 = coll.find()
                                        .projection(projection6)
                                        .sort(criteria7)
                                        .limit(2)       // Limit only the first two entries
                                        .skip(1)        // Skip the first entry. So start from second
                                        .into(new ArrayList<Document>());
        
        for (Document movieDoc : movieDocs3)
        {
        //  Helpers.printJson(movieDoc);
        }       
        
// --------------------------------------------------------------------------------------------------------------
// Update and Replace
// --------------------------------------------------------------------------------------------------------------               
        // NOTE 22. The below will replace "Titanic" row with new one.
        // "replaceOne" is a WHOLE-CELL replacement
        // So all the old values i.e. "imdb" and "year" will get removed as well
        //coll.replaceOne(Filters.eq("title", "Titanic"), new Document("title", "Titanic2")
        //                                              .append("Updated", true));
        
        // NOTE 23. updateOne
        /*coll.updateOne(Filters.eq("title", "Titanic"), new Document("$set",
                                                                            new Document("title", "Titanic3")
                                                                            .append("Updated2", true)));
        */
        
        // NOTE 24. Update using Updates class
        coll.updateOne(Filters.eq("title", "Usual Suspects"), Updates.combine(Updates.set("year", 1950),
                                                                              Updates.set("Updated", true)));
        
        // NOTE 25. Upserts i.e. Insert new document if mising 
        coll.updateOne(Filters.eq("title", "Panchathandhiram"), Updates.combine(Updates.set("_id", 1),
                                                                                Updates.set("year", 2005),
                                                                                Updates.set("imdb", "ttyassf"),
                                                                                Updates.set("Updated", true)),
                                                                new UpdateOptions().upsert(true));

        // NOTE 23b / 26. Update imdb of the movie that has _id = 1
        coll.updateOne(new Document("_id", 1), new Document("$set", 
                                                            new Document("imdb", "ppyasdf")));

        // NOTE 27. UpdateMany
        coll.updateMany(Filters.gte("year", 2000), Updates.inc("year", 5));
        
// --------------------------------------------------------------------------------------------------------------
// Delete
// --------------------------------------------------------------------------------------------------------------               
        // NOTE 28. deleteOne and deleteMany
        // deleteOne will delete just one entry even if multiple entries are present
        coll.deleteOne(Filters.gte("year", 2005));
        
        coll.deleteMany(Filters.gte("year", 2005));
        
        for (Document movieDoc : coll.find().into(new ArrayList<Document>()))
        {
            Helpers.printJson(movieDoc);
        }           
            
// --------------------------------------------------------------------------------------------------------------
// HOMEWORK 2.3
// --------------------------------------------------------------------------------------------------------------               
        System.out.println("Homework Week 2");
        MongoClient client2_3 = new MongoClient();
        
        // Both the database name and collection name is movies
        MongoDatabase db2_3 = client2_3.getDatabase("students");
        MongoCollection<Document> collection2_3 = db2_3.getCollection("grades");

        Bson filter2_3 = new Document("type", "homework");
        Bson criteria2_3 = Sorts.orderBy(Sorts.ascending("student_id"), Sorts.ascending("score"));

        List<Document> movieDocs2_3 = collection2_3.find(filter2_3)
                                                 .sort(criteria2_3)
                                                 .into(new ArrayList<Document>());

        System.out.println("Entire collection after applying homework and sort filter");
        for (Document movieDoc : movieDocs2_3)
        {
            //Helpers.printJson(movieDoc);
        }
        
        boolean newStudent = true;
        int prevStudId = -1;
        
        System.out.println("Deleting entries with lowest score");
        for (Document movieDoc : movieDocs2_3)
        {
            int curStudId = (Integer) movieDoc.get("student_id");
            if (prevStudId != curStudId)
            {
                //Helpers.printJson(movieDoc);
                // Delete the entry and the scores are sorted by asceding
                collection2_3.deleteOne(Filters.eq("_id", movieDoc.getObjectId("_id")));
                //collection2_3.deleteOne(Filters.eq("type", "homework"));

                newStudent = false;
            }
            else
            {
                newStudent = true;
            }
            
            prevStudId = curStudId;
        }

        List<Document> movieDocs2_3b = collection2_3.find()
                                                    .into(new ArrayList<Document>());

        System.out.println("Aftering deleting the entries");
        for (Document movieDoc : movieDocs2_3b)
        {
            //Helpers.printJson(movieDoc);
        }
        
        System.out.println("Grades Count: " + collection2_3.count());

        List<Document> movieDocs2_3c = collection2_3.find()
                                                    .sort(Sorts.descending("score"))
                                                    .skip( 100 )
                                                    .limit( 1 )
                                                    .into(new ArrayList<Document>());

        for (Document movieDoc : movieDocs2_3c)
        {
            //Helpers.printJson(movieDoc);
        }
        
        // db.grades.find().sort( { 'score' : -1 } ).skip( 100 ).limit( 1 )
        // db.grades.find( { }, { 'student_id' : 1, 'type' : 1, 'score' : 1, '_id' : 0 } ).sort( { 'student_id' : 1, 'score' : 1, } ).limit( 5 )
        // db.grades.aggregate( { '$group' : { '_id' : '$student_id', 'average' : { $avg : '$score' } } }, { '$sort' : { 'average' : -1 } }, { '$limit' : 1 } )

// --------------------------------------------------------------------------------------------------------------
// HOMEWORK 3.1
// --------------------------------------------------------------------------------------------------------------               
        System.out.println("Homework Week 3");
        MongoClient client3_1 = new MongoClient();
        
        MongoDatabase db3_1 = client3_1.getDatabase("school");
        MongoCollection<Document> collection3_1 = db3_1.getCollection("students");

        Bson filter3_1 = new Document("scores.type", "homework");
        //Bson criteria3_1 = Sorts.orderBy(Sorts.ascending("student_id"), Sorts.ascending("scores.score"));
        Bson criteria3_1 = Sorts.orderBy(Sorts.ascending("student_id"));

        Bson filter3_1a = Filters.eq("scores.type", "homework");
        Bson projection3_1 = Projections.fields(Projections.include("_id", "name"), 
                                                Projections.exclude("_id"));

        /*List<Document> studentDocs3_1 = collection3_1.find(filter3_1)
                                                     .into(new ArrayList<Document>());
                                                     */

        List<Document> studentDocs3_1 = collection3_1.find()
                                                     .sort(criteria3_1)
                                                     .projection(projection3_1)
                                                     .into(new ArrayList<Document>());

        System.out.println("Entire collection sorted by student id");
        for (Document studentDoc : studentDocs3_1)
        {
            Helpers.printJson(studentDoc);
        }
        
        /*
        boolean newStudent = true;
        int prevStudId = -1;
        
        System.out.println("Deleting entries with lowest score");
        for (Document studentDoc : studentDocs3_1)
        {
            int curStudId = (Integer) studentDoc.get("student_id");
            if (prevStudId != curStudId)
            {
                Helpers.printJson(studentDoc);
                // Delete the entry and the scores are sorted by asceding
                collection3_1.deleteOne(Filters.eq("_id", studentDoc.getObjectId("_id")));
                //collection3_1.deleteOne(Filters.eq("type", "homework"));

                newStudent = false;
            }
            else
            {
                newStudent = true;
            }
            
            prevStudId = curStudId;
        }

        List<Document> studentDocs3_1b = collection3_1.find()
                                                    .into(new ArrayList<Document>());

        System.out.println("Aftering deleting the entries");
        for (Document studentDoc : studentDocs3_1b)
        {
            Helpers.printJson(studentDoc);
        }
        
        System.out.println("Grades Count: " + collection3_1.count());

        List<Document> studentDocs3_1c = collection3_1.find()
                                                    .sort(Sorts.descending("score"))
                                                    .skip( 100 )
                                                    .limit( 1 )
                                                    .into(new ArrayList<Document>());

        for (Document studentDoc : studentDocs3_1c)
        {
            //Helpers.printJson(studentDoc);
        }
        */
        
        // db.grades.find().sort( { 'score' : -1 } ).skip( 100 ).limit( 1 )
        // db.grades.find( { }, { 'student_id' : 1, 'type' : 1, 'score' : 1, '_id' : 0 } ).sort( { 'student_id' : 1, 'score' : 1, } ).limit( 5 )
        // db.grades.aggregate( { '$group' : { '_id' : '$student_id', 'average' : { $avg : '$score' } } }, { '$sort' : { 'average' : -1 } }, { '$limit' : 1 } )
    }
}
