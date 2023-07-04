import { DeudasPagarForm } from "../../components/EducationService/DeudasPagarForm";

export function PagarDeudas() {
  return (
    <>
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-4">Formulario de Pago</h1>
      <div className="max-w-md mx-auto">
        <DeudasPagarForm />
      </div>
    </div>
  </>
  );
}
