
class Logger:

    @staticmethod
    def write(message: str) -> None:
        print(f'\033[2K{message}')

    @staticmethod
    def rewrite(message: str) -> None:
        print(f'\033[2K{message}', end='\r', flush=True)
