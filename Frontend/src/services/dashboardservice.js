import api from "../api/axios";

export const getSummary =
async () => {

    const response =
    await api.get("/dashboard/summary");

    return response.data;

};


export const getReports = async () => {

    const response = await api.get(
        "/dashboard/reports"
    );

    return response.data;

};