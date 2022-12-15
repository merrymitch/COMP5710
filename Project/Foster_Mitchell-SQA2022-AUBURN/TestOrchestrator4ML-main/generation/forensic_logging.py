# Title:       Project for Software Quality Assurance (COMP 5710/6710)
# Description: Logging method used to integrate forensics in various functions
# Team:        Mary Mitchell (mem0250) and Adia Foster (azf0046)
# Source:      This code comes from workshop 9 
# Course:      COMP5710 - Software Quality Assurance
# Due Date:    1 December 2022

import logging

def getLoggerObj():
    logging.basicConfig(filename='../../FORENSICS.LOG', level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%d-%b-%y %H-%M-%S')
    loggerObj = logging.getLogger('project-logger')
    return loggerObj