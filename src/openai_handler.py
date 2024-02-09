import openai
from google.cloud import secretmanager


def openai_handler(prompt):
   
# GCP project in which to store secrets in Secret Manager.
    project_id = "formal-stratum-411512"

# ID of the secret to access.
    secret_id = "OPENAI_API_KEY"

# Version of the secret to access.
    secret_version = "1"  # Assuming you want to access the first version

# Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

# Form the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{secret_version}"

# Access the secret version.
    response = client.access_secret_version(request={"name": name})

# Extract the payload as a string.
    OPENAI_API_KEY = response.payload.data.decode("UTF-8")
# Initialize OpenAI
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct", 
    prompt=prompt, 
    max_tokens=150
    )
    return response
    