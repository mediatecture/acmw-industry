# Workshop recap mode

Attendees use this to go back over the workshop *From Research to Industry*: to revise it, to
catch a part they missed, or to try the exercises on their own material. Run it as a
conversation, the way it ran in the room, not as a document dump.

## How to run it

1. **Offer the menu.** Unless they've already named a section, list the five sections below with
   one plain line each, and ask which one they want. Keep it short.
2. **One step at a time.** Give a small piece, then stop and let them respond. For the quiz, that
   means one myth per message. Don't print a whole section in one go; that turns it into notes,
   and they can read notes anywhere.
3. **Let them answer before you explain.** Where the workshop asked the room a question, ask them
   the same question and wait.
4. **Connect it to them.** After each section, offer to apply it to their own resume or a bullet
   from it. The recap is a warm-up for the real work.
5. **Same voice rules as the rest of the skill.** Plain, specific, no slogans (see "How you write"
   in SKILL.md). Don't add enthusiasm the workshop didn't have ("Great answer!"). If they got a
   myth right, say so in a few words and give the reason.
6. **Don't invent workshop content.** Stick to what's in this file. If they ask about something
   that isn't here (for example, something the speaker said out loud), say it isn't in your notes
   from the workshop, then answer from the rest of the skill if you can.
7. **Stop when they want to.** After a section, offer the next one or a switch to their resume.
   Don't push through all five.
8. **Random every time.** The myths quiz draws 5 random questions from a pool of 21, and the
   before/after examples come in a random order, so students who repeat the recap, or compare
   notes with each other, get a different set. See "Getting a random order" below.

## Getting a random order

You can't pick a random order reliably in your head; you'll tend to repeat the same sequence. So
before you ask the first question of the myths quiz or the before/after examples, run the shuffle
script in this skill's `scripts` folder:

```
python3 scripts/shuffle.py myths          # myths quiz: 5 random questions out of 21
python3 scripts/shuffle.py myths --all    # only if they ask for every question
python3 scripts/shuffle.py examples       # the before/after examples, all 4 in random order
```

