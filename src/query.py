#!/usr/bin/env python
# encoding: utf-8
'''
Script for running a long read set against BLASTing against multiple SRA ids, 
parsing the data and collecting in format compatible with our classifier

@author:     cjustin
@contact:    cjustin@bcgsc.ca
'''

class Query:
    
    def __init__(self, reads):
        """Constructor"""
        self._reads = readIDs
    
    def run(self, inputSRAs):
        """Run multiple SRA ids from a list, splitting into different processes"""       
        outputFiles = []
        #parse input
        sraFH = open(inputSRAs);
        for files in sraFH:
            outputFiles.append(files + ".results.txt")
            runSingle(files, files + ".results.txt")
        
        #combine results into single files
        compileResults(outputFiles)
    
    def runSingle(self, inputSRA, output):
        """Run a single sra ids"""
        pass

    def parseLine(self, line):
        """parse blast output into format needed for classifier"""
        pass
    
    def compileResults(self, outputList):
        """compile counts and results from multiple files"""
        pass
    
if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input", metavar="INPUT",
                      help="input file of list of SRA files")
    parser.add_option("-r", "--reads", dest="reads", metavar="READS", 
                      help="reads file")
                
    (options, args) = parser.parse_args()
        
    if options.input and options.reads:
        runner = Query(options.reads)
        runner.run(options.input)        
    else:
        print 'ERROR: Missing Required Options. Use -h for help'