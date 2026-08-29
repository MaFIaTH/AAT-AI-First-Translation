# Phoenix Wright: Ace Attorney — Thai Translation & Localization Project

This repository contains the localization scripts, tools, and specialized Thai translation guidelines for the *Phoenix Wright: Ace Attorney* trilogy.

---

## 🚀 Beginner Quick-Start Guide (Git & AI Agent CLI)

This project is built for **AI-First Local Development**. You do not copy-paste lines back and forth into web chatbots. Instead, you launch an AI Coding Agent directly inside the repository folder, and the agent reads guidelines, executes scripts, extracts dialogue, validates text, and merges files autonomously.

### 1. Requirements
Make sure you have installed:
- **Git** ([Download Git](https://git-scm.com/))
- **Python 3.8+** ([Download Python](https://www.python.org/))
- An **AI Coding Agent CLI / IDE** (e.g., Claude Code, Cursor, Aider, Gemini CLI / Antigravity, or VS Code with Roo/Cline).

---

### 2. Step-by-Step Setup

#### Step 1: Clone the Repository
Open your terminal (or Command Prompt / PowerShell / Git Bash) and run:
```bash
git clone https://github.com/MaFIaTH/AAT-AI-First-Translation.git
```

#### Step 2: Open the Project Directory
Navigate into the newly cloned project folder:
```bash
cd "AAT-AI-First-Translation"
```
*(Or open/drag this folder into your AI agent IDE / terminal).*

#### Step 3: Launch Your AI Agent CLI
Start your CLI Agent in this folder. For example:
- **Claude Code**: run `claude`
- **Aider**: run `aider`
- **Antigravity / Gemini CLI**: run `agy` or open the workspace in the agent window.

---

## 🤖 How to Prompt Your AI Agent (Workflow Guide)

Once your AI Agent is open in this repository, follow these simple prompt scenarios. The agent will do all the heavy lifting (running python tools, checking syntax, editing guides).

### ⚠️ Pre-requisite: Initializing the AI Agent (Mandatory First Prompt)
Always run this prompt first when starting a new session with an agent so it loads all master styling rules into memory:
> *"Acknowledge that you have read the master guidelines inside `Guides/agent_guide.md`, `Guides/name_reference.md`, and `Guides/pronouns_and_relationship.md`. Summarize their top 3 most critical rules to confirm your understanding."*

---

### 🛠️ Scenario 1: Translating a New Case for the First Time
1. **Human Action**: Place the raw English script template (e.g., `sc2_1_0_text_u.txt`) into `Workspace/Original/`.
2. **Human Prompt**:
   > *"Translate the new script at `Workspace/Original/sc2_1_0_text_u.txt`."*
3. **What the AI Does Autonomously**:
   - Runs `python3 Scripts/translate_helper.py extract` to separate dialogue.
   - Translates lines according to character registers and tags.
   - Runs `python3 Scripts/translate_helper.py verify` to check for formatting/tag errors.
   - Merges translated dialogue back into `Workspace/Translated/`.

---

### 🔄 Scenario 2: Training the AI with Your Refined/Polished Script
When you (human) have reviewed and polished a translation and want the AI to learn your phrasing choices, nicknames, or register corrections for future cases:
1. **Human Action**: Save your polished file in `Workspace/Refined/` (e.g., `Workspace/Refined/sc2_0_text_u_refined.txt`).
2. **Human Prompt**:
   > *"I have finished refining `Workspace/Refined/sc2_0_text_u_refined.txt`. Please run a comparison check against `Workspace/Translated/sc2_0_text_u.txt`, update the master guides inside `Guides/` to incorporate my refined spelling/register choices, and commit the updates to Git."*
3. **What the AI Does Autonomously**:
   - Compares the two files to identify what you changed.
   - Updates the corresponding reference files in `Guides/` with new conventions.
   - Commits the updated guides.

---

### ✍️ Scenario 3: Adding or Updating Case-Specific Guidelines
When you want to define specific dialects, accents, or special character names for a new case before translating:
1. **Human Action**: None.
2. **Human Prompt**:
   > *"Please update `Guides/ep4_goodbyes_reference.md` to add registers for Lotta Hart (Southern country accent localized as Southern Thai dialect, uses self-pronoun 'นุ้ย', ending particle 'นิ') and Manfred von Karma (arrogant snaps, no polite particles, calls Phoenix 'ทนายไร้ระดับ')."*
3. **What the AI Does Autonomously**:
   - Creates or updates the episode markdown guide directly with tables and examples.

---

## 📂 Project Directory Structure

- **`Guides/`**: Master Thai localization guidelines and character dictionaries:
  - **[agent_guide.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/agent_guide.md)**: Main technical guide (script syntax, formatting, line distribution, stutter timing, and wait controls).
  - **[name_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/name_reference.md)**: Core `<Name>` tag rules, main cast spellings, and Kurain Fey clan terminology.
  - **[pronouns_and_relationship.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/pronouns_and_relationship.md)**: Interpersonal relationship registers (e.g., Maya's casual sibling tone vs. Pearl's courtly register).
  - **[ep3_big_top_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/ep3_big_top_reference.md)**: JFA Episode 3 circus terminology, Moe's puns, and Trilo's insults.
  - **[names_pwaa.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/names_pwaa.md)**: Character & item dictionary for PWAA (Episodes 1 to 5).
  - **[names_jfa_ep1_ep2_ep4.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/names_jfa_ep1_ep2_ep4.md)**: Character & item dictionary for JFA (Episodes 1, 2, and 4).
- **`Scripts/`**: Automation tools:
  - **[translate_helper.py](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Scripts/translate_helper.py)**: Python helper to extract dialogue (`extract`), verify syntax (`verify`), and merge translations (`merge`).
- **`Workspace/`**: Working directories for translation (ignored by Git, managed locally):
  - `Original/`: Place raw English script templates here.
  - `Refined/`: Place human-polished scripts here for AI training.
  - `Translated/`: Automated merged output files are generated here.

---

## ⚠️ CRITICAL DISCLAIMER: Token Consumption

> [!WARNING]
> Ace Attorney script files are massive (often containing thousands of lines per case with complex branchings and engine commands).
> 
> While this workflow uses automated extraction to cut token usage by over 80% (by stripping non-dialogue engine commands), **running a full case translation will still consume a massive amount of LLM tokens**.
> 
> - **Be mindful of rate limits & quota limits** on your LLM API subscription.
> - **Never paste raw script files directly into chat prompts** — always let the CLI Agent run the extraction workflow to minimize unnecessary token burn.
