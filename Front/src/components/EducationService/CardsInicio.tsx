import { Link } from "react-router-dom";

export function CardsInicio({ to, text }: { to: string; text: string }) {
  return (
    <Link
      to={to}
      className="bg-sky-600 hover:bg-blue-800 text-white py-2 px-4 rounded mt-2 mb-4 inline-block"
    >
      {text}
    </Link>
  );
}
