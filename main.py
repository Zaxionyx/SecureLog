import datetime


class Logging_Functions:
    def __init__(self):
        self.categories = { "error": [], "info": [], "access": [] }
    
    def add_log_entry(self,category, message, level):
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S %m - %d- %Y")
        print(f"Current Date and Time:{now}")

        log_entry = (now, message, level)
        if category in self.categories:
            self.categories[category].append(log_entry)
        else:
            print(f"Warning: Category '{category}' not found. Log not added.")

logbook = Logging_Functions()
        



  



    


        

    
        











