import {

    AppBar,

    Toolbar,

    Typography,

    Box,

    Avatar,

} from "@mui/material";

function Navbar() {

    return (

        <AppBar

            elevation={0}

            position="static"

            sx={{

                background: "white",

                color: "#111827",

            }}

        >

            <Toolbar>

                <Typography

                    variant="h5"

                    fontWeight="bold"

                >

                    AI Powered Board Reporting

                </Typography>

                <Box sx={{ flexGrow: 1 }} />

                <Avatar>

                    V

                </Avatar>

            </Toolbar>

        </AppBar>

    );

}

export default Navbar;