import os
import time as tt
import resource
import subprocess

max_iters = 8000  # The number of iterations executed in total
episode_iters = 20  # The number of iterations executed in each episode

if __name__ == "__main__":

    if not os.path.exists("./Logs"):
        os.makedirs("./Logs")

    if not os.path.exists("./tmp"):
        os.makedirs("./tmp")

    exp_name = ""
    iters = 0
    counter_store_model = 1

    while iters < max_iters:
        processes = []
        subprocess.call(['python process_worker_job.py -i '+str(iters)+ ' -c '+str(counter_store_model)+' -e '+str(episode_iters)], shell=True)
        # Get the maximum resident set size (memory usage) of the current process using the resource module.
        usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print(usage)
        counter_store_model = counter_store_model + episode_iters
        iters = iters + episode_iters


