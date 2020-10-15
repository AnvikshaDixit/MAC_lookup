# MAC_lookup

**Prerequisite:**
- Docker 



1. Navigate to the path where you have cloned the repository
2. run 
  ```  docker build -t myimage .```
3. Check if my image is present in images or not
    ```docker images```
4. Lastly run 
    ```docker run -ti myimage```


**SECURITY SOLUTIONS :**

Security theft is a major concern nowadays. 
  To ensure we can make sure of the following things :
  
    1. Secure API Access : 
    
        We can have secure API access by doing any of the below-mentioned authentications:
            - HTTP Basic Authentication
            - JSON Web Tokens (JWT) 
            - OAuth
            - User Authorization with API Keys(Used in this repository)
            
    2. Input Validation: They are required to avoid 'sql injection' and data security threat to the customer
    
    3. Response Security Headers: To restrict the type and scope of requests
    
    4. API Client Restrictions: REST service operators should restrict connecting clients to the minimum capabilities required for the service.
