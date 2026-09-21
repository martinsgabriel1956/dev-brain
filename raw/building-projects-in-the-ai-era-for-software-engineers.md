# Building Projects in the AI Era for Software Engineers

- **Author:** Himanshu Singh
- **Published:** September 13, 2026
- **Source URL:** https://hsnice16.medium.com/building-projects-in-the-ai-era-for-software-engineers-72f3ddcd2a40

---

4 min read

Sep 13, 2026

Hello everyone 👋, I am Himanshu Singh.

If you are reading my blog for the first time, let me introduce myself.

I am a Full-stack Software Engineer leaning towards the frontend. I have been pushing code to production since 2022, mainly in the Web3 space. I have worked on a crypto wallet extension, a perpetual DApp, and an automated market maker (if you know all these terms :'))

Let's begin our blog!

## What this blog is about

Recently, we've all been witnessing advancements in LLM tools, especially in the quality of the code they generate. And since most things are software, they indirectly affect everything related to software.

I built two projects entirely using AI, without reading the code or typing anything by hand. An LLM did it all.

In this blog, I will share what I learned from building two projects in the AI era.

> I have built [**agentfriendlycode.com**](https://agentfriendlycode.com/) and [**usetu.la**](https://usetu.la/).
>
> Agent-Friendly Code ranks public repositories based on their agent-friendliness. You can use the scorer in a GitHub Action, as an Agent Skill, and you can also live-score a public repository.
>
> Tula shows your cross-venue exposure on **HyperLiquid**, **Aave**, and more venues, what breaks first, and more.

## What I learned

Well, whatever I have shared below is based on my personal learnings, so take it with a pinch of salt.

### Asking too many questions

Since I am not coding or checking the code that the agent is producing, I ask a lot of questions to give the agent an exact idea of what we are looking for from the session. That way, the agent can better understand what it needs to do.

I generally start with the problem statement that we are trying to solve with the project, and then start by asking, "Let's brainstorm on the possible solutions," and start the discussion from there.

Then, based on the response, I ask the following questions, and after making sure we have decided on the user flow, security concerns, and architecture, I ask it to start the implementation.

### Don't take things for granted

I don't take things for granted. Before committing, I always ask the agent to do these things:

- Make sure the code is following all the best practices.
- Make sure the written comments are concise, correct, and there is no beating around the bush.
- Make sure all the files in the whole codebase are in sync, consistent, correct, and up to date.
- Make sure there are no critical or confidential data leaks anywhere in the whole project.
- There should be no compromise on user experience and security.
- You could spin up multiple agents if needed, and you can also search the Internet if required to complete these things.
- Make sure you do it carefully. This is important.

I run this before every commit and sometimes in between big changes because this is important.

### Hack to make sure the agent has not started hallucinating

This could be a dumb thing, but whenever I start seeing a not-so-good response, I try to end the conversation with a closing statement, then close the terminal, and start a fresh new session.

This is helping me so far.

If I want the agent to pick something from any of our last conversations, I just ask the agent if it can search for the conversation in which we were having a discussion about a particular thing.

It works.

### Giving a reference produces good output

I have noticed this with user interfaces: if you give the agent a reference for what you are expecting and what the correct thing should look like, it produces a good output within a couple of iterations (sometimes it is the first shot itself).

_You might think, but then how can we produce new things for which we don't have any reference?_

What I meant was, suppose some parts of the generated UI have issues. Instead of just typing that this part of the UI has this issue and that issue, if you could take a screenshot of the part having issues and share it with the agent, pointing out that this part has this issue and it should be like this, then it would produce good output.

## No agent swarms?

Some of the readers will surely think I am not a chad of vibe coding, and that's true.

I have seen folks on X mentioning how they are running swarms of agents to do multiple things at once, to tackle multiple issues at once, or sometimes running them to do different things for a single problem statement.

But I don't think I can do that right now. Maybe because I don't have that many things to run at once.

## We are at the end

This was all for now. As I keep building more projects entirely using AI, I might learn more new things. Then we can do a Part 2 of this blog, and I will share the new learnings in that.

Thank you for reading it till the end.

Stay fit. Stay healthy.
