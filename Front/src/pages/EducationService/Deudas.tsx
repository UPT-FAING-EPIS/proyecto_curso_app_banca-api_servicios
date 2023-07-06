import { DeudasList } from "../../components/EducationService/DeudasList";
import { Regresar } from "../../components/Regresar";

export function Deudas() {
  return (
    <>
      <Regresar to="/Servicios/Educacion" />
      <div className="flex flex-col gap-4">
        <DeudasList />
      </div>
    </>
  );
}
