import subprocess
import evaluation.evaluation as eval


print("Starting Training Process...")

process_trainer = subprocess.Popen(["python", "trainer.py", "-tdata/train.txt", "-c"+str(0.5), "-rdebug","-mglove-twitter-200", "-l8", "-k425", "-n3"], shell=True)
process_trainer.wait()
process_trainer.kill()
output_file = open("suggestion_list.txt", "w")
process = subprocess.Popen(["python","pcfg_guesser.py","-ssession2","-rdebug","-n10000000"], stdout=output_file,universal_newlines=True)
process.wait()
process.kill()
eval.main("test.txt",["suggestion_list.txt"])
