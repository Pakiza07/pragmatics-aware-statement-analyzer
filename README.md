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
