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

   
Mitigation Plan:
1.	For which teammate did you implement “Microservice A”
a.	Antonio Rodriguez 
2.	What is the current status of the microservice?
a.	It is complete and has been tested. 
3.	If the microservice isn’t done, which part’s aren’t done and when will they be done?
a.	Not Applicable.  The microservice is done. 
4.	How is your teammate going to access your microservice?
a.	Antonio can download / clone the code from the GitHub repository and run it locally.  
b.	Linke to repository: https://github.com/joshua-gage-osu/Microservice-A/tree/main
5.	If your teammate cannot access/call your microservice, what should they do? 
a.	If after importing flask and pandas modules the microservice still does not work, Antonio should reach out to me directly by text anytime before 6 pm CST, and may call anytime between 6 pm – 11 pm CST.  
6.	If your teammate cannot access / call your microservice, by when do they need to tell you? 
a.	Please inform me of any issues by text at least 36 hours before the submission deadline. 
7.	Is there anything else your teammate needs to know? 
a.	The current microservice is set to deploy on a debugging / test server locally.  If you want to change this, you will need to change the code at the very bottom of the app.py file to reflect the new location.  
b.	I would make a virtual environment and install the python packages from requirements.txt before trying to test or implement the microservice.  I have assumed that you have an up to date version of python on your local machine, so if you don’t please let me know so we can verify the code still works on an older version. 
c.	Backup plan: If for some reason we cannot get the microservice to work on your machine, I can deploy the web application on either the OSU server or a cloud service until after the final project gets graded.  
