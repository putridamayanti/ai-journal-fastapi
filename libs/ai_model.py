import os

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

AI_MODEL_NAME = os.environ.get("AI_MODEL_NAME")

tokenizer = AutoTokenizer.from_pretrained(AI_MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(AI_MODEL_NAME)

def generate_title(content: str) -> str:
    prompt = f"Generate a short diary title:\n{content}"

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        output_ids = model.generate(**inputs, max_length=20, num_beams=5, early_stopping=True)

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
