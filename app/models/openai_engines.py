TEXT_MODELS = [
    {
        "model": "davinci",
        "description": "The most capable GPT-3 API. Handles any task except for safe content generation (use the content-filtered models for that).",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "text-davinci-edit-001",
        "description": "A modified version of Davinci that is better at editing text.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "text-davinci-001",
        "description": "Davinci-001 is a language model developed by OpenAI that uses a deep neural network architecture called Transformer to generate natural language text. It has been trained on a massive amount of diverse text data and can perform various language tasks such as text generation, translation, and question-answering. The model has a large number of parameters and is considered one of the most advanced language models available. It is a powerful tool for natural language processing and has many practical applications in fields such as chatbots, content creation, and customer service.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "text-davinci-003",
        "description": "A modified version of Davinci that is better at generating creative writing.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "davinci-instruct-beta",
        "description": "A beta version of Davinci that is capable of following instructions.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.009
    },
    {
        "model": "ada",
        "description": "A text generation model that is optimized for creative writing tasks. It is based on the GPT architecture and has been trained on a diverse range of text data to enable it to generate human-like responses to a wide range of prompts.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0025
    },
    {
        "model": "curie-instruct-beta",
        "description": "A beta version of the Curie model that is capable of following instructions. This model can be used for tasks such as automated content creation, question-answering, and chatbots.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.009
    },

    {
        "model": "babbage-similarity",
        "description": "A text similarity model that is optimized for finding similarities between text data. This model can be used for tasks such as clustering similar documents or finding similar phrases.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "text-curie-001",
        "description": "",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.002
    },
    {
        "model": "code-search-babbage-code-001",
        "description": "",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "text-ada-001",
        "description": "",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0025
    },
    {
        "model": "text-embedding-ada-002",
        "description": "A model that produces high-quality vector embeddings for text data. These embeddings can be used for a wide range of natural language processing tasks such as text classification, sentiment analysis, and clustering.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "text-similarity-ada-001",
        "description": "A model that is optimized for finding similarities between text data. This model can be used for tasks such as clustering similar documents or finding similar phrases.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },

    {
        "model": "ada-similarity",
        "description": "A text similarity model that is optimized for finding similarities between text data. This model can be used for tasks such as clustering similar documents or finding similar phrases.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0025
    },
    {
        "model": "text-davinci-003",
        "description": "A modified version of Davinci that is better at generating creative writing.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "text-search-ada-query-001",
        "description": "A text search model that is designed to search through a corpus of text data and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "davinci-search-document",
        "description": "A model that is good at searching documents and answering questions about their contents.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "ada-code-search-text",
        "description": "A code search model that is designed to search through code and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0025
    },
    {
        "model": "text-search-ada-doc-001",
        "description": "A text search model that is designed to search through a corpus of text data and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "davinci-instruct-beta",
        "description": "A beta version of Davinci that is capable of following instructions.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.009
    },
    {
        "model": "text-similarity-curie-001",
        "description": "A model that is optimized for finding similarities between text data. This model can be used for tasks such as clustering similar documents or finding similar phrases.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0035
    },
    {
        "model": "ada-search-query",
        "description": "A model that is optimized for generating search queries based on natural language input.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "text-search-davinci-query-001",
        "description": "A text search model that is designed to search through a corpus of text data and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "curie-search-query",
        "description": "A model that is optimized for generating search queries based on natural language input.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.003
    },
    {
        "model": "text-search-curie-doc-001",
        "description": "A text search model that is designed to search through a corpus of text data and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.003
    },
    {
        "model": "babbage-search-query",
        "description": "A model that is optimized for generating search queries based on natural language input.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "text-babbage-001",
        "description": "A language model developed by OpenAI that can generate text responses to natural language prompts. It is based on the GPT architecture and has been trained on a diverse set of text data, including social media conversations, emails, and news articles. The model can produce human-like responses to a wide range of topics.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0025
    },
    {
        "model": "text-search-davinci-doc-001",
        "description": "A text search model that is designed to search through a corpus of text data and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.003
    },

]
CODE_MODELS = [
    {
        "model": "code-davinci-edit-001",
        "description": "Code-Davinci-Edit-001 is an OpenAI language model that specializes in completing and generating code. This model is capable of understanding code syntax and semantics, and can generate code snippets and entire programs based on prompts given to it. It has a max_tokens parameter, which determines the maximum number of tokens the model will generate in response to a prompt. This model can be used for tasks such as autocompletion of code, code generation, and code translation. The cost_by_token for this model is higher than some of the other OpenAI models, as it is optimized for code-related tasks and requires more computational resources.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "babbage-code-search-text",
        "description": "A text search model that is designed to search through code and find relevant matches based on a given query.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "ada-code-search-code",
        "description": "A model that is designed to search through code and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0025
    },
    {
        "model": "code-search-ada-code-001",
        "description": "A code search model that is designed to search through code and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0025
    },
    {
        "model": "davinci-search-query",
        "description": "A model that is optimized for generating search queries based on natural language input.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "babbage-search-document",
        "description": "A model that is good at searching documents and answering questions about their contents.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "text-search-curie-query-001",
        "description": "A text search model that is designed to search through a corpus of text data and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.003
    },
    {
        "model": "text-search-babbage-doc-001",
        "description": "A text search model that is designed to search through a corpus of text data and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.003
    },
    {
        "model": "code-search-babbage-text-001",
        "description": "A code search model that is designed to search through code and find relevant matches based on a given query.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    {
        "model": "code-search-ada-text-001",
        "description": "A code search model that is designed to search through code and find relevant matches based on a given query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0025
    },


]
DOCUMENTS_MODELS = [
    {
        "model": "davinci-search-document",
        "description": "A model that is good at searching documents and answering questions about their contents.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "curie-search-document",
        "description": "A model that is good at searching documents and answering questions about their contents.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.0035
    },
    {
        "model": "ada-search-document",
        "description": "A model that is optimized for finding documents related to a given search query.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
    ]
CHAT_MODELS = [
    {
        "model": "gpt-3.5-turbo",
        "description": "An advanced natural language processing model developed by OpenAI. It is based on the GPT-3 architecture and is capable of performing a wide range of language tasks, including natural language generation and text classification. This model has a large number of parameters and is considered one of the most powerful language models available.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "gpt-3.5-turbo-0301",
        "description": "An advanced natural language processing model developed by OpenAI. It is based on the GPT-3 architecture and is capable of performing a wide range of language tasks, including natural language generation and text classification. This model has a large number of parameters and is considered one of the most powerful language models available.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.006
    },
    {
        "model": "gpt-4",
        "description": "An advanced natural language processing model developed by OpenAI. It is based on the GPT architecture and is capable of performing a wide range of language tasks, including natural language generation and text classification. This model has a large number of parameters and is considered one of the most powerful language models available.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.005
    },
    {
        "model": "gpt-4-0314",
        "description": "An advanced natural language processing model developed by OpenAI. It is based on the GPT architecture and is capable of performing a wide range of language tasks, including natural language generation and text classification. This model has a large number of parameters and is considered one of the most powerful language models available.",
        "max_tokens": None,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.005
    },
]
SPEECH_MODEL = [
    {
        "model": "whisper-1",
        "description": "A text generation model that is designed to generate coherent and engaging chatbot responses. It is based on a GPT architecture and has been trained on a large corpus of conversational data.",
        "max_tokens": 2048,
        "support_until": "Supported on each new iteration",
        "data_extend_to": "",
        "cost_by_token": 0.001
    },
]

