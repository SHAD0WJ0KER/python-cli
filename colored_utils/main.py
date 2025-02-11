from colorama import Fore, Back, Style, just_fix_windows_console, init

class ColoredUtils():
    """
    TODO: document
    """
    FG_RED      = FG_ERROR   = Fore.RED
    FG_GREEN    = FG_SUCCESS = Fore.GREEN
    FG_BLUE     = FG_INFO    = Fore.BLUE
    FG_YELLOW   = FG_WARNING = Fore.YELLOW
    FG_DEFAULT  =              Fore.WHITE
    STYLE_RESET =              Style.RESET_ALL

    def __init__(self, bright : bool = False) -> None:

        #init(convert=True)
        
        self.bright = bright
        
        self.info = f"{Fore.BLUE}[INFO]{Style.RESET_ALL}"
        self.success = f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL}"
        self.warning = f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL}"
        self.error = f"{Fore.RED}[ERROR]{Style.RESET_ALL}"
        self.bg = [Back.LIGHTBLACK_EX, Back.MAGENTA]

        if self.bright:
            self.info = f"{Style.BRIGHT}" + self.info
            self.success = f"{Style.BRIGHT}" + self.success
            self.warning = f"{Style.BRIGHT}" + self.warning
            self.error = f"{Style.BRIGHT}" + self.error
            self.bg = [Back.BLACK, Back.MAGENTA]
        
    def get_success(self, end : str = " ") -> str:
        """
        Returns string stored in self.success (default: green colored [SUCCESS]) 
        with an additional string appended.

        Parameters
        ----------
        end : str, optional
            String that will be added afterwards (default = " ")
        
        Returns
        -------
        str
            String 
        """
        return self.success + end

    def get_info(self, end : str = " ") -> str:
        """
        Returns string stored in self.info (default: blue colored [INFO]) 
        with an additional string appended.

        Parameters
        ----------
        end : str, optional
            String that will be added afterwards (default = " ")
        
        Returns
        -------
        str
            String 
        """
        return self.info + end

    def get_error(self, end : str = " ") -> str:
        """
        Returns string stored in self.success (default: red colored [ERROR]) 
        with an additional string appended.

        Parameters
        ----------
        end : str, optional
            String that will be added afterwards (default = " ")
        
        Returns
        -------
        str
            String 
        """
        return self.error + end

    def get_warning(self, end : str = " ") -> str:
        """
        Returns string stored in self.success (default: yellow colored [WARNING]) 
        with an additional string appended.

        Parameters
        ----------
        end : str, optional
            String that will be added afterwards (default = " ")
        
        Returns
        -------
        str
            String 
        """
        return self.success + end

    def colored(self, text: str = "", color: int = Fore.WHITE) -> str:
        """
        Method that returns foreground colored text. Background not implemented yet.

        Parameters
        ----------
        text : str, optional
            Text that will be colored in desired color (default = "").
        color : int, optional
            Color in which the text will be returned (default = Fore.WHITE).
            It's recommendad to use colorama's `Fore` or `ColoredUtils` static attributes,
            e.g. from ColoredUtils: ColoredUtils.FG_RED, ColoredUtils.FG_ERROR or
            from Fore: Fore.RED, Fore.GREEN.
        
        Returns
        -------
        str
            Returns formatted text with style reset afterwards, so text
            after it is not affected.
        """
        temp = "" if not self.bright else f"{Style.BRIGHT}"
        temp +=  f"{color}{text}{Style.STYLE_RESET}"
        return temp
    
    def print_colored(self, text, color: int = Fore.WHITE, end : str = "\n") -> None:
        """
        Method that will print text in wanted color. 

        Parameters
        ----------
        text : str
            Text that will be printed
        color : int, optional
            Color in which color will appear (default = Fore.WHITE).
        end : str, optional
            Ending delimiter for print (default = "\n")
        
        Returns
        -------
        None
        """
        temp = "" if not self.bright else f"{Style.BRIGHT}"
        temp += f"{color}{text}{Style.STYLE_RESET}"
        print(temp, end=end)

    def reset(self) -> None:
        """
        Reset class attributes to initial values.

        Parameters
        ----------

        Returns
        -------
        None
        """

        self.info = f"{Fore.BLUE}[INFO]{Style.RESET_ALL}"
        self.success = f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL}"
        self.warning = f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL}"
        self.error = f"{Fore.RED}[ERROR]{Style.RESET_ALL}"
        
        if self.bright:
            self.info = f"{Style.BRIGHT}" + self.info
            self.success = f"{Style.BRIGHT}" + self.success
            self.warning = f"{Style.BRIGHT}" + self.warning
            self.error = f"{Style.BRIGHT}" + self.error