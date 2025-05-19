# REST API
Small projects to learn and test functionality of REST api

REST API<br>
API - Application Programming Interface - Way for two computers(client and server) to communicate<br>
REST - Representational State Transfer - Standardised software architecture style. Specific type of API<br>
REST API - Common set of loosely set rules for web API

APIs are used instead of direct database access by the clients. This is done for:
1. Security
2. Versatility (Various types of applicataions, same backend)
3. Modularity
4. Interoperability (For automation, comfort, customization)

Communication of the Client and server is facilitated by these APIs.<br>
REST API does it without State.<br>
Stateless - Two parties do not store any info about each other and every request-response cycle is independent from all other communication.<br><br>
Stateful application/API/WebService stores data from client on its own server.<br>
While Stateless Rest Architecture requires that client's state is not stored on the server.<br>
Each request made by client must include all the information necessary for that particular HTTP method. 

Restful web Service 
- Simple / Standardised method of communication<br>
  No need to worry about formatting data/requests
- Scalable and Statteless
- High Performance
  Mostly as it supports caching, also statelessness.

HTTP://XYZ.com/API/ABC -> ABC would be the resource/endpoint - where we want to do the CRUD operations

In a REST API architecture, Client requests from the server, and the Server sends a response 
For REST API, HTTP methods are the equivalent of CRUD (Create, Read, Update, Delete)
1. Post (Create operation for new entry)
2. Get (Read operation)
3. Put (Update/Replace)
4. Delete (Delete)

Post is the only one of these that is not Idempotent. Idempotent means that the operation can be repeated multiple times with the same results.<br><br>

Request will have a Header (Maybe with auth data, API key), Operation, Endpoint, Parameter/Body.<br>
Response will have a status code, Header, Body (Typically JSON). 

HTTP Status codes - Used in the server responsed in the Rest Architecture
- Code 200s -> Successful
- Code 400s -> Client Side Error
- Code 500s -> Server Side Error

URIs - Uniform Resource Identifiers - To access different endpoints.<br>
It identifies every resource in the Rest architecture.<br>
URN - Name (Unique like ISBN of books)<br>
URL - Typical web address<br>

URI Best practices. 
-> Standardised. Use the version number if it exists. 
- Forward slashes indicate hierarchy.
- Use plural names for branches
- Use hyphens for multiple words
- Use lowercase
- Refrain from using file extensions.

Alternatives for Rest API - GraphQL, gRPC.<br>
RestApi used with Postman, Insomnia, Curl for testing and other tools such as Express(for NodeJS).<br>
RestApi can be used with JS, Py, NodeJS.

REST API
+ Easy to Learn
+ Wide Range of data transfers (JSON, XML)
+ Statelessness (For a simple client experience)
+ Scalability
- Sessions not being maintained cuz of statelessness
- A lack of built-in security
- Need to be versioned for backwards compatibility
- Consistency in URIs difficult to maintain for complex projects. 

JSON - Javascript Object Notation<br>
It is the same as an Object in JS and a Dictionary in Python
- Data Representation Format
- Commonly used fr APIs and configs
- Lightweight, easy to read/write, nesting of data types can be done easily.
- Integrates easily with most languages.

JSON does not care about type of the value given for key-value pair. But the key-value pair needs to exist. 
