# Title:       Project for Software Quality Assurance (COMP 5710/6710)
# Description: Automatically fuzzes five methods from TestOrchestrator4ML
# Authors:     Mary Mitchell (mem0250) and Adia Foster (azf0046)
# Course:      COMP5710 - Software Quality Assurance
# Due Date:    1 December 2022
# Run:         fuzz.py will be automatically executed from GitHub actions or 'python3 fuzz.py'

import os
import detection.constants as constants
from detection.py_parser import checkMetricNames 
from generation.py_parser import checkAlgoNames
from generation.main import generateAttack
from label_perturbation_attack.cliffsDelta import runs
from label_perturbation_attack.knn import euc_dist

def fuzzCheckMetricNames():
    # Initialize a wide variety of inputs to try on checkMetricNames
    fuzzValues = [0, None, 'RANDOMSTRING', {'RANDOM': 'DICTIONARY'}, {0, 5, 10.3, 'RANDOMSTRING'}, 3.14159, {None}, [None], {0}, [0], b'0000', int(b'0000'), {}, [], "\"`'><script>\\xE2\\x80\\xA8javascript:alert(1)</script>'", '', [[]]]
    print("Start fuzzing checkMetricNames...")
    # Loop through all the input values and determine if they create errors
    for input in fuzzValues:
        try: 
            checkMetricNames(input)
            print("checkMetricNames passed with input" + str(input))
        except:
            print("checkMetricNames failed with input: " + str(input))  
    print("Finish fuzzing checkMetricNames...")

def fuzzCheckAlgoNames():
    # Initialize a wide variety of inputs to try on checkAlgoNames
    fuzzValues = [0, None, 'RANDOMSTRING', {'RANDOM': 'DICTIONARY'}, {0, 5, 10.3, 'RANDOMSTRING'}, 3.14159, {None}, [None], {0}, [0], b'0000', int(b'0000'), {}, [], "\"`'><script>\\xE2\\x80\\xA8javascript:alert(1)</script>'", '', [[]]]
    print("Start fuzzing checkAlgoNames...")
    # Loop through all the input values and determine if they create errors
    for input in fuzzValues:
        try: 
            checkAlgoNames(input)
            print("checkAlgoNames passed with input" + str(input))
        except:
            print("checkAlgoNames failed with input: " + str(input)) 
    print("Finish fuzzing checkAlgoNames...")

def fuzzGenerateAttack():
    directory = os.getcwd() # Use current directory as an input directory for this function
    # Initialize a wide variety of inputs to try on generateAttack
    fuzzValue1 = [directory, 'THIS/IS/WHAT/A/PATH/LOOKS/LIKE']
    fuzzValue2 = [3.14159, 0, 22, None, 'RANDOMSTRING', -8.9, {}, []]
    print("Start fuzzing generateAttack...")
    # Loop through various combinations of the input values and determine if they create errors
    for val1 in fuzzValue1:
        for val2 in fuzzValue2:
            try:
                generateAttack(val1, val2)
                print("generateAttack passed with inputs: " + str(val1) + " and " + str(val2))
            except:
                print("generateAttack failed with inputs: " + str(val1) + " and " + str(val2))
    print("Finish fuzzing generateAttack...")

def fuzzRuns():
    # Initialize a wide variety of inputs to try on runs
    fuzzValues = [0, None, 'RANDOMSTRING', {'RANDOM': 'DICTIONARY'}, {0, 5, 10.3, 'RANDOMSTRING'}, 3.14159, {None}, [None], {0}, [0], b'0000', int(b'0000'), {}, [], "\"`'><script>\\xE2\\x80\\xA8javascript:alert(1)</script>'", '', [[]]]
    print("Start fuzzing runs...")
    # Loop through all the input values and determine if they create errors
    for input in fuzzValues:
        try: 
            runs(input)
            print("runs passed with input" + str(input))
        except:
            print("runs failed with input: " + str(input)) 
    print("Finish fuzzing runs...")

def fuzzEuc_Dist():
    # Initialize a wide variety of inputs to try on euc_dist
    fuzzValue1 = [0, 1, 2, -1, None, 3.14159, 'RANDOMSTRING1', {'RANDOM': 'DICTIONARY'}, [], {}, ]
    fuzzValue2 = [0, 2, 1, -4, None, 43, 'RANDOMSTRING2', {None}, [0], 0.000001]
    print("Start fuzzing euc_dist...")
    # Loop through various combinations of the input values and determine if they create errors
    for val1 in fuzzValue1:
        for val2 in fuzzValue2:
            try:
                euc_dist(val1, val2)
                print("euc_dist passed with inputs: " + str(val1) + " and " + str(val2))
            except:
                print("euc_dist failed with inputs: " + str(val1) + " and " + str(val2))
    print("Finish fuzzing euc_dist...")

def main():
    print("*** Begin Fuzzer ***")
    fuzzCheckMetricNames()
    fuzzCheckAlgoNames()
    fuzzGenerateAttack()
    fuzzRuns()
    fuzzEuc_Dist()
    print("*** End Fuzzer ***")

if __name__ == "__main__":
    main()