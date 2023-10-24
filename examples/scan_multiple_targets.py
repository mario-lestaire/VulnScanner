from vulnscanner_v1 import VulnScanner

def main():
    targets = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]  # Reemplaza estas IPs con las de tus objetivos.
    for target in targets:
        scanner = VulnScanner(target)
        scanner.run()

if __name__ == "__main__":
    main()