(Use the path to the skill's folder, e.g. `python3 /path/to/phd-industry-resume/scripts/shuffle.py
myths`.) It prints item numbers from the tables below, e.g. `17, 2, 9, 14, 5`. Ask exactly those
questions, in exactly that order, and keep to it for the rest of the section. Run it again if
they want another round; a new round gives a new set.

- Don't show the list or the item numbers to the user. Number questions by position
  ("Question 1 of 5"), not by their number in the table.
- Run the script once per round, not once per question.
- If you can't run code in this conversation, don't fall back to the table order or the first
  five. Pick five from across the whole table, avoiding any run of consecutive numbers, and
  choose a different set if they ask for another round.

## The menu

1. **Why your PhD counts:** what a PhD shows an employer, and the roles you've already done
2. **Resume myths quiz:** five yes/no statements about resumes, different each time
3. **Writing a good industry resume:** the five rules, STAR, and before/after rewrites
4. **What not to do:** a real example of what to avoid, and the don'ts
5. **After graduation:** a checklist for the weeks after you finish

---

## 1. Why your PhD counts

The workshop opened with the speaker's own path through academia, consulting and industry, across
projects in co-design, immersive art, media architecture, usability testing and AI governance.
The point: a research career builds skills that transfer, even when the projects look nothing
like an industry job.

Key message: **a PhD is evidence of commitment, and of a broad and flexible skillset.**

**Exercise.** Ask: "Most people see their PhD as making them an expert in one topic. What other
roles do you think you played during your PhD?" Let them answer, then show the full list:

- **Expert:** deep knowledge, methods, tools
- **Storyteller:** talks, writing for non-specialists, outreach, media
- **Investigator:** research design, interviews, experiments, analysis
- **Educator:** tutoring, lecturing, supervising, running workshops
- **Project lead:** running a multi-year project to deadline, budgets, ethics, events
- **Fundraiser:** grants, scholarships, travel funding, partnerships
- **Collaborator:** co-authors, industry or government partners, community groups

Then ask them to pick the two roles they've done most, and name one concrete example of each.
Those examples are material for resume bullets; offer to turn one into a bullet.

## 2. Resume myths quiz

First run `shuffle.py myths` (see "Getting a random order"). It picks 5 of the 21 statements
below. Never go through the table top to bottom.

Ask one statement at a time: "Question 1 of 5. Yes or no: [statement]". Wait for their answer.
Then give the answer and the reason in two or three sentences, and move to the next. At the end,
give the score in a few words and mention the ones they got wrong. Then offer another round of
five (run the script again) or a check of their own resume for these myths.

Statements 1–11 come from the workshop slides. Statements 12–21 were added afterwards; they all
follow from the most common misconception, that an industry resume works like an academic CV: a
complete record read carefully by experts, when in fact it's the case for one job, skimmed by a
non-specialist.

| # | Statement | Answer | Reason to give |
|---|---|---|---|
| 1 | My resume can be longer than 3 pages. | No | Nobody reads past page 2 closely, and a long resume suggests you can't prioritise. Aim for 1–2 pages as a recent graduate, 3 at most with more experience. |
| 2 | My PhD counts as work experience. | Yes | It's years of self-directed, funded work with deadlines and outcomes. List it under Experience as a job. |
| 3 | Managing a supervisor counts as stakeholder management. | Yes, if you show it | Negotiating scope, timelines and expectations with supervisors, panels and partners is real stakeholder work. A concrete example counts; the bare phrase doesn't. |
| 4 | I should list my academic publications. | It depends | For research-heavy roles (R&D, data science, policy research), list a selected 3–5. For other roles, one line with a count and a link is enough. |
| 5 | A recruiter or employer will read my entire resume. | No | They skim, often only the top of page one, before deciding. Put your strongest evidence there. |
| 6 | Someone will Google me before an interview. | Yes | Make sure your LinkedIn matches your resume and that what they find helps you. |
| 7 | I can use one resume for all job applications. | No | Keep a base resume and tailor a version for each application. |
| 8 | I should mention my communication skills. | No | Everyone claims them, so the phrase says nothing. Show it instead: talks, media, workshops, reports for non-specialists. |
| 9 | My resume should lead with my education. | No | Lead with a short summary and your experience. "PhD" after your name already tells them. Education goes near the end. |
| 10 | My email address can be party.pink.755@hotmail.com. | No | Use something like firstname.lastname on a provider you'll keep. Not your uni email either, since you'll lose it. |
| 11 | My H-index will impress an industry employer. | No | Most won't know what it is, and those who do won't weigh it much. Show reach, adoption or change instead. |
| 12 | A recruiter spends about a minute on the first look at my resume. | No | Eye-tracking studies put the first scan at under 10 seconds. Whatever is at the top of page one decides whether they read on. |
| 13 | Listing my duties shows an employer what I can do. | No | Duties show what the job was. Results show what you can do: what changed because of you. |
| 14 | A hiring manager will understand my field's terms. | No | Write for a smart reader from outside your field. If a bullet needs your field's vocabulary to make sense, rewrite it. |
| 15 | A PhD makes me look overqualified, so I should play it down. | No | Hiding it leaves a gap of several years. Present it as a job with results, and it reads as experience. |
| 16 | Tutoring counts as relevant experience for jobs that aren't teaching. | Yes | Explaining hard ideas, running a room and giving feedback are skills most jobs need. |
| 17 | An honest estimate like "~200 participants" is fine on a resume. | Yes | An estimate you can explain beats a vague claim. A number you can't defend in an interview doesn't. |
| 18 | Grant funding I helped win belongs on my resume. | Yes | Winning money is something employers understand. State your role honestly, such as "co-wrote" or "led". |
| 19 | Experience only counts if someone paid me for it. | No | Volunteering, side projects, outreach and organising events all count if they show the skills the job needs. |
| 20 | A two-column template with icons and skill bars helps me stand out. | No | It can confuse applicant tracking systems, and many applicants use the same templates. Plain and well spaced reads better. |
| 21 | Applying online is enough; I don't need to talk to anyone. | No | Conversations with people in the field tell you which jobs to aim for and how to frame your resume. Sometimes they lead to a referral. |

## 3. Writing a good industry resume

Take this in three short parts, pausing after each.

**Part A: the five rules.** Give them as a short list:

1. Keep it short and front-loaded
2. A PhD is work experience
3. Show metrics that matter
4. Curate and tailor
5. Online presence is part of it

Then the principle behind them: **on a resume, don't tell them what you learned; show them what
you delivered.** Ask which rule they think their current resume breaks most.

**Part B: STAR.** Explain briefly: Situation (the problem), Task (the goal), Action (what you
did), Result (what changed). On a resume, Situation and Task are often squeezed into a few words;
Action and Result must be there.

Then run the before/afters as a guessing game. First run `shuffle.py examples` (see "Getting a
random order") and use that order; the examples below are numbered 1–4. Show the "before" and
ask: "What's missing, and how would you improve it?" Let them try, then show the "after" and name
what changed.

1. **Before:** Sessional tutor for Introduction to Robotics (2024–2026).
  **After:** Taught weekly labs of 25 first-year students across 4 semesters; redesigned C++
  exercises around hands-on challenges, lifting student satisfaction from 3.8 to 4.5.
  *Changed: a job title became an action, with scale, an initiative and a measured result.*

2. **Before:** Conducted interviews for PhD research.
  **After:** Recruited and interviewed 40 farmers across regional Victoria, building a dataset now
  used by two other research projects.
  *Changed: recruitment counted as work, a specific number, and evidence that others used it.*

3. **Before:** Responsible for customer interviews and research operations.
  **After:** Rebuilt research operations: 4x customer contact (~25 to ~100 interviews a quarter)
  and 20% lower operating costs, by consolidating tools and livestreaming all interviews.
  *Changed: "responsible for" became "rebuilt", with two numbers a business understands.*

4. **Before:** Created an AI art installation exhibited at several venues, which attracted media
  attention.
  **After:** Reached an estimated 250m people through media coverage (~$250k advertising
  equivalent), secured $180k to build a touring museum exhibit, and gave talks at international
  policy forums.
  *Changed: vague attention became reach, money won, and who invited them.*

Do two or three, not all four, unless they want more. Take them from the start of the shuffled
order, so different students see different examples.

**Part C: one bullet, three questions.** Show this bullet:

> Ran 4 urban field studies, with findings published in peer-reviewed venues.

Walk through the three questions, one at a time, showing the rewrite each produces:

1. **What did I actually do?** → Designed and built 4 interactive displays and evaluated them
   with local residents, with support from councils and an industry partner.
2. **So what? Who cared?** → Published findings at international venues (20–25% acceptance), with
   coverage on national TV, radio and newspapers.
3. **For this role?**
   - UX research: Ran 4 field studies with 32 residents to test how people use public technology;
     findings shaped design guidelines adopted by industry partners.
   - Government or policy: Partnered with 2 city councils to test digital tools for community
     participation, reaching ~200 residents and informing a council's procurement strategy.

The point to make: each version is true, and each suits a different reader. That's why one resume
can't serve every application.

Close the section with the checklist from the workshop:

- **Start with action verbs:** led, built, secured, redesigned, delivered
- **Everything needs a number:** taught 100 students, supervised 3 Honours students, managed a
  $120k budget, cited in 2 government reports
- **Cut academic filler:** "was involved in" → "helped build"; "assisted with data collection" →
  "collected data"; "it could be argued that" → delete it
- **Make it an exciting read**
- **Keep the full story for interviews**

Then ask them for one bullet from their own resume and work through the three questions on it
together. Follow the drafting rules in SKILL.md: only their facts, `[?]` for missing numbers.

## 4. What not to do

Show this cover letter opening and ask: "What do you learn about this person from this
paragraph?"

> I am thrilled to apply for this exciting opportunity at your innovative organisation. In today's
> rapidly evolving landscape, I am eager to leverage my passion for research and my unique blend of
> analytical and creative skills to drive meaningful impact. Throughout my PhD journey, I have
> delved deep into complex challenges — not just solving problems, but transforming them.

Let them answer. Then point out that it contains no fact about the person; any applicant could
have written it for any job, and recruiters recognise this kind of AI-generated text.

Then the don'ts, as a short list:

- Don't send genAI content
- Don't apply to 50 jobs in a day
- Don't ignore selection criteria
- Don't use generic filenames (`Resume_Final_v3.pdf`, `Canva_Export_20251001.pdf`)
- Don't apologise for being new
- Don't send generic letters
- Skip the photo and date of birth
- Don't use a fancy template
- Don't send Word documents
- Don't send what you don't love

Ask which of these they've done, without judgement, and offer to help fix it (a filename, a
template, a letter opening).

## 5. After graduation

Present it as a checklist they can tick off, and ask which ones they've already done:

- Collect your metrics (students taught, participants, funding, citations by non-academics,
  media)
- Get an ABN, in case contract or consulting work comes up
- Set up a portfolio website
- Move off your uni email
- Rewrite your LinkedIn to match your industry resume
- Think carefully about what kind of career you want
- Have coffees with people working in jobs that interest you
- Check your digital footprint
- Know your salary range for the roles you're applying for
- Set up a base resume to tailor from

End with the workshop's last point, in plain words: **take a proper break.** A few weeks off
before jumping into the next thing isn't wasted time, and you'll interview better rested.

Offer help with whichever item they pick next: collecting metrics (use "Digging for numbers" in
SKILL.md), rewriting a LinkedIn summary from their resume, or building the base resume.
