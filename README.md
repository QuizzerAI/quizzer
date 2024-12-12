# Quizzer

**Quizzer** is an AI tool that allows you to create custom quizzes directly from your study material.

## How it works

**Quizzer** consists of 3 main components:

1. `quizzer.py`: this script transforms your **pdf** files into **json** files containing the questions. This type of file is called **airesponse**. It is the only script that uses AI.
2. `packer.py`: this script transforms your **airesponse** files into **json** files containing the questions in a more manageable format. This format is called **quizpack**.
3. `quiz.py`: this script reads your **quizpack** files and presents the test to you.

So, to take a test, you need to follow a few steps:

```txt
file.pdf --[quizzer.py]--> file.airesponse.json --[packer.py]--> file.quizpack.json
```

## Installation

 > WARNING
 > These operations are only required if you want to use the `quizzer.py` script.
 > If you only want to use `quizpack` files without generating new ones, you can skip the installation.

Once you have downloaded the repository, you just need to install the required packages by going to the repo folder and running

```sh
pip install -r requirements.txt
```

After running the command, you will need to access the OpenAI API dashboard and create a new assistant. Select the desired model (suggested: `gpt-4o-mini`) and enter the content of the `system.prompt` file under the _System instructions_ section.

Once this is done, you will need to create a `.env` file in the root of the repo folder and insert two lines structured as follows:

```sh
OPENAI_API_KEY=sk-...MA
ASSISTANT_ID=asst_...0R
```

Obviously replacing with the corresponding values that you can find on your dashboard.

After this, make sure you have credit on OpenAI. With this configuration, the script is very economical; I was able to test all the material for the Computer Networks course for only €0.02. Choosing to use `gpt-4o` might get you better-structured quizzes, but the cost is 10 times higher.

## How to use it

Let's see how to start with your pdf file and get to taking the quiz on the covered topics.

### `quizzer.py`

This command must receive the name of the file to be analyzed as an argument; it then prints the result to the output. An example of use:

```sh
./quizzer.py Slides/lesson16.pdf > lesson16.airesponse.json
```

### `packer.py`

This command receives an _airesponse_ file on the pipe and prints the associated quizpack. Example:

```sh
cat lesson16.airesponse.json | ./packer.py > lesson16.quizpack.json
```

### `quiz.py`

This command receives a _quizpack_ file on the pipe and starts the associated quiz. Example:

```sh
cat lesson16.quizpack.json | ./quiz.py
```

## Why pipes

During testing, it was the simplest solution to verify that each component behaved as expected. Pipes allow you to concatenate multiple commands into a more complete one. In the future, it will definitely be necessary to support input and output on files via arguments.

## How to contribute

Anyone who wants to contribute is free to do so in any way: with suggestions, pull requests, writing, translating, and organizing documentation, and in any other way!

## What's next?

In addition to solving stability issues related to AI responses, it will be necessary to expand the toolset with scripts that allow more freedom in managing quizpack files, so that they can be rearranged (both in an orderly and random manner), filtered, mapped, merged, and split. Improving the tool's setup phase with automatic installation scripts and OpenAI API configuration will also be necessary. Additionally, improving the flexibility of the existing tools will be another very useful step to make this tool even more convenient: allowing multiple input files as arguments, specifying an output file, using asynchronous functions to parallelize calls to OpenAI; these are just some of the ideas to improve Quizzer.
