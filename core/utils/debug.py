from settings import GlobalSettings
from colorama import Style, Fore

import time


class Logger:
    @staticmethod
    def pyprint(log_type: str, title: str, log: str, forced_log: bool = False, same_line: bool = False):
        '''Debug Mode formatted print statements.
        
        Supported message types:
        - INFO -> Light blue
        - DATA -> Cyan
        - WARN -> Yellow
        - ERRO -> Light red
        - SUCCESS -> Light green

        Args:
            log_type (str): Type of the log (Unsupported title returns white colored log).
            title (str): The title of the log.
            log (str): Printed log message.
            include_path (bool, optional): Include the path in the log. Defaults to False.
            forced_log (bool, optional): Force even if not in debug mode. Defaults to False.
            same_line (bool, optional): Print over the previous line.
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
                
                if len(title) == 0:
                    output = f'{color}[{log_type}] {log}{Style.RESET_ALL}'
                else:
                    output = f'{color}[{log_type}] {title}: {log}{Style.RESET_ALL}'
                
                if same_line:
                    print_end = '\r'
                else:
                    print_end = None
                    
                print(output, end=print_end)
                    

    @staticmethod
    def extime(
        name: str,
        timer: int,
        multiply_timer: int = 1,
        print_msg: bool = True,
        approximated_value: bool = False,
    ) -> str:
        '''Automatic timer format (ns, µs, ms, s and mins units).
        
        Args:
            name (str): Name of the timer.
            timer (int): Using time.perf_counter_ns() to get the starting point of the timer.
            multiply_timer (int, optional): Multiply the time by a value (To estimate time).
            print_msg (bool, optional): If True, it also prints the formatted timer message.
            approximated_value (bool, optional): If True, adds the "~" character for an approximation.
            
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
            res = round(timer / powers[0])
            i = 1
        elif powers[1] <= timer < powers[2]:
            res = round(timer / powers[1])
            i = 2
        elif powers[2] <= timer:
            res = timer / powers[2]
            i = 3
            
            # Using minutes instead
            if res > 120:
                res = round(res / 60)
                i = 4
        
        res = round(res, 2)
        
        if approximated_value:
            output = f'{name}: ~{res}{units[i]}'
        else:
            output = f'{name}: {res}{units[i]}'
        
        if print_msg:
            Logger.pyprint('SUCCESS', '', output, True)
        
        return output
