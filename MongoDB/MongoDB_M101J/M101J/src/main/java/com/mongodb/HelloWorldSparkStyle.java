package com.mongodb;
import static spark.Spark.*;

import org.apache.log4j.BasicConfigurator;

import spark.Request;
import spark.Response;
import spark.Route;
import spark.Spark;

public class HelloWorldSparkStyle {
	public static void main(String args[])
	{
		BasicConfigurator.configure();
		get("/", (Request req, Response res) -> "Hello World from Spark");
		/*Spark.get("/", new Route() {
		  	public Object handle(final Request request, final Response response){
            return "Hello World from Spark";
        	}
        });*/
	}
}
