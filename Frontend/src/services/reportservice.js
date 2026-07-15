import api from "../api/axios";

export const getReport = async (id) => {

    const response = await api.get(
        `/dashboard/report/${id}`
    );

    return response.data;
};

export const getKPIs = async (id) => {

    const response = await api.get(
        `/dashboard/kpis/${id}`
    );

    return response.data;
};