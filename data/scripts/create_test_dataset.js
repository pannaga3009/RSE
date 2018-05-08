/**
 Data Cleaning Script 
*/


// Scenario 1: How to get the subset of data from yelp dataset ?

// 1. Load the dataset JSON into mongodb
// 2. Run below query

use dataset;

db.review.aggregate(
   [ { $sample: { size: 100 } } ] // It will fetch 100 records
)

// 3. Export the query result to file

///////////////////////////////////////////////////////////////////////////////////////////



// Scenario 2: How to make Test dataset ?

use dataset;
db.review_test.aggregate(
   [
     { 
       $group : { 
                  _id : "$business_id",
       		        reviews: { 
                        $push: { 
                          text: "$text", 
                          ratings:"$stars",
                          useful:"$useful" 
                        } 
                     } 
                } 
     },
     { 
       $out: "review_group" 
     }
   ],
    {
      allowDiskUse: true
    }
)

