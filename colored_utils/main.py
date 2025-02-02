from colorama import Fore, Back, Style, just_fix_windows_console

class Colored_utils():

    def __init__(self, bright=False):
        self.FG_RED      = self.FG_ERROR   = Fore.RED
        self.FG_GREEN    = self.FG_SUCCESS = Fore.GREEN
        self.FG_BLUE     = self.FG_INFO    = Fore.BLUE
        self.FG_YELLOW   = self.FG_WARNING = Fore.YELLOW
        self.FG_DEFAULT  =                   Fore.LIGHTWHITE_EX
        self.STYLE_RESET =                   Style.RESET_ALL
        self.bright      =                   bright
        self.BRIGHT      =                   Style.BRIGHT
    
    def colored(self, text: str = "", color: str = self.FG_DEFAULT) -> str:
        if self.bright:
            return f"{self.BRIGHT}{color}{text}{self.STYLE_RESET}"
        else:
            return f"{color}{text}{self.STYLE_RESET}" 

    def warning(self, text: str = "", all: bool = False) -> str:
        
        if all:
            return f"{self.FG_WARNING}[Warning] {text}{self.STYLE_RESET}"
        
        return f"{self.FG_WARNING}[Warning] {self.STYLE_RESET}{text}"

    def info(self, text: str = "", all: bool = False) -> str:

        if all:
            return f"{self.FG_INFO}[INFO] {text}{self.STYLE_RESET}"
        
        return f"{self.FG_INFO}[INFO] {self.STYLE_RESET}{text}"

    def success(self, text: str = "", all: bool = False) -> str:
        
        if all:
            return f"{self.FG_SUCCESS}[SUCCESS] {text}{self.STYLE_RESET}"
        
        return f"{self.FG_SUCCESS}[SUCCESS] {self.STYLE_RESET}{text}"

    def print_colored(self, text: str = "", color: str = self.FG_DEFAULT) -> None:
        if self.bright:
            print(f"{self.BRIGHT}{color}{text}{self.STYLE_RESET}")
        else:
            print(f"{color}{text}{self.STYLE_RESET}" 

    def print_warning(self, text: str = "", all: bool = False) -> None:)
        
        if all:
            print(f"{self.FG_WARNING}[Warning] {text}{self.STYLE_RESET}")
        
        print(f"{self.FG_WARNING}[Warning] {self.STYLE_RESET}{text}")

    def print_info(self, text: str = "", all: bool = False) -> None:

        if all:
            print(f"{self.FG_INFO}[INFO] {text}{self.STYLE_RESET}")
        
        print(f"{self.FG_INFO}[INFO] {self.STYLE_RESET}{text}")

    def print_success(self, text: str = "", all: bool = False) -> None:
        
        if all:
            print(f"{self.FG_SUCCESS}[SUCCESS] {text}{self.STYLE_RESET}")
        
        print(f"{self.FG_SUCCESS}[SUCCESS] {self.STYLE_RESET}{text}")