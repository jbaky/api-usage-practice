import openai

openai.api_key = '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'
prompt = input('Enter your command: ')
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

text = response.get('choices')[0].get('text')
print(text)