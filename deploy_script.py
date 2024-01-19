import subprocess
import sys

def despliegue(port):
    # Comando para construir la imagen del contenedor
    build_command = f"docker build -t desafio_rockingdata ."

    # Comando para ejecutar el contenedor exponiendo el puerto especificado
    run_command = f"docker run -p {port}:5000 desafio_rockingdata"

    try:
        # Construir la imagen del contenedor
        subprocess.run(build_command, shell=True, check=True)

        # Ejecutar el contenedor
        subprocess.run(run_command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python deploy_script.py <puerto>")
        sys.exit(1)

    puerto = sys.argv[1]
    despliegue(puerto)

