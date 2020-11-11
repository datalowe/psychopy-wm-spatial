﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Wed Nov 11 15:09:47 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

### SET EXPERIMENT CONSTANTS ###
# width/height of area where targets
# can appear, in degrees
AREA_WIDTH_DEG = 22
AREA_HEIGHT_DEG = 13

# target size, in degrees
TARGET_SIZE_DEG = 2.5

# target neutral (not lit up and not awaiting response) color
TARGET_NEUTRAL_COL = "#AAAAAA"
# target light up (or click) color
TARGET_LIGHT_COL = "#FFFF00"
# target awaiting participant response color
TARGET_AWAIT_COL = "#FFFFFF"

# target text clicked color
TARGET_CLICKED_COL = "#BBFFBB"

# number of trials to run per difficulty level
NUM_TRIALS = 3

# number of potential targets to show in each trial
NUM_TARGETS = 9

# starting difficulty level, ie number of targets
# lighting up in the first trial
START_DIFFICULTY = 2
# highest difficulty level, ie number of squares
# lighting up in the last trial (if the participant
# doesn't fail X number of times in a row before then)
END_DIFFICULTY = 9

# duration for which targets should light up while
# demonstrating the sequence to the participant.
# durations are specified in window flips (one flip
# corresponds to 1/60s for most screens)
DEMO_LIGHT_DUR = 60
# duration to wait inbetween lighting up targets
# during demonstration phase
DEMO_INTER_DUR = 30
# duration for which targets should flash when clicked
RESP_FLASH_DUR = 3

# large/medium/small instructions text size,
# in degrees
TXT_SIZE_L = 2
TXT_SIZE_M = 0.8
TXT_SIZE_S = 0.6

# experiment instructions
# "In this test you will be shown squares. The squares will
# light up in a particular order. You are to memorize the
# order in which the squares light up. Once the squares
# have finished lighting up, you are to click the squares
# in the same order.\n\n
# Use the left mouse button to click the squares."
INSTRUCTIONS_TXT = (
    "I det här testet kommer du att visas rutor. " 
    "Rutorna kommer att lysa upp i en viss ordning."
    "Du ska memorisera i vilken ordning som "
    "rutorna lyser upp. När rutorna lyst klart ska du klicka "
    "på rutorna i samma ordning.\n\n"
    "Använd vänster musknapp för att klicka på rutorna."
)

# instructions screen 'continue' message
# "Click here to see an example"
INSTRUCTIONS_CONTINUE_TXT = (
    "Tryck här för att se ett exempel"
)

#    "Testet tar ca 3 minuter att genomföra."

### END SET EXPERIMENT CONSTANTS ###
# in order to subclass the Rect class (see 'Begin Experiment') 
# it must be directly imported, see
# https://github.com/psychopy/psychopy/issues/1159
from psychopy.visual.rect import Rect

# import random.choices for sampling with replacement 
# in 'Begin Experiment' -> gen_light_order
from random import choices


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'click_baseline'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/workingman/Documents/ASD_and_Synesthesia/Python/psychopy/PsychoPy projects/wm_spatial/wm_spatial.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='macMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text=INSTRUCTIONS_TXT,
    font='Arial',
    units='deg', pos=(0, 0), height=TXT_SIZE_M, wrapWidth=25, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse_instructions = event.Mouse(win=win)
