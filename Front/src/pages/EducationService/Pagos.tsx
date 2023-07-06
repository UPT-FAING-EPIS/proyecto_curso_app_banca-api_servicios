import { PagosList } from "../../components/EducationService/PagosList";
import { Regresar } from "../../components/Regresar";

export function Pagos() {
  return (
    <>
      <Regresar to="/Servicios/Educacion" />
      <div className="flex flex-col gap-4">
        <PagosList />
      </div>
    </>
  );
}
