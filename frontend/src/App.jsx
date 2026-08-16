import { Routes, Route, Navigate } from "react-router-dom";
import Menu from "./pages/Menu";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/menu" />} />
      <Route path="/menu" element={<Menu />} />
    </Routes>
  );
}

export default App;