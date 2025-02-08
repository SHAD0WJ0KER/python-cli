from colorama import Fore, Back, Style, just_fix_windows_console

class ColoredUtils():
    """
    TODO: document
    """
    FG_RED      = FG_ERROR   = Fore.RED
    FG_GREEN    = FG_SUCCESS = Fore.GREEN
    FG_BLUE     = FG_INFO    = Fore.BLUE
    FG_YELLOW   = FG_WARNING = Fore.YELLOW
    FG_DEFAULT  =              Fore.LIGHTWHITE_EX
    STYLE_RESET =              Style.RESET_ALL
    BRIGHT      =              Style.BRIGHT
    
    def __init__(self, bright=False):
        self.bright = bright
    
    def colored(self, text: str = "", color: int = Fore.LIGHTWHITE_EX) -> str:
        """
        Method that returns foreground colored text. Background not implemented yet.

        Parameters
        ----------
        text : str, optional
            Text that will be colored in desired color (default = "").
        color : int, optional
            Color in which the text will be returned (default = Fore.LIGHTWHITE_EX).
            It's recommendad to use colorama's `Fore` or `ColoredUtils` static attributes,
            e.g. from ColoredUtils: ColoredUtils.FG_RED, ColoredUtils.FG_ERROR or
            from Fore: Fore.RED, Fore.GREEN.
        
        Returns
        -------
        str
            Returns formatted text with style reset afterwards, so text
            after it is not affected.
        """
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

    def print_colored(self, text: str = "", color: int = Fore.LIGHTWHITE_EX) -> None:
        if self.bright:
            print(f"{self.BRIGHT}{color}{text}{self.STYLE_RESET}")
        else:
            print(f"{color}{text}{self.STYLE_RESET}")

    def print_warning(self, text: str = "", all: bool = False) -> None:
        
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
