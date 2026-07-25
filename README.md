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

## 🤖 AI Agent Autonomous Workflow (Optimal Translation Execution)

You are an agentic AI coding assistant tasked with translating script files in this repository. Follow this optimal autonomous workflow to execute translations efficiently and correctly.

### Step 1: Automated Dialogue Extraction
Before starting translation, run `Scripts/translate_helper.py` in your shell using the `extract` command. This strips out engine commands, speaker labels, and non-translatable text into a clean text file, reducing your active context size by ~80%:
```bash
python3 Scripts/translate_helper.py extract -i "Workspace/Original/<file_name>.txt" -o "Workspace/<file_name>_dialogue.txt"
```
*Note: Never attempt to translate or parse raw CSV/template scripts directly. Only process the extracted dialogue file.*

### Step 2: Context Selection & Context Loading
Read and load ONLY the relevant guides from `Guides/` into your active context:
1. Always load **[agent_guide.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/agent_guide.md)** (syntax/formatting rules).
2. Always load **[name_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/name_reference.md)** and **[pronouns_and_relationship.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/pronouns_and_relationship.md)** (core characters register).
3. **Isolate Reference Context:** Read only the active chapter-specific guide (e.g., **[ep3_big_top_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/ep3_big_top_reference.md)**). Do not read other episode files to minimize prompt token overhead.

### Step 3: Concurrency and Chunking
If the extracted dialogue text contains over 300 dialogue lines:
- Write a short python script to split the dialogue file into smaller files (approx. 300 dialogues each) in your scratch directory.
- Define a specialized translation subagent type equipped with these guides, and launch multiple subagents concurrently to translate the chunks in parallel.
- Concatenate the outputs when done.

### Step 4: Automated Merging
Reassemble the translated dialogue lines back into the original template structure to generate the final playable script in `Workspace/Translated/`:
```bash
python3 Scripts/translate_helper.py merge -g "Workspace/Original/<file_name>.txt" -t "Workspace/<file_name>_translated.txt" -o "Workspace/Translated/<file_name>.txt"
```

### Step 5: Integrity Validation
Before concluding, verify your output:
- Ensure the line count of the merged output file exactly matches the original template.
- Write a script to verify that no color formatting commands (`[SetTextColor(...);]`) are wrapped around empty strings `#""`.
- Verify that spacing after line breaks (`[NewLine();]` and `[ReadKey();]`) starts flush-left, and tag spacing around `<...>` names is tight.
- Clean up all backslashes (`\`) from the final dialogue lines.
- Stage your changes and commit them cleanly in git.

