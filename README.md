# pragmatics-aware-statement-analyzer
An NLP system that analyzes text to identify pragmatic linguistic markers linked to manipulative or strategic communication. These markers frequemtly occur in politics, courtrooms, criminal trials, business meetings, and even online discourse. 

The language patterns that the system is aiming to identify are hedging, evasion, emotional coercion, ambiguity and implicit claims. 
1. Hedging: Hedging is the use of cautious language to manage the strength of a claim. You often use it to make criticism, opinions, and claims less harsh or rigid. Some examples of hedging terms are 'suggest', 'tend to', and, 'possibly'. For instance, in the phrase "You tend to get mad at me quite often", the accusation might sound less harsh because of the use of the phrase 'tend to'.
2. Evasion: Evasion refers to the act of avoiding answering a question or giving out information either directly or through the use of tangents as distraction. For example in the conversation:
   A: Do you believe in ghosts?
   B: Ghosts are elusive creatures. Some people think they are real, some don't.
   My grandma swears she had a paranormal encounter once. She tells the story every Thanksgiving.
the speaker is avoiding giving their opinion and is speaking around it.
3. Emotional Coercion: Emotional coercion in communication is using feelings—like guilt, fear, obligation, or shame—to manipulate someone into doing things against their will or best interest, creating a power imbalance through tactics like gaslighting, constant criticism, or isolating them, making them feel trapped, ashamed, and unsure of themselves to gain control.
4. Ambiguity: This means the act of being purposefully vague in order to avoid confrontation, commitment or responsibility. It can also be used to create a false sense of competence, awareness or influence.
5.  Implicit claims: An implicit claim is an argument or idea that requires the listeners/audience/people making jugdements to use clues and context to infer or "read between the lines" to understand the speaker's true meaning. To make this clearer we can consider two slogans for the same coffee company:
              i. "XYZ coffee gives you energy"
              ii. "Start your day with XYZ cofee"
    here, the second slogan doesn't explicitly claim that the coffee can give you enery but it implies that if you drink it you will be able to start your day in an energetic manner.


## Project Scope (v0.1)
This initial version focuses on detecting hedging in written text. Other manipulation types (evasion, ambiguity, emotional coercion, implicit claims) are planned for future iterations.

## System Overview
The system takes a written statement as input and processes it through a pipeline consisting of text preprocessing, feature extraction, classification, and explainability. The output includes a predicted label indicating the presence of hedging-related language patterns, along with supporting explanations highlighting relevant phrases. In this project, hedging is operationalized through lexical cues, modal constructions, and uncertainty expressions that weaken or soften propositional commitment. The system is designed to be modular, allowing additional pragmatic categories to be incorporated as independent detection modules in future versions.

## Dataset Observations (v0.1)
- Class imbalance toward non-hedging statements
- Labels are consistent and binary
- Statements are short or mid-length
- Some annotations are context-sensitive

  
## Baseline Evaluation Results
----------------------------
Accuracy: 0.9235294117647059
Precision: 0.9204545454545454
Recall: 0.9310344827586207
F1 Score: 0.9257142857142857

## Baseline Performance Summary
| Text | Expected Label | Predicted Label | Verdict | Error Type |
|------|---------------|----------------|---------|-----------|
| Fibre also appears to help the body get rid of bile acids which lowers cholesterol thus decreasing the risk of cardiovascular disease | 1 | 1 | TRUE POSITIVE | NA |
| All of this can have an impact on our brains the next day | 0 | 0 | TRUE NEGATIVE | NA |
| The study found that former professional footballers are five times more likely to develop Alzheimer's disease | 1 | 1 | TRUE POSITIVE | NA |
| Psychologists have found that people tend to become less neurotic and more conscientious and agreeable over the course of a lifetime | 1 | 1 | TRUE POSITIVE | NA |
| This revolutionary tech could heal broken bones | 1 | 1 | TRUE POSITIVE | NA |
| There is something you can do to help promote your lungs' natural self-cleaning capacity though | 0 | 1 | FALSE POSITIVE | Contextual ambiguity |
| Taking a break from alcohol often allows them to engage more meaningfully with loved ones | 0 | 1 | FALSE POSITIVE | Weak lexical hedge |
| Alcohol has long been known to have a negative impact on sleep | 0 | 0 | TRUE NEGATIVE | NA |

| Dataset Version | Total Samples | False Positives | False Negatives |
|----------------|---------------|----------------|----------------|
| v1 — Initial Dataset | 55 | 5 | 6 |
| v2 — Expansion Round 1 | 135  | 5 | 7 |
| v3 — Expansion Round 2 | 170 | 5 | 7 |

False positives primarily arise from lexical hedges used in neutral informational contexts rather than manipulative discourse

## Dataset History
Initial dataset: 55 samples
Expansion 1: +80 samples
Expansion 2: +35 samples
Current total: 170 samples

## Dataset Integrity Check
Checked for duplicate statements.
Total statements checked: 170
Duplicate statements found: 0
Action taken: None required

