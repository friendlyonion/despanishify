from openai import OpenAI
import csv
client = OpenAI()
translation_string = ''
with open('mexican.csv') as f:
    translations = csv.reader(f)
    for row in translations:
        translation_string = translation_string + str(row)
        
statement = "Translate this statement {translate_this} using this dictionary{dictionary}".format(translate_this='Pasame el jack', dictionary = translation_string)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a professional translater"},
    {"role": "user", "content": statement+". Make sure that you only reply with the translation, nothing extra."}
  ]
)
print(completion.choices[0].message.content)
