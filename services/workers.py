# Scraper worker thread for getting and sanitizing data from the eia sharepoint site

# Imports
from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal
from model.client import client_info

import traceback

# Scraper worker class inherits from QRunnable


class ScraperWorker(QRunnable):

    # Init
    def __init__(self, fn, id, *args, **kwargs):

        # Sper method
        super(ScraperWorker, self).__init__()

        # Signals
        self.signals = WorkerSignals()

        # ID arg
        self.id = id

        # Function to run
        self.func = fn

    # Run function when the thread is started
    @pyqtSlot()
    def run(self):

        try: 

            # Emit the running signal
            self.signals.running.emit(True)

            # Run the provided function
            result, func_trace = self.func(self.id)

            # Emit true if the client has not been found 
            if client_info['case_number'] == '':
                self.signals.client_not_found_error.emit(True)

            # Emit the traceback from the chrome driver (if there is one)
            if result == -1:
                self.signals.error.emit(func_trace)

        except: 
            self.signals.error.emit(traceback.format_exc())

        else:
            # Emit false for running signal
            self.signals.running.emit(False)

        finally:
            #Emit the finished signal
            self.signals.finished.emit(True)

             


# Worker signals to emit results
class WorkerSignals(QObject):

    '''
    Signals available from a currently running worker thread:

    finished 
        Returns true or false --indicates process is done

    running 
        Returns true if thread is still processing or not

    error
        Returns true if client was not found 

    '''

    finished = pyqtSignal(bool)
    running = pyqtSignal(bool)
    error = pyqtSignal(str)
    client_not_found_error = pyqtSignal(bool)
