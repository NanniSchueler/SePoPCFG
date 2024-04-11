import subprocess
import evaluation.evaluation as eval

### How To Use ###
# This file executes all steps of PCFG automatically
# We used our best parameters, that are
# word-embedding: Glove Twitter 200
# l = 8
# k = 425 (number of nearest neighbors in the embedding)
# n = 3
#
# To define a password policy, enter
# (1) minimum required length (example: 4)
# (2) minimum amount of digits (example: 2)
# (3) mimimum amount of special characters (example: 1)
# This results in parameter (-p)4#2#1
# If no policy is required either set all to 0 or delete the parameter
### ---------- ###

print("Starting Training Process...")
# For Linux
process_trainer = subprocess.Popen(["python", "trainer.py", "-tdata/train.txt", "-c"+str(0.5), "-rdebug", "-mglove-twitter-200", "-l8", "-k425", "-n3"])
# For Windows
#process_trainer = subprocess.Popen(["python", "trainer.py", "-tdata/train.txt", "-c"+str(0.5), "-rdebug", "-mglove-twitter-200", "-l8", "-k425", "-n3"], shell=True)
process_trainer.wait()
process_trainer.kill()
output_file = open("suggestion_list.txt", "w")
# For Linux
process = subprocess.Popen(["python", "pcfg_guesser.py", "-ssession2", "-rdebug", "-n10000000", "-p4#2#1"], stdout=output_file, universal_newlines=True)
# For Windows
#process = subprocess.Popen(["python", "pcfg_guesser.py", "-ssession2", "-rdebug", "-n10000000", "-p4#2#1"], stdout=output_file, universal_newlines=True, shell=True)
process.wait()
process.kill()
eval.main("test.txt", ["suggestion_list.txt"])
