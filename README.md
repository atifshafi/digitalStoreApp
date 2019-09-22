# Digital Store App

This app for anyone who needs a tool to manage an online store. It supports multiple users with safety features such JWT authentication and easy to use.

A user can create, edit or delete items for a store and register multiple users who can access the DB. 

## Setup

Please run the requirements.txt file.

## Usage

There are 4 endpoints to interact with.

**GET /items**

This endpoint returns all the available items in the store with prices.

**GET /item/<**name**>**

This end point with GET request returns a specific item (<*name>*) from the DB. It requires JWT authentication.
Add "Authorization" as a key and "JWT XXX", where "XXX" is the access token, as the value under Headers.


**POST /item/<**name**>**

This endpoint with POST request adds a new item (<*name>*) on the DB.

Use the following JSON body as an example:

    {
	"price":15.99
    }
    
**DEL /item/<**name**>**

This endpoint with DEL request deletes an item (<*name>*) from the DB.

**PUT /item/<**name**>**

This endpoint with PUT request updates an existing item in the list.

Use the following JSON body as an example:

    {
	"price":15.99
    }

**POST /register**

This endpoint adds a new user to the DB.

Use the following JSON body as an example:

    {   
	"username":"atifshafi",
	"password":"asdf"
    }

**POST /auth**

This endpoint returns JWT authentication token required for certain requests. 

Use the following JSON body as an example:

    {   
	"username":"atifshafi",
	"password":"asdf"
    }
    
*Note that in order to get access token, username and password needs to be registered using POST register endpoint.*
