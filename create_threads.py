from openai import OpenAI
client = OpenAI(api_key = "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"
)

message_thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Hello, what is AI?",
      "file_ids": ["file-abc123"],
    },
    {
      "role": "user",
      "content": "How does AI work? Explain it in simple terms."
    },
  ]
)

print(message_thread)
