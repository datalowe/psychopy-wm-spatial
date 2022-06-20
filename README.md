# Psychopy Spatial Working Memory Test

<img width="400px" alt="An example of the experiment running. Target squares light up, and a mouse cursor then clicks the targets in the same order." src="./wm_spatial_example.gif">

This is a [Psychopy](https://psychopy.org) project consisting of a spatial working memory task. 

In each trial of the experiment, the participant is shown a sequence of targets lighting up. The participant is then to click the targets in the same sequence that they lit up. The sequences increase in length from 2 to 9 targets, with 3 trials for each difficulty level. If the participant fails all trials of a difficulty level, the experiment ends straight away in order to prevent participant frustration.

Placement of targets is randomly generated in a way that prevents overlapping targets. 

## Modifying the experiment
Most experiment specifications, e. g. number of trials/difficulty level, min/max difficulty level, square size et c, are done in a code snippet linked to the first routine (in the PsychoPy Builder interface), meaning that you can easily change them. This includes whether randomly arranged numbers should appear on top of the targets. All instruction messages (in American English by default) are also defined in this code snippet, which simplifies translation.

If you don't want target 'light-up sequences', coordinates and numbering to be randomly generated, you can set the experiment to use the same configurations for every run. This is useful if you want each participant to go through exactly the same experiment. For instructions on how to do this, open up the scripts in the folder 'specifications_generation' with a text editor and read the documentation at the top of each file. 

## Translating the experiment
For instructions specifically about translating the experiment, read the 'translations_instructions.txt' document in the 'translations' directory.

## Experiment data output
For each trial the experiment saves participant response times (saving the time for each click), the correct sequence, what sequence the participant clicked the boxes in, and whether the participant's responses were correct or not. Note that target numbering, as used when saving sequences, has nothing to do with targets' positions or the numbers that randomly appear on targets (if you have enabled these). If you want detailed information about spatial patterns of participants' responses you should activate saving coordinates on every click for the trial's mouse component.

The most relevant output data files are the 'CSV'/'.csv' files, saved to the 'data' directory. The most important columns in these files are as follows:
* response_times: These are the times at which the participant clicked targets, where times are stored in a comma-separated 'list' within square brackets, e.g. `[1.2335563814267516, 2.2506016893312335]` for a trial where the participant is to click two targets.
    - In the example here, '1.2335563814267516' would correspond to the time, counting from trial start, at which the participant clicked the first target, and '2.2506016893312335' would be the time at which the second target was clicked (whether correct or not).
* trial_start_time: Trial start time, counting from experiment start.
* trial_type: Trial type, saying whether or not targets had digits drawn on top of them or not
    - Possible values: 'with_digits', 'without_digits'
* correct_order: The correct order to click targets in. e.g. `[2, 7]` indicates that in order to produce a correct trial response, the participant needed to first click target 2, then target 7.
    - Note that the 'target numbering' does relate to the digits shown on targets for 'with_digits' trials, but has no particular meaning for 'without_digits' trials.
* click_order: The actual order that the participant clicked the targets in. e.g. if `correct_order` is `[2, 7]`, and `click_order` is `[2, 8]`, this means that the participant's first click was correct, but the second was incorrect.
* response_correct: Indicates whether or not participant response was correct.
    - Possible values: `True` or `False`.

## (not) Running the experiment online
When developing this experiment, the only intention was to run it locally, on a lab computer. This means that the code has not been translated to JavaScript for running the experiment online, and wasn't written with this in mind. PsychoPy offers a tool for 'transpiling' (essentially translating from one programming language to another) Python code to JavaScript, but the tool has many flaws, not least since transpiling is hard. The code snippets in this experiment uses much Python-specific functionality which is not transpilation-friendly. Moreover, the code itself is structured on a more general level in a way that doesn't agree with certain assumptions made by PsychoPy's transpiler. If you'd like to run the experiment online, you're probably better off trying to recreate it from scratch, checking along the way to see if PsychoPy is able to transpile your project.