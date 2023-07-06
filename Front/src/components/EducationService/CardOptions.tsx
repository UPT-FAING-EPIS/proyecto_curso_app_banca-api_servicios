import { Link } from "react-router-dom";

export function CardOptions({
  imageSrc,
  altText,
  to,
}: {
  imageSrc: string;
  altText: string;
  to: string;
}) {
  return (
    <Link to={to}>
      <div className="flex justify-center items-center w-full h-full">
        <div className="bg-white rounded-lg shadow-lg p-4">
          <img src={imageSrc} alt={altText} className="w-full h-auto" />
        </div>
      </div>
    </Link>
  );
}
