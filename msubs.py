#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' TORQUE/MOAB Multisubmitter

This is a wrapper script to submit multiple jobs to the TORQUE queueing system
or the MOAB scheduler. It will take the msub/qsub arguments and multiple shell
scripts as input, and execute the msub/qsub feature for each shell script with
the provided msub/qsub arguments.
'''
import sys, os, time

def main(args):
   ''' Get and execute submission jobs, wait one second between submissions '''
   jobs = CreateMsubJobs(args)
   for job in jobs:
      os.system(job)
      time.sleep(1)

def CreateMsubJobs(args):
   '''
   TEST_EXAMPLE:
      >>> sysargs = ("msubs msub -W group_list=cge -A cge -l "
                     "nodes=1:ppn=1,mem=5gb,walltime=24:00:00 "
                     "job1.sh job2.sh job3.sh job4.sh")
      >>> args = sysargs.split()[1:]
      >>> jobs = CreateMsubJobs(args)
      >>> print('\n'.join(jobs))
      msub -W group_list=cge -A cge -l nodes=1:ppn=1,mem=5gb,walltime=24:00:00 job1.sh
      msub -W group_list=cge -A cge -l nodes=1:ppn=1,mem=5gb,walltime=24:00:00 job2.sh
      msub -W group_list=cge -A cge -l nodes=1:ppn=1,mem=5gb,walltime=24:00:00 job3.sh
      msub -W group_list=cge -A cge -l nodes=1:ppn=1,mem=5gb,walltime=24:00:00 job4.sh
   '''
   jobs = []
   # Find the first occuring shell script
   arg_end = -1
   for i, a in enumerate(args):
      if a.split('.')[-1] == 'sh':
         arg_end = args.index(a)
         break
   
   # Set msub template cmd
   msub_tmp = ' '.join(args[:arg_end])
   
   # Make submission job for each shell script in the arguments
   for script in args[arg_end:]:
      if script.split('.')[-1] == 'sh':
         jobs.append(' '.join([msub_tmp, script]))
      else:
         print("Warning: The following argument was not a shell script, and thus "
               "misplaced in the end. Please only provide shell scripts as end "
               "arguments (%s)"%script)
   return jobs

if __name__ == "__main__":
   # Run main method with sys arguments
   main(sys.argv[1:])
