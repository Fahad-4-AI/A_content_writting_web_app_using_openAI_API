import openai
import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY

# Set up the OpenAI API client

 
name = "AI"

def defination():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"What is the definition of {name}?",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        )
    result = response['choices'][0]['text']
    print(result)
defination()    
    
