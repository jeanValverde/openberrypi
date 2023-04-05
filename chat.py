#pip install openai

import os
import openai
 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if  OPENAI_API_KEY is not None :

    openai.api_key = OPENAI_API_KEY

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Me puedes contar un chiste de chile por favor"}
    ]
    )

    print(completion.choices[0].message)
else:
    print("Debe configurar la variable de entorno OPENAI_API_KEY")

