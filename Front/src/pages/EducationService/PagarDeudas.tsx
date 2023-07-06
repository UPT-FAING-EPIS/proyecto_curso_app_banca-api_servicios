import { CardOptions } from "../../components/EducationService/CardOptions";
import { DeudasPagarForm } from "../../components/EducationService/DeudasPagarForm";
import { Regresar } from "../../components/Regresar";

export function PagarDeudas() {
  return (
    <>
      <Regresar to="/Servicios/Educacion" />
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-4">Elija la entidad</h1>
        <div className="max-w-md mx-auto gap-10 flex flex-row">
          <CardOptions
            imageSrc="../../assets/images/LogoUnjbg.png"
            altText="Logo Unjbg"
            to="/"
          />
          <CardOptions
            imageSrc="../../assets/images/LogoUpt.png"
            altText="Logo Upt"
            to="/Servicios/Educacion/BusquedaPago"
          />
        </div>
      </div>
    </>
  );
}
