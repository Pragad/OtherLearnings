vals = db.albums.aggregate( [  { '$unwind': '$images' } ] ).map(function(albums){return albums.images;})
cursor = db.images.find({_id : {$nin : vals}});
while(cursor.hasNext()){
    printjson(cursor.next());
}
