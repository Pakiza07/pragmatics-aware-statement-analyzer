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

## Baseline Performance
serial number, text, expected label, true label, verdict
Text	Expected Label	 True Label	 Verdict
Fibre also appears to help the body get rid of bile acids which lowers cholesterol thus decreasing the risk of cardiovascular disease,	1,	1,	TRUE POSITIVE
All of this can have an impact on our brains the next day,	0,	0,	TRUE NEGATIVE
The study found that former professional footballers are five times more likely to develop Alzheimer's disease,	1,	1,	TRUE POSITIVE
Psychologists have found that people tend to become less neurotic and more conscientious and agreeable over the course of a lifetime,	1,	1,	TRUE POSITIVE
We can correct myopia with spectacles and contact lenses as we have for a long time,	0,	0,	TRUE NEGATIVE
This revolutionary tech could heal broken bones,	1,	1,	TRUE POSITIVE
Ex-pro footballers are 3 times more likely to get dementia from heading balls,	1,	1,	TRUE POSITIVE
Most people probably wouldn't want to eat two or three as that's quite a lot of oranges,	1,	1,	TRUE POSITIVE
if people in the United States and Europe can get over the ick edible insects could revolutionise food systems,	1,	1,	TRUE POSITIVE
cutting back on caffeine can mean we get more REM sleep,	0,	0,	TRUE NEGATIVE
People carry bacteria as part of their skin microbiome and can shed them in large numbers,	0,	0,	TRUE NEGATIVE
You are more likely to find pathogenic bacteria in hospital linen where sick patients have been sleeping than in the bed clothes of healthy people,	1,	1,	TRUE POSITIVE
We think the reason why you find so much fungi in our pillows is because most of us sweat at night from our heads,	1,	1,	TRUE POSITIVE
There could be billions or trillions of fungal particles in every pillow,	1,	1,	TRUE POSITIVE
If we're willing to commit we can not only get the cardiovascular benefits but also develop the heart of an athlete,	0,	0,	TRUE NEGATIVE
Daily pill intake is common for many medications potentially leading to better long-term adherence,	1,	1,	TRUE POSITIVE
There is something you can do to help promote your lungs' natural self-cleaning capacity though,	0,	1,	FALSE POSITIVE
The dangers of contact sports have actually been known about for almost 100 years,	0,	0,	TRUE NEGATIVE
That force causes the brain inside the skull to move away from the site of impact,	0,	0,	TRUE NEGATIVE
Typically people want to become more extraverted and conscientious while being less neurotic,	0,	0,	TRUE NEGATIVE
Everything from obesity and ultra-processed foods to antibiotics and the microbiome to air pollution and microplastics have been suggested,	1,	1,	TRUE POSITIVE
You will not be able to work in the United Kingdom if you do not have digital ID,	0,	0,	TRUE NEGATIVE
it's going to take you longer to eat food hew them and swallow them,	0,	0,	TRUE NEGATIVE
Inflammation is an important part of the immune response but when you have excessive inflammation or if you have sustained inflammation that doesn't calm down it damages your tissues and it's detrimental for pretty much every body system,	0,	0,	TRUE NEGATIVE
The endothelium has the function of making your vessels stiffer if you need your blood pressure to go up,	0,	0,	TRUE NEGATIVE
You can't eat poorly all day long and think that it's enough to have a glass of tart cherry juice before bedtime,	0,	1,	FALSE POSITIVE
One of the most important things before sleep is to stop eating a few hours before bed especially not having the biggest bulk of calories before bed,	0,	0,	TRUE NEGATIVE
When you have a clearer separation between day and night the brain has an easier time recognising that it's time for sleep,	0,	0,	TRUE NEGATIVE
At some point in the future we'll be consuming insects more,	0,	1,	FALSE POSITIVE
it's unrealistic to expect insects to become a major meat substitute,	0,	0,	TRUE NEGATIVE
Plant-based meats don't trigger the same disgust response as insects,	0,	0,	TRUE NEGATIVE
Cutting back on caffeine will not directly cause vivid dreams,	0,	0,	TRUE NEGATIVE
In hospitals they wash linen at very high temperatures,	0,	0,	TRUE NEGATIVE
If you eat in bed then washing the sheets very regularly is important,	0,	0,	TRUE NEGATIVE
If finding time to exercise in the week is a challenge and you're only able to work out at weekends rest assured this is still beneficial,	0,	0,	TRUE NEGATIVE
A lot of people who don’t currently drink are people who used to drink heavily or who have health problems that led them to quit,	0,	0,	TRUE NEGATIVE
The most obvious and impactful change is the removal of the psychological and physical barrier of self-injection,	0,	0,	TRUE NEGATIVE
The distinctive difference is the pill provides greater flexibility in how patients choose to take their medication,	0,	0,	TRUE NEGATIVE
The pill’s effectiveness is highly dependent on strict adherence to the dosing instructions,	0,	0,	TRUE NEGATIVE
There is a specific contraindication for the pill that does not apply to the injection,	0,	0,	TRUE NEGATIVE
You still have to make the right food choices,	0,	0,	TRUE NEGATIVE
If you eliminate or reduce as much as possible carbohydrates and sugars that’s going to direct the body towards burning the fat more and that’s the goal,	0,	0,	TRUE NEGATIVE
Taking a break from alcohol often allows them to engage more meaningfully with loved ones,	0, 1,	FALSE POSITIVE
Alcohol has long been known to have a negative impact on sleep,	0,	0,	TRUE NEGATIVE
Alcohol can also worsen or unmask underlying conditions such as sleep apnea,	0,	0,	TRUE NEGATIVE
If you are struggling with alcohol use or addiction you should seek professional or medical careTrusted Source for assistance,	0,	0, TRUE NEGATIVE
Sleep has a perpetual association with the ethereal dreams altered states and emotions,	0,	0, TRUE NEGATIVE
Dreams are thought to occur primarily during REM sleep,	0,	0,	TRUE NEGATIVE
Do not shout or startle the person and do not physically restrain them unless they’re in danger, 0, 0,	TRUE NEGATIVE
The best advice is to avoid late-night meals reduce alcohol intake and be gentle with sleepwalkers,	0,	0,	TRUE NEGATIVE
Flu vaccines cut the risk of hospitalization or intensive care admission for children by about half and the risk of pneumonia by 70%,	0,	0,	TRUE NEGATIVE
Flu vaccines do prevent some people from getting the flu but in general vaccines aren’t great at preventing respiratory infections,	0,	1,	FALSE POSITIVE
So vaccination basically eliminated about two-thirds of the hospitalizations that would have occurred without it,	0,	1,	FALSE POSITIVE
We can’t expect a shot that we get in our arm to put up this magic force shield that blocks those respiratory viruses from entry in our nose, 0, 0, TRUE NEGATIVE

