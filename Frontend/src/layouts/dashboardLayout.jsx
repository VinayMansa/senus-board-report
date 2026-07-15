import {

    Box,

} from "@mui/material";

import Sidebar from "../components/Sidebar";

import Navbar from "../components/Navbar";

function DashboardLayout({

    children,

}) {

    return (

        <Box
            sx={{
                display: "flex",
                bgcolor: "#F5F7FB",
                minHeight: "100vh",
            }}
        >

            <Sidebar />

            <Box
                sx={{
                    flexGrow: 1,
                }}
            >

                <Navbar />

                <Box
                    sx={{
                        p: 4,
                    }}
                >

                    {children}

                </Box>

            </Box>

        </Box>

    );

}

export default DashboardLayout;