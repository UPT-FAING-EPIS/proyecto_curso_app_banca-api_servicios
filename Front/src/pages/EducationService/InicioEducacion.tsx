import { CardsInicio } from "../../components/EducationService/CardsInicio";
export function InicioEducation() {
  return (
    <>
      <h1 className="text-4xl font-bold mb-6 text-left mt-2">
        Pagos de Educación
      </h1>
      <CardsInicio to="/Servicios/Educacion/Pagar" text="Pagar Deuda" />
      <CardsInicio to="/Servicios/Educacion/Deudas" text="Deudas" />
      <CardsInicio to="/Servicios/Educacion/Pagos" text="Pagos" />
    </>
  );
}
