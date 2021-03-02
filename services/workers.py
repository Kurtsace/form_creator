# Scraper worker thread for getting and sanitizing data from the eia sharepoint site

# Imports
from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal

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
            result = self.func(self.id)

            # Emit true if the client has not been found 
            if not result:
                self.signals.error.emit(True)

        except: 
            traceback.print_exc()

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
    error = pyqtSignal(bool)
