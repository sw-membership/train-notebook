import torch

from transformers import ElectraForSequenceClassification, ElectraTokenizerFast

# MODEL_PATH = './model/16000'
MODEL_PATH = './model/24000'

discriminator = ElectraForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = ElectraTokenizerFast.from_pretrained('google/electra-small-discriminator')


def predict(text, discriminator=discriminator, tokenizer=tokenizer):
    with torch.no_grad():
        tokens = tokenizer(text, padding="max_length", truncation=True, return_tensors="pt")
        output = discriminator(**tokens)
        logits = output.logits
        pred = logits.argmax().item()
        score = logits.softmax(1).max().item()
        return {"label": pred, "score": score}


if __name__ == '__main__':
    INPUT_PATH = 'text.txt'
    OUTPUT_PATH = 'result.txt'

    lines, labels, scores = [], [], []
    with open(INPUT_PATH, 'r') as f:
        while True:
            line = f.readline()
            if not line: break

            lines.append(line)
            prediction = predict(line)
            labels.append(prediction['label'])
            scores.append(prediction['score'])
    
    with open(OUTPUT_PATH, 'w') as f:
        for i in range(len(lines)):
            line, label, score = lines[i], labels[i], scores[i]
            f.write(f'{label},{score},{line}')
