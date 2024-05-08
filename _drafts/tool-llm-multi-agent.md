---
layout: post
title: "[Tool] LLM Multi-Agent"
---

## BabyAGI

BabyAGI inspired many projects, including MetaGPT, ChatDev, and LocalAI.
[https://github.com/yoheinakajima/babyagi/blob/main/docs/inspired-projects.md]

[ ] MetaGPT
[ ] ChatDev

## LocalAI

[https://localai.io/basics/build/]

```
# install build dependencies
brew install abseil cmake go grpc protobuf wget

# clone the repo
git clone https://github.com/go-skynet/LocalAI.git

cd LocalAI

# build the binary
make build

# Download gpt4all-j to models/
wget https://gpt4all.io/models/ggml-gpt4all-j.bin -O models/ggml-gpt4all-j

# Use a template from the examples
cp -rf prompt-templates/ggml-gpt4all-j.tmpl models/

# Run LocalAI
./local-ai --models-path=./models/ --debug=true

# Now API is accessible at localhost:8080
curl http://localhost:8080/v1/models

curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json" -d '{
     "model": "ggml-gpt4all-j",
     "messages": [{"role": "user", "content": "How are you?"}],
     "temperature": 0.9
   }'
```

## References
[https://github.com/geekan/MetaGPT]

[https://aws.amazon.com/cn/blogs/machine-learning/generating-value-from-enterprise-data-best-practices-for-text2sql-and-generative-ai/]

[ ] [https://github.com/wbbeyourself/MAC-SQL]
[https://github.com/kalaspuff/ai-assisted-task-executor]
[ ] [https://github.com/reworkd/AgentGPT]
[ ] [https://www.langchain.com/]
[ ]