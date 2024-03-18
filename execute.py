import subprocess
import evaluation.evaluation as eval




process_trainer = subprocess.Popen(["python","trainer.py","-tdata/train.txt","-c"+str(0.5),"-rdebug","-mglove-twitter-200","-l8","-k100"])
process_trainer.wait()
process_trainer.kill()
output_file = open("output.txt","w")
process = subprocess.Popen(["python","pcfg_guesser.py","-ssession2","-rdebug","-n10000000"], stdout=output_file,universal_newlines=True)
process.wait()
process.kill()
eval.main("test.txt")
