import requests

# An incredibly simple HSTS tester. 
# Can test a single URL given from the command line or a list of URLs from a file.
# Usage examples:
# python main.py -u https://www.google.com
# python main.py -f urls.txt

# tests the HSTS header of a given URL
def test_hsts(url):
    try:
        response = requests.get(url, timeout=5)
        if response.headers.get('Strict-Transport-Security'):
            return True
        else:
            return False
    except:
        return False
    
# tests the HSTS header of a list of URLs from a file
def test_hsts_file(file):
    with open(file, 'r') as f:
        for line in f:
            if test_hsts(line.strip()):
                print(line.strip() + " is HSTS enabled")
            else:
                print(line.strip() + " is not HSTS enabled")

# tests the HSTS header of a single URL given from the command line
def test_hsts_url(url):
    if test_hsts(url):
        print(url + " is HSTS enabled")
    else:
        print(url + " is not HSTS enabled")

# main function
def main():
    import argparse
    parser = argparse.ArgumentParser(description='HSTS tester. Can test a single URL given from the command line or a list of URLs from a file.')
    parser.add_argument('-u', '--url', help='URL to test')
    parser.add_argument('-f', '--file', help='File containing URLs to test')
    args = parser.parse_args()
    if args.url:
        test_hsts_url(args.url)
    elif args.file:
        test_hsts_file(args.file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()