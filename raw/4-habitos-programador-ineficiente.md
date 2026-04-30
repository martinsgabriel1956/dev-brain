# 4 Habits That Make You an Inefficient Developer

**Source:** https://medium.com/better-programming/4-habits-that-make-you-an-inefficient-developer-f4384c4b9df5  
**Author:** Dano  
**Date added:** 2026-04-29

---

## Overview

You are not a bad programmer — you may have the habits of a bad programmer. This article clarifies 4 of those habits.

An important distinction: **being something vs. being in a state of something.** When people say "I'm not a good programmer," it's like saying "I am tired" as if it were a permanent identity, when in reality you can *be in a state* of a bad development level, just as you can be in a state of tiredness.

The brain often chooses between two paths:
- One that may generate progress, but guarantees discomfort.
- One that will not generate progress, but guarantees comfort.

Videos and articles that generate discomfort are the ones with the highest potential for real progress.

---

## Habit #1 — Saying "Yes" to Everything

Helping everyone is a laudable posture. However, a promise is a debt. Accumulating unlimited commitments will:

- Blow up your time budget.
- Dramatically reduce your productivity and performance as a programmer due to constant interruptions.

**The hidden cost of always saying yes:** People become addicted to your opinion. They stop assuming their own risks. Instead of unlocking new leaders within the team, you end up diluting responsibility into a single person — a bottleneck.

**A counterintuitive approach:** When someone asks you to review an e-mail or decision before acting, let them act first, then give feedback. The person assumes 100% of the risk and 100% of the potential return — which is far more powerful for their growth.

**Caveat:** Calibrate the seniority level with the risk level. Don't leave a junior developer who just gained production database access to answer their own question about whether to run an `UPDATE` without a `WHERE` clause.

> *"When you say yes to others, make sure you are not saying no to yourself."* — Paulo Coelho

---

## Habit #2 — Your Definition of "Done" Probably Isn't Done

Writing code is only one of many tasks a programmer must complete. There's a visible difference between programmers who understand this and those who don't.

If you believe "it compiles and the ticket is closed = done," you are likely far from done. Ask yourself:

- **Can another developer easily understand this code?** If not, you have strong evidence it needs refactoring — and the work wasn't truly finished.
- **Does the change reflect in documentation?** If not, it's a draft.
- **During code review, are you reading for style errors instead of business logic?** Business rules are harder to review, but they matter infinitely more.
- **Did you test only the happy path?** Then see Habit #3.

---

## Habit #3 — Not Testing Your Own Code

Testing only the happy path is as pointless as agreeing with your own opinion.

Regardless of whether your team has a dedicated QA engineer, you must:

1. **Write automated tests.** Start as early as possible to build speed and fluency.
2. **Test error paths too.** Guarantee behavior for both success cases and cases that should return error messages.
3. **Earn the right to be fooled by your own test** — that level of rigor is where the skill really develops.

---

## Habit #4 — Making Giant Commits

A giant pull request is a nightmare: nobody wants to review it, and nobody knows when it will end.

A common antipattern: one commit breaks a test, the next commit fixes that test — two separate, disconnected units of change.

**The fix:** In a single commit, bundle the code change *and* the test change that validates it. Make each commit a functional unit of change, not a diary entry.

Benefits:
- Each commit becomes more valuable and better scoped.
- Reviews are faster.
- History is easier to understand and bisect.

---

## Connection

All four habits point in the same direction: becoming a faster, more deliberate, and more professional developer. Fewer bad habits = higher output quality = greater market value.
