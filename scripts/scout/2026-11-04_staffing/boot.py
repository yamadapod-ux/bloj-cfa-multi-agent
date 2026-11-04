# Runner: keeps scripts apart from downloaded data. Usage: python -I boot.py <script.py> args...
import sys, os, runpy
here = os.path.dirname(os.path.abspath(__file__))
sys.path.append(here)
os.chdir(os.path.join(here, 'data'))
script = sys.argv[1]; sys.argv = sys.argv[1:]
runpy.run_path(os.path.join(here, script), run_name='__main__')
