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
- **`Example/`**: Reference CSV scripts for script testing.

---

## ⚠️ CRITICAL DISCLAIMER: Token Consumption

> [!WARNING]
> Ace Attorney script CSV files are extremely large (containing over 15,000 lines of speaker labels, blank lines, and game-engine control commands). 
> 
> **Attempting to translate raw script CSV files directly will lead to massive LLM token waste, prompt bloating, and rapid quota exhaustion.** You must use the extraction workflow detailed below to isolate dialogue lines, which reduces active translation tokens by up to **80%**.

---

## 🚀 How to Use an AI Agent to Translate (Optimal Workflow)

To translate a new script file with maximum efficiency and high-fidelity output, follow these steps:

### Step 1: Extract Translatable Dialogue
Extract only the dialogue rows into a clean, compact text format to strip out engine commands and non-translatable text:
```bash
python3 Scripts/translate_helper.py extract -i "Workspace/Original/sc2_0_text_u.txt" -o "Workspace/extracted_dialogue.txt"
```

### Step 2: Deploy the Translation Agent
Deploy your translation agent (or write your prompt) providing `Workspace/extracted_dialogue.txt` as the input. Instruct the agent to reference the localization guides:
1. Provide **[agent_guide.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/agent_guide.md)** for syntax and formatting.
2. Provide **[name_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/name_reference.md)** and **[pronouns_and_relationship.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/pronouns_and_relationship.md)** for core registers.
3. **Only provide the active chapter-specific guide** (e.g. **[ep3_big_top_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/ep3_big_top_reference.md)**) to keep the context window small and avoid wasting tokens on rules for inactive characters.

### Step 3: Merge Translated Dialogue Back
Once the agent outputs the translated text file (e.g., `Workspace/translated_dialogue.txt`), merge the translated lines back into the original template structure to generate the final playable script:
```bash
python3 Scripts/translate_helper.py merge -g "Workspace/Original/sc2_0_text_u.txt" -t "Workspace/translated_dialogue.txt" -o "Workspace/Translated/sc2_0_text_u.txt"
```

---

## 💡 LLM Token Optimization Tips
- **Isolate Reference Context**: When feeding rules to your LLM, only supply the spelling guides relevant to the active episode.
- **Partition in Chunks**: If translating large blocks (1,000+ lines), split the extracted text file into smaller sub-chunks (approx. 300 dialogues each) and translate them concurrently using lightweight subagents.
- **Index-Targeted Edits**: When retranslating or fixing specific parts, extract only the specific line indices using a script rather than resubmitting the entire file.
