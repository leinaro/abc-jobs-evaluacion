# abc-jobs-evaluacion

Microservicio de evaluacion del experimento para el proyecto ABC

## Configuracion de Docker
1. Crear la network para los dos microservicios del experimento (correr solo una vez)

    ```bash
    docker network create abc-network
    ```
2. Construir la imagen de docker 
    ```bash
     docker build -t evaluacion .
    ```
3. Crear y iniciar el container (correr solo una vez)
    ```bash
    docker run --network=abc-network --name evaluacion -p 5000:5000 evaluacion
    ```
4. Iniciar el container de nuevo:
    ```bash
    docker start evaluacion
    ```
