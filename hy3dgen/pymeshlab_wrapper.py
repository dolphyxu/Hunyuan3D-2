"""
PyMeshLab wrapper to handle E57 plugin loading errors.
This module provides a safe way to import PyMeshLab while suppressing
E57 plugin loading errors that occur due to libffi version mismatches.
"""
import os
import sys
import warnings
import io
from contextlib import redirect_stderr, redirect_stdout

# Capture and suppress all output during import
f = io.StringIO()
with redirect_stderr(f), redirect_stdout(f):
    # Import pymeshlab with all output suppressed
    import pymeshlab

# Check if E57 format is available and print a notice if not
if not hasattr(pymeshlab, 'Format_E57'):
    print("Notice: E57 file format support is not available in this PyMeshLab installation.")
    print("This is likely due to a libffi version mismatch.")
    print("Other mesh formats (OBJ, PLY, STL, etc.) should still work normally.")

# Export all pymeshlab attributes
for attr in dir(pymeshlab):
    if not attr.startswith('_'):
        globals()[attr] = getattr(pymeshlab, attr)
