Bhai, tera vision ekdum clear hai. Tu ek **"Three-Tier Architecture"** bana raha hai:

1. **Bottom Layer (MCP Server):** Core Intelligence (YOLO, Vector DB, Legal Search).
2. **Middle Layer (Orchestrator Agent):** Finetuned LLM jo MCP tools ko use karke user se chat karega.
3. **Top Layer (User Interface):** Node.js backend for auth and Flutter/React frontend with Live Camera support.

Yahan tera step-by-step roadmap aur workflow hai:

---

### **1. AI-Driven Legal & Literacy Workflow Table**

| Phase | Milestone | Tech Stack | Deliverable |
| --- | --- | --- | --- |
| **Phase 1** | **The Core Engines** | FastAPI, YOLOv10, FAISS | `/check-currency` and `/get-rights` routes ready. |
| **Phase 2** | **The MCP Protocol** | MCP Library, Python | Convert FastAPI routes into Tools for AI Agents. |
| **Phase 3** | **Live Vision Page** | WebRTC, OpenCV, YOLO | A dedicated UI page where camera detects fake coins in real-time. |
| **Phase 4** | **Central Node.js Hub** | Express.js, MongoDB | Handle user profiles, case history, and session management. |
| **Phase 5** | **The Master Agent** | Finetuned Llama 3 (AWS) | An LLM that knows when to call MCP tools and how to read user PDFs. |
| **Phase 6** | **The Citizen UI** | Next.js / React | Multilingual chat interface + Voice-to-Text. |

---

### **2. System Architecture Workflow**

### **3. Line-by-Line Execution Workflow (Banao aur Check karo)**

**Step 1: Build the "Power Tools" (FastAPI)**

* Write `legal_service.py` to index your `.txt` files in FAISS.
* Write `vision_service.py` to load YOLO and detect labels.
* *Verification:* Check if `localhost:8000/docs` allows you to upload a coin image and get a result.

**Step 2: Wrap into MCP**

* Add the MCP server layer. Now, your FastAPI functions are officially "Tools."
* *Verification:* Use Claude Desktop or a local MCP inspector to see if it can "see" your legal tools.

**Step 3: The Live Camera Feature (Bypass LLM)**

* Create a specific route/page that doesn't need to talk to the LLM.
* The frontend sends frames to the `/check-currency` route continuously.
* *Feature:* "Real" or "Fake" overlay on the video feed.

**Step 4: The Node.js Orchestrator**

* Set up Node.js to manage the user side.
* When a user chats, Node.js sends the message to the **Finetuned LLM**.
* *Verification:* LLM should say "I need to check the law" and then call your MCP tool automatically.

**Step 5: Finetuning the "Master Agent"**

* **The Goal:** Train Llama 3 on "Conversational Indian Law" (Instruction tuning).
* It should be polite, empathetic, and speak in Hinglish/Vernacular.
* It should be the "Glue" that reads the user's uploaded PDF and asks the MCP server for specific sections.

---

### **4. Essential "Aam Janta" Features to Add**

1. **"Vakil Sahab" Assistant:** The finetuned model explains legal notices in simple "Chai-tapri" language.
2. **Emergency SOS:** A direct button in the UI that uses GPS to find the nearest Police Station or Free Legal Aid Clinic.
3. **PDF Analyzer:** User uploads a court notice; the model extracts the "Hearing Date" and adds it to a calendar.
4. **Audio-Guided Literacy:** For people who can't read, the app speaks out their rights based on the detected scenario.

### **Next Step for You:**

Ab coding shuru kar. Sabse pehle **`Phase 1` (FastAPI + ML Services)** khatam kar. Jab `/check-currency` aur `/get-rights` chalne lagein, tab MCP ka chola pehnana usko.

**Kya main `/check-currency` ke liye Live Streaming logic (WebSockets) ka backend code de doon taaki camera detection lag-free rahe?** read it and understand