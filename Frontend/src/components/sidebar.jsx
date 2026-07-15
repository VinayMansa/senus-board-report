import {
    Drawer,
    Toolbar,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import DescriptionIcon from "@mui/icons-material/Description";
import SmartToyIcon from "@mui/icons-material/SmartToy";
import LogoutIcon from "@mui/icons-material/Logout";

import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const drawerWidth = 240;

function Sidebar() {

    const { logout } = useAuth();

    const navigate = useNavigate();

    const handleLogout = () => {

        logout();

        navigate("/");

    };

    return (

        <Drawer
            variant="permanent"
            sx={{
                width: drawerWidth,
                flexShrink: 0,
                "& .MuiDrawer-paper": {
                    width: drawerWidth,
                    boxSizing: "border-box",
                },
            }}
        >

            <Toolbar />

            <List>

                <ListItemButton
                    component={Link}
                    to="/dashboard"
                >
                    <ListItemIcon>
                        <DashboardIcon />
                    </ListItemIcon>

                    <ListItemText
                        primary="Dashboard"
                    />
                </ListItemButton>

                <ListItemButton>

                    <ListItemIcon>
                        <DescriptionIcon />
                    </ListItemIcon>

                    <ListItemText
                        primary="Reports"
                    />

                </ListItemButton>

                <ListItemButton>

                    <ListItemIcon>
                        <SmartToyIcon />
                    </ListItemIcon>

                    <ListItemText
                        primary="AI Summary"
                    />

                </ListItemButton>

                <ListItemButton
                    onClick={handleLogout}
                >

                    <ListItemIcon>
                        <LogoutIcon />
                    </ListItemIcon>

                    <ListItemText
                        primary="Logout"
                    />

                </ListItemButton>

            </List>

        </Drawer>

    );
}

export default Sidebar;