# Data Engineer assignment

In this assignment, you are tasked with creating a script (or a series of scripts) that take two JSON Lines files that record user actions
and produce a CSV file with measurements of how much time a given user spent on a given study.

In other words, for each `study` found in the `references_log.jsonl`, and each user assigned to this study (via `extraction_task`), you
should calculate aggregate time (duration) that this user spent on working on this study.

Your output should follow this format:

```
user_id,study_id,reference_id,accession_number,doi,is_qa,duration,start_timestamp,last_timestamp
36f789a5-1077-418e-9735-29791182e264,thorne1978,21a9c4d9-aaec-41f1-805c-4e81ca6ab462,647139.0,10.1007/BF01685810. 10.1007/bf01685810,False,581.388941,2023-11-01 17:31:48.968509+00:00,2023-11-01 17:41:30.357450+00:00
...
```

You get two input files:

- `references_log.jsonl` - every entry in this log record 'save' operation on the result for a particular study. In this dataset, there is 1:1 relationship between references and studies.
The same study may be worked on by more than one user.
- `user_actions.jsonl` – entries in this log record other actions of the users in the system. 

You need to use both logs to calculate how much time users spent on their tasks. `references_log` record when they saved their work.
By tracking what event happend before saving the work (e.g. looking in the `user_actions.jsonl`) you will be able to find out when the user started the work. You should assume that immediate previous action marks the start of the work on a given study.

The instructions are intentionally scarce, to encourage you to explore the data and come up with a solution to the problem.

You can use any tool or programming language that you like. It is not necessary to build a scalable data pipeline for this assignment.
You can assume that the processing can be run on a single Unix machine. You are free to use any AI tools to create your answer.


Please add your solution to this repo, edit this README file with instructions how to run your code and send us the zipped files *or* put it in a private repo (do not make it public please!) and send an invitation to **anowak** (https://github.com/anowak))

```
<your instructions go here>
```
