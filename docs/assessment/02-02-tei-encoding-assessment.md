---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Assessment: <TEI Encoding>

::::{admonition} Note
:class: note
This assessment helps you check your understanding of the chapter *<TEI Encoding: Preparing Texts for Programmable Corpora>*.

- There is no grading and nothing is stored.
- Read the feedback for each option carefully, even if you answered correctly.
- If you are unsure, return to the relevant section of the chapter (or the interface/tool) and verify what you see.

_Note: the following information needs to be checked._
Estimated time: <20–30 minutes>.
::::

## Exercise 1: Encoding Strategy

### The Characteristics of the Encoding Strategies

**Assign the correct characteristics to the following encoding strategies.**

_Note: The answers still need to be shuffled!_

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [
  {
    "question": "<manual encoding in an XML editor>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<knowledge of XML/TEI necessary during the encoding process itself, no programming skills necessary>", "correct": True, "feedback": "<Correct!>"},
      {"answer": "<knowledge of XML/TEI necessary, basic programming skills necessary>", "correct": False,  "feedback": "<Incorrect, you do not need programming for manual encoding.>"},
      {"answer": "<knowledge of XML/TEI necessary, advanced programming skills necessary>", "correct": False, "feedback": "<Incorrect, you do not need programming for manual encoding.>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to know XML/TEI during the manual encoding process itself.>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, prompting skills necessary, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to know XML/TEI during the manual encoding process itself.>"}
    ]
  }
]

display_quiz(q1, max_width=1000)
:::

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q2 = [
  {
    "question": "<semi-automatic encoding with a regular expression transformation script>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<knowledge of XML/TEI necessary during the encoding process itself, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to have basic programming skills for encoding a text with a regular expression transformation script.>"},
      {"answer": "<knowledge of XML/TEI necessary, basic programming skills necessary>", "correct": True,  "feedback": "<Correct!>"},
      {"answer": "<knowledge of XML/TEI necessary, advanced programming skills necessary>", "correct": False, "feedback": "<Incorrect, you do not need advanced programming skills for encoding a text with a regular expression transformation script.>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to have basic programming skills for encoding a text with a regular expression transformation script.>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, prompting skills necessary, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to have basic programming skills and you do not have to have prompting skills for encoding a text with a regular expression transformation script.>"}
    ]
  }
]

display_quiz(q2, max_width=1000)
:::

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q3 = [
  {
    "question": "<semi-automatic encoding with a transformation script (R, Python, XSLT, XQuery)>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<knowledge of XML/TEI necessary during the encoding process itself, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to have advanced programming skills for encoding a text with such a transformation script.>"},
      {"answer": "<knowledge of XML/TEI necessary, basic programming skills necessary>", "correct": False,  "feedback": "<Incorrect, you have to have advanced programming skills for encoding a text with such a transformation script.>"},
      {"answer": "<knowledge of XML/TEI necessary, advanced programming skills necessary>", "correct": True, "feedback": "<Correct!>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to have advanced programming skills for encoding a text with such a transformation script.>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, prompting skills necessary, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to have advanced programming skills and you do not have to have prompting skills for encoding a text with such a transformation script.>"}
    ]
  }
]

display_quiz(q3, max_width=1000)
:::

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q4 = [
  {
    "question": "<semi-automatic encoding with EzDrama>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<knowledge of XML/TEI necessary during the encoding process itself, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you do not have to know TEI/XML to mark up a text with EzDrama.>"},
      {"answer": "<knowledge of XML/TEI necessary, basic programming skills necessary>", "correct": False,  "feedback": "<Incorrect, you do not need any programming skills to mark up a text with EzDrama.>"},
      {"answer": "<knowledge of XML/TEI necessary, advanced programming skills necessary>", "correct": False, "feedback": "<Incorrect, you do not need any programming skills to mark up a text with EzDrama.>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, no programming skills necessary>", "correct": True, "feedback": "<Correct!>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, prompting skills necessary, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you do not have to have prompting skills to mark up a text with EzDrama.>"}
    ]
  }
]

display_quiz(q4, max_width=1000)
:::

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q5 = [
  {
    "question": "<semi-automatic encoding with a Large Language Model (LLM)>",
    "type": "multiple_choice",
    "answers": [
      {"answer": "<knowledge of XML/TEI necessary during the encoding process itself, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you only have to know XML/TEI for revising the generated file.>"},
      {"answer": "<knowledge of XML/TEI necessary, basic programming skills necessary>", "correct": False,  "feedback": "<Incorrect, you do not need any programming skills to encode a text with an LLM.>"},
      {"answer": "<knowledge of XML/TEI necessary, advanced programming skills necessary>", "correct": False, "feedback": "<Incorrect, you do not need any programming skills to encode a text with an LLM.>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, no programming skills necessary>", "correct": False, "feedback": "<Incorrect, you have to have prompting skills additionally.>"},
      {"answer": "<knowledge of XML/TEI necessary for evaluation and revision, prompting skills necessary, no programming skills necessary>", "correct": True, "feedback": "<Correct!>"}
    ]
  }
]

