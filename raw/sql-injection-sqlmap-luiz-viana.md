# SQL Injection with SQLMap — Luiz Viana (transcript, translated from Portuguese)

Have you ever imagined that an entire database could be exposed just by typing text into a website's form? Welcome to the world of SQL injection — literally injecting malicious SQL commands into a site's database through forms and parameters.

My name is Luiz Viana, a hacking and pentest specialist, and in this video you'll learn how to break into databases by exploiting SQL injection vulnerabilities using the SQLMap tool. After today, you'll never look at a form or a simple URL parameter the same way again.

SQL injection is one of the most dangerous vulnerabilities that exist, because with it an attacker can extract sensitive data from the database, take over administrator logins, and even make the database execute commands on the operating system. If you're already into this, you've probably heard of the classic `OR 1=1` trick to bypass a login — that's just the tip of the iceberg.

## What SQL injection actually is

First, a quick recap of what SQL is. SQL is the language used to talk to a database — it's how web applications search for products, verify logins, or display your data on screen.

What happens when an application doesn't correctly filter what you type into a form field or a URL parameter? That's what we call SQL injection. Instead of the system just reading what you wrote, it ends up *executing* what you wrote as if it were a legitimate command to the database.

For this to work, you first need to break the structure of the original query — and that's where the famous quote character comes in. Inserting a single quote in the middle of an input is meant to interrupt the query structure being built by the backend.

Why does this work? Because in SQL, any text value needs to be wrapped in quotes. When you type something into a field like a login field, that value gets embedded inside a query that already has quotes prepared in the application's code. If you add one more quote, you end up closing that string prematurely, and everything you type after that gets treated as part of the SQL instruction instead of as plain text.

That's exactly where the flaw is born: by breaking the original query's structure, you gain the freedom to inject your own commands into the database. The application doesn't notice what's happening because it just concatenates strings and sends them to the database — and the database, obediently, just executes them. Of course, this only happens in the context of a vulnerable application. That's why you should never build a SQL query through string concatenation — instead, sanitize user input and, above all, use parameterized queries.

## Why use SQLMap

Now imagine exploring SQL injection manually: inserting quotes into every parameter, then rewriting queries by hand to extract all the data. That's a lot of work — which is why there's a tireless robot that tests hundreds of injections per second: SQLMap.

SQLMap is an open-source tool that automates the detection and exploitation of SQL injection. It identifies the database type, tests parameters for vulnerabilities, picks the most suitable technique, and extracts data with precision — all under your control.

It's an extremely powerful tool, but only for someone who understands what they're doing. Simply running SQLMap and expecting results won't get you far if you don't know how SQL injection works. It's essential to understand how a query can be manipulated, how parameters behave, and what each type of injection does to the database. Without that manual foundation, SQLMap becomes just another tool running without direction — it executes commands based on the exploitation logic you define.

## Lesson 1 — Classic SQL injection

The simplest case of all. The scenario: a URL with a visible `id` parameter. The page loads normally when `id=1`, showing the data for the user whose ID is 1.

What if we mess with that parameter? Replace it with something unexpected — a single quote — and the page comes back with an error message: a SQL syntax error, indicating that the query structure was broken. We've found SQL injection, and the error even reveals the database type — in this case MariaDB, a MySQL fork.

Why does this happen? When we insert a stray quote, the application tries to build the query for the database, but the query ends up broken, so the database complains and throws that syntax error, since the query's structure is incorrect. This is our starting point for exploitation.

We could exploit this manually — testing payloads by hand to enumerate tables, columns, and extract each piece of data — but SQLMap does all that work for us.

On Kali Linux, open a terminal and run:

```
sqlmap -u <URL> -p id --dbms=mysql
```

- `-u` points to the target URL.
- `-p id` specifies the exact parameter to test.
- `--dbms` indicates the database type — not mandatory, but since we already saw from the error message that it's MySQL, specifying it speeds up detection a lot, since SQLMap will only test MySQL payloads.

