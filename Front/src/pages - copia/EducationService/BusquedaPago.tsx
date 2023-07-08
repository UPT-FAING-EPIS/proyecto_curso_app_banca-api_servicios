import { useState } from "react";
import { useForm } from "react-hook-form";
import { buscarDeuda } from "../../api/education.api.ts";
import { Deudor } from "../../Types/educationservice.ts";
import { ContentTDeudas } from "../../components/EducationService/ContentTDeudas";
import { Regresar } from "../../components/Regresar.tsx";

export function BusquedaPago() {
  const [deudores, setDeudores] = useState<Deudor[]>([]);
  const [error, setError] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = handleSubmit(async (data) => {
    const codigoEstudiante = data.codigoEstudiante;

    try {
      const response = await buscarDeuda(parseInt(codigoEstudiante));
      setDeudores(response.data);
      setError("");
    } catch (error) {
      console.log(error);
      setDeudores([]);
      setError("Alumno no encontrado");
    }
  });

  return (
    <>
      <Regresar to="/Servicios/Educacion/Pagar" />
      <div className="mt-4">
        <form onSubmit={onSubmit}>
          <div className="relative">
            <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg
                className="w-4 h-4 text-gray-500 dark:text-gray-400"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 20 20"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                />
              </svg>
            </div>
            <input
              type="search"
              id="default-search"
              {...register("codigoEstudiante", { required: true })}
              className="block w-full p-4 pl-10 text-lg text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Ingrese el código del estudiante"
              required
            />
            {errors.codigoEstudiante && (
              <span className="text-red-500">
                Código de estudiante requerido
              </span>
            )}
            <button
              type="submit"
              className="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-lg px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Search
            </button>
          </div>
        </form>{" "}
        <div className="container mx-auto px-4 py-8">
          {error && <p className="text-red-500">{error}</p>}
          {deudores.length > 0 ? (
            <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
              <table className="w-full text-sm text-left text-gray-300 dark:text-gray-300">
                <thead className="text-xs text-gray-600 uppercase dark:text-gray-300">
                  <tr>
                    <th scope="col" className="px-6 py-3 text-gray-600">
                      Codigo de deuda
                    </th>
                    <th scope="col" className="px-6 py-3 text-gray-600">
                      Cantidad
                    </th>
                    <th scope="col" className="px-6 py-3 text-gray-600">
                      Vencimiento
                    </th>
                    <th scope="col" className="px-6 py-3 text-gray-600">
                      Estado
                    </th>
                    <th scope="col" className="px-6 py-3 text-gray-600">
                      Codigo Estudiante
                    </th>
                    <th scope="col" className="px-6 py-3 text-gray-600">
                      Accion
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {deudores.map((deudor) => (
                    <ContentTDeudas
                      key={deudor.CodigoDeuda}
                      codigoDeuda={deudor.CodigoDeuda.toString()}
                      cantidadDeuda={deudor.CantidadDeuda}
                      fechaVencimiento={deudor.FechaVencimiento}
                      estado={deudor.Situacion}
                      codigoestudiante={deudor.fkCodigoAlumno}
                    />
                  ))}
                </tbody>
              </table>
            </div>
          ) : null}
        </div>
      </div>
    </>
  );
}
