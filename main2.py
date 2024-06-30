from openai import OpenAI
import json

# Initialize the OpenAI API client with your API key


# Define the dataset for fine-tuning
# dataset = [
#     {
#         "prompt": "I got F on my final exam for Algebra II",
#         "completion": "I'm sorry to hear that. Failing an exam can be really discouraging, but it's important to remember that one setback doesn't define your overall abilities or future success."
#     }
# ]
#
# # Write the dataset to a JSONL file
# with open('fine_tune_data.jsonl', 'w') as f:
#     for item in dataset:
#         f.write(json.dumps(item) + '\n')
#
# # Upload the dataset to OpenAI
# response = client.files.create(file=open('fine_tune_data.jsonl', 'rb'), purpose='fine-tune')
# print(response)
# file_id = "file-H1gKFRmGKdCvWNQ7ptjTN30P"
# # Create a fine-tuning task
# client.fine_tuning.jobs.create(
#     training_file=file_id,
#     model='gpt-3.5-turbo'
)
def get_response(prompt):
    client = OpenAI(api_key='sk-proj-9BoJxrxzdiBr8FspiCoTT3BlbkFJIpwKsp5JqQB7ng8ooVFE')
    messages = [{'role': 'user', 'content': prompt}]
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = messages,
        temperature=0
    )
    return response.choices[0].message.content
#print(response.choices[1].message.content)

# Low temperature:
# - the model becomes more deterministic
# - predictable response. (low randomness)
# - accurate, reliable responses.

# High Temperature:
# - The model becomes more random
# - generate more diverse and creative responses


# temperature = 0, I'm sorry to hear that. Is there anything I can do to help you study or prepare for future exams?
# temperature= 0.7: I'm sorry to hear that. It's important to remember that one exam does not define your abilities or intelligence. It's okay to feel disappointed, but try to use this as a learning experience and take steps to improve for future exams. Don't be too hard on yourself. You can always seek help from your teacher or a tutor if needed. Keep pushing forward and stay positive.