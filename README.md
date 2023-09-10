# abc-jobs-evaluacion

### 1) clonar el repositorio de evaluación
        https://github.com/leinaro/abc-jobs-evaluacion

## abrir una consola de comandos en la carpeta y ubicarse en la que se descargó el repositorio de evaluacion

## ejecutar el comando 
        docker network create abc-network

## ejecutar el comando
        docker build -t evaluacion .

 ## ejecutar el comando
        docker run --network=abc-network --name evaluacion -p 5000:5000 evaluacion

 ## En otra consola de comandos ejecutar el siguiente comando
        docker start evaluacion

# abc-jobs-gateway
### 2) clonar el repositorio de gateway
        https://github.com/tom-uniandes/abc-jobs-gateway

## abrir una consola de comandos en la carpeta y ubicarse en la que se descargó el repositorio de gateway
        docker build -t gateway .

## ejecutar el comando
        docker run --network=abc-network --name gateway -p 5005:5005 gateway

 ## En otra consola de comandos ejecutar el siguiente comando
        docker start gateway

# k6
### 3) instalar k6 
  
## tutorial + instaladores para otros sistemas operativos
        https://k6.io/docs/es/empezando/instalacion/

## instalador para windows
        https://dl.k6.io/msi/k6-latest-amd64.msi


### 4) ejecutar el comando
    k6 run script.js --out json=Experimento1.json --out csv=Experimento1.csv --log-output=file=Experimento1.log

## salida en consola

![image](https://github.com/tom-uniandes/abc-jobs-gateway/assets/123895702/490afc11-e324-48c0-b1de-6608e9f25851)



### 5) validar los archivos  
    Experimento1.json 
    Experimento1.csv 
    Experimento1.log

### 6) validar el archivo 
    Experimento1.html

![image](https://github.com/tom-uniandes/abc-jobs-gateway/assets/123895702/eae3b2e8-3336-414e-9456-c63a0f78cb82)

    
## ir a la seccion Checks & Groups
![image](https://github.com/tom-uniandes/abc-jobs-gateway/assets/123895702/b08e1059-e018-40d9-85ea-f6030ca08854)



# **************************integracion con grafana**************************

### 7) integracion con grafana
 clonar o descargar el repositorio de grafana + influxdb + k6
    https://github.com/grafana/k6


## ejecutar el comando
    docker-compose up -d influxdb grafana

## configurar el dasboard en grafana
![image](https://github.com/tom-uniandes/abc-jobs-gateway/assets/123895702/a0417ad2-0fe7-4263-b3b5-cc07c730d52d)

## importar el archivo DashboardK6.json
![image](https://github.com/tom-uniandes/abc-jobs-gateway/assets/123895702/bf906ef4-7787-4c4f-a3f9-1c0e0bd3cf14)


## vista general del dashboard
![image](https://github.com/tom-uniandes/abc-jobs-gateway/assets/123895702/7253e480-7f23-47f3-a0c4-e689a5f52605)

## vista del gráfico **CHECKS PER SECOND**

![image](https://github.com/tom-uniandes/abc-jobs-gateway/assets/123895702/45399e8c-a5b4-4d25-ab8c-cf7112577585)


## abrir una consola de comandos en la carpeta en la que se encuentra el archivo script.js
## ejecutar el comando 
    k6 run script.js --out json=Experimento1.json --out csv=Experimento1.csv --log-output=file=Experimento1.log --out influxdb=http://localhost:8086/k6    
