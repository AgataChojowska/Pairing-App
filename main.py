from file.input_reader import InputReader
from file.output_writer import OutputWriter
from pairer.pairer import Pairer


def main():
    reader = InputReader('input.json')
    writer = OutputWriter('output.json')
    inputs = reader.read_input()
    pairer = Pairer(inputs, 12)
    out = pairer.compute()
    writer.write_file(out)


if __name__ == '__main__':
    main()
