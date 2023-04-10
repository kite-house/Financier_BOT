from datetime import datetime

datetime = datetime.today().replace(microsecond=0)
logfile = 'Logging/logfile.txt'

class Logging():
    def output_log(text, logfile):
        print(text)
        with open(logfile, 'a') as file:
            file.write(text)
            file.close()

    def start():
        text = f"INFO: DATETIME: {datetime} - START: COMPLETED!\n"
        Logging.output_log(text,logfile)
            
    def stop():
        text = f'INFO: DATETIME: {datetime} - STOP\n'
        Logging.output_log(text,logfile)

    def action(action, zone, result):
        text = f'INFO: DATETIME: {datetime}; LOGING ACTION: {action}; ZONE: {zone}; RESULT: {result}\n'
        Logging.output_log(text,logfile)

    def system(action, zone, result):
        text = f'SYSTEM-INFO: DATETIME: {datetime}; LOGING ACTION: {action}; ZONE: {zone}; RESULT: {result}\n'
        Logging.output_log(text,logfile)