import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { MainServicesPages } from "./pages/MainServicesPages";
import { EducationPages } from "./pages/EducationService/EducationPages";
import { PagarDeudas } from "./pages/EducationService/PagarDeudas";
import { Navigation } from "./components/Navigation";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto px-2">
        <Navigation />
        <Routes>
          <Route path="/" element={<Navigate to="/Servicios" />} />
          <Route path="/Servicios" element={<MainServicesPages />} />
          <Route path="/Servicios/Educacion" element={<EducationPages />} />
          <Route path="/Servicios/Educacion/Pagos" element={<PagarDeudas />} />
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;
