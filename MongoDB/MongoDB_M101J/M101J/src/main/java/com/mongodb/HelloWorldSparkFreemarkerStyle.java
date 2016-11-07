package com.mongodb;

import static spark.Spark.get;

import java.io.IOException;
import java.io.StringWriter;
import java.util.HashMap;
import java.util.Map;

import org.apache.log4j.BasicConfigurator;
import org.bson.Document;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

import freemarker.core.ParseException;
import freemarker.template.Configuration;
import freemarker.template.MalformedTemplateNameException;
import freemarker.template.Template;
import freemarker.template.TemplateException;
import freemarker.template.TemplateNotFoundException;
import spark.Request;
import spark.Response;
import spark.Route;
import spark.Spark;

public class HelloWorldSparkFreemarkerStyle {
	public static void main(String args[])
	{
		final Configuration configuration = new Configuration();
		configuration.setClassForTemplateLoading(
				HelloWorldSparkFreemarkerStyle.class, "/");
		
		BasicConfigurator.configure();
		
		// NOTE 1. Setup MongoDB
		MongoClient client = new MongoClient();
		
		// Both the database name and collection name is movies
		MongoDatabase db = client.getDatabase("movies");
		final MongoCollection<Document> coll = db.getCollection("movies");
		
		// NOTE 2. Delete the existing collection
		coll.drop();		
		
		// NOTE 3. Add an element to the document
		coll.insertOne(new Document("name", "MongoDB Sample by Prag"));
		
        Spark.get("/", new Route() 
        {
            public Object handle(final Request request, final Response response)
            {
            	StringWriter strWriter = new StringWriter();
        		try 
        		{
        			Template helloTemplate = configuration.getTemplate("hello.ftl");
        			
        			// NOTE 3. Adding a name directly
        			//Map<String, Object> helloMap = new HashMap<String, Object>();
        			//helloMap.put("name", "Prag Thiru");
        			
        			// NOTE 4. Fetching a name from  MongoDB
        			Document doc = coll.find().first();
        			try 
        			{
        				// NOTE 3b.
        				//helloTemplate.process(helloMap, strWriter);
        				
        				helloTemplate.process(doc, strWriter);
        			} 
        			catch (TemplateException e) 
        			{
        				// TODO Auto-generated catch block
        				e.printStackTrace();
        			}
        			
        		} 
        		catch (Exception e) 
        		{
        			// TODO Auto-generated catch block
        			e.printStackTrace();
        		}
        		
				return strWriter;
            }
        });
	}
}
