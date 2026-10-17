<a href="https://elmirabd.me"><img src="assets/banner.svg?v=5" width="100%" alt="Elmir Abdullaiev, AI and software engineer, M.Eng. Computer Science at Cornell Tech. From a 4.62 KB model on a microcontroller to RAG assistants and live voice agents. Opens elmirabd.me."></a>

<h3 align="center">Hi, I'm Elmir</h3>

<p align="center">
  AI and software engineer, M.Eng. CS candidate at <b>Cornell Tech</b>.<br>
  Background in cybersecurity (B.Sc. honors, M.Sc. in progress), now focused on applied ML systems that ship.
</p>

<p align="center">
  📍 New York, NY &nbsp;·&nbsp; 🎓 Cornell Tech, M.Eng. CS (May 2027) &nbsp;·&nbsp; <a href="https://elmirabd.me">elmirabd.me</a>
</p>

## Selected projects

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/elmir132/fire-drill-core">Agent Fire Drill, a crash test for AI agents</a></h3>
      <p>A mock payment times out after it was processed. A verifier reads the real ledger to see whether the agent refunds twice, then a guardrail is applied and the run repeated in a fresh Daytona sandbox. Across 32 runs on Amazon Bedrock (16 per model), Claude Haiku 4.5 double-refunded in 8 of 8 runs without the guardrail and in 0 of 8 with it; Claude Sonnet 5.5 stayed safe in all 16. Built with a teammate at the Daytona HackSprint with Arize AI. Mock payments, one fault. <a href="https://elmirabd.me/fire-drill-core/">Interactive demo</a>.</p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/elmir132/ble_vulnerability_tinyml">TinyML BLE vulnerability detection</a></h3>
      <p>Neural classifier for real-time Bluetooth Low Energy threat detection on embedded hardware. Published at <i>CH&amp;CMiGIN-2026</i>, Kraków (<a href="https://ceur-ws.org/Vol-4278/short03.pdf">CEUR-WS Vol-4278</a>, Scopus-indexed).</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/elmir132/fire-drill-core"><img src="assets/stat-firedrill.svg?v=2" alt="Unsafe runs: Claude Haiku 4.5 8 of 8 without the guardrail and 0 of 8 with it; Claude Sonnet 5.5 0 of 16; 32 runs in total, 16 per model"></a>
      <br>
      <code>Python</code> <code>Daytona</code> <code>Amazon Bedrock</code> <code>Arize</code>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/elmir132/ble_vulnerability_tinyml"><img src="assets/stat-ble.svg?v=6" alt="99.68 percent accuracy, 4.62 KB model on an ESP32-S3, 75.5 percent smaller after INT8 quantization (from 18.88 KB), per the paper"></a>
      <br>
      <code>TensorFlow Lite Micro</code> <code>ESP32-S3</code> <code>BLE</code> <code>0.9&nbsp;ms</code>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/elmir132/rental-law-navigator">Rental Law Navigator</a></h3>
      <p>Address-level housing-law lookup. A language model proposes rules from the source documents, a verifier rejects any quote that is not literally in the source, and a deterministic engine decides which rules apply. Built solo overnight for the Hack-Nation RealPage challenge. Not legal advice. <a href="https://rental-law-navigator.streamlit.app/">Live demo</a>.</p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/elmir132/streetscript">StreetScript, 1st place hack night</a></h3>
      <p>Team project (with Pranav, Divyesh and Sahil) that writes poems and letters using only words cut from 1940s NYC storefront photos, every word traced back to its photo. I built the Rearrange feature, a hybrid vocabulary search and Mistral moderation.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/elmir132/rental-law-navigator"><img src="assets/stat-rental.svg?v=4" alt="59 source documents, 500 addresses, 9 cities"></a>
      <br>
      <code>Python</code> <code>Streamlit</code> <code>Gemini</code>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/elmir132/streetscript"><img src="assets/stat-streetscript.svg?v=4" alt="1st place, team of 4, 165 tests"></a>
      <br>
      <code>Python</code> <code>Elasticsearch</code> <code>Mistral</code>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/elmir132/advocate">Advocate, live interpreter for renters</a></h3>
      <p>A renter and a landlord talk through one button. It works out who spoke from the language, translates both ways, and flags vague commitments, promises and money terms. Built in one day at a Google DeepMind hackathon. Not legal advice. <a href="https://elmirabd.me/advocate/">Scripted demo</a>.</p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/elmir132/hermes">Hermes, personal AI assistant</a></h3>
      <p>Telegram assistant deployed for a single user, with long-term memory: RAG over a SQLite vector store, quota-aware routing across several models with automatic fallback, supervised by systemd on a Linux server.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/elmir132/advocate"><img src="assets/stat-advocate.svg?v=4" alt="On 20 scripted lines: 0.90 precision and 1.00 recall"></a>
      <br>
      <code>Gemini Live</code> <code>FastAPI</code> <code>JavaScript</code>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/elmir132/hermes"><img src="assets/stat-hermes.svg?v=4" alt="6 model tiers with automatic fallback, 20 tests"></a>
      <br>
      <code>Python</code> <code>SQLite</code> <code>RAG</code> <code>systemd</code>
    </td>
  </tr>
</table>

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

<a href="https://github.com/elmir132?tab=repositories"><img src="assets/stack.svg?v=5" width="100%" alt="Languages: Python, TypeScript and JavaScript, C and C++, SQL. ML and AI: TensorFlow, TensorFlow Lite Micro, PyTorch, Gemini, Amazon Bedrock, RAG, Arize. Backend and data: FastAPI, Flask, MongoDB Atlas, PostgreSQL, SQLite, vector search. Infra: Docker, systemd, Azure, Daytona. Hardware: ESP32-S3, BLE, MQTT. Opens the repository list."></a>

## Contact

<p align="center">
  <a href="https://linkedin.com/in/elmirabd"><img src="assets/link-linkedin.svg?v=4" height="56" alt="LinkedIn: in/elmirabd"></a>
  <a href="https://elmirabd.me"><img src="assets/link-site.svg?v=4" height="56" alt="Website: elmirabd.me"></a>
  <a href="mailto:ea488@cornell.edu"><img src="assets/link-email.svg?v=4" height="56" alt="Email: ea488@cornell.edu"></a>
</p>

<p align="center"><sub>Banner and badges are generated by <a href="scripts/build.py"><code>scripts/build.py</code></a>. Every number comes from the linked project READMEs.</sub></p>
