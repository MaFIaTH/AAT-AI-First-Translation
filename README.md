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
You are an expert Thai localizer. I want you to translate the English dialogue lines located in the file:
`[Insert path to Workspace/extracted_dialogue.txt]`

Your goal is to translate only the text after the '->' symbol on each line. Output the translation format exactly as `LINE_XXXXX: English text -> Thai translation`. Do not modify the original line numbers or prefix tags.

Before you begin, read and strictly comply with the localization and formatting guides in this repository:
1. Guides/agent_guide.md - Syntax, spacing, phonetic stuttering (e.g. ม-ม-ไม่), punctuation rules, and dialogue distribution.
2. Guides/name_reference.md - Person name wrapping rule in `<>` brackets (e.g., `<นิค>`, `<มายา>`) and standard core spellings.
3. Guides/pronouns_and_relationship.md - Core character pronouns and register dynamics (e.g., Maya Fey sibling register vs Pearl Fey polite register).
4. Guides/[Insert active episode guide, e.g., ep3_big_top_reference.md] - Specific character voice dialects, terminology, and episode spellings.

Important Constraints:
- Do not overuse casual particles like 'นะ', 'น่ะ', 'ล่ะ'. Maintain Maya's sisterly register naturally by avoiding formal particles (ค่ะ/คะ/นะคะ) instead of repetitive ending particles.
- Dialogue distribution: Translate the dialogue sections naturally, and distribute the Thai text across the original lines as closely to the original splits as possible. Squash/combine only when grammatically necessary (subsequent combined lines must be left strictly as `#""`).
- Flush-Left: Any line immediately following a [NewLine();] or [ReadKey();] command must not start with a leading space.
- No backslashes: Do not escape internal quotation marks with backslashes (\). Use straight double quotes ("").

If the input file has more than 300 dialogue lines, you are highly encouraged to split the file into smaller chunks, translate them using subagents, and concatenate the outputs back to save token limits.
```


