# URL SUMMARIZER
This is a URL summarizer application which can summarize the content of a URL, if it is text based. The frontend of this application is made with react, the backend consist of Springboot and fastAPI. Here the frontend sends requests to the springboot server. The springboot server act as a middleman and sends the requests to the fastAPI which performs the actual summarization task using thisrd party API 'SMMRY API'.
The fastAPI server then sends the response to springboot server which eventually send it back to frontend. The resquest history is also recorded by the springboot server in PostgreSQL database.

Links to other parts of the project:
1. Link to react frontend: https://github.com/Parna2000/url-summarizer-frontend/tree/main
2. Link to springBoot server: https://github.com/Parna2000/url-summarizer/tree/main/backend/Spring-Boot

## FASTAPI-SERVER FOR URL SUMMARIZER
This is the fastapi-server which perform the actual summarization task by interacting with a third party API 'SMMRY API'.
To run this file locally, follow these steps:
1. Fork the repository.
2. Clone the repository to the local environment.
3. Generate an api-key from SMMRY API and replace <your-api-key> with that in `services/summarizer.py`
4. Install dependencies in requirements.txt.
5. Run `uvicorn main:app --reload`

Hope you enjoy and like my project!
