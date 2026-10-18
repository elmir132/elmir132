# Elmir Abdullaiev

AI and software engineer in New York, NY, M.Eng. CS candidate at Cornell Tech (May 2027).

Background in cybersecurity (B.Sc. honors, M.Sc. in progress), now focused on applied ML systems that ship.

[LinkedIn](https://linkedin.com/in/elmirabd) · [elmirabd.me](https://elmirabd.me) · [ea488@cornell.edu](mailto:ea488@cornell.edu)

## Selected projects

### [Agent Fire Drill, a crash test for AI agents](https://github.com/elmir132/fire-drill-core)

A mock payment times out after it was processed. A verifier reads the real ledger to see whether the agent refunds twice, then a guardrail is applied and the run repeated in a fresh Daytona sandbox. Across 32 runs on Amazon Bedrock (16 per model), Claude Haiku 4.5 double-refunded in 8 of 8 runs without the guardrail and in 0 of 8 with it; Claude Sonnet 5.5 stayed safe in all 16. Built with a teammate at the Daytona HackSprint with Arize AI. Mock payments, one fault. [Interactive demo](https://elmirabd.me/fire-drill-core/).

Stack: Python, Daytona, Amazon Bedrock, Arize

### [TinyML BLE vulnerability detection](https://github.com/elmir132/ble_vulnerability_tinyml)

Neural classifier for real-time Bluetooth Low Energy threat detection on embedded hardware: 99.68% accuracy from a 4.62 KB model on an ESP32-S3, 75.5% smaller after INT8 quantization (from 18.88 KB), at 0.9 ms, per the paper. Published at *CH&CMiGIN-2026*, Kraków ([CEUR-WS Vol-4278](https://ceur-ws.org/Vol-4278/short03.pdf), Scopus-indexed).

Stack: TensorFlow Lite Micro, ESP32-S3, BLE

### [Rental Law Navigator](https://github.com/elmir132/rental-law-navigator)

Address-level housing-law lookup covering 500 addresses in 9 cities from 59 source documents. A language model proposes rules from the source documents, a verifier rejects any quote that is not literally in the source, and a deterministic engine decides which rules apply. Built solo overnight for the Hack-Nation RealPage challenge. Not legal advice. [Live demo](https://rental-law-navigator.streamlit.app/).

Stack: Python, Streamlit, Gemini

### [StreetScript, 1st place hack night](https://github.com/elmir132/streetscript)

Team project (with Pranav, Divyesh and Sahil) that writes poems and letters using only words cut from 1940s NYC storefront photos, every word traced back to its photo. I built the Rearrange feature, a hybrid vocabulary search and Mistral moderation.

Stack: Python, Elasticsearch, Mistral

### [Advocate, live interpreter for renters](https://github.com/elmir132/advocate)

A renter and a landlord talk through one button. It works out who spoke from the language, translates both ways, and flags vague commitments, promises and money terms. On 20 scripted lines: 0.90 precision and 1.00 recall. Built in one day at a Google DeepMind hackathon. Not legal advice. [Scripted demo](https://elmirabd.me/advocate/).

Stack: Gemini Live, FastAPI, JavaScript

### [Hermes, personal AI assistant](https://github.com/elmir132/hermes)

Telegram assistant deployed for a single user, with long-term memory: RAG over a SQLite vector store, quota-aware routing across 6 model tiers with automatic fallback, supervised by systemd on a Linux server.

Stack: Python, SQLite, RAG, systemd

## More projects

| Project | What it is |
|:--|:--|
| [Security Overflow](https://github.com/elmir132/security-overflow) | Flask scanner that orchestrates Wapiti, SQLMap and Nikto behind one interface, with LLM-generated remediation guidance. Successor to my B.Sc. thesis scanner. |
| [PharOS](https://github.com/elmir132/pharos) | Team hackathon project (4 people): a 3D Manhattan crash-history map with live street-video review. I built the near-miss measurement and the shared map color scale. |
| [Chronicle](https://github.com/elmir132/mongodb-hackathon) | Self-healing project memory from a MongoDB hackathon (team of 4). I built the resolution engine: conflict resolution by source authority and recency, and policy learning from human corrections. |
| [Utility Debt Shield](https://github.com/elmir132/utility-debt-shield) | Prototype API that flags utility activation friction before a lease is signed (mock data only). |
| [ClipTidy](https://github.com/elmir132/cliptidy) | macOS menu-bar app that cleans clipboard text with one shortcut. |
| [Multi-model research orchestrator](https://github.com/elmir132/multi-model-research-orchestrator) | CLI that compares several AI providers on one question and shows where they disagree. |
| [tuichat](https://github.com/elmir132/terminal-llm-chat) | Full-screen terminal chat client for Ollama and OpenAI-compatible models. |
| [Crypto trend dashboard](https://github.com/elmir132/crypto-trend-dashboard), [NFT call builder](https://github.com/elmir132/nft-call-builder) | Small Flask and Node tools on public market data. |

## Stack

- Languages: Python, TypeScript and JavaScript, C and C++, SQL
- ML and AI: TensorFlow, TensorFlow Lite Micro, PyTorch, Gemini, Amazon Bedrock, RAG, Arize
- Backend and data: FastAPI, Flask, MongoDB Atlas, PostgreSQL, SQLite, vector search
- Infra: Docker, systemd, Azure, Daytona
- Hardware: ESP32-S3, BLE, MQTT

Every number comes from the linked project READMEs.
