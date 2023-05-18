import subprocess

def start_program(program_path):
    subprocess.Popen(program_path, shell=True)

# List of programs to start
programs = [
    'python "C:/Users/MetaSuit P1/Documents/github/cv_angle_tracking/MetaSuitLegAngle/SPE.py"',
    '"C:/Users/MetaSuit P1/Documents/github/metasuit_launcher/ContAcqVoltageSamples_IntClk.application"',
    r'C:\Program Files (x86)\National Instruments\NI ELVISmx\Fgen.exe',
]

# Start each program
for program in programs:
    start_program(program)


#    "unity /path/to/unity_game.exe",
#        "NI ELVISmx /path/to/elvismx_function.exe",
