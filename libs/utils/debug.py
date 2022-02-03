from settings import GlobalSettings
from colorama import Style, Fore

import time
import sys
import os


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
                    color = Fore.LIGHTBLUE_EX 
                elif log_type == GlobalSettings.debug_types[1]:
                    color = Fore.CYAN
                elif log_type == GlobalSettings.debug_types[2]:
                    color = Fore.YELLOW
                elif log_type == GlobalSettings.debug_types[3]:
                    color = Fore.LIGHTRED_EX
                elif log_type == GlobalSettings.debug_types[4]:
                    color = Fore.LIGHTGREEN_EX
                
                print(f'{color}[{log_type}] {log}{Style.RESET_ALL}')


    @staticmethod
    def extime(name: str, timer: int, multiply_timer: int = 1, print_msg: bool = True) -> str:
        '''Automatic timer format (ns, µs, ms, s and min units).
        
        Args:
            name (str): Name of the timer.
            timer (int): Using time.perf_counter_ns() to get the starting point of the timer.
            multiply_timer (int, optional): Multiply the time by a value (To estimate time).
            print_msg (bool, optional): If True, it also prints the formatted timer message.
            
        Returns:
            str: The formatted timer message
        '''

        timer = (time.perf_counter_ns() - timer) * multiply_timer
        
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
        
        if print_msg:
            Logger.pyprint(f'{name}: {res}{units[i]}', 'SUCCESS', True)
        
        return f'{name}: {res}{units[i]}'
