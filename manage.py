
"""
Manage Control Project
"""

# Libraries
import sys
from src import init

if __name__ == '__main__':
    if len(sys.argv) > 1:
        entity = sys.argv[1]
        init(entity)
    else:
        print('[Error] - Entity File Not Found')

        
