import { Link } from "react-router-dom";
import { DeudasList } from "../../components/EducationService/DeudasList";
import { PagosList } from "../../components/EducationService/PagosList";

export function EducationPages() {
  return (
    <>
      <h1 className="text-4xl font-bold mb-6 text-left mt-2">
        Zona de Pagos de Educación
      </h1>
      <Link
        to="/Servicios/Educacion/Pagos"
        className="bg-sky-600 hover:bg-blue-800 text-white py-2 px-4 rounded mt-2 mb-4 inline-block"
      >
        Pagar Deuda
      </Link>
      <div className="flex flex-col gap-4">
        <DeudasList />
        <PagosList />
      </div>
    </>
  );
}
