# PhD to industry resume coach

A Claude skill that helps PhD graduates, postdocs and early-career researchers turn an academic CV
into an industry resume.

Custom-made by **Niels Wouters** ([nielswouters.au](https://nielswouters.au)) for attendees
of the ACM-W workshop *From Research to Industry*, organised by the ACM-W Student Chapter at Monash
University together with the Monash FIT EDI Portfolio.

## What it does

Give Claude your CV or resume and it will help you in one of three ways:

- **Convert** a long academic CV into a 1–3 page industry resume, with your PhD listed as work
  experience.
- **Critique** an existing resume: what a recruiter sees on page one, the main fixes, and
  bullet-by-bullet rewrites.
- **Tailor** your resume to a specific job ad: what to move up, what to cut, and how to reframe
  your experience for that role.
- **Recap** the workshop: go back over a section, take the resume myths quiz, try the
  before/after exercises, or work through the after-graduation checklist. No resume needed.

It works as a coach, not a ghostwriter. It only uses facts you give it, and when a bullet needs a
number it doesn't have, it leaves a gap like `[how many?]` and asks you. It won't make up
results for you.

The advice is written for the Australian job market, with notes for other countries.

## What's in this repo

```
phd-industry-resume/
├── SKILL.md                  How Claude runs the coaching
└── references/
    ├── rules.md              Core rules, common resume myths, and things to avoid
    ├── bullets.md            How to rewrite a bullet, with before/after examples
    ├── tailoring.md          Reading a job ad and adjusting for different role types
    ├── australia.md          Australian conventions and government roles, plus other countries
    ├── model-resume.md       An anonymised, annotated example resume
    └── workshop-recap.md     The workshop sections, run as an interactive recap
```

## Install it

### In the Claude app (claude.ai, desktop or mobile)

1. Download the `phd-industry-resume.skill` file from this repository. There's also a release you can consider via `https://github.com/mediatecture/acmw-industry/releases`.
2. Make sure code execution is on: **Settings > Capabilities**, then turn on **Code execution
   and file creation**. On a Team or Enterprise account, your organisation admin controls this.
3. Zip the `phd-industry-resume` folder (the folder itself, not the whole repo).
4. Go to **Customize > Skills**, click **+**, then **Create skill > Upload a skill**, and upload
   the zip.
5. Check the skill is switched on in your skills list.

Skills work on Free, Pro, Max, Team and Enterprise plans. Menu names change from time to time;
see Anthropic's guide, [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude),
for the current steps.

### In Claude Code

Copy the `phd-industry-resume` folder into `~/.claude/skills/`.

## Use it

Start a new chat, attach or paste your CV, and say what you want. For example:

- "I'm finishing my PhD in computer science. Can you turn this academic CV into an industry
  resume? I'm aiming for UX research roles."
- "Is my resume any good for data science jobs?"
- "Here's my resume and a job ad for a policy officer at the Department of Health. Help me tailor
  it."
- "Quiz me on the resume myths from the workshop."
- "Recap the workshop. I missed the part on writing bullets."

Claude may ask a few questions first (what roles you're after, how much experience you have),
then give you feedback and rewritten text to put into your own resume.

## A few things to keep in mind

- **Read every rewrite before you use it.** Change anything you wouldn't say yourself. Your resume
  should sound like you.
- **Check every number.** If you can't back it up in an interview, leave it out.
- **Send a PDF**, named something like `Firstname_Lastname_Resume_Organisation.pdf`.
- **Think about what you share.** Remove details you don't want to give an AI service, such as
  your home address or referees' contact details.
- **No proven success.** This skill is only one of several tools you might want to consider when you're writing a resume. There's definitely to guarantee of success, and you shouldn't just copy-and-paste the outputs of this skill. It's just there to help you think differently about your current resume.


## Feedback

Questions or suggestions: [nielswouters.au](https://nielswouters.au).
