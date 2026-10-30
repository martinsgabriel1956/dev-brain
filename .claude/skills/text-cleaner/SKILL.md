---
name: text-cleaner
description: Specializes in cleaning text from technical noise (timestamps, comments like [laughter], [music], HTML tags) while preserving the original text unchanged. ALWAYS use this skill if the user provides a transcript, subtitle files (SRT, VTT), messy copy-pasted web text, or asks to clean text from timestamps, noise, or formatting clutter.
metadata:
  version: 1.0.5
  local_note: auto-update step removed on install (manual updates only)
  repository: https://github.com/BogdanovychA/skills
---

# Text Cleaner (text-cleaner)

This skill specializes in cleaning text from technical noise and "clutter" that hinders reading, while preserving the original content and every word of the author unchanged.

## Mission
To help users get clean, readable text from "dirty" transcripts, subtitles, or text copied from web pages. **The skill activates upon requests to clean text from timestamps, noise, HTML tags, or other technical clutter.**

## Main Goal
To remove everything that is not part of the speech or the main content, without resorting to shortening, paraphrasing, or summarizing.

## Text Processing Rules
- **Completeness of Text:** **CRITICAL:** Keep the input text verbatim. It is FORBIDDEN to shorten, generalize, or throw out any sentences. Every word of the author must remain in place. If the text is very long, process it in chunks to avoid hitting output limits, but NEVER omit content.
- **Noise Cleaning:**
    - Remove timestamps in any format (e.g., `00:00:10`, `[12:34]`, `12:34.567`).
    - Remove comments about background sounds or non-verbal actions (e.g., `[laughter]`, `[music]`, `(laughs)`, `[applause]`, `[сміх]`, `[музика]`).
    - Remove HTML tags and unnecessary attributes (e.g., `<div>`, `<p class="...">`, `&nbsp;`).
    - Remove promotional inserts if they are clearly technical (e.g., "Subscribe to the channel", "Subscribe", if it's a system subtitle insert).
    - Remove all emojis.
- **Paragraphs:** If the text is a solid block, break it into logical paragraphs for readability.
- **Minimal Formatting:**
    - Output the result in Markdown format (`.md`).
    - **Header:** ALWAYS start the text with a top-level header (`#`) that reflects the overall essence and topic of the text.
    - Use a minimal number of subheaders (`##`) only to separate very large blocks of text by meaning, if logically necessary. In other cases, paragraph separation is sufficient.
    - It is FORBIDDEN to add a TOC (table of contents), Summary, or YAML blocks unless the user explicitly asked for them. The output should be just clean text.
- **Quality Verification:** After cleaning, you **MUST** perform a rigorous self-check. Compare the input and output text side-by-side to ensure that no sentences or key information were lost during the removal of technical noise. If you identify any unintended omissions or shortened sections, you **MUST** restore them immediately to match the original verbatim content. The integrity of the original content is paramount.

## File Name Format
If the user asks to save the result to a file, the name should be meaningful, based on the text topic, and use Latin letters (slug).
Format: `YYYY-MM-DD-slug-name.md`
Example: for text about the number pi — `2026-04-20-number-pi-square-circle.md`

## Example

**Input:**
User: "Clean this text from timestamps and background noises:
[00:01:05] [laughter] Alright, let's start the meeting.
[00:01:10] First of all, we need to review the Q4 marketing plan (which is almost done). [music]
[00:01:20] Next, John will show the demo."

**Output:**
```markdown
# Meeting Start and Q4 Marketing Plan

Alright, let's start the meeting.

First of all, we need to review the Q4 marketing plan (which is almost done).

Next, John will show the demo.
```

## How to Work with This Skill

1. **Language Policy**: Respond to the user in the same language they used to ask their question to ensure a natural and clear communication flow.
