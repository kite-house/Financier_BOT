from datetime import datetime

datetime = datetime.today().replace(microsecond=0)
logfile = 'Logging/logfile.txt'
crashlogfile = 'Logging/crashlogfile.txt'

class Logging():
    def output_log(text, filename):
        print(text)
        with open(filename, 'a') as file:
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

    def crash_report(Error):
        text = f'CRASH-REPORT: DATETIME: {datetime}; STATUS-CODE: ERROR; DESCRIPTION: {Error}'
        Logging.output_log(text,crashlogfile)