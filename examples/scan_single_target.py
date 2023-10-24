from vulnscanner_v1 import VulnScanner

def main():
    target = "192.168.1.1"  # Por favor, reemplaza esta IP con la de tu objetivo.
    scanner = VulnScanner(target)
    scanner.run()

if __name__ == "__main__":
    main()
