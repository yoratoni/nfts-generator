from pyostra import pyprint, LogTypes
from pathlib import Path
from typing import Union

import os


class GeneralPaths:
    """Handles all the general path operations.
    """
    
    @staticmethod
    def scan_structure(dir_path: Path, return_paths: bool = False) -> Union[list[Path], list[str]]:
        """Get the files/sub-dirs structure of a directory.

        Args:
            dir_path (Path): Absolute path of the directory that is scanned.
            return_paths (bool, optional): If True, returns a list of paths instead of just names.

        Returns:
            Union[list[Path], list[str]]: List of paths/names found inside the specified dir.
        """
        
        structure = []
        
        if os.path.exists(dir_path):
            scan = os.listdir(dir_path)
            
            for element in scan:
                if return_paths:
                    file = os.path.join(dir_path, element)
                else:
                    file = element
                    
                structure.append(file)
        
        pyprint(LogTypes.DATA, f"Structure scanned [{dir_path}]")
        return structure
    
    
    @staticmethod
    def get_filenames_from_paths(paths: list[Path]) -> list[str]:
        """Converts a list of paths to a list of filenames with extensions.

        Args:
            paths (list[Path]): A list of absolute paths.

        Returns:
            list[str]: The converted list of filenames.
        """

        filenames = []
        
        for path in paths:
            filenames.append(os.path.basename(path))
            
        return filenames
    
    
    @staticmethod
    def get_formatted_filenames_from_paths(paths: list[Path]) -> str:
        """Works exactly like "get_filenames_from_paths()" but returns a formatted string
        instead of a list (filenames are separated with a comma and extensions are removed).
        
        Example:
            [E:\ARCHIVES\FOO.py, E:\ARCHIVES\BAR.txt] -> "FOO, BAR"

        Args:
            paths (list[Path]): A list of absolute paths.

        Returns:
            Union[str, None]: The formatted string of filenames.
        """
            
        filenames = ""
        
        for path in paths:
            curr_filename = os.path.basename(path)
            
            # Remove any extension
            (prefix, _, _) = curr_filename.rpartition(".")
            
            filenames += f"{prefix}, "
            
        # Removes the extra last comma
        if filenames[-2:] == ", ":
            filenames = filenames[:-2]
            
        return filenames


    @staticmethod
    def get_filename_index_in_paths(paths: list[Path], filename: str) -> Union[int, None]:
        """Get the index of a filename inside a list of paths.

        Args:
            paths (list[Path]): A list of absolute paths.
            filename (str): The filename that will be checked inside the list of paths.

        Returns:
            Union[int, None]: Returns the index of the file inside the list or None if not found.
        """
        
        for i, path in enumerate(paths):
            if os.path.basename(path) == filename:
                return i