x, y = [None, None]
mouse_instructions.mouseClock = core.Clock()
text_go = visual.TextStim(win=win, name='text_go',
    text=INSTRUCTIONS_CONTINUE_TXT,
    font='Arial',
    units='deg', pos=(0, -6), height=TXT_SIZE_S, wrapWidth=25, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "inter_trial_5000ms"
inter_trial_5000msClock = core.Clock()
text_iti_timekeeper = visual.TextStim(win=win, name='text_iti_timekeeper',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
class LightRect(Rect):
    """
    Represents a rectangle that can light up and be clicked.
    
    Attributes
    ----------
    is_lit : boolean
        Should be True if the rectangle is lighting up, 
        otherwise should be False.
    light_flip_countdown: int
        Represents the number of window flips left before
        the rectangle should stop being lit up.
    rest_color: string
        A hex color code that describes what color the rectangle
        should have when in its resting (non-lit-up) state.
    lit_color: string
        A hex color code that describes what color the rectangle
        should have when in its lit-up state.
    Methods
    ----------
    switch_on: See docstring
    switch_off: See docstring
    """
    is_lit = False
    light_flip_countdown = 0
    lit_color = TARGET_LIGHT_COL
    rest_color = TARGET_NEUTRAL_COL
    
    
    def switch_on(self, duration):
        """
        Checks if this rectangle is already in a lit up state.
        If not, sets the rectangle to be in lit state for 'duration' flips, 
        changes this rectangle's color and sets `is_lit` to True. Returns
        True if switched on, otherwise False.
        """
        switched_on = False
        if not self.is_lit:
            self.light_flip_countdown = duration
            self.is_lit = True
            self.fillColor = self.lit_color
            self.lineColor = self.lit_color
            switched_on = True
        return switched_on
    
    def switch_off(self):
        """
        Checks if this rectangle is in a lit up state, and if so,
        decrements the flip countdown counter. If the counter
        is then <=0, reverts this rectangle's color back to neutral
        and resets `is_lit`. Returns True if switched off, otherwise
        False.
        """
        switched_off = False
        if self.is_lit:
            self.light_flip_countdown -= 1
        if self.light_flip_countdown <= 0:
            self.fillColor = self.rest_color
            self.lineColor = self.rest_color
            self.is_lit = False
            switched_off = True
        return switched_off

class Point:
    """
    Represents (x, y) coordinates in 2-dimensional space.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        """
        Returns the euclidean distance between this and the
        other passed point.
        """
        dist = ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)
        return dist
    
    def __str__(self):
        """
        Returns a string representation '(x, y)' of this point.
        """
        return "({}, {})".format(self.x, self.y)
    
    def __repr__(self):
        """
        Returns a description of how this point can be
        recreated.
        """
        return "Point({}, {})".format(self.x, self.y)
    
    def as_tuple(self):
        """
        Returns a (x, y) tuple with this point's x/y coordinates.
        """
        return self.x, self.y

def points_collide(point_ls, new_point):
    """
    Goes through a list of Point instances and compares
    the new_point to see if the new_point is too close
    to one of the points in the point_ls. Returns True if
    there is a collision, otherwise False.
    """
    collides = False
    for old_point in point_ls:
        if (new_point - old_point) < TARGET_SIZE_DEG * 2:
            collides = True
            break
    return collides

def gen_rand_point():
    """
    Generates a random point within the target area.
    """
    x_coord = randint(-AREA_WIDTH_DEG//2, AREA_WIDTH_DEG//2)
    y_coord = randint(-AREA_HEIGHT_DEG//2, AREA_HEIGHT_DEG//2)
    return Point(x_coord, y_coord)

def gen_point_ls():
    """
    Generates a list of (x, y) coordinate Point instances until
    there are as many instances as there should be targets/trial.
    """
    point_ls = []
    while len(point_ls) < NUM_TARGETS:
        new_point = gen_rand_point()
        if not points_collide(point_ls, new_point):
            point_ls.append(new_point)
    return point_ls

def gen_light_order(seq_len, num_targets):
    """
    Generates a random order in which targets should
    be lit up, with length based on the passed sequence
    length, and numbers based on
    the number of targets.
    """
    num_population = [x for x in range(num_targets)]
    order_ls = choices(num_population, k=seq_len)
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
    for seq_len in range(min_seq_len, max_seq_len+1):
        for trial in range(num_trials):
            order_ls = gen_light_order(seq_len, num_targets)
            trial_orders.append(order_ls)
    return trial_orders

# generate (x, y) coordinates for the targets
point_ls = gen_point_ls()

# generate order of targets lighting up for each
# trial
trial_orders = gen_trial_orders(
    NUM_TARGETS, 
    START_DIFFICULTY,
    END_DIFFICULTY,
    NUM_TRIALS
)

# generate one TextStim instance for each target
# (numbering starting from 0)
targets = []
for i in range(NUM_TARGETS):
    new_target = LightRect(
        win=win, 
        name='target_{}'.format(i),
        units='deg', 
        ori=0,
        pos=point_ls[i].as_tuple(), 
        width=TARGET_SIZE_DEG,
        height=TARGET_SIZE_DEG,
        fillColor=TARGET_NEUTRAL_COL, 
        lineColor=TARGET_NEUTRAL_COL, 
        lineWidth=1,
        lineColorSpace='rgb', 
        fillColorSpace='rgb',
        opacity=1,
        depth=-2.0,
        interpolate=True)
    targets.append(new_target)

# initialize trial counter
trial_counter = 0
mouse_trial = event.Mouse(win=win)
x, y = [None, None]
mouse_trial.mouseClock = core.Clock()

# Initialize components for Routine "end_routine"
end_routineClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Nu är du klar. Tack!',
    font='Arial',
    units='deg', pos=(0, 0), height=TXT_SIZE_L, wrapWidth=25, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_instructions
mouse_instructions.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [text_instructions, mouse_instructions, text_go]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions* updates
    if text_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.tStart = t  # local t and not account for scr refresh
        text_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions, 'tStartRefresh')  # time at next scr refresh
        text_instructions.setAutoDraw(True)
    # *mouse_instructions* updates
    if mouse_instructions.status == NOT_STARTED and t >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        mouse_instructions.frameNStart = frameN  # exact frame index
        mouse_instructions.tStart = t  # local t and not account for scr refresh
        mouse_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_instructions, 'tStartRefresh')  # time at next scr refresh
        mouse_instructions.status = STARTED
        mouse_instructions.mouseClock.reset()
        prevButtonState = mouse_instructions.getPressed()  # if button is down already this ISN'T a new click
    if mouse_instructions.status == STARTED:  # only update if started and not finished!
        buttons = mouse_instructions.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [text_go]:
                    if obj.contains(mouse_instructions):
                        gotValidClick = True
                        mouse_instructions.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_go* updates
    if text_go.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_go.frameNStart = frameN  # exact frame index
        text_go.tStart = t  # local t and not account for scr refresh
        text_go.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_go, 'tStartRefresh')  # time at next scr refresh
        text_go.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=NUM_TRIALS * (END_DIFFICULTY - START_DIFFICULTY + 1), method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "inter_trial_5000ms"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # reset targets
    for target in targets:
        target.rest_color = TARGET_NEUTRAL_COL
        target.fillColor = TARGET_NEUTRAL_COL
        target.lineColor = TARGET_NEUTRAL_COL
    
    # keep track of which components have finished
    inter_trial_5000msComponents = [text_iti_timekeeper]
    for thisComponent in inter_trial_5000msComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    inter_trial_5000msClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "inter_trial_5000ms"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = inter_trial_5000msClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=inter_trial_5000msClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_iti_timekeeper* updates
        if text_iti_timekeeper.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_iti_timekeeper.frameNStart = frameN  # exact frame index
            text_iti_timekeeper.tStart = t  # local t and not account for scr refresh
            text_iti_timekeeper.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_iti_timekeeper, 'tStartRefresh')  # time at next scr refresh
            text_iti_timekeeper.setAutoDraw(True)
        if text_iti_timekeeper.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_iti_timekeeper.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_iti_timekeeper.tStop = t  # not accounting for scr refresh
                text_iti_timekeeper.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_iti_timekeeper, 'tStopRefresh')  # time at next scr refresh
                text_iti_timekeeper.setAutoDraw(False)
        # draw all of the targets
        for target in targets:
            target.draw()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inter_trial_5000msComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "inter_trial_5000ms"-------
    for thisComponent in inter_trial_5000msComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_iti_timekeeper.started', text_iti_timekeeper.tStartRefresh)
    trials.addData('text_iti_timekeeper.stopped', text_iti_timekeeper.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # fetch order in which targets should light up at beginning
    # of this trial
    light_order = trial_orders[trial_counter]
    
    # form list of targets, arranged in order in which they should
    # light up
    light_targets = [targets[index] for index in light_order]
    
    # store the sequence length
    seq_len = len(light_targets)
    
    # reset counter used for looping over order in which
    # targets should light up
    light_counter = 0
    
    # reset countdown timer for counting down time inbetween
    # targets lighting up during demonstration phase
    inter_light_countdown = 0
    
    # set the initial target that should light up and switch
    # it on (make it light up)
    light_target = light_targets[light_counter]
    light_target.switch_on(DEMO_LIGHT_DUR)
    
    # reset booleans indicating whether which phase of
    # the trial that is currently running
    demo_phase = True
    response_phase = False
    
    # reset counter for registering number of clicks on targets
    click_counter = 0
    
    # reset list of times when valid (on target) click responses 
    # occur
    response_times = []
    
    # reset list of order in which the participant makes clicks
    click_order = []
    
    # fetch the routine start time
    trial_start_time = globalClock.getTime()
    
    # setup some python lists for storing info about the mouse_trial
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [mouse_trial]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # if in the demonstration phase
        if demo_phase:
            # decrement the countdown timer which keeps track of
            # number of flips until active target should light up
            inter_light_countdown -= 1
            # attempt to turn off the active target
            switched_off = light_target.switch_off()
            # if the active target was successfully switched off
            if  switched_off:
                light_counter += 1
                # if there are more targets to light up
                if light_counter < seq_len:
                    # proceed to the next target to light up and start the
                    # countdown timer until the target should light up
                    inter_light_countdown = DEMO_INTER_DUR
                    light_target = light_targets[light_counter]
                # if the whole sequence is done
                elif light_counter > seq_len:
                    demo_phase = False
            # if it's time to switch on the active target
            if inter_light_countdown <= 0:
                light_target.switch_on(DEMO_LIGHT_DUR)
        
        # if the lighting phase is finished and response phase
        # isn't started yet, start the response phase
        if not demo_phase and not response_phase:
            for target in targets:
                target.rest_color = TARGET_AWAIT_COL
                target.fillColor = TARGET_AWAIT_COL
                target.lineColor = TARGET_AWAIT_COL
            response_phase = True
            rphase_start_time = trialClock.getTime()
        
        # if in the response phase
        if response_phase:
            # try to switch off each of the targets (so that
            # clicked targets are switched off properly)
            for target in targets:
                target.switch_off()
        
        # check if mouse button has been clicked
        buttons = mouse_trial.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            # if currently in response phase and a new click was made 
            if response_phase and sum(buttons) > 0:  
                # loop over the targets
                for target in targets:
                    # if mouse was inside of target
                    if target.contains(mouse_trial):
                        # switch on the target, increase counter, register
                        # which target the participant clicked
                        target.switch_on(RESP_FLASH_DUR)
                        click_counter += 1
                        click_order.append(targets.index(target))
                        # save the click time
                        response_time = trialClock.getTime() - rphase_start_time
                        response_times.append(response_time)
        
        # if all responses have been collected, end the trial
        if click_counter >= seq_len:
            continueRoutine = False
        
        # draw all of the targets
        for target in targets:
            target.draw()
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ## save trial data
    trials.addData('response_times', response_times)
    trials.addData('trial_start_time', trial_start_time)
    trials.addData('click_order', click_order)
    # increment trial counter
    trial_counter += 1
    # store data for trials (TrialHandler)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed NUM_TRIALS * (END_DIFFICULTY - START_DIFFICULTY + 1) repeats of 'trials'


# ------Prepare to start Routine "end_routine"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_routineComponents = [text_end]
for thisComponent in end_routineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_routine"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_routineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_routineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_end.tStop = t  # not accounting for scr refresh
            text_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
            text_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_routineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_routine"-------
for thisComponent in end_routineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
