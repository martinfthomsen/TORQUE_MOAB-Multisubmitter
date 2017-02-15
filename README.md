# TORQUE_MOAB-Multisubmitter
This is a repository for wrapper scripts to submit multiple jobs to the TORQUE queueing system or the MOAB scheduler. It will take the msub/qsub arguments and multiple shell scripts as input, and execute the msub/qsub feature for each shell script with the provided msub/qsub arguments

# EXAMPLE (usage on computerome)
    git clone https://github.com/martinfthomsen/TORQUE_MOAB-Multisubmitter.git msubs
    echo "#!/bin/bash\necho 'hello world 1'\n" > job1.sh
    echo "#!/bin/bash\necho 'hello world 2'\n" > job2.sh
    msubs/msubs.py msub -W group_list=MYGROUP -A MYGROUP -l nodes=1:ppn=1,mem=1gb,walltime=0:00:30 job1.sh job2.sh