After running the command, SQLMap starts sending a series of test payloads to the `id` parameter. Within seconds it identifies that `id` is vulnerable. The first technique it finds here is **boolean-based blind SQL injection**: the site doesn't display the query's result, so SQLMap tries conditions that return true or false and observes the application's behavior. For example: is the first letter of the table name "a"? If so, the page responds differently; if not, it doesn't change (or responds some other way). This is how it gradually extracts data based on these responses. It's called "blind" because the database executes the query but the response isn't directly visible.

Within blind injection there's also **time-based**, where confirmation comes from response timing: SQLMap sends a sleep condition, and if the site takes a few seconds longer to respond, it understands the condition was true, extracting data the same way.

Since we know the site displays error messages, SQLMap can also use **error-based** injection, forcing the database to emit error messages containing useful information like table names and query data — this speeds up exploitation a lot. There's also **UNION-based**, when you can append the original query's SELECT with a custom SELECT, letting you extract exactly the information you want directly. There are also more specific techniques like stacked queries or inline queries, which SQLMap also tests.

The nice part: SQLMap adapts the technique based on the application's behavior. If there's an error, it exploits that; if data appears on screen, it uses UNION; if nothing appears, it falls back to boolean-based or time-based blind. That's why it works so well.

Once the injection is confirmed, extraction commands include:

- `--dbs` — list all databases
- `-D <database>` — select a database, combined with `--tables` to list its tables
- `-T <table>` — select a table, combined with `--columns` to list its columns
- `-C <col1,col2>` — select specific columns
- `--dump` — extract the selected data

Imagine if this were a real site — this could expose data for thousands of people, and the internet is full of sites vulnerable in exactly this way.

SQLMap also lets you add custom HTTP headers, like session cookies or a custom user-agent — useful when the site requires authentication or when you want to simulate a real browser. Use `--headers` to pass a custom header (e.g., `User-Agent`), or pass session cookies the same way. In Lesson 1 this wasn't necessary, but if authentication were required, we could pass our cookies.

Another way to extract everything from the database at once is `--dump-all` — this pulls absolutely everything. If the database is large, this can take a while, so extracting step by step can be better in some cases.

## Lesson 7 — Reading server files via SQL injection

SQL injection isn't limited to manipulating the database — it can also be used to read files from the server. Some databases, like MySQL, allow filesystem access through specific functions, one of them being `LOAD_FILE`, which can read a file on the server and return its contents.

For security, MySQL usually has an option called `secure_file_priv` that restricts where you can read files from. If that option is disabled or misconfigured, you can read files from other parts of the system.

In Lesson 7's lab, we try reading `/etc/passwd` — the Linux file that lists system users:

```
sqlmap -u <URL> -p id --file-read=/etc/passwd
```

`--file-read` tells SQLMap to try reading the file via SQL injection, exploiting `LOAD_FILE` or an equivalent function. If it succeeds, SQLMap saves the file locally, and you can `cat` it to read the contents.

This is extremely critical: with this kind of read access, you can find configuration files that often contain database passwords, API keys, sensitive information, or even private SSH keys, giving direct access to the system.

And if, beyond reading files, you could also *write* files to the server — yes, that's possible too, and much more dangerous. Some databases like MySQL allow writing files to the filesystem via statements like `INTO OUTFILE`. If the database user has the right permissions, you can create files directly on the server and, from there, achieve remote command execution (RCE).

## Lesson 10 — Level and risk

The focus here isn't a new SQL injection technique, but a way to improve *detection* of injection points using the `--level` and `--risk` arguments, which help reveal flaws that would go unnoticed in a standard test.

By default, SQLMap runs with `level=1` and `risk=1` — basic tests on the most common parameters, using safe, fast payloads. Great for finding simple flaws quickly, but in some cases the application may be vulnerable in less obvious ways, and that's when SQLMap needs more freedom to test.

