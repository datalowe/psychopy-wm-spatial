"""
Script for generating specifications for each trial for which number should go
on which target. E. g. "digit '1' should appear on top of the third target
in the tenth trial". Note that target numbering is arbitrary and isn't related
to target placement. This script, together with 'wm_generate_sequences' is 
for helping you make sure that numbers appear in the same positions every 
time the experiment is run.

If you're not using numbers on top of targets, you don't need this script.

Use this script if you want the placement of numbers to be the same for every
participant. If you instead want number placements to be randomly generated
for each experiment run, you don't need this.

Make specifications by changing the values given to constants (in ALL CAPS)
below. Then run the script, and the result will be saved to
'generated_number_positions.txt' in this folder. Then, open up the experiment's
.psyexp file with PsychoPy Builder, go to the 'instructions' routine and open up
'code_constants'. Scroll down to 'NUMBER_POSITIONS = []'. Copy->paste in the
.txt file's content, replacing the square brackets ('[]').
"""
from random import shuffle


# number of potential targets to show in each trial
NUM_TARGETS = 9

# number of trials to run per difficulty level
NUM_TRIALS = 3

# starting difficulty level, ie number of targets
# lighting up in the first trial
START_DIFFICULTY = 2
# highest difficulty level, ie number of squares
# lighting up in the last trial (if the participant
# doesn't fail X number of times in a row before then)
END_DIFFICULTY = 12

trials_number_positions = []

# generate one list of number positions per trial
num_levels = END_DIFFICULTY - START_DIFFICULTY + 1
for i in range(NUM_TRIALS * num_levels):
    rand_number_ls = [x for x in range(1, NUM_TARGETS + 1)]
    shuffle(rand_number_ls)
    trials_number_positions.append(rand_number_ls)

out_str = "[\n"

for number_positions in trials_number_positions:
    out_str += f"    {str(number_positions)},\n"
out_str += "]"

with open('generated_number_positions.txt', 'w') as f:
    f.write(out_str)
