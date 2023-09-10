import http from 'k6/http';
import { check } from 'k6';
import { htmlReport } from "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";
import { textSummary } from "https://jslib.k6.io/k6-summary/0.0.1/index.js";

/*Escenarios de prueba*/
export const options = {
    httpDebug: 'full',
    scenarios: {
      
      shared_iter_scenario: {
        executor: "shared-iterations",
        vus: 50,
        iterations: 10000,
        startTime: "0s",
      }
      
      
      /*
      per_vu_scenario: {
        executor: "per-vu-iterations",
        vus: 10,
        iterations: 10000,
        startTime: "10s",
      },
      */

    },
  };



  /* Request */
export default function () {
    const url = 'http://localhost:5005/send-answer';
    const payload = JSON.stringify({
      id_pregunta: 1,
      id_respuesta: 3,
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(url, payload, params);
  const myJson = res.json();


/* checks */

  check(res, {
    'is status 200': (r) => r.status === 200,
  });

  check(res, {
    'response time is less than 5 seconds': (r) => r.timings.duration <= 5000,
  });

  check(res, {
    'peticiones con "El envío falló, intente nuevamente"': (r) => r.json().message === "El envío falló, intente nuevamente",
  });

  

}

/* Generacion de reporte */ 
export function handleSummary(data) {
    return {
      "Experimento1.html": htmlReport(data),
      "title":    "Arquitectura",
      stdout: textSummary(data, { indent: " ", enableColors: true }),
    };
  }

