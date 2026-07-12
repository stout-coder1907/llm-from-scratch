import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")
text = "hello do you like tea<|end of text|> i am sudhanshu"
integers = tokenizer.encode(text, allowed_special={"<|end of text|>"})
print(integers)

strings = tokenizer.decode(integers)
print(strings)
