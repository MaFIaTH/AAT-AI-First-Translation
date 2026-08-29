# Phoenix Wright: Ace Attorney — Names Spelling Reference & Dictionary

This document serves as the official spelling dictionary and terminology reference for localizing character names, locations, and special terms in the *Phoenix Wright: Ace Attorney* series into Thai.

---

## 1. Core Name Formatting Rules

### A. The Name Wrapping Rule (`<Name>`)
To facilitate automated global replacements of localized names, all character names (first name, last name, and full name) **must** be enclosed in `<>` brackets in the Thai translation.
- **Rule:** Any titles, honorifics, or prefixes (e.g., "คุณ", "พี่", "ผู้หมวด", "อัยการสูงสุด") must be placed **outside** the brackets.
- **Examples:**
  - `Mr. Wright` $\rightarrow$ `คุณ<ไรท์>`
  - `Ms. Mia Fey` $\rightarrow$ `คุณ<มีอา เฟย์>`
  - `Detective Gumshoe` $\rightarrow$ `ผู้หมวด<กัมชู>`
  - `Chief Prosecutor Lana Skye` $\rightarrow$ `อัยการสูงสุด<ลาน่า สกาย>`
  - `sis` (spoken by Ema to Lana) $\rightarrow$ `พี่<ลาน่า>`
- **Exceptions:**
  - Non-person names (such as items, locations, or pets) do not use `<>` unless they are officially listed as characters in this names dictionary.
  - The **`Judge`** (translated as `ผู้พิพากษา` or `ท่านผู้พิพากษา`) is a special exception and **must not** be enclosed in `<>` brackets.

### B. Tag Spacing Rule
Prefer **no space** immediately before or after name tags (e.g., `เห็น<มายา>บอก` is preferred over `เห็น <มายา> บอก`). It is rarer to see a space around tags in refined scripts, so keep formatting tight unless a space is stylistically required.

### C. No Name Hallucination (Strict Rule)
If a character's name does not exist in the original English dialogue line, **do not insert or inject a name tag** in the Thai translation.
- **Pronoun usage:** When characters address each other naturally using pronouns like `you`, translate it using Thai interpersonal pronouns (e.g., `พี่`, `คุณ`, `นาย`, `เธอ`) **without adding the name tag `<>`**.
- **Examples:**
  - *English:* `Maybe you should leave the drama alone.` $\rightarrow$ **Correct:** `บางทีพี่ควรเก็บเรื่องดราม่าไว้ดีกว่า` (❌ **Incorrect:** `บางทีพี่<นิค>ควร...`).
  - *English:* `I guess you didn't hear.` $\rightarrow$ **Correct:** `สงสัยพี่จะไม่ได้ยิน` (❌ **Incorrect:** `สงสัยพี่<นิค>จะ...`).
  - *English:* `I'm sure you will win.` $\rightarrow$ **Correct:** `หนูมั่นใจว่าพี่จะชนะ` (❌ **Incorrect:** `หนูมั่นใจว่าพี่<นิค>...`).

### D. Strict Name Length Matching (No Arbitrary Lengthening or Shortening)
Translate names strictly according to the exact form written in the English source. **Never expand a shortened name or shorten a full name arbitrarily:**
- **`Max`** $\rightarrow$ **`<แม็ก>`** (Do not lengthen to `<แม็กซิมิเลี่ยน>`).
- **`Maximillion`** $\rightarrow$ **`<แม็กซิมิเลี่ยน>`**.
- **`Maximillion Galactica`** $\rightarrow$ **`<แม็กซิมิเลี่ยน กาแลกติก้า>`**.
- **`Nick`** $\rightarrow$ **`<นิค>`** (Do not lengthen to `<ฟีนิกซ์ ไรท์>`).
- **`Mr. Wright`** $\rightarrow$ **`คุณ<ไรท์>`**.
- **`Phoenix Wright`** $\rightarrow$ **`<ฟีนิกซ์ ไรท์>`**.
- **`Ben`** $\rightarrow$ **`<เบ็น>`** (Do not lengthen to `<เบนจามิน วูดแมน>`).
- **`Benjamin Woodman`** $\rightarrow$ **`<เบนจามิน วูดแมน>`**.

