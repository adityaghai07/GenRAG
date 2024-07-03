from transformers import AutoTokenizer, AutoModelForCausalLM  
import torch
tokenizer = AutoTokenizer.from_pretrained("llmware/bling-sheared-llama-1.3b-0.1")  
model = AutoModelForCausalLM.from_pretrained("llmware/bling-sheared-llama-1.3b-0.1")

# device = "cuda" if torch.cuda.is_available() else "cpu"
device="cpu"



def llm_response(new_prompt:str,context:str):
    """
    Takes a prompt and returns a response from the Bling-Sheared Llama model.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # device ="cpu"
    prompt = f"""<human>: 
        {context}

        Given the context answer the following questions.

        {new_prompt}
        <bot>:
                """

    inputs = tokenizer(prompt, return_tensors="pt")  
    start_of_output = len(inputs.input_ids[0])



    outputs = model.generate(
            inputs.input_ids.to(device),
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.3,
            max_new_tokens=100,
            )

    output_only = tokenizer.decode(outputs[0][start_of_output:],skip_special_tokens=True)  


    eot = output_only.find("<|endoftext|>")
    if eot > -1:
        output_only = output_only[:eot]

    return output_only