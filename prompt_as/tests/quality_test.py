

try:
    from .test_system import Prompt_As_Test_System
    from ..prompt_as_f_decorator import pf
except ImportError:
    from test_system import Prompt_As_Test_System
    from prompt_as_f_decorator import pf



@pf
def save_user(username:str, password:str):
    """
    Saves the given username and pass to an sqlite database.
    If there is no exception return True otherwise return False
    """


@pf
def check_password(username:str, password:str):
    """
    Checks the given password is correct for given username username in the sqllite database.
    And return True or False bool
    """

@pf
def my_ip() -> str:
    """
    Returns the IP of machine in str, if there is an exception it should return None
    """


@pf
def hackernews() -> list:
    """
    Returns the latest hacker news posts (10) in a list format with their links. If there is an exception return None
    """



@pf
def encrypt_via_fernet(data:str, encryption_key:str) -> str:
    """
    Encrypts data with encryption_key string and returns the encrypted data.
    I will give encryption_key in string format and you will use for key generation. 
    If there is an exception return None.
    If succed you will return string to me.
    """

@pf
def decrypt_via_fernet(encrypted_data:str, encryption_key:str) -> str:
    """
    Decrypts data with encryption_key string and returns the decrypted data. 
    I will give encryption_key in string format and you will use for key generation. 
    If there is an exception return None.
    If succed you will return string to me.
    """


@pf
def total_memory_size_in_gb()->int:
    """
    Returns the total memory in gigabytes of the machine. put "GB" at the end of the result If there is an exception return None
    """

@pf
def available_disk_space_in_gb() -> int:
    """
    Returns the available disk space in gigabytes of the machine in integer format. If there is an exception return None
    """

@pf
def get_current_system_time() -> str:
    """
    Returns the current system time in string format. If there is an exception return None
    """

@pf
def operating_system() -> str:
    """
    Returns the name of the operating system. Returns None if unable to detect.
    """
 
@pf 
def all_running_processes()-> list:
    """
    Lists format all currently running processes. Returns None in case of an error. Lists format all currently running processes
    """   
    
@pf
def battery_status()-> str:
    """
    Returns the charge percentage of the machine's battery and whether it is charging. If unsuccessful, return None.
    """

@pf
def network_status()-> str:
    """
    Checks if the machine is connected to a network. Returns 'Connected' or 'Disconnected'. If unsuccessful, return None.
    """

@pf
def network_speed_tests()-> str:
    """
    It returns whether the machine is connected to the internet and upload, download and latency values ​​in Mb/sec. In case of error, it returns none.   
    """

@pf
def system_locales()-> str:
    """
    Returns the current locale setting of the system. Returns None on error.    
    """

@pf
def speaker_volume()-> str:
    """
    Returns the current speaker volume level as a percentage. Returns None on error.
    """


@pf
def audio_volume()->str:
    """
    Returns the current audio volume level as a percentage. Returns None if it cannot be retrieved.
    """

@pf
def wifi_signal_strength()->str:
    """
    Measures and returns of the  machine the WiFi signal strength as a percentage. Returns None on error.
    """

@pf
def bluetooth_connection_status()->str:
    """
    Checks if the machine is connected to a bluetooth. Returns 'Connected' or 'Disconnected'. Returns None if it cannot be retrieved.
    """

@pf
def machine_ram()->int:
    """
    Returns the RAM of machine from int, if there is an exception it should return None.
    """


@pf
def get_btc_price()->int:
    """
    Returns the BTC price from int , if there is an exception it should return None
    """

@pf
def get_eth_price()-> int:
    """
    Returns the ETH price from int, if there is an exception it should return None
    """

@pf
def get_usd_to_bbd_price()-> str:
    """
    Returns the USD-BBD pair price, if there is an exception it should return None
    """    

@pf
def get_city_weather(city)-> int:
    """
    Returns the given city weather from int used web if there is an exception it should return None
    """

@pf
def calculate_age(birthdate)-> int:
    """
    Calculates and return from int the age based on the provided birthdate. If the birthdate is invalid or in the future, returns None.
    """    

@pf
def convert_temperature(temp, unit)-> str:
    """
    Converts a temperature from Celsius to Fahrenheit or vice versa. Input is temperature and 'C' for Celsius or 'F' for Fahrenheit.
    Returns None if the unit is invalid.

    """

@pf
def parse_url(url)-> str:
    """
    Parses a URL and returns its components. if there is an exception it should return None
    """    