In Lesson 10, running SQLMap with default settings finds nothing — the parameter looks safe. But somewhere in the output there's a hint suggesting you increase level and risk. That's because the payload needed to exploit this flaw involves double quotes or a structure that's only tested at higher levels.

Increasing `--level` makes SQLMap test more parameters and more payload variations; increasing `--risk` makes it use more aggressive (and potentially more intrusive but more effective) payloads. In this case we use `--level 2 --risk 2`, plus `-v` (verbose) to show every payload being injected. With that, SQLMap easily identifies the vulnerability.

Lesson: trusting only SQLMap's default mode can produce a false negative. When the application doesn't reveal a vulnerability right away, adjust level and risk to widen the analysis — but be careful about the impact this has on the target application.

## Lesson 11 — Injection via POST parameters (login form)

So far we've only seen injection via GET parameters in the URL, but the process is the same for POST parameters in the request body. In the lab, there's a login form in Lesson 11. Inspecting the request, the application sends fields like `username`, `password`, and a submit button. If these values are inserted directly into a SQL query without protection, we have SQL injection here too.

Entering a simple quote produces a query/syntax error — one could even manipulate this to authenticate as administrator without extracting any data from the database.

Two ways to exploit this with SQLMap:

1. **Manual**, building the command with `--method POST` and `--data` carrying the exact request body the browser sends.
2. **From a captured request file** — useful when you need to send not just headers (cookies, user-agent) but the full body with all parameters exactly as sent by the application. The most practical way to capture this is opening the browser's Network tab, submitting the form, and copying the full raw request (including body). Then use `-r <file>` with SQLMap, pointing to that file — it will test every parameter found in it.

## Lesson 20 — Injection via HTTP headers (cookies)

A type of injection many people ignore: SQL injection in HTTP headers, especially cookies — cases where the server uses a cookie value directly inside a SQL query without proper handling.

In the lab, Lesson 20 has a login form. Putting a single quote directly into the form doesn't trigger an error — no direct SQL injection there. But looking at the information gathered after authenticating, we notice we receive a cookie called something like `uname` containing the username. If the backend takes that cookie value and puts it into a query without sanitizing it, we have SQL injection.

To test this, pass the URL and a custom `--headers` value with the cookie, using an asterisk (`*`) to mark the exact injection point inside the URL or headers — this tells SQLMap precisely where the injection should occur, even if it wouldn't normally recognize that spot as injectable. This customization is especially useful for APIs or when testing path parameters (parameters embedded in the URL path itself).

## Bypassing filters and WAFs

But what if the application has some kind of authentication or filter blocking injection attempts? That's where things get real. When the application has a WAF or an anti-injection filter, classic payloads stop working — they get detected and blocked before ever reaching the database. SQLMap has several features to try to bypass these protections.

- **Tampers**: scripts that disguise SQL commands without changing how the injection functions. A classic example is `space2comment`, which replaces spaces in the query with SQL comments — the database still understands it the same way, but the WAF may not recognize it as an injection attempt. Another is `randomcase`, which randomizes letter casing to bypass filters that match fixed-case keywords. Activate these with `--tamper=<script name>`; you can combine several. List all available tampers with `--list-tampers`.
- **`--technique`**: control which injection techniques SQLMap uses — e.g., `--technique=T` for time-based, `--technique=B` for boolean-based, `--technique=U` for UNION-based. Forcing a specific technique can also help bypass some WAFs.
- **`--random-agent`**: rotates the User-Agent on every request, simulating different browsers.
- **`--delay`**: adds an interval between requests to avoid rate-limit/lockout blocking.

SQLMap has many more commands, options, and exploitation techniques than covered here, but this gives you the fundamentals of the tool.

---
*Source: pentest/hacking training video by Luiz Viana on SQL injection and SQLMap. Transcribed and translated from Portuguese for the wiki.*
