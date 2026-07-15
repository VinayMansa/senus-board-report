import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
    palette: {
        primary: {
            main: "#2563EB",
        },
        secondary: {
            main: "#14B8A6",
        },
        background: {
            default: "#F5F7FB",
            paper: "#FFFFFF",
        },
    },

    typography: {
        fontFamily: "'Poppins', sans-serif",

        h4: {
            fontWeight: 700,
        },

        h5: {
            fontWeight: 600,
        },

        h6: {
            fontWeight: 600,
        },
    },

    shape: {
        borderRadius: 15,
    },
});

export default theme;