#!/usr/bin/env python3

import argparse
import subprocess

class VulnScanner:
    def __init__(self, target):
        self.target = target

    def scan(self):
        command = ["nmap", "-Pn", "-T4", "-sV", self.target, "-p-"]
        
        try:
            output = subprocess.check_output(command).decode("utf-8")
            return output
        except Exception as e:
            print(f"Error al escanear {self.target}: {str(e)}")
            return None

    def check_vulnerabilities(self, service_output):
        parts = service_output.split(" ")
        if len(parts) == 2:
            service_name, service_version = parts
        elif len(parts) > 2:
            service_name, service_version = parts[0], " ".join(parts[2:])
        else:
            print(f"No se pudo obtener información detallada para: {service_output}")
            return None

        command = ["searchsploit", service_name, service_version]
        
        try:
            exploits = subprocess.check_output(command).decode("utf-8")
            if "Exploit titles" in exploits:
                return exploits
            return None
        except:
            return None

    def run(self):
        scan_result = self.scan()
        
        if not scan_result:
            return
        
        for line in scan_result.split("\n"):
            if "open" in line and "tcp" in line:
                details = line.split()
                port_protocol = details[0]
                state = details[1]
                service_info = " ".join(details[2:])
                
                print(f"-----------------------")
                print(f" Puerto y Protocolo: {port_protocol}")
                print(f" Estado: {state}")
                print(f" Servicio: {service_info}")
                
                exploits = self.check_vulnerabilities(service_info)
                if exploits:
                    print(f"\nVulnerabilidades encontradas para el servicio {service_info} en {self.target}:\n{exploits}")
                else:
                    print(f"\nNo se encontraron vulnerabilidades conocidas para el servicio {service_info} en {self.target}.")
        print(f"-----------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='vulnscanner: Una herramienta de escaneo de vulnerabilidades.')
    parser.add_argument('target', type=str, help='IP o dominio objetivo')
    
    args = parser.parse_args()

    scanner = VulnScanner(args.target)
    scanner.run()
