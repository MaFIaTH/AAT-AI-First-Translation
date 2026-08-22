# Phoenix Wright: Ace Attorney — Thai Translation & Localization project

This repository contains the localization scripts, tools, and specialized guides for translating the *Phoenix Wright: Ace Attorney* series into Thai.

---

## 📂 Project Directory Structure

- **`Guides/`**: Specialized Thai localization guidelines and spelling references:
  - **[agent_guide.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/agent_guide.md)**: Main technical guide detailing script formatting rules, line distribution strategy, phonetic stuttering, and pacing wait controls.
  - **[name_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/name_reference.md)**: Core name tags `<>` rules, standard name spellings, and Kurain Fey clan terminology.
  - **[pronouns_and_relationship.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/pronouns_and_relationship.md)**: Core relationship registers (e.g. Maya Fey sibling dynamic vs Pearl Fey courtly voice).
  - **[ep3_big_top_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/ep3_big_top_reference.md)**: Episode-specific reference for JFA Episode 3 (Turnabout Big Top) containing circus terminology and dialects.
  - **[names_pwaa.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/names_pwaa.md)**: spelling list for PWAA (Episodes 1 to 5).
  - **[names_jfa_ep1_ep2_ep4.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/names_jfa_ep1_ep2_ep4.md)**: spelling list for JFA (Episodes 1, 2, and 4).
- **`Scripts/`**: Workflow scripts for parsing and processing text files:
  - **[translate_helper.py](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Scripts/translate_helper.py)**: The main automation helper used to extract dialogue and merge translations.
- **`Workspace/`**: Development directory containing script files being translated:
  - `Original/`: Raw English source CSV script.
  - `Refined/`: Human-refined polished translation drafts.
  - `Translated/`: Reassembled merged Thai translation script.

---

## ⚠️ CRITICAL DISCLAIMER: Token Consumption

> [!WARNING]
> Ace Attorney script CSV files are extremely large (containing over 15,000 lines of speaker labels, blank lines, and game-engine control commands). 
> 
> **Attempting to translate raw script CSV files directly will lead to massive LLM token waste, prompt bloating, and rapid quota exhaustion.** You must use the AI workflow detailed below to isolate and process dialogue lines, reducing active translation tokens by up to **80%**.

---

## 🤖 AI-First Workflow & Prompt Templates (Human Guide)

The AI agent is responsible for executing tools, running scripts, updating guidelines, and validating output autonomously by reading the rules inside the `Guides/` directory. 

### ⚠️ Pre-requisite: Initializing the AI Agent (Mandatory First Step)
Before asking the AI to translate or edit files, you **must** force the agent to load the master guidelines into its active context. Copy and paste this prompt first:
> *"Acknowledge that you have read the master guidelines inside `Guides/agent_guide.md`, `Guides/name_reference.md`, and `Guides/pronouns_and_relationship.md`. Summarize their top 3 most critical rules to confirm your understanding."*

Once the AI agent summarizes the rules correctly, proceed with the workflow prompts below:

---

### 🛠️ Scenario 1: Translating a New Case for the First Time
When a new script template is ready for translation:
1. **Human Action**: Place the raw script template in the `Workspace/Original/` directory.
2. **Human Prompt**:
   > *"Translate the new script at `Workspace/Original/ep4_template.txt`."*
3. **Autonomous AI Action**: The AI agent reads the guides, runs the extraction command, translates the lines, runs verification checks, and merges the final script.

---

### 🔄 Scenario 2: Training the AI with a Human-Refined Script
When you have polished a script and want the AI to learn your style rules, vocabulary, and registers:
1. **Human Action**: Place the polished script in the `Workspace/Refined/` directory.
2. **Human Prompt**:
   > *"I have finished refining `Workspace/Refined/sc2_0_text_u_refined.txt`. Please run a comparison check against `Workspace/Translated/sc2_0_text_u.txt`, update the master guides inside `Guides/` to incorporate my refined spelling/register choices, and commit the updates to Git."*
3. **Autonomous AI Action**: The AI agent performs the discrepancy check, updates the spelling dictionaries and relationship guides, and commits the changes.

---

### ✍️ Scenario 3: Updating the AI Guide for a Specific Case
When you want to add unique character speech patterns, accents, or dialects:
1. **Human Action**: None.
2. **Human Prompt**:
   > *"Please update `Guides/ep4_goodbyes_reference.md` to add registers for Lotta Hart (Southern country accent localized as Southern Thai dialect, uses self-pronoun 'นุ้ย', ending particle 'นิ') and Manfred von Karma (arrogant snaps, no polite particles, calls Phoenix 'ทนายไร้ระดับ')."*
3. **Autonomous AI Action**: The AI agent edits the episode reference document directly and commits the changes to Git.
