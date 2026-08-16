import { useEffect, useState } from "react";
import { getFoods } from "../services/foodService";

function Menu() {
  const [foods, setFoods] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchFoods = async () => {
      try {
        const data = await getFoods();
        setFoods(data.results || data);
      } catch (error) {
        console.error(error);
        setError("Failed to load menu.");
      } finally {
        setLoading(false);
      }
    };

    fetchFoods();
  }, []);

  if (loading) {
    return <p className="text-center mt-10">Loading menu...</p>;
  }

  if (error) {
    return (
      <p className="text-center mt-10 text-red-500">
        {error}
      </p>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-4xl font-bold text-center mb-8">
        Our Menu 🍕
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {foods.map((food) => (
          <div
            key={food.id}
            className="bg-white rounded-2xl shadow-md p-6"
          >
            <h2 className="text-2xl font-bold">
              {food.name}
            </h2>

            <p className="text-gray-600 mt-2">
              {food.description}
            </p>

            <p className="text-xl font-bold mt-4">
              ₹{food.price}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Menu;