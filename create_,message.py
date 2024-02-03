from openai import OpenAI
client = OpenAI(api_key = "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"
)

thread_message = client.beta.threads.messages.create(
  ""thread_f3YycG5UbrqXADcYZoKeRIB4"",
  role="user",
  content="How does AI work? Explain it in simple terms.",
)
print(thread_message)
