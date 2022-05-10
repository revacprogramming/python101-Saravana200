text = "X-DSPAM-Confidence:    0.8475"
print(float(text[slice(text.find("0"),len(text),1)]))