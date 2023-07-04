import { useForm } from "react-hook-form";
import { pagarDeuda } from "../../api/education.api.ts";
import { Deuda } from "../../Types/educationservice";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-hot-toast";

export function DeudasPagarForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const navigate = useNavigate();
  const onSubmit = handleSubmit(async (data) => {
    const deudaData: Deuda = {
      CodigoDeuda: parseInt(data.CodigoDeuda),
      MontoPago: parseInt(data.MontoPago),
    };
    const res = await pagarDeuda(deudaData);
    console.log(res);
    toast.success("Pago realizado correctamente", {
      position: "top-right",
      style: {
        background: "#202033",
        color: "#fff",
      },
    });
    navigate("/Servicios/Educacion");
  });

  return (
    <>
      <form
        onSubmit={onSubmit}
        className="flex flex-col gap-4 items-center mx-auto mt-4"
      >
        <input
          type="number"
          min="0"
          placeholder="Código de deuda"
          {...register("CodigoDeuda", { required: true })}
          className="p-2 rounded border border-gray-300"
        />
        {errors.CodigoDeuda && (
          <span className="text-red-500">Código de deuda requerido</span>
        )}

        <input
          type="number"
          min="0"
          placeholder="Cantidad de deuda"
          {...register("MontoPago", { required: true })}
          className="p-2 rounded border border-gray-300"
        />
        {errors.MontoPago && (
          <span className="text-red-500">Monto de pago requerido</span>
        )}

        <div className="flex gap-4">
          <Link
            to="/Servicios/Educacion"
            className="bg-gray-500 hover:bg-gray-600 text-white py-2 px-4 rounded"
          >
            Atras
          </Link>
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded"
          >
            Guardar
          </button>
        </div>
      </form>
    </>
  );
}
