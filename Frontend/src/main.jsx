import React from "react";
import ReactDOM from "react-dom/client";
import "@fontsource/poppins";
import { ThemeProvider } from "@mui/material/styles";
import { BrowserRouter } from "react-router-dom";
import { theme } from "./theme/theme";
import App from "./App";
import { AuthProvider } from "./context/AuthContext";

import CssBaseline from "@mui/material/CssBaseline";

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <BrowserRouter>
            <AuthProvider>
                <CssBaseline />
                <ThemeProvider theme={theme}>
                <App />
                </ThemeProvider>
            </AuthProvider>
        </BrowserRouter>
    </React.StrictMode>
);