---

## 2. Standard Core Terminology

- **`Channeling Chamber`** $\rightarrow$ **`โถงทำพิธี`** or **`โถงพิธี`** (never `ห้องอัญเชิญวิญญาณ` or `ห้องทรงเจ้า`).
- **`Master`** (of the Kurain Fey Clan) $\rightarrow$ **`ปรมาจารย์`** (never `ท่านเจ้าสำนัก` or `เจ้าสำนัก`).
- **`Winding Way`** $\rightarrow$ **`ทางคดเคี้ยว`**.
- **`Steel Samurai`** $\rightarrow$ **`ซามูไรเหล็กไหล`** (Steel Samurai show localization).
- **`Court Record`** $\rightarrow$ **`บันทึกคดี`** (never `สำนวนคดี` when referencing the active court records index).
- **`Added to Court Record` (UI)** $\rightarrow$ **`ลงในบันทึกคดีแล้ว`** / **`ลงไปในบันทึกคดีแล้ว`**.
- **`Testimony` (in court/trial)** $\rightarrow$ **`คำเบิกความ`** (never `คำให้การ`, which is reserved for pre-trial police statements).
- **`Witness Stand`** $\rightarrow$ **`คอกพยาน`** or **`คอก`** (never `แท่นพยาน`).
- **`Autopsy Report`** $\rightarrow$ **`รายงานผลชันสูตร`** (natural, concise court standard).

---

## 3. Core Names Spelling Dictionary
This list contains core characters who appear repeatedly across multiple episodes and games.

| English Name | Thai Translation | Tagged / Brackets Format | Notes |
|---|---|---|---|
| Phoenix Wright | ฟีนิกซ์ ไรท์ | `<ฟีนิกซ์ ไรท์>` (Nick: `<นิค>`) | |
| Maya Fey | มายา เฟย์ | `<มายา เฟย์>` (Nick: `<มายา>`) | |
| Mia Fey | มีอา เฟย์ | `<มีอา เฟย์>` (Nick: `<พี่มีอา>`) | |
| Pearl Fey | เพิร์ล เฟย์ | `<เพิร์ล เฟย์>` (Nick: `<เพิร์ลลี่>`) | |
| Dick Gumshoe | ดิกค์ กัมชู | `<ดิกค์ กัมชู>` | Spoken of as: ผู้หมวด<กัมชู> |
| Miles Edgeworth | ไมล์ เอ็จเวิร์ธ | `<ไมล์ เอ็จเวิร์ธ>` | Standardized with **เอ็จ** (`จ`) |
| Franziska von Karma | ฟรานซิสกา ฟอน คาร์มา | `<ฟรานซิสกา ฟอน คาร์มา>` | Standardized as **คาร์มา** (no tone mark) |
| Manfred von Karma | มัลเฟรด ฟอน คาร์มา | `<มัลเฟรด ฟอน คาร์มา>` | |
| Winston Payne | วินสตัน เพย์น | `<วินสตัน เพย์น>` | |
| Judge | ผู้พิพากษา | `ผู้พิพากษา` | **NO BRACKETS** |

---

## 4. Episode-Specific References
For names and terms specific to individual episodes, refer to the following sub-documents:
- **[names_pwaa.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/names_pwaa.md)**: Spelling reference for PWAA (Episodes 1 to 5).
- **[names_jfa_ep1_ep2_ep4.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/names_jfa_ep1_ep2_ep4.md)**: Spelling reference for JFA (Episodes 1, 2, and 4).
- **[ep3_big_top_reference.md](file:///home/beaver_bloyde/Desktop/ATT%20Project/AI%20Training/Guides/ep3_big_top_reference.md)**: Spelling reference and terminology standard for JFA Episode 3 (Turnabout Big Top).
