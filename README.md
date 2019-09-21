# Digital Store App

This app for anyone who needs a tool to manage an online store. It supports multiple users with safety features such JWT authentication and easy to use.

A user can create, edit or delete items for a store and register multiple users who can access the DB. 

### Setup

Please 

### Usage

There are 4 endpoints to interact with.

**GET /items**

This endpoint returns all the available items in the store with prices.

**GET /item/<**name**>**

This end point with GET request returns a specific item (<*name>*) from the DB. It requires JWT authentication.

**POST /item/<**name**>**

This endpoint with POST request adds a new item (<*name>*) on the DB.

**DEL /item/<**name**>**

This endpoint with DEL request deletes an item (<*name>*) from the DB.

**PUT /item/<**name**>**

This endpoint with PUT request updates an existing item in the list.

**POST /register**

This endpoint adds a new user to the DB

**POST /auth**

This endpoint returns JWT authentication token required for certain requests. 

