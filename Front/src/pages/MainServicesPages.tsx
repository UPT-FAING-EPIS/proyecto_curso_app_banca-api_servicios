import { Link } from "react-router-dom";
import {
  BsBook,
  BsGlobe,
  BsLightning,
  BsDroplet,
  BsPhone,
} from "react-icons/bs";

export function MainServicesPages() {
  const cardStyles =
    "bg-sky-700 hover:bg-sky-600 rounded-xl flex flex-col items-center justify-center text-center p-4 text-white";
  return (
    <div className="py-8 px-4 ">
      <h1 className="text-black text-3xl font-bold mb-4">
        Escoga su opción de pago
      </h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
        <Link to="/Servicios/Educacion" className={cardStyles}>
          <div className="text-4xl text-orange-300 mb-4">
            <BsBook />
          </div>
          <h2 className="text-lg font-bold">Pago de Educación</h2>
        </Link>
        <Link to="/Servicios/Internet" className={cardStyles}>
          <div className="text-4xl text-gray-300 mb-4">
            <BsGlobe />
          </div>
          <h2 className="text-lg font-bold">Pago de Internet</h2>
        </Link>
        <Link to="/Servicios/Luz" className={cardStyles}>
          <div className="text-4xl text-yellow-400 mb-4">
            <BsLightning />
          </div>
          <h2 className="text-lg font-bold">Pago de Luz</h2>
        </Link>
        <Link to="/Servicios/Agua" className={cardStyles}>
          <div className="text-4xl text-sky-400 mb-4">
            <BsDroplet />
          </div>
          <h2 className="text-lg font-bold">Pago de Agua</h2>
        </Link>
        <Link to="/Servicios/Telefonia" className={cardStyles}>
          <div className="text-4xl text-gray-400 mb-4">
            <BsPhone />
          </div>
          <h2 className="text-lg font-bold">Pago de Telefonía</h2>
        </Link>
      </div>
    </div>
  );
}
