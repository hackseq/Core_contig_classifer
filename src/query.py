#!/usr/bin/env python
# encoding: utf-8
'''
Script for running a long read set against BLASTing against multiple SRA ids, 
parsing the data and collecting in format compatible with our classifier

@author:     cjustin
@contact:    cjustin@bcgsc.ca
@editor:     dcgenomics
'''

from optparse import OptionParser
import subprocess
import sys

class Query:
    
    def __init__(self, reads):
        """Constructor"""
        self._reads = reads
    
    def run(self, inputSRAs):
        """Run multiple SRA ids from a list, splitting into different processes"""       
#         outputFiles = []
        #parse input
        sraFH = open(inputSRAs);
        #TODO THREAD ME
        for files in sraFH:
            file = files.strip()
#             outputFiles.append( file + ".bam")
            self._runSingle(file, file + ".bam")
        
        #combine results into single files
#         compileResults(outputFiles)
    
    def _runSingle(self, inputSRA, output):
        """Run a single sra ids"""
        cmd = "magicblast -paired -splice F -db " + self._reads + " -sra " + inputSRA + " > " + output
#         cmd = "sleep 60 > " + output
        cmd += " 2> " + output + ".log ; rm ~/ncbi/public/sra/" + inputSRA + ".sra.cache"
#         print(cmd)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
#     def compileResults(self, outputList):
#         """compile counts and results from multiple files"""
#         pass
    
if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input", metavar="INPUT",
                      help="input file of list of SRA IDs")
    parser.add_option("-r", "--reads", dest="reads", metavar="READS", 
                      help="blast DB")
                
    (options, args) = parser.parse_args()
        
    if options.input and options.reads:
        runner = Query(options.reads)
        runner.run(options.input)        
    else:
        print 'ERROR: Missing Required Options. Use -h for help'
