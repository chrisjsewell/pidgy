from ._version import *

with __import__('importnb').Notebook():
    from .markdown import MarkdownImporter
    from . import magics
    from . import shell
    from . import kernel
    from . import macros
    
_ipython_display_ = shell._ipython_display_

def load_ipython_extension(ip):
    MarkdownImporter().__enter__()
    # Jinja2Importer().__enter__()
    # Jinja2MarkdownImporter().__enter__()
    for module in (magics, shell, kernel, macros):
        module.load_ipython_extension(ip)
        
def unload_ipython_extension(ip):
    MarkdownImporter().__exit__()
    # Jinja2Importer().__enter__()
    # Jinja2MarkdownImporter().__enter__()
    for module in (magics, shell, kernel, macros):
        module.unload_ipython_extension(ip)