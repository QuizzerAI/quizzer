import os
from typing import List
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.beta import Assistant, Thread
from openai.types.beta.threads import Message
from openai.types.beta.threads.run import Run
from openai.types.file_object import FileObject


class Quizzer:
    __client: OpenAI
    __assistant: Assistant
    __file_ids: List[str] = []
    __threads: List[str] = []

    def __init__(self):
        load_dotenv()
        __assistant_id = os.getenv("ASSISTANT_ID")
        self.__client = OpenAI()
        self.__assistant = self.__client.beta.assistants.retrieve(__assistant_id)

    def __del__(self):
        self.__clean_up()

    def __clean_up(self):
        for file_id in self.__file_ids:
            self.__client.files.delete(file_id)
        for thread_id in self.__threads:
            self.__client.beta.threads.delete(thread_id)

    def __upload_file(self, path_to_doc: Path) -> FileObject:
        file = self.__client.files.create(
            file=open(path_to_doc, "rb"),
            purpose="assistants"
        )
        self.__file_ids.append(file.id)
        return file
    
    def __create_thread(self) -> Thread:
        thread = self.__client.beta.threads.create()
        self.__threads.append(thread.id)
        return thread
    
    def __forge_message(self, thread: Thread, file: FileObject) -> Message:
        message = self.__client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content="Analyze this document and generate a list of questions and answers.",
            attachments=[{"file_id": file.id, "tools":[{"type": "file_search"}]}]
        )
        return message
    
    def __run_thread(self, thread: Thread) -> Run:
        run = self.__client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=self.__assistant.id,
        )
        return run
    
    def __get_last_message_text(self, thread: Thread) -> str:
        messages = self.__client.beta.threads.messages.list(
            thread_id=thread.id
        )
        return messages.data[0].content[0].text.value

    def quizzify(self, path_to_doc: Path) -> str:
        file = self.__upload_file(path_to_doc)
        thread = self.__create_thread()
        self.__forge_message(thread, file)
        run = self.__run_thread(thread)
        if run.status == 'completed': 
            return self.__get_last_message_text(thread)
        else:
            raise Exception("Error in the response status: " + run.status)
