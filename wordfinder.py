"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Function for finding random words from a dictionary."""
    
    def __init__(self, path):
        """Read the dictionary and return number of words read"""
        
        dict_file = open(path)
        
        self.words = self.parse(dict_file)
        
        print(f'{len(self.words)} words read')
        
    def parse(self, dict_file):
        """Parse the list of words (dict_file)"""
        
        # The strip() method removes any leading, and trailing whitespaces.
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return a random word"""
        
        # The choice() method returns a randomly selected element from the specified sequence.
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder. Excludes blank lines and/or comments."""
    
    def parse(self, dict_file):
        """Parse list of words (dict_file). Skip blanks and comments"""
        
        return [w.strip() for w in dict_file
               if w.strip() and not w.startswith("#")]
