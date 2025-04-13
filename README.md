# Suggestion - API

This is the backend/API of Suggestion - an OpenAI GPT 3.5 LLM-powered web application that suggests helpful mental health guidance for a hypothetical patient facing challenge(s) ([_Suggestion_]) (https://suggestion-ui.vercel.app/). The web backend/API of Suggestion is a deployed Docker container within an active Amazon Lambda serverless function that receives JSON POST requests from the frontend/UI of Suggestion (https://github.com/ah-berry/suggestion-ui).

## Table of Contents

- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Contact](#contact)

## Technologies Used

To be more specific, the backend/API of Suggestion is a FastAPI (scaffolded by Magnum) application with a single POST request "/suggestion" endpoint that uses LlamaIndex + OpenAI GPT 3.5 LLM model for suggestion text generation. The primary technologies used for the backend/API of Suggestion are as follows:

- Python v3.X
- FastAPI v0.115.12
- LlamaIndex v0.12.30
- OpenAI v1.73.0
- Amazon Lambda (Deployment)

## Setup

1. Open your terminal and `git clone` the GitHub repository URL in your desired directory.
2. Navigate to the cloned directory with `cd <cloned_repository>`.
3. It is highly recommended to use a Python virtual environment management tool like [_pipenv_](https://pipenv.pypa.io/en/latest/) for project-specific dependencies/libraries isolation purposes among other uses.
4. Create the virtualenv (with the Pipefile) and activate it with `pipenv shell`.
5. Install the dependencies with `pipenv install fastapi llama-index openai magnum python-dotenv`.
6. You can create a version of the "get_suggestion" function in `api_serverless/main` where you pass in a mock user_message (and set your OPEN_API_KEY environmental variable in a .env file in the root directory), invoke the Amazon Lambda function, and print out the response for testing. Let me know if you would like my Open AI key (it was only $5 and being used for this project) for the environmental variable and to allow your localhost as an allowed origin on the Lambda function to accept your requests.

## Contact

The application was created by yours truly! Feel free to follow me on [_LinkedIn_](https://www.linkedin.com/in/ahmed-gorashi-546447b5/) and let me know if you liked using Suggestion!
