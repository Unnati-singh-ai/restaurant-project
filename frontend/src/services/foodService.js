import api from "./axios";

export const getFoods = async () => {
  const response = await api.get("/menu/foods/");
  return response.data;
};

export const getCategories = async () => {
  const response = await api.get("/menu/categories/");
  return response.data;
};