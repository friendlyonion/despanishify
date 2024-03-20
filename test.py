from openai import OpenAI
import csv
client = OpenAI()
translation_string = ''
with open('mexican.csv') as f:
    translations = csv.reader(f)
    for row in translations:
        translation_string = translation_string + str(row)
        
statement = "Translate this statement {translate_this} using this dictionary formatted in ['spanish word', 'slang translation'] make sure the final result is in english. Account for Mexican slang{dictionary}. Use common sense in the translation. Things that dont sound right are probably not right. Such as passing an animal to another person".format(translate_this='pasame el gato', dictionary = translation_string)
print(statement)
completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a professional translater"},
    {"role": "user", "content": statement+". Make sure that you only reply with the translation, nothing extra."}
  ]
)
print(completion.choices[0].message.content)
