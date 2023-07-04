import { useEffect, useState } from "react";
import { obtenerPagos } from "../../api/education.api.ts";
import { Pago } from "../../Types/educationservice.ts";

export function PagosList() {
  const [pagos, setPagos] = useState<Pago[]>([]); 

  useEffect(() => {
    async function cargarPagos() {
      const res = await obtenerPagos();
      setPagos(res.data); 
      console.log(res)
    }
    cargarPagos();
  }, []);

  return (
    <>
    <h2>Lista de pagos</h2>
      <table>
        <thead>
          <tr>
            <th>Código pago</th>
            <th>Monto pago</th>
            <th>Fecha de pago</th>
            <th>Codigo de deuda</th>
          </tr>
        </thead>
        <tbody>
          {pagos.map((pago) => (
            <tr key={pago.CodigoPago}>
              <td>{pago.CodigoPago}</td>
              <td>{pago.MontoPago}</td>
              <td>{pago.FechaPago}</td>
              <td>{pago.FKCodigoDeuda}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
}