@pf
def add_two_single_digit(number_one:int, number_two:int) -> int:
    """
    Adds two single digit numbers and returns in int format. if there is an exception it should return None
    """

@pf
def add_tree_single_digits(number_one:int, number_two:int, number_tree:int) -> int:
    """
    Adds tree single digit numbers and returns in int format. if there is an exception it should return None

    """    

@pf
def multpley_two_single_digit(number_one:int, number_two:int) -> int:
    """
    Multpley two single digit numbers and returns in int format. if there is an exception it should return None
    """    

def multpley_tree_single_digit(number_one:int , number_two:int, number_tree:int)-> int:
    """
    Multpley tree single digit numbers and returns in int format. if there is an exception it should return None
    """

@pf
def add_two_double_digit(number_one:int, number_two:int) -> int:
    """
    Adds two double digit numbers and returns in int format. if there is an exception it should return None
    """

@pf
def add_three_double_digit(number_one:int, number_two:int, number_three:int) -> int:
    """
    Adds three double digit numbers and returns in int format. if there is an exception it should return None
    """

@pf
def multpley_two_double_digit(number_one:int , number_two:int ) -> int:
    """
    Multpley two double digit numbers and returns in int format. if there is an exception it should return None
    """

@pf
def multpley_three_double_digit(number_one: int, number_two: int, number_three:int) -> int:
    """
    Multpley three double digit numbers and returns in int format. if there is an exception it should return None
    """

class QualityTest:
    def __init__(self, test_systems): 
        self.test_systems = test_systems

    def run_tests(self):
        results = []
        for test_system in self.test_systems:
            result = test_system.run_test()
            results.append(result)

        print("\n\n\n\n\n*******************")
        print("All results:\n")
        for result in results:
            print(result)

