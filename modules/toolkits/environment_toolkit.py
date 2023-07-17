import platform


class EnvironmentToolkit():
    (bit, linkage) = platform.architecture()
    arch: str = "64" if bit == "64bit" else "32"

    is_mac: bool = True if platform.system() == "Mac" else False
    is_linux: bool = True if platform.system() == "Linux" else False
    is_windows: bool = True if platform.system() == "Windows" else False

    @staticmethod
    def get_platform_name() -> str:
        if(platform.system() == "Mac"):
            return "osx"
        if(platform.system() == "Linux"):
            return "linux"
        if(platform.system() == "Windows"):
            return "windows"
        return "unknown"
        
