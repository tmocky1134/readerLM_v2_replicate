import sys
import json
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("jinaai/ReaderLM-v2")
model = AutoModelForCausalLM.from_pretrained("jinaai/ReaderLM-v2")

def predict(input_text):
    # Tokenize the input and generate output
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=200, do_sample=True)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

if __name__ == "__main__":
    # Read input from stdin; expects JSON with key "prompt"
    input_data = sys.stdin.read()
    try:
        data = json.loads(input_data)
        prompt = data.get("prompt", "")
    except Exception:
        prompt = input_data.strip()
    
    result = predict(prompt)
    
    # Output the result as JSON
    print(json.dumps({"result": result}))
