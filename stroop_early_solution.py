import os
# here we define the position of the pygame-controlled surface within the computer screen
surface_position_x = 10
surface_position_y = 10
os.environ["SDL_VIDEO_WINDOW_POS"] = "{},{}".format(surface_position_x,surface_position_y)

# now we import pygame and submodules of pygame needed for events
import pygame
from pygame.locals import *

# in order to do some reliable experimental psychology, we need to randomize stuff, so we need this module
import random

# using variables to store some values related to our experimental paradigme
# variables about dimensions
surface_width = 500
surface_height = 500
stimuli_text_size = 60
instruction_text_size = 30

# colors
blue = (0,0,255)
red = (255,0,0)
bg_color = (255,255,255)
text_color_neutral = (0,0,0)
fixation_color = (0,0,0)
fixation_size = 20

# 
number_of_repetitions = 5

# this is a quick way to repeat some value several times to make a list
# our list is made of character strings
trials_list = ['congruent' for x in range(number_of_repetitions)]+['incongruent' for x in range(number_of_repetitions)] # this is the 

# ISI stands for inter_stimuli_interval, we want to counter_balance over conditions the duration of the fixation cross between trials
# thus we select 5 values because we have 5 repetitions of each condition
isi_values=range(1000,2001,250)+range(1000,2001,250)

# randomization is made on a trial_number_list, in order to use the same draw for both the trials_list and the ISI
trials_order=range(len(trials_list))
random.shuffle(trials_order)

# timing
instuction_minimal_duration = 2000
start_delay_duration = 400
stimuli_duration = 1000

try:
    pygame.init()
    my_surface = pygame.display.set_mode((surface_width, surface_height))
    my_surface.fill(bg_color)
    pygame.display.flip()
    # this first display of a brackgound color window is a good way to start

    # create font object
    myfont_for_stimuli = pygame.font.Font(None, stimuli_text_size) # uses default pygame font
    myfont_for_instructions = pygame.font.Font(None, instruction_text_size)

    # create text images, get their rectangles and set the rectangle center on the center of the pygame-controlled surface
    my_text_instruction = myfont_for_instructions.render("Press Space as soon as you read BLUE", True, text_color_neutral, bg_color)
    my_text_ready = myfont_for_instructions.render('Ready? Press Space button to start', True, text_color_neutral, bg_color)
    my_text_end = myfont_for_instructions.render('The end!', True, text_color_neutral, bg_color)
    my_text_blue_congruent = myfont_for_stimuli.render('BLUE', True, blue, bg_color)
    my_text_blue_incongruent = myfont_for_stimuli.render('BLUE', True, red, bg_color)
    
    rect_text_instruction = my_text_instruction.get_rect()
    rect_text_ready = my_text_ready.get_rect()
    rect_text_end = my_text_end.get_rect()
    rect_text_blue_congruent = my_text_blue_congruent.get_rect()
    rect_text_blue_incongruent = my_text_blue_incongruent.get_rect()

    rect_text_instruction.center = rect_text_ready.center = rect_text_end.center = (surface_width/2,surface_height/2)
    rect_text_blue_congruent.center = rect_text_blue_incongruent.center = (surface_width/2,surface_height/2)


    # show the instructions
    my_surface.fill(bg_color)
    my_surface.blit(my_text_instruction, rect_text_instruction) 
    pygame.display.flip()

    # leave some time for the subject to read
    pygame.time.wait(instuction_minimal_duration)

    # start of the experiment is 
    my_surface.fill(bg_color)
    my_surface.blit(my_text_ready, rect_text_ready) 
    pygame.display.flip()

    # there might be weird things in the event list, so let's clear it before we are using it
    pygame.event.clear()

    ready=False # we initialize a variable used in the while loop
    while not ready:
        for wait_ready in pygame.event.get(): # in the for loop, wait_ready is going to be taking its successive values from the list of events collected when the pygame.event.get() is executed. Here there are 2 steps in one : 1. collect a list of events 2. loop over the list
            if wait_ready.type == KEYDOWN and wait_ready.key == K_SPACE: # 
                ready=True # ok now our subject is ready to perform the experiment

    print "The experiment is starting" # experimenters need feedback too

    # a little delay for the subject to not be surpized by the first trial
    my_surface.fill(bg_color)
    pygame.display.flip()

    pygame.time.wait(start_delay_duration)


    # Now the experimental trials will start

    reaction_time_congruent=[]
    reaction_time_incongruent=[]

    for trial in trials_order:

        #select the stimuli that will be displayed relatively to the condition stored in the trials_list
        if trials_list[trial] == 'congruent':
            stim_text = my_text_blue_congruent
            stim_rect = rect_text_blue_congruent
        else:
            stim_text = my_text_blue_incongruent
            stim_rect = rect_text_blue_incongruent

        #fixation cross
        my_surface.fill(bg_color)
        pygame.draw.line(my_surface,fixation_color,(surface_width/2-fixation_size/2,surface_height/2),(surface_width/2+fixation_size/2,surface_height/2))
        pygame.draw.line(my_surface,fixation_color,(surface_width/2,surface_height/2-fixation_size/2),(surface_width/2,surface_height/2+fixation_size/2))
        pygame.display.flip()

        pygame.time.wait(isi_values[trial]) # we want to randomize the duration of the fixation cross so that appearance of the stim couldn't be predictible

        # stimulus drawing on the background window
        my_surface.fill(bg_color)
        my_surface.blit(stim_text, stim_rect) # here we use the variable which were assigned to one of the two condition's stimuli properties : text and rect

        reaction_time = 'na' # initialization of the reaction_time variable

        pygame.display.flip() # show the stimulus on the screen
        t0 = pygame.time.get_ticks() # take the stimulus onset time
        pygame.event.clear() # clear the event list, while there should be no answer yet (a bit dangerous still if the operation takes more than 50ms)

        while pygame.time.get_ticks()-t0 < stimuli_duration: # the duration of the stim is enforced by the loop with the timing condition
            e = pygame.event.poll() # get the last event in the eventlist
            if reaction_time == 'na' and e.type == KEYDOWN and e.key == K_SPACE: # no need for a counter anymore since we initialized the variable reaction_time
                reaction_time = pygame.time.get_ticks()-t0

        #
        if trials_list[trial] == 'congruent': # here we prepare the results by making 2 lists using the method ".append" in order to add the reaction time values in list corresponding to the trial condition
            reaction_time_congruent.append(reaction_time)
        else:
            reaction_time_incongruent.append(reaction_time)

        print "Condition {} : {} ms".format(trials_list[trial],reaction_time) # experimenters need feedback too

        for problem in pygame.event.get(): # in case there actually is a problem, remember to put something to close the experiment nicely
            if problem.type == QUIT:
                raise Exception

    # this is just to display a background color screen and wait a bit at the end before closing everything
    my_surface.fill(bg_color)
    my_surface.blit(my_text_end, rect_text_ready) 
    pygame.display.flip()
    pygame.time.wait(500) 

    print reaction_time_congruent # experimenters need feedback too
    print reaction_time_incongruent # experimenters need feedback too

    result_file = open('result_stroop.csv','w') # open a file in which we can write

    # now we can print some results in that file
    for value in range(len(reaction_time_congruent)): # print first all values from the congruent list
        result_file.write("{};{}\n".format('congruent',reaction_time_congruent[value]))

    for value in range(len(reaction_time_incongruent)): # and then the same for incongruent
        result_file.write("{};{}\n".format('incongruent',reaction_time_incongruent[value]))
            
    result_file.close() # never forget to close a file!

finally:
    pygame.quit()
