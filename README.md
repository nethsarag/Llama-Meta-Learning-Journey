# Llama Learning Journey

Learning path from Python fundamentals to LLM/AI engineering, built entirely through hands-on projects with Llama.

**Starting point:** Comfortable with Python basics, no prior ML experience, laptop GPU (consumer-grade).

**Repo structure:** each project lives in its own folder: `01-cli-assistant/`, `02-llama-first-run/`, etc. Each folder has its own README with what it does, what I learned, and how to run it.

---

## Phase 1 — Python foundations
**Goal:** be comfortable enough with Python to work with LLM libraries.

- [ ] Project 1: Python CLI AI assistant *(argparse, functions, classes, exceptions, JSON, calling an API, basic Git)*

## Phase 2 — LLM fundamentals (concepts, no coding project yet)
Understand: tokens → embeddings → transformer → next-token prediction → generated text.
Also: tokenizers, attention, context windows, temperature, top-p, system/user/assistant roles.

- [ ] Notes doc: "How an LLM generates text" (write it in your own words — best test of understanding)

## Phase 3 — Learn Llama itself
- [ ] Project 2: Run a Llama model locally via Ollama and chat with it through Python

## Phase 4 — Local Llama development
- Beginner path: Ollama + Python + REST APIs
- Deeper path: Hugging Face Transformers, PyTorch, quantization, bitsandbytes, vLLM

## Phase 5 — Serious Llama applications
- [ ] Project 3: Llama chatbot with conversation history
- [ ] Project 4: Llama RAG assistant (chunking → embeddings → vector DB → retrieval → Llama)
- [ ] Project 5: PDF question-answering system
- [ ] Project 6: Structured info extractor (unstructured text → Llama → JSON)
- [ ] Project 7: Llama API (FastAPI wrapper)
- [ ] Project 8: Local AI coding assistant (tools, files, code execution)

## Phase 6 — Fine-tuning
Pre-training → instruction tuning → fine-tuning.
- [ ] Notes doc: LoRA vs QLoRA vs full fine-tuning — when to use which
- [ ] Project 9: Fine-tune a small Llama model on a custom dataset with QLoRA (likely on Colab GPU)

## Phase 7 — LLM engineering
Inference (throughput, latency, batching, KV cache), RAG at scale (hybrid search, reranking, eval), fine-tuning rigor (dataset quality, overfitting, eval), production (Docker, auth, monitoring, cost).

- [ ] Project 10: Dockerize and deploy one earlier project as a small production-style service

---

## Stack
Python → PyTorch → Hugging Face → Llama → Transformers → Ollama → RAG → PEFT/LoRA/QLoRA → TRL → vLLM → Docker
