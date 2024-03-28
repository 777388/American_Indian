import __future__
import traceback
import trace
import networkx
import microscope
try:
    __future__.all_feature_names = "Inward"
    traceback.extract_tb.__init_subclass__
    trace.Trace._annotations__("%00")
    microscope.__annotations__(networkx.adjacency_spectrum.__class__)
except:
    try:
        UnboundLocalError.__call__
    except:
        UserWarning.__cause__