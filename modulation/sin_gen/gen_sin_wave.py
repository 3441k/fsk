import math
import argparse
import os

EN_PLT = True

try:
    from matplotlib import pyplot as plt
except ModuleNotFoundError:
    print("matplotlib is not installed, disabling plot")
    EN_PLT = False


 

def generate_sine_samples(length=1024, amplitude=65535, gen_hex=False):
    """
    :param length: Number of samples
    :param amplitude: Amplitude of sin wave
    :return: list of samples
    """
    sin_samples = []
    max_amplitude = amplitude // 2
    for index, item in enumerate((math.sin(2*math.pi*i/length) for i in range(length))):
        if math.modf(item)[0] > 0.5:
            value = int(math.ceil((item*max_amplitude)))
        else:
            value = int(math.floor((item*max_amplitude)))

        if gen_hex:
            sin_samples.append(hex(value))
        else:
            sin_samples.append(value)
           
    return sin_samples

def parse_args():
    """
    :return: args namespace with command line arguments
    """
    __description__ = """Command Prompt Options:
        Exclusive:
        [--length]           - Type: int. numbe of samples
        [--amplitude]        - Type: int. Max Amplitude of wave
        [--outfile]          - Type: str. file name to store fenerated values
        [--store_hex]        - Type: bool. store samples in hex
        [--plot_sin]         - Type: bool. plot generated sin

        Optional:
        [--help] or [-h]
        """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=__description__,
        add_help=False,
        usage='gen_sin_wave.py [-h] [The required arguments to gen sin wave'
              ' --csv  --output ]'
    )
    parser.add_argument("--length", "-l",   default=1024, type=int, help=argparse.SUPPRESS)
    parser.add_argument("--amplitude", "-A", default=65535, type=int, help=argparse.SUPPRESS)
    parser.add_argument("--outfile", "-o", default="sine.mem", type=str, help=argparse.SUPPRESS)
    parser.add_argument("--store_hex", action='store_true', help=argparse.SUPPRESS)
    parser.add_argument("--plot_sin", action='store_true', help=argparse.SUPPRESS)
    
    return parser.parse_args()
    
def twos_complement(n, bits):
    if n < 0:
        n = (1 << bits) - abs(n)
    return n


def write_into_file(file_name, samples_to_dump, store_hex, bits):
    with open(file_name, "w") as OF:
        OF.writelines([f"{sample if not store_hex else hex(twos_complement(sample,bits))}\n".lstrip('0').lstrip('x') for sample in samples_to_dump])

if __name__ == '__main__':
    
    args = parse_args()

    samples = generate_sine_samples(length=args.length, amplitude=args.amplitude)

    if not os.path.exists(os.path.dirname(args.outfile)) and os.path.dirname(args.outfile) != "":
        exit(f"Parent folder {args.outfile} does not exist")
    n_of_bits = len(bin(args.amplitude)) - 2
    print(n_of_bits)
    write_into_file(file_name=args.outfile, samples_to_dump=samples, store_hex=args.store_hex, bits=n_of_bits)
    
    print(len(samples))
    if args.plot_sin and EN_PLT:
        plt.plot(samples)
        plt.show()


