import argparse
from rich.console import Console
from rich.table import Table
from . import parsers
from . import license_fetcher

def search_license(filepath):
    # create empty dictionary to hold results
    results = {}
    # assign the parsed file to variable of libraries (will be a list of tuples)
    libraries = parsers.parse_requirements_file(filepath)
    print(libraries)

    # cycle through each tuple and find license for package
    for library in libraries:
        package = library[0]
        lic = license_fetcher.fetch_license(package)

        if lic == "":
            results[package] = "License not found"
        else:
            results[package] = lic
    # return key, value dictionary
    return results


def format_results(filepath):
    results = search_license(filepath)

    console = Console()
    table = Table(title="📦 License Compliance Results")

    table.add_column("Package", style="cyan", no_wrap=True)
    table.add_column("License", style="green")

    for package, license_type in results.items():
        license_str = license_type if license_type else "[red]Not Found"
        table.add_row(package, license_str)

    console.print(table)


def main():
    parser = argparse.ArgumentParser(description="Check licenses of dependancies from a requirements.txt file")
    parser.add_argument(
        "--file",
        required = True,
        help="Path to requirements.txt file"
    )
    args = parser.parse_args()
    format_results(args.file)

if __name__ == "__main__":
    main()
