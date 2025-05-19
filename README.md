# REST API

Small projects to learn and test functionality of REST API.

---

## REST API

**API** - Application Programming Interface — A way for two computers (client and server) to communicate  
**REST** - Representational State Transfer — A standardized software architecture style; a specific type of API  
**REST API** - A common set of loosely defined rules for web APIs

---

## Why Use APIs Instead of Direct Database Access?

APIs are used instead of direct database access by the clients. This is done for:

1. **Security**
2. **Versatility** (Various types of applications, same backend)
3. **Modularity**
4. **Interoperability** (For automation, comfort, customization)

---

## Statelessness in REST

Communication between the client and server is facilitated by these APIs.  
REST API does it without state.

- **Stateless** – Two parties do not store any info about each other. Every request-response cycle is independent from all other communication.
- **Stateful** – Stores data from the client on the server.

While Stateless REST architecture requires that the client's state is not stored on the server,  
**each request made by the client must include all the information necessary for that particular HTTP method.**

---

## RESTful Web Service

- Simple / Standardized method of communication  
  → No need to worry about formatting data/requests  
- Scalable and Stateless  
- High Performance  
  → Mostly because it supports caching and is stateless

---

## REST API Endpoint Structure

Example:  
`HTTP://XYZ.com/API/ABC` → `ABC` would be the **resource/endpoint** — where we want to do the CRUD operations.

---

## HTTP Methods = CRUD Operations

In a REST API architecture, the client requests from the server, and the server sends a response.  
The following HTTP methods correspond to CRUD operations:

1. **POST** – Create operation for new entry
2. **GET** – Read operation
3. **PUT** – Update / Replace
4. **DELETE** – Delete

**Note:**  
`POST` is the only one of these that is **not idempotent**.  
_Idempotent_ means that the operation can be repeated multiple times with the same results.

---

## REST Request and Response Structure

**Request includes:**
- Header (possibly with authentication data, API key)
- Operation
- Endpoint
- Parameter / Body

**Response includes:**
- Status Code
- Header
- Body (typically in JSON)

---

## HTTP Status Codes

Used in the server response in the REST architecture:

- **2xx** – Successful
- **4xx** – Client-Side Error
- **5xx** – Server-Side Error

---

## URIs (Uniform Resource Identifiers)

Used to access different endpoints.  
URIs identify every resource in the REST architecture.

- **URN** – Name (Unique like ISBN of books)
- **URL** – Typical web address

### URI Best Practices

- Standardized: Use the version number if it exists
- Forward slashes indicate hierarchy
- Use **plural names** for branches
- Use **hyphens** for multiple words
- Use **lowercase**
- Refrain from using file extensions

---

## Alternatives to REST API

- **GraphQL**
- **gRPC**

---

## Tools

- **Postman**, **Insomnia**, **Curl** — For testing
- **Express (for NodeJS)** — Lightweight framework
- REST API can be used with **JavaScript**, **Python**, **NodeJS**, etc.

---

## Pros and Cons of REST API

### Advantages:
- Easy to learn
- Wide range of data transfers (JSON, XML)
- Statelessness → Simple client experience
- Scalable

### Disadvantages:
- Sessions not being maintained due to statelessness
- Lack of built-in security
- Need to be versioned for backward compatibility
- Consistency in URIs can be difficult to maintain for complex projects

---

## JSON (JavaScript Object Notation)

- Data representation format
- Commonly used for APIs and configurations
- Lightweight, easy to read/write
- Supports nesting of data types
- Integrates easily with most languages

JSON is the same as an **object in JavaScript** and a **dictionary in Python**.  
It does **not** care about the type of the value given for a key-value pair, but the key-value pair **must exist**.

---
