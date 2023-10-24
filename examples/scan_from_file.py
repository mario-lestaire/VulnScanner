from vulnscanner_v1 import VulnScanner

def main():
    with open("targets.txt", "r") as file:  # Asegúrate de tener un archivo targets.txt con una IP/dominio por línea.
        for line in file:
            target = line.strip()
            if target:  # Comprobar que la línea no está vacía.
                scanner = VulnScanner(target)
                scanner.run()

if __name__ == "__main__":
    main()
