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

## 🚀 How to Prompt Your AI Agent (Human Guide)

Once you have extracted the dialogue text file (e.g., `Workspace/extracted_dialogue.txt`) using the `extract` tool command in **Step 1**, you can prompt your AI translation agent using the template below. 

Copy and paste this template prompt into the chat with your AI agent to ensure optimal translation fidelity and structural alignment:

---

### 📋 Copy-Paste Agent Prompt Template

```text
You are an expert Thai localizer. Translate the English dialogue lines located in:
`[Insert path to Workspace/extracted_dialogue.txt]`

Follow these instructions:
1. Translate only the text after the '->' symbol on each line. Output format must match `LINE_XXXXX: English text -> Thai translation` exactly. Do not alter line indices.
2. Read and strictly comply with the formatting rules, spacing conventions, spelling dictionary, and character voice registers detailed in the guides inside the `Guides/` directory:
   - `Guides/agent_guide.md` (formatting rules, dialogue distribution, whitespace spacing, pacing)
   - `Guides/name_reference.md` (name wrapping rules, core spellings)
   - `Guides/pronouns_and_relationship.md` (pronouns, register dynamics)
   - `Guides/[active_chapter_reference].md` (episode-specific names, terminology, and character registers)
3. **Mandatory Verification Check**: Before submitting the final translation, run a proofreading/validation sweep over your translated lines using `Scripts/translate_helper.py verify -t <translated_file>` (or write a scratch verification script) to check for structural typos, mismatched name tags `<>`, odd quote counts, invalid backslashes `\`, and spacing anomalies. Report and correct any errors found.

If the file contains more than 300 dialogue lines, you are highly encouraged to chunk it and translate concurrently using subagents.
```


