
from transformers import AutoTokenizer
import evaluate
import numpy as np

repo_id = "distilroberta-base"

tokenizer = AutoTokenizer.from_pretrained(repo_id)
def tokenize_fn(example):
  return tokenizer(example["sentence1"], example["sentence2"], truncation=True)


from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)



def compute_metrics(eval_pred):
  metric = evaluate.load("glue", "mrpc")
  logits, labels = eval_pred
  predictions = np.argmax(logits, axis=-1)
  return metric.compute(predictions=predictions, references=labels)


