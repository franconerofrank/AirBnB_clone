#!/usr/bin/python3                                                                                                                      
"""                                                                                                                                     
Airbnb Console                                                                                                                          
"""                                                                                                                                     
import cmd                                                                                                                              
from models.base_model import BaseModel                                                                                                 
from models.__init__ import storage                                                                                                     
from models.user import User                                                                                                            
from models.place import Place                                                                                                          
from models.amenity import Amenity                                                                                                      
from models.review import Review                                                                                                        
from models.city import City                                                                                                            
from models.state import State                                                                                                          
                                                                                                                                        
                                                                                                                                        
class HBNBCommand(cmd.Cmd):                                                                                                             
    """                                                                                                                                 
    The entry point for the command interpreter                                                                                         
    """                                                                                                                                 
    prompt = '(hbnb) '                                                                                                                  
    classes = ['BaseModel', 'User', 'Place', 'State',                                                                                   
               'City', 'Amenity', 'Review']                                                                                             
    dotcmds = ['.all()', '.count()']
