def parse_requirements_file(filepath):
    """
    Will parse a requirements.txt file and return a list of (package, version) tuples
    """
    libraries = []

    try:
        with open(filepath) as f:
            for line in f:
                # strip line
                line = line.strip()
                # Ignore comments and empty lines
                if not line or line.startswith("#"):
                    continue
                # Ignore lines that are not package specifications
                if "==" in line:
                        package, version = line.split("==")

                elif ">=" in line:
                        package, version = line.split(">=")
                else:
                    continue
                # add package and version to tuple
                libraries.append((package.strip(), version.strip()))
                
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error reading file: {filepath}, Error: {e}")
    
    # return libraries list of tuples
    return libraries


if __name__ == "__main__":
    print(parse_requirements_file("/Users/jordancroft/Documents/Documents - Jordan.’s MacBook Air/GitHub/license-checker/requirements.txt"))



