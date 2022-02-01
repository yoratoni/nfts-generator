from settings import GlobalSettings
from colorama import Style, Fore

import time


class Logger:
    @staticmethod
    def pyprint(log: str, log_type: str, forced_log: bool = False):
        '''Debug Mode formatted print statements.
        
        Supported message types:
        - INFO -> Green
        - DATA -> Light blue
        - WARN -> Yellow
        - ERRO -> Light red

        Args:
            log (str): Printed log message.
            log_type (str): Type of the log (Unsupported title returns white colored log).
            include_path (bool, optional): Include the path in the log. Defaults to False.
            forced_log (bool, optional): Force even if not in debug mode. Defaults to False.
        '''
        
        if not GlobalSettings.dist_mode and (GlobalSettings.verbose_debugging or forced_log):
                color = Fore.WHITE
                
                if log_type == GlobalSettings.debug_types[0]:
                    color = Fore.GREEN
                elif log_type == GlobalSettings.debug_types[1]:
                    color = Fore.LIGHTBLUE_EX
                elif log_type == GlobalSettings.debug_types[2]:
                    color = Fore.YELLOW
                elif log_type == GlobalSettings.debug_types[3]:
                    color = Fore.LIGHTRED_EX

                print(f'{color}__{log_type}__ >>> {log}{Style.RESET_ALL}')


    @staticmethod
    def extime(timer: int):
        '''Automatic timer format (ns, µs, ms, s and min units).
        '''

        timer = (time.time_ns() - timer)
        units = ['ns', 'µs', 'ms', 's', ' mins']
        powers = [10**3, 10**6, 10**9]
        res = 0
        i = 0
        
        if timer < powers[0]:
            res = timer
        elif powers[0] <= timer < powers[1]:
            res = timer / powers[0]
            i = 1
        elif powers[1] <= timer < powers[2]:
            res = timer / powers[1]
            i = 2
        elif powers[2] <= timer:
            res = timer / powers[2]
            i = 3
            
            # Using minutes instead
            if res > 120:
                res = round(res / 60)
                i = 4
        
        Logger.pyprint(f'Execution Time: {res}{units[i]}', 'WARN', True)
