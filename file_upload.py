from openai import OpenAI
client = OpenAI(api_key = "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"
)

client.files.create(
  file=open("test.pdf", "rb"),
  purpose="assistants"
)


# file_id = "file-xfFe9kHyuV8m1MRDNUgsdlBZ"