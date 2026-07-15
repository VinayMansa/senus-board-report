import {
    Drawer,
    Toolbar,
    Typography,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
    Box,
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import DescriptionIcon from "@mui/icons-material/Description";
import SmartToyIcon from "@mui/icons-material/SmartToy";
import LogoutIcon from "@mui/icons-material/Logout";

import { Link, useNavigate } from "react-router-dom";

import { useAuth } from "../context/AuthContext";

const drawerWidth = 260;

function Sidebar() {

    const navigate = useNavigate();

    const { logout } = useAuth();

    const handleLogout = () => {

        logout();

        navigate("/");

    };

    return (

        <Drawer
            variant="permanent"
            sx={{

                width: drawerWidth,

                "& .MuiDrawer-paper": {

                    width: drawerWidth,

                    background: "#111827",

                    color: "white",

                    border: 0,

                },

            }}
        >

            <Toolbar>

                <Typography
                    variant="h5"
                    fontWeight="bold"
                >

                    Senus AI

                </Typography>

            </Toolbar>

            <Box
                sx={{
                    mt: 2,
                }}
            >

                <List>

                    <ListItemButton
                        component={Link}
                        to="/dashboard"
                    >

                        <ListItemIcon>

                            <DashboardIcon
                                sx={{
                                    color: "white",
                                }}
                            />

                        </ListItemIcon>

                        <ListItemText
                            primary="Dashboard"
                        />

                    </ListItemButton>

                    <ListItemButton>

                        <ListItemIcon>

                            <DescriptionIcon
                                sx={{
                                    color: "white",
                                }}
                            />

                        </ListItemIcon>

                        <ListItemText
                            primary="Reports"
                        />

                    </ListItemButton>

                    <ListItemButton>

                        <ListItemIcon>

                            <SmartToyIcon
                                sx={{
                                    color: "white",
                                }}
                            />

                        </ListItemIcon>

                        <ListItemText
                            primary="AI Summary"
                        />

                    </ListItemButton>

                    <ListItemButton
                        onClick={handleLogout}
                    >

                        <ListItemIcon>

                            <LogoutIcon
                                sx={{
                                    color: "white",
                                }}
                            />

                        </ListItemIcon>

                        <ListItemText
                            primary="Logout"
                        />

                    </ListItemButton>

                </List>

            </Box>

        </Drawer>

    );

}

export default Sidebar;