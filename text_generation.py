from transformers import GPT2Config
from transformers import OpenAIGPTTokenizer
from transformers import OpenAIGPTLMHeadModel


# Initializing a GPT2 configuration
def initialize():
    global model, tokenizer
    model = OpenAIGPTLMHeadModel.from_pretrained("openai-gpt")
    tokenizer = OpenAIGPTTokenizer.from_pretrained("openai-gpt")


def generate_next_word(prompt_text):
    encoded_prompt = tokenizer.encode(prompt_text,
                                      add_special_tokens=False,
                                      return_tensors="pt")
    num_sequences = 1
    length = 5
    generated_sequences = model.generate(
        input_ids=encoded_prompt,
        do_sample=True,
        max_length=length + len(encoded_prompt[0]),
        temperature=1.0,
        top_k=0,
        top_p=0.9,
        repetition_penalty=1.0,
        num_return_sequences=num_sequences,
    )
    text = tokenizer.decode(generated_sequences[0], clean_up_tokenization_spaces=True)
    newtext  = text.replace("\"","")
    return newtext
