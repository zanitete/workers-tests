#!/usr/bin/python

from analysis_core import AnalysisItem, AnalysisDataset, SimulationAnalysisItem, CircuitAnalysisItem
from workflow.type_decorator import accepts,returns
import workflow.types as wt
from types import *
'''
do not import external modules here (add them in process method)
'''


class Sqrt(AnalysisItem):
    """ Plot an analysis and file it

    What:

    Do an analysis

    AnalysisDatasets:

    """

    # Analysis Meta-data attributes
    caption = """Sqrt"""
    name = "Sqrt"
    author = "zaninett"
    description = "Square root"
    
    '''
    Annotate 'process' method with input and output parameters type.
    
    Available types:
       { workflow.types.URI, workflow.types.ListURI, BooleanType, IntType, LongType
       		FloatType, StringType, UnicodeType }
       
    workflow.types.URI and workflow.types.ListURI must provide a mime type among:
       { circuitconfig, blueconfig, metype set, morphology set, neurondb_dat, simconfig, bioname_recipe,
       		ccell_release_dir, dataset, etype, jpeg, jpg, png, avi }
    
    ------------------
         EXAMPLES
    ------------------
	1)  @accepts('ignore', wt.URI("blueconfig"))
	    @returns(wt.List_URI("png"))

    2)	@accepts('ignore',bioname_recipe, wt.URI("neurondb_dat"), wt.URI("ccell_release_dir"))
    	@returns(wt.URI("bioname_recipe"))

    3)	@accepts('ignore', IntType, IntType)
    	@returns(IntType)
    '''
    @accepts('ignore', IntType)
    @returns(FloatType)
    def process(self, arg0):
        '''
        TODO: auto-generated function, implementation goes here"
        '''
        import math
        result = math.sqrt(arg0)
        print "square root of %s is %s" % (str(arg0), str(result))
        return result
        
    def __init__(self, job=None):
        # call the base constructor
        AnalysisItem.__init__(self,job)
        
    def precheck(self, uri):

        '''
        This function is invoked before 'process()'
        TODO: Precondition goes here
        '''
        
        return True
        
    def save_report_flag(self):
        '''
        Tell file_report that we want to delete the report if it is successfully filed
        This is the default behaviour
        '''
        return False
                
        
def workflow_items():
    '''
    advertise which classes in this file should be processed by the py-workflow-items code generator
    '''
    return [Sqrt]
