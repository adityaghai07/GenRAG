# GenRAG

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

GenRAG is a terminal tool designed to set up a Retrieval-Augmented Generation Pipeline locally from scratch, without utilizing any high-level frameworks like LangChain or vector databases. It includes features such as recursive text splitting, chunking, and building embeddings. The embeddings are stored in a CSV file,without using any Vector Databases and searching is based on cosine similarity.

## Features

- Recursive text splitting
- Text chunking
- Building embeddings
- Storing embeddings in a CSV file
- Searching based on cosine similarity
- Inference from local LLM/API


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/adityaghai07/GenRAG.git
    cd GenRAG
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Add a PDF file to the `data` folder and change the path in the script as necessary.
2. Create embeddings by running:
    ```sh
    python3 create_embeddings.py
    ```
   You should see a CSV file generated in the `data` folder.

3. Run the main script:
    ```sh
    python3 main.py
    ```
   Enter your query when prompted.




## LLM Response

You can use both a local LLM or an LLM from an API like Gemini for generating responses.

- **Local LLM**: If you have the capability to run a local LLM, you can use it for generating responses. Cause mine is too slow :(

- **LLM from API**: If your system is not powerful enough for local inference, you can use an API like Gemini. To do this, create a `.env` file and pass the Gemini API key.

### Using Gemini API

1. Create a `.env` file in the root directory of the project.
2. Add your Gemini API key to the `.env` file:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```
3. The system will use the API key for generating responses through the Gemini API.



## Credits

Special thanks to the following YouTube channels and research papers for their invaluable resources and insights:

### YouTube Channels

- [AI Anytime](https://www.youtube.com/@AIAnytime)
- [Daniel Brouke](https://www.youtube.com/@mrdbourke)
- [Krish Naik](https://www.youtube.com/@krishnaik06)
- [Codebasics](https://www.youtube.com/@codebasics)
- [CampusX](https://www.youtube.com/@campusx-official)

### Research Papers

- Patrick Lewis ., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
- Vaswani et al., "Attention is All You Need" [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- Reimers et al., "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks" [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
