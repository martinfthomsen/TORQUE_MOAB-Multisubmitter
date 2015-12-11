#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' TORQUE msub Multisubmitter

This is a wrapper script for the msub feature of the TORQUE queueing
system. It will take the msub arguments and multiple shell scripts as input,
and execute the msub feature for each shell script with the provided msub
arguments
'''
import sys, os, time

def main(args):
   '''  '''
   jobs = CreateMsubJobs(args)
   for job in jobs:
      os.system(job)
      time.sleep(1)

def CreateMsubJobs(args):
   '''
   TEST_EXAMPLE:
      >>> sysargs = ("msubs -W group_list=cge -A cge -l "
                     "nodes=1:ppn=1,mem=5gb,walltime=24:00:00 "
                     "job1.sh job2.sh job3.sh job4.sh")
      >>> args = sysargs.split()[1:]
      >>> jobs = CreateMsubJobs(args)
      >>> print '\n'.join(jobs)
      msub -W group_list=cge -A cge -l nodes=1:ppn=1,mem=5gb,walltime=24:00:00 job1.sh
      msub -W group_list=cge -A cge -l nodes=1:ppn=1,mem=5gb,walltime=24:00:00 job2.sh
      msub -W group_list=cge -A cge -l nodes=1:ppn=1,mem=5gb,walltime=24:00:00 job3.sh
      msub -W group_list=cge -A cge -l nodes=1:ppn=1,mem=5gb,walltime=24:00:00 job4.sh
   '''
   jobs = []
   # Find the first occuring shell script. This will be the end marker for the
   # msub args
   arg_end = -1
   for i, a in enumerate(args):
      if a.split('.')[-1] == 'sh':
         arg_end = args.index(a)
         break
   
   # Set msub template cmd
   msub_tmp = "msub %s "%(' '.join(args[:arg_end]))
   
   # Loop shell scripts
   for script in args[arg_end:]:
      if script.split('.')[-1] == 'sh':
         jobs.append(msub_tmp + script)
      else:
         print ("Warning: The following argument was not a shell script, and thus "
               "misplaced in the end. Please only provide shell scripts as end "
               "arguments (%s)"%script)
   return jobs

if __name__ == "__main__":
   # Run main method with sys arguments
   main(sys.argv[1:])
