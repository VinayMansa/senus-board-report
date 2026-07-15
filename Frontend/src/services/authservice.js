import api from "../api/axios";

export const loginUser = async (email, password) => {

    const response = await api.post(
        "/users/login",
        {
            email: email,
            password: password,
        }
    );

    return response.data;
};