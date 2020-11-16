"""
Script for generating specifications of, for each trial, in which sequence targets
should light up. Note that target numbering is arbitrary and has nothing
to do with where targets are placed. This script, together with 
'wm_generate_target_coordinates.py', is for helping you make sure that 
targets light up in the same sequence every time the experiment
is run.

Use this script if you want the target 'light-up sequences' to be the same for every
participant. If you instead want sequences to be randomly generated
for each experiment run, you don't need this.

Make specifications by changing the values given to constants (in ALL CAPS)
below. Then run the script, and the result will be saved to
'generated_sequences.txt' in this folder. Then, open up the experiment's
.psyexp file with PsychoPy Builder, go to the 'instructions' routine and open up
'code_constants'. Scroll down to 'TARGET_SEQUENCES = []'. Copy->paste in the
.txt file's content, replacing the square brackets ('[]').
"""
from random import choice

# number of trials to run per difficulty level
NUM_TRIALS = 3
# number of potential targets to show in each trial
NUM_TARGETS = 9

# maximum allowed repeats of the same target 'lighting up'
# in a row.
# (set a very high number, eg 9999, if you want
# completely random target sequences)
MAX_REPEAT_NUM = 2

# starting difficulty level, ie number of targets
# lighting up in the first trial
START_DIFFICULTY = 2
# highest difficulty level, ie number of squares
# lighting up in the last trial (if the participant
# doesn't fail all trials of a difficulty level before 
# then)
END_DIFFICULTY = 12


def gen_light_order(seq_len, num_targets):
    """
    Generates a pseudorandom order in which targets should
    be lit up, with length based on the passed sequence
    length, and numbers based on
    the number of targets. The same target is allowed to
    light up twice, but not more, in a row.
    """
    # generate set of all target numbers
    num_population = {x for x in range(num_targets)}
    order_ls = []
    while len(order_ls) < seq_len:
        # create set which represents valid numbers to add to order list
        eligible_nums = num_population
        if len(order_ls) >= MAX_REPEAT_NUM:
            # check if the MAX_REPEAT_NUM most recent
            # elements all have the same value, and if so,
            # exclude this value from the set of eligible choices
            recent_nums = set(order_ls[-MAX_REPEAT_NUM:])
            max_repeated = len(recent_nums) == 1
            if max_repeated:
                eligible_nums = num_population.difference(recent_nums)
        new_num = choice(tuple(eligible_nums))
        order_ls.append(new_num)
    return order_ls


def gen_trial_orders(
        num_targets,
        min_seq_len,
        max_seq_len,
        num_trials):
    """
    Generates a list of lists, where each inner lists holds
    a random order in which targets should be lit up, based
    on:
        num_targets - number of targets in each screen
        min_seq_len - minimum sequence length
        max_seq_len - maximum sequence length
        num_trials - number of trials per difficulty level
    """
    trial_orders = []
    for seq_len in range(min_seq_len, max_seq_len + 1):
        for trial in range(num_trials):
            order_ls = gen_light_order(seq_len, num_targets)
            trial_orders.append(order_ls)
    return trial_orders

# generate order of targets lighting up for each
# trial
trial_orders = gen_trial_orders(
    NUM_TARGETS,
    START_DIFFICULTY,
    END_DIFFICULTY,
    NUM_TRIALS
)

out_str = '[\n'
for order in trial_orders:
    out_str += f'    {str(order)},\n'
out_str += ']'

with open('generated_sequences.txt', 'w') as f:
    f.write(out_str)