display_quiz(q5, max_width=1000)
:::

### Choosing an Encoding Strategy: Case 1

**You want to encode a corpus of 50 texts from a digital text collection. The format is HTML. Core elements, such as the headings, speaker names, or stage directions, are marked up regularly.**

_Note: The answers still need to be shuffled!_

:::{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("..")
from assessment import DragDropQuiz

quiz = DragDropQuiz()
quiz.create_matching_quiz(
    title="Rank the following encoding strategies from most to least time-consuming:",
    descriptions=[
        "manual encoding in an XML editor",
        "semi-automatic encoding with EzDrama",
        "semi-automatic encoding with a transformation script (regular expression; R, Python, XSLT, XQuery)"
    ],
    options=["1", "2", "3"],
    correct_mapping={
        "manual encoding in an XML editor": "1",
        "semi-automatic encoding with EzDrama": "2",
        "semi-automatic encoding with a transformation script (regular expression; R, Python, XSLT, XQuery)": "3"
    }
)
:::

_Note: The answers still need to be shuffled!_

:::{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("..")
from assessment import DragDropQuiz

quiz = DragDropQuiz()
quiz.create_matching_quiz(
    title="Rank the following encoding strategies from those that are the most transparent and allow the most direct control in the encoding process to those which are least transparent and allow the least direct control in the encoding process:",
    descriptions=[
        "manual encoding in an XML editor",
        "semi-automatic encoding with EzDrama",
        "semi-automatic encoding with a transformation script (regular expression; R, Python, XSLT, XQuery)",
        "semi-automatic encoding with a Large Language Model (LLM)"
    ],
    options=["1", "2", "3", "4"],
    correct_mapping={
        "manual encoding in an XML editor": "1",
        "semi-automatic encoding with EzDrama": "2",
        "semi-automatic encoding with a transformation script (regular expression; R, Python, XSLT, XQuery)": "3",
        "semi-automatic encoding with a Large Language Model (LLM)": "4"
    }
)
:::

### Choosing an Encoding Strategy: Case 2

**You want to encode “De Monfort” by Joanna Baillie. Your text source has no pre-existing markup. The format is TXT.**  

Here is an excerpt from act 1, scene 2:[^1]

```
SCENE II.
_(A Small Apartment in JEROME'S House: a table and breakfast set out. Enter DE MONFORT, followed by MANUEL, and sets himself down by the table, with a cheerful face.)_
DE MON. Manuel, this morning's sun shines pleasantly:
These old apartments too are light and cheerful.
Our landlord's kindness has reviv'd me much;
He serves as though he lov'd me. This pure air
Braces the listless nerves, and warms the blood;
I feel in freedom here.
_(Filling a cup of coffee, and drinking.)_

MAN. Ah! sure, my Lord,
No air is purer than the air at home.

DE MON. Here can I wander with assured steps,
Nor dread, at every winding of the path,
Lest an abhorred serpent cross my way,
And move—_(Stopping short.)_

MAN. What says your honour?
There are no serpents in our pleasant fields.

DE MON. Think'st thou there are no serpents in the world
But those who slide along the grassy sod,
And sting the luckless foot that presses them?
There are who in the path of social life
Do bask their spotted skins in Fortune's sun,
And sting the soul—Ay, till its healthful frame
Is chang'd to secret, fest'ring, sore disease,
So deadly is the wound.

MAN. Heaven guard your honour from such horrid skathe:
They are but rare, I hope?

DE MON. _(Shaking his head.)_ We mark the hollow eye, the wasted frame,
The gait disturb'd of wealthy honour'd men,
But do not know the cause.

MAN. 'Tis very true. God keep you well, my Lord!
```

:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [
  {
    "question": "<Which of the following encoding strategies may be suitable? (Multiple answers are possible.)>",
    "type": "many_choice",
    "answers": [
      {"answer": "<manual encoding in an XML editor>", "correct": True, "feedback": "<Correct!>"},
      {"answer": "<semi-automatic encoding with a regular expression transformation script>", "correct": True,  "feedback": "<Correct!>"},
      {"answer": "<semi-automatic encoding with a transformation script (R, Python, XSLT, XQuery)>", "correct": False, "feedback": "<Incorrect, as there is no pre-existing markup in XML.>"},
      {"answer": "<semi-automatic encoding with EzDrama>", "correct": True, "feedback": "<Correct!>"},
      {"answer": "<semi-automatic encoding with a Large Language Model>", "correct": True, "feedback": "<Correct!>"}
    ]
  }
]

display_quiz(q1, max_width=1000)
:::

### Choosing an Encoding Strategy: Case 3

**You want to encode “The Belle’s Stratagem” by Hannah Cowley. Your text source has no pre-existing markup. The format is TXT.**

Here is an excerpt from act 3, scene 1:[^1]

```
ACT III.
SCENE I. Mr. Hardy's.
Enter Letitia and Mrs. Racket.
Mrs. Racket. Come, prepare, prepare; your Lover is coming.
Letit. My Lover!—Confess now that my absence at dinner was a severe mortification to him.
Mrs. Rack. I can't absolutely swear it spoilt his appetite; he eat as if he was hungry, and drank his wine as though he liked it.
Letit. What was the apology?
Mrs. Rack. That you were ill;—but I gave him a hint, that your extreme bashfulness could not support his eye.
Letit. If I comprehend him, aukwardness and bashfulness are the last faults he can pardon in a woman; so expect to see me transform'd into the veriest maukin.
Mrs. Rack. You persevere then?
Letit. Certainly. I know the design is a rash one, and the event important;—it either makes Doricourt mine by all the tenderest ties of passion, or deprives me of him for ever; and never to be his wife will afflict me less, than to be his wife and not be belov'd.
Mrs. Rack. So you wo'n't trust to the good old maxim—"Marry first, and love will follow?"
Letit. As readily as I would venture my last guinea, that good fortune might follow. The woman that has not touch'd the heart of a man before he leads her to the altar, has scarcely a chance to charm it when possession and security turn their powerful arms against her.—But here he comes.—I'll disappear for a moment.—Don't spare me.
Exit Letitia.
```
:::{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

q1 = [
  {
    "question": "<Which of the following encoding strategies may be suitable? (Multiple answers are possible.)>",
    "type": "many_choice",
    "answers": [
      {"answer": "<manual encoding in an XML editor>", "correct": True, "feedback": "<Correct!>"},
      {"answer": "<semi-automatic encoding with a regular expression transformation script>", "correct": False,  "feedback": "<Incorrect. Note that there are no (layout) markers to distinguish the speaker name, the speech, or the stage directions from one another.>"},
      {"answer": "<semi-automatic encoding with a transformation script (R, Python, XSLT, XQuery)>", "correct": False, "feedback": "<Incorrect, as there is no pre-existing markup in XML.>"},
      {"answer": "<semi-automatic encoding with EzDrama>", "correct": True, "feedback": "<Correct!>"},
      {"answer": "<semi-automatic encoding with a Large Language Model>", "correct": True, "feedback": "<Correct!>"}
    ]
  }
]

display_quiz(q1, max_width=1000)
:::

## Exercise 2: Manual Encoding

### Manual Encoding: Case 1

_Note: The following question still needs to be implemented correctly._

Complete the encoding of the following passage from act 1, scene 2 of “De Monfort” by Joanna Baillie.[^1] The play is written in verse.

```xml
<div type="ADD" n="ADD">
<head>SCENE II.<ADD>
<ADD>(A Small Apartment in JEROME'S House: a table and breakfast set out. Enter DE MONFORT, followed by MANUEL, and sets himself down by the table, with a cheerful face.)<ADD>
<sp who="#de-monfort">
<speaker>DE MON.</speaker>
<l>Manuel, this morning's sun shines pleasantly:<ADD>
<l>These old apartments too are light and cheerful.</l>
<ADD>Our landlord's kindness has reviv'd me much;</l>
<l>He serves as though he lov'd me. This pure air</l>
<l>Braces the listless nerves, and warms the blood;</l>
<l>I feel in freedom here.<ADD>
<ADD>(Filling a cup of coffee, and drinking.)<ADD>
</sp>
<sp who="#manuel">
<ADD>MAN.<ADD>
<ADD>Ah! sure, my Lord,<ADD>
<ADD>No air is purer than the air at home.<ADD>
<ADD>
[...]
</div>
```

Answer:  
```xml
<div type="scene" n="2">
<head>SCENE II.</head>
<stage>(A Small Apartment in JEROME'S House: a table and breakfast set out. Enter DE MONFORT, followed by MANUEL, and sets himself down by the table, with a cheerful face.)</stage>
<sp who="#de-monfort">
<speaker>DE MON.</speaker>
<l>Manuel, this morning's sun shines pleasantly:</l>
<l>These old apartments too are light and cheerful.</l>
<l>Our landlord's kindness has reviv'd me much;</l>
<l>He serves as though he lov'd me. This pure air</l>
<l>Braces the listless nerves, and warms the blood;</l>
<l>I feel in freedom here.</l>
<stage>(Filling a cup of coffee, and drinking.)</stage>
</sp>
<sp who="#manuel">
<speaker>MAN.</speaker>
<l>Ah! sure, my Lord,</l>
<l>No air is purer than the air at home.</l>
</sp>
[...]
</div>
```
### Manual Encoding: Case 2

_Note: The following question still needs to be implemented correctly._

Encode the following passage from act 3, scene 1 of “The Belle’s Stratagem” by Hannah Cowley.[^1] The speaker ID for Letitia is “letitia”, the one for Mrs. Racket is “mrs-racket”. The play is written in prose.
```xml
<div type="act" n="3">
<ADD>ACT III.<ADD>
<div type="scene" n="1">
<ADD>SCENE I.<ADD>Mr. Hardy's.<ADD><ADD>
<ADD>Enter Letitia and Mrs. Racket.<ADD>
<ADD>
<ADD>Mrs. Racket.<ADD>
<ADD>Come, prepare, prepare; your Lover is coming.<ADD>
<ADD>
<ADD>
<ADD>Letit.<ADD>
<ADD>My Lover!—Confess now that my absence at dinner was a severe mortification to him.<ADD>
<ADD>
<ADD>
<ADD>Mrs. Rack.<ADD>
<ADD>I can't absolutely swear it spoilt his appetite; he eat as if he was hungry, and drank his wine as though he liked it.<ADD>
<ADD>
<ADD>
<ADD>Letit.<ADD>
<ADD>What was the apology?<ADD>
<ADD>
<ADD>
<ADD>Mrs. Rack.<ADD>
<ADD>That you were ill;—but I gave him a hint, that your extreme bashfulness could not support his eye.<ADD>
<ADD>
<ADD>
<ADD>Letit.<ADD>
<ADD>If I comprehend him, aukwardness and bashfulness are the last faults he can pardon in a woman; so expect to see me transform'd into the veriest maukin.<ADD>
<ADD>
<ADD>
<ADD>Mrs. Rack.<ADD>
<ADD>You persevere then?<ADD>
<ADD>
<ADD>
<ADD>Letit.<ADD>
<ADD>Certainly. I know the design is a rash one, and the event important;—it either makes Doricourt mine by all the tenderest ties of passion, or deprives me of him for ever; and never to be his wife will afflict me less, than to be his wife and not be belov'd.<ADD>
<ADD>
<ADD>
<ADD>Mrs. Rack.<ADD>
<ADD>So you wo'n't trust to the good old maxim—"Marry first, and love will follow?"<ADD>
<ADD>
<ADD>
<ADD>Letit.<ADD>
<ADD>As readily as I would venture my last guinea, that good fortune might follow. The woman that has not touch'd the heart of a man before he leads her to the altar, has scarcely a chance to charm it when possession and security turn their powerful arms against her.—But here he comes.—I'll disappear for a moment.—Don't spare me.<ADD>
<ADD>
<ADD>Exit Letitia.<ADD>
[...]
</div>
</div>
```

Answer:
```xml
<div type="act" n="3">
<head>ACT III.</head>
<div type="scene" n="1">
<head>SCENE I.<stage>Mr. Hardy's.</stage></head>
<stage>Enter Letitia and Mrs. Racket.</stage>
<sp who="#mrs-racket">
<speaker>Mrs. Racket.</speaker>
<p>Come, prepare, prepare; your Lover is coming.</p>
</sp>
<sp who="#letitia">
<speaker>Letit.</speaker>
<p>My Lover!—Confess now that my absence at dinner was a severe mortification to him.</p>
</sp>
<sp who="#mrs-racket">
<speaker>Mrs. Rack.</speaker>
<p>I can't absolutely swear it spoilt his appetite; he eat as if he was hungry, and drank his wine as though he liked it.</p>
</sp>
<sp who="#letitia">
<speaker>Letit.</speaker>
<p>What was the apology?</p>
</sp>
<sp who="#mrs-racket">
<speaker>Mrs. Rack.</speaker>
<p>That you were ill;—but I gave him a hint, that your extreme bashfulness could not support his eye.</p>
</sp>
<sp who="#letitia">
<speaker>Letit.</speaker>
<p>If I comprehend him, aukwardness and bashfulness are the last faults he can pardon in a woman; so expect to see me transform'd into the veriest maukin.</p>
</sp>
<sp who="#mrs-racket">
<speaker>Mrs. Rack.</speaker>
<p>You persevere then?</p>
</sp>
<sp who="#letitia">
<speaker>Letit.</speaker>
<p>Certainly. I know the design is a rash one, and the event important;—it either makes Doricourt mine by all the tenderest ties of passion, or deprives me of him for ever; and never to be his wife will afflict me less, than to be his wife and not be belov'd.</p>
</sp>
<sp who="#mrs-racket">
<speaker>Mrs. Rack.</speaker>
<p>So you wo'n't trust to the good old maxim—"Marry first, and love will follow?"</p>
</sp>
<sp who="#letitia">
<speaker>Letit.</speaker>
<p>As readily as I would venture my last guinea, that good fortune might follow. The woman that has not touch'd the heart of a man before he leads her to the altar, has scarcely a chance to charm it when possession and security turn their powerful arms against her.—But here he comes.—I'll disappear for a moment.—Don't spare me.</p>
</sp>
<stage>Exit Letitia.</stage>
[...]
</div>
</div>
```
## Exercise 3: Semi-Automatic Encoding with EzDrama

_Note: The following question still needs to be implemented correctly._

Encode the following passage from the beginning of act 1, scene 1 of “The Beau Defeated, or The Lucky Younger Brother” by Mary Pix [^1], with EzDrama syntax:
```
ACT I. SCENE I.
Enter Mrs. Rich with Betty, her Maid.
Betty.
What's the matter, Madam? What has happen'd to you? What has any body done to you?
Mrs. Rich.
An Affront? ... Ah! I die: An affront! ... I faint: I cannot speak. A Chair quickly.
Betty.
[Giving a Chair.] An affront! to you, Madam, an affront! Is it possible!
Mrs. Rich.
But too true, my poor Betty. Oh! I shall dye. To disrespect me in the open Street! What Insolence!
Betty.
How, Madam! Not to show respect to such a person as you? Madam Rich; the Widow of an honest Banker, who got Two Hundred Thousand Pounds in the King's service? Pray, Madam, who has been thus insolent?
Mrs. Rich.
A Dutchess; who had the confidence to thrust my Coach from the Wall, and make it run back above twenty yards.
```

Convert the encoded text to TEI/XML using one of the methods suggested in the EzDrama repository {cite}`dracor2022ff.easy`. Look at the resulting TEI/XML file. Given your current understanding of TEI/XML, does it look correct? Are there things that need to be corrected manually? If so, where would it make more sense to introduce a correction in each case: the EzDrama input, or the TEI/XML output?
Possible solution:
```txt
#ACT I. 
##SCENE I.
$Enter Mrs. Rich with Betty, her Maid.
@Betty.
WHat's the matter, Madam? What has happen'd to you? What has any body done to you?
@Mrs. Rich.
An Affront? ... Ah! I die: An affront! ... I faint: I cannot speak. A Chair quickly.
@Betty.
%[Giving a Chair.] 
An affront! to you, Madam, an affront! Is it possible!
@Mrs. Rich.
But too true, my poor Betty. Oh! I shall dye. To disrespect me in the open Street! What Insolence!
@Betty.
How, Madam! Not to show respect to such a person as you? Madam Rich; the Widow of an honest Banker, who got Two Hundred Thousand Pounds in the King's service? Pray, Madam, who has been thus insolent?
@Mrs. Rich.
A Dutchess; who had the confidence to thrust my Coach from the Wall, and make it run back above twenty yards.
```

## Exercise 4: Encoding with LLMs

Pick an entire play of your choice that is available to you in plain text and in the public domain. As an option, you may visit dracor.org and access the full text of any drama in plain text in the ‘Full text’ tab {cite}`fischerdracororg` (see Chapter 03). Try prompting an LLM of your choice to encode the play in TEI. Assess the results. Was the LLM able to process the whole play? Did it omit anything? Do you notice any obvious hallucinations? Are there any obvious markup errors?  

If the play could not be processed in one go, try encoding it in chunks. You can also try different strategies: with / without examples of TEI-encoded drama, with / without explicitly mentioning DraCor, with / without explicitly asking to mark speeches, stage directions, and so on. 
Do you see any differences? Reflect on the current state of LLM-powered encoding and its limitations. 

## Bibliography
```{bibliography}
```

[^1] The text passage was taken from {cite}`baillie1789monfort, pp. 313-314`, and the format was slightly adapted for the exercise.

[^1] The text passage was taken from {cite}`cowley2024belles`, and the format was slightly adapted for the exercise.

[^1] The text passage was taken from {cite}`pixbeau`, and the format was slightly adapted for the exercise.