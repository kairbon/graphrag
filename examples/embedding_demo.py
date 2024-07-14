from http import HTTPStatus

import dashscope

inputs = ['风急天高猿啸哀', '渚清沙白鸟飞回', '无边落木萧萧下', '不尽长江滚滚来']
resp = dashscope.TextEmbedding.call(
    model=dashscope.TextEmbedding.Models.text_embedding_v1,
    input=inputs
)
print(resp)
if resp.status_code == HTTPStatus.OK:
    res = [embedding["embedding"] for embedding in resp.output["embeddings"]]
    print(res)
