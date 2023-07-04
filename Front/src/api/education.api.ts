import axios from "axios";
import { Deuda } from "../Types/educationservice";

export const obtenerDeudores = () => {
  return axios.get("http://127.0.0.1:8000/ServicioEducacion/deudas/");
};

export const pagarDeuda = (pago: Deuda) => {
  return axios.post("http://127.0.0.1:8000/ServicioEducacion/pagar/", pago);
};

export const obtenerPagos = () => {
  return axios.get("http://127.0.0.1:8000/ServicioEducacion/pagos/");
};