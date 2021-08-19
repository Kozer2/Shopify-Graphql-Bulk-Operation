# Shopify-Graphql-Bulk-Operation
This project was made to gather customer data from the Shopify API. Including the Customer ID field. 
Due to the way the Shopify API limits calls to 250 per request, large store sizes need a way to gather more data. This project uses a Graphql POST request to gather data on all a stores customers. 

![Status Image](https://travis-ci.com/travis-ci/travis-web.svg?branch=master)

To run this Application you will need to get Admin rights to your Shopify store. Steps for which can be found [here](https://help.shopify.com/en/manual/apps/private-apps#enable-private-app-development-from-the-shopify-admin)
Once you have generated the API and received the password you are ready to begin. 

Note: This app does not run automatically, you will need to babysit it. 


### Setup

`pip install pandas`

`pip install requests`

Once setup is completed, you will need to enter your shop name as it appears in the homepage URL of your Shopify Store. Then enter the API password as the token. 
Now you can begin running the code. I suggest you run the functions one at a time. IE: Comment out the second function call and print statements at the bottom and only run the first function. Comment out that function call and prints and now just run the second one. That will give you back the status. Upon completion you can grab the file and open and turn it into a CSV 

