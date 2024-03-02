#author: Jay Sanders
#class: CS 325
#due: 2024-03-01

#this uses the D principle by having a base class called "Sys_Log" that has a generic log function that gets tailored to each logging library

from abc import ABC, abstractmethod
import logging

class Sys_Log:
    @abstractmethod
    def log(self, message):
        pass
class Logging(Sys_Log):
    def __init__(self, lib):
        self.lib = lib
    def log(self, message):
        logging.warning(message)
def main():
    log_system = Logging("logging")
    log_system.log("This is a test of the web application")
    #This is where the web application would be implemented, and it would use the logging system to track any errors

if __name__ == "__main__":
    main()