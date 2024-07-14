import tiktoken

# 创建一个编码器
encoder = tiktoken.get_encoding("cl100k_base")

# 将文本编码为数字序列
text = "Hello, world!"
tokens = encoder.encode(text)
print(tokens)  # 输出: [15496, 1917, 0]

# 将数字序列解码为文本
decoded_text = encoder.decode(tokens)
print(decoded_text)  # 输出: "Hello, world!"
