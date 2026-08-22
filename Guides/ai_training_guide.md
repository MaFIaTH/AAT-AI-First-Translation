# AI Training & Workflow Guide (Ace Attorney Trilogy Thai Localization)

This repository is designed specifically for localizing the **Ace Attorney Trilogy** into Thai using agentic AI assistants. The AI agent is responsible for executing tools, running scripts, updating guidelines, and validating output autonomously by reading the rules inside the `Guides/` directory.

As a human coordinator, your prompts should be simple and direct.

---

## 🛠️ Scenario 1: Translating a New Case for the First Time
When a new script template is ready for translation:

1. **Human Action**: Place the raw script template in the `Workspace/Original/` directory.
2. **Human Prompt**:
   > *"Translate the new script at `Workspace/Original/ep4_template.txt`."*
3. **Autonomous AI Action**: The AI agent reads the guides, runs the extraction command, translates the lines, runs verification checks, and merges the final script.

---

## 🔄 Scenario 2: Training the AI with a Human-Refined Script
When you have polished a script and want the AI to learn your style rules, vocabulary, and registers:

1. **Human Action**: Place the polished script in the `Workspace/Refined/` directory.
2. **Human Prompt**:
   > *"I have finished refining `Workspace/Refined/sc2_0_text_u_refined.txt`. Please run a comparison check against `Workspace/Translated/sc2_0_text_u.txt`, update the master guides inside `Guides/` to incorporate my refined spelling/register choices, and commit the updates to Git."*
3. **Autonomous AI Action**: The AI agent performs the discrepancy check, updates the spelling dictionaries and relationship guides, and commits the changes.

---

## ✍️ Scenario 3: Updating the AI Guide for a Specific Case
When you want to add unique character speech patterns, accents, or dialects:

1. **Human Action**: None.
2. **Human Prompt**:
   > *"Please update `Guides/ep4_goodbyes_reference.md` to add registers for Lotta Hart (Southern country accent localized as Southern Thai dialect, uses self-pronoun 'นุ้ย', ending particle 'นิ') and Manfred von Karma (arrogant snaps, no polite particles, calls Phoenix 'ทนายไร้ระดับ')."*
3. **Autonomous AI Action**: The AI agent edits the episode reference document directly and commits the changes to Git.
