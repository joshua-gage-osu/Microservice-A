Microservice A: Music Practice Set Request
Making the Requests: 
The data can be requested by a POST method to the API endpoints / webservice URL addresses

1.	Requesting the Practice Set:
•	Endpoint: /get_practice_set
•	Method:  POST
•	Request Format:** JSON
•	example:
     {
    "username": "john_doe",
    "level": "Intermediate"
    }
     
•	Response Format:** JSON
•	Example:
   {
    "id": 3,
    "level": "Intermediate",
    "set_name": "Set C",
    "description": "Advanced chords"
  }


  2. Marking a Practice Set as Complete:
•	Endpoint: /update_history
•	Method:  POST
•	Request Format: JSON
•	Example:
    {
    "username": "john_doe",
    "set_id": 3
    }
     
•	Response Format: JSON
•	Example:
   {
    "message": "History updated"
  }
UML Diagram: 
![Microservice A UML](https://github.com/user-attachments/assets/cd5826c8-f5ad-4934-96bb-39fb03621c38)

   

