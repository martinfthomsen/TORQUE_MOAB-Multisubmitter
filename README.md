# TORQUE_MOAB-Multisubmitter
This is a repository for a wrapper script to submit multiple jobs to the TORQUE
queueing system or the MOAB scheduler. It will take the msub/qsub arguments and
multiple shell scripts as input, and execute the msub/qsub feature for each
shell script with the provided msub/qsub arguments.

# How it works
The msubs.py script will create a job for each shell script specified in the
end arguments, using the parameter arguments specified.
Each job is then submitted to the queing system with a waiting time of one
second in between to avoid overloading the system.

# Usage
To use this wrapper script is very simple.
First argument should be either "qsub" or "msub".
next comes the arguments for qsub or msub, this could for instance be
"-W group_list=MYGROUP -A MYGROUP -l nodes=1:ppn=1,mem=1gb,walltime=0:00:30"
and in the end you can list all the shell scripts you want submitted with the
previous defined submission parameters.

# Example (usage on computerome)
    git clone https://github.com/martinfthomsen/TORQUE_MOAB-Multisubmitter.git msubs
    echo "#!/bin/bash\necho 'hello world 1'\n" > job1.sh
    echo "#!/bin/bash\necho 'hello world 2'\n" > job2.sh
    msubs.py msub -W group_list=MYGROUP -A MYGROUP -l nodes=1:ppn=1,mem=1gb,walltime=0:00:30 job1.sh job2.sh

# Dry run
To make a dry run and see what is submitted, the commands can be run with echo
as the first argument.
    $ ./msubs.py echo msub -W group_list=MYGROUP -A MYGROUP -l nodes=1:ppn=1,mem=1gb,walltime=0:00:30 job1.sh job2.sh
    msub -W group_list=MYGROUP -A MYGROUP -l nodes=1:ppn=1,mem=1gb,walltime=0:00:30 job1.sh
    msub -W group_list=MYGROUP -A MYGROUP -l nodes=1:ppn=1,mem=1gb,walltime=0:00:30 job2.sh
