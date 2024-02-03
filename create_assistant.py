from openai import OpenAI


client = OpenAI(api_key = "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"
)

file = "file/test.pdf"

def file_upload(file):
    file = client.files.create(
        file=open(file, "rb"),
        purpose="assistants"
    )

    # print(file)
    return file.id

def assistant_creator():
    my_assistant = client.beta.assistants.create(
        instructions="너는 목회지원 서비스를 제공하는 인공지능이야. 목사님들의 여러 사역을 도와주는 역할을 하는거야. 특히 목사님들이 설교를 작성할때, 많은 성경구절을 참고하고, 성경이야기를 참고해. 그리고 적절한 이야기들을 설교에 적용해. 이를 예화라고 하지. 너는 이 예화, 이야기들을 잘 찾아주는 목회 비서 역할을 하는거야.",
        name="목회지원",
        tools=[{"type": "retrieval"}],
        model="gpt-3.5-turbo-1106",
        file_ids=["file-xfFe9kHyuV8m1MRDNUgsdlBZ"],
    )
    print(my_assistant)

    return my_assistant.id
    
# my_assistant_id = assistant_creator()


"asst_o6ct3M2Ot3sBn56G3U3pqh9S"

###########

empty_thread = client.beta.threads.create()
print(empty_thread)

"thread_5iXWqxm8uiqNBf8MdZUMATnc"