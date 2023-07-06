// EducationRoutes.tsx
import { Route, Routes } from "react-router-dom";
import { InicioEducation } from "../pages/EducationService/InicioEducacion";
import { Deudas } from "../pages/EducationService/Deudas";
import { Pagos } from "../pages/EducationService/Pagos";
import { PagarDeudas } from "../pages/EducationService/PagarDeudas";
import { BusquedaPago } from "../pages/EducationService/BusquedaPago";

export const EducacionRoutes = () => (
  <Routes>
    <Route path="/" element={<InicioEducation />} />
    <Route path="/Deudas" element={<Deudas />} />
    <Route path="/Pagos" element={<Pagos />} />
    <Route path="/Pagar" element={<PagarDeudas />} />
    <Route path="/BusquedaPago" element={<BusquedaPago />} />
  </Routes>
);
