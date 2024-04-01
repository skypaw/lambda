import argparse
import json


def handler(context: argparse.Namespace):
    # lambda writing to the file
    with open('lambda-code/output.json', 'w') as file:
        print(json.dumps(context.__dict__))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("save json to outputs")
    parser.add_argument("--string-input",dest="string-input", type=str, help="String will be written to output")

    args = parser.parse_args()
    handler(args)