# Example usage:
test_systems = [
    Prompt_As_Test_System(hackernews, [([],{})], None, [None], list),
    Prompt_As_Test_System(my_ip, [([],{})], None, [None], str),
    Prompt_As_Test_System(save_user, [(["onuratakan", "6431"],{})], [True], [None]),
    Prompt_As_Test_System(check_password, [(["onuratakan", "13532"],{})], [False], [None]),
    Prompt_As_Test_System(check_password, [(["onuratakan", "6431"],{})], [True], [None]),
    Prompt_As_Test_System(total_memory_size_in_gb, [([],{})], None, [None], int),
    Prompt_As_Test_System(available_disk_space_in_gb, [([],{})], None, [None], int),
    Prompt_As_Test_System(get_current_system_time, [([],{})], None, [None], int),
    Prompt_As_Test_System(operating_system, [([],{})], None, [None], str),
    Prompt_As_Test_System(all_running_processes, [([],{})], None, [None], list),
    Prompt_As_Test_System(battery_status, [([],{})], None, [None], str),
    Prompt_As_Test_System(network_status, [([],{})], None, [None], str),
    Prompt_As_Test_System(network_speed_tests, [([],{})], None, [None], str),
    Prompt_As_Test_System(system_locales, [([],{})], None, [None], str),
    Prompt_As_Test_System(speaker_volume, [([],{})], None, [None], str),
    Prompt_As_Test_System(audio_volume, [([],{})], None, [None], str),
    Prompt_As_Test_System(wifi_signal_strength, [([],{})], None, [None], str),
    Prompt_As_Test_System(bluetooth_connection_status, [([],{})], None, [None], str),
    Prompt_As_Test_System(machine_ram, [([],{})], None, [None], int),
    Prompt_As_Test_System(get_btc_price, [([],{})], None, [None], int),
    Prompt_As_Test_System(get_eth_price, [([],{})], None, [None], int),
    Prompt_As_Test_System(get_usd_to_bbd_price, [([],{})], None, [None], str),
    Prompt_As_Test_System(get_city_weather, [("Istanbul",)], None, [None], int),
    Prompt_As_Test_System(calculate_age, [("2005-05-05",)], [19] , [None], int),
    Prompt_As_Test_System(convert_temperature, [(100, 'C')], [212], [None], str),
    Prompt_As_Test_System(convert_temperature, [(212, 'F')], [100], [None], str),
    Prompt_As_Test_System(parse_url, [("https://github.com/Upsonic/prompt-as-function")], None, [None], str),    
    Prompt_As_Test_System(add_two_single_digit, [(1, 2)], [3], [None], int),
    Prompt_As_Test_System(add_two_single_digit, [(1, 9)], [10], [None], int),
    Prompt_As_Test_System(add_two_single_digit, [(9, 9)], [18], [None], int),
    Prompt_As_Test_System(add_two_single_digit, [(0, 1)], [1], [None], int),
    Prompt_As_Test_System(add_two_single_digit, [(5, 5)], [10], [None], int),
    Prompt_As_Test_System(add_tree_single_digits, [(1, 2, 3)], [6], [None], int),
    Prompt_As_Test_System(add_tree_single_digits, [(1, 9, 3)], [13], [None], int),     
    Prompt_As_Test_System(add_tree_single_digits, [(9, 8, 9)], [26], [None], int), 
    Prompt_As_Test_System(add_tree_single_digits, [(0, 1, 2)], [3], [None], int),
    Prompt_As_Test_System(add_tree_single_digits, [(5, 5, 5)], [15], [None], int),
    Prompt_As_Test_System(multpley_two_single_digit, [(1, 2)], [2], [None], int),
    Prompt_As_Test_System(multpley_two_single_digit, [(1, 9)], [9], [None], int),
    Prompt_As_Test_System(multpley_two_single_digit, [(9, 9)], [81], [None], int),
    Prompt_As_Test_System(multpley_two_single_digit, [(0, 1)], [0], [None], int),
    Prompt_As_Test_System(multpley_two_single_digit, [(5, 5)], [25], [None], int),
    Prompt_As_Test_System(multpley_tree_single_digit, [(1, 2, 3)], [6], [None], int),
    Prompt_As_Test_System(multpley_tree_single_digit, [(1, 9, 3)], [27], [None], int),
    Prompt_As_Test_System(multpley_tree_single_digit, [(9, 8, 9)], [648], [None], int),
    Prompt_As_Test_System(multpley_tree_single_digit, [(0, 1, 2)], [0], [None], int),
    Prompt_As_Test_System(multpley_tree_single_digit, [(5, 5, 5)], [125], [None], int),
    Prompt_As_Test_System(add_two_double_digit, [(40, 20)], [60], [None], int),
    Prompt_As_Test_System(add_two_double_digit, [(10, 90)], [100], [None], int),
    Prompt_As_Test_System(add_two_double_digit, [(90, 90)], [180], [None], int),
    Prompt_As_Test_System(add_two_double_digit, [(10, 10)], [20], [None], int),
    Prompt_As_Test_System(add_two_double_digit, [(50, 50)], [100], [None], int),
    Prompt_As_Test_System(add_three_double_digit, [(40, 20, 10)], [70], [None], int), 
    Prompt_As_Test_System(add_three_double_digit, [(10, 90, 10)], [110], [None], int),
    Prompt_As_Test_System(add_three_double_digit, [(90, 90, 10)], [190], [None], int),
    Prompt_As_Test_System(add_three_double_digit, [(10, 10, 10)], [30], [None], int),
    Prompt_As_Test_System(add_three_double_digit, [(50, 50, 40)], [140], [None], int),
    Prompt_As_Test_System(multpley_two_double_digit, [(40, 20)], [800], [None], int),
    Prompt_As_Test_System(multpley_two_double_digit, [(10, 90)], [900], [None], int),
    Prompt_As_Test_System(multpley_two_double_digit, [(90, 90)], [8100], [None], int),
    Prompt_As_Test_System(multpley_two_double_digit, [(10, 10)], [100], [None], int),
    Prompt_As_Test_System(multpley_two_double_digit, [(50, 50)], [2500], [None], int),
    Prompt_As_Test_System(multpley_three_double_digit, [(40, 20, 10)], [8000], [None], int),
    Prompt_As_Test_System(multpley_three_double_digit, [(10, 90, 10)], [9000], [None], int),
    Prompt_As_Test_System(multpley_three_double_digit, [(90, 90, 20)], [162000], [None], int),
    Prompt_As_Test_System(multpley_three_double_digit, [(10, 10, 10)], [1000], [None], int),
    Prompt_As_Test_System(multpley_three_double_digit, [(50, 50, 40)], [100000], [None], int),
    Prompt_As_Test_System(encrypt_via_fernet, [("Hello World", "I am encrypt1234")], None, [None], str),
    Prompt_As_Test_System(decrypt_via_fernet, [("gok", "bora")], None, [None], str),





]

quality_test = QualityTest(test_systems)
