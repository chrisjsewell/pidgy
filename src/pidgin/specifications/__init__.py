with __import__('importnb').Notebook():  
    from .. import tangle
    from . import transform_cell
with tangle.Pidgin():
    from .. import shell
    from . import emojis, yaml_, json, transform_ast
    from ..specifications import loaders
    
with tangle.Pidgin():
    from . import  testing, markdown, template, colors
    