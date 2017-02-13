# TORQUE-msub-Multisubmitter
This is a wrapper program for the msub feature of the TORQUE queueing system. It will take the msub arguments and multiple shell scripts as input, and execute the msub feature for each shell script with the provided msub arguments


# EXAMPLE (usage on computerome)
git clone https://github.com/martinfthomsen/TORQUE-msub-Multisubmitter.git msubs
echo "#!/bin/bash\necho 'hello world 1'\n" > job1.sh
echo "#!/bin/bash\necho 'hello world 2'\n" > job2.sh
msubs/msubs -W group_list=MYGROUP -A MYGROUP -l nodes=1:ppn=1,mem=1gb,walltime=0:00:30 job1.sh job2.sh